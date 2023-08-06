from __future__ import annotations

import json
import logging
import time
from datetime import timezone
from typing import TYPE_CHECKING, Any, Dict, List, Optional
from urllib.parse import urljoin

import requests
import socketio
from dateutil import parser
from dateutil.tz import tzlocal
from pydantic import BaseModel

from servicefoundry.internal.util import request_handling, upload_package_to_s3
from servicefoundry.io.output_callback import OutputCallBack
from servicefoundry.lib.config_utils import _get_profile
from servicefoundry.lib.const import DEFAULT_PROFILE_NAME, REFRESH_ACCESS_TOKEN_IN_SEC
from servicefoundry.lib.exceptions import ConfigurationException
from servicefoundry.lib.model.session import ServiceFoundrySession
from servicefoundry.lib.session_factory import get_session
from servicefoundry.v2.lib.models import BuildResponse, Deployment

DEPLOYMENT_LOGS_SUBSCRIBE_MESSAGE = "DEPLOYMENT_LOGS"
BUILD_LOGS_SUBSCRIBE_MESSAGE = "logs"

if TYPE_CHECKING:
    from servicefoundry.auto_gen.models import Application

logger = logging.getLogger(__name__)

VERSION_PREFIX = "v1"


def _get_or_throw(definition, key, error_message):
    if key not in definition:
        raise ConfigurationException(error_message)
    return definition[key]


class PresignedUrl(BaseModel):
    uri: str
    presigned_url: str


class ServiceFoundryServiceClient:
    def __init__(
        self,
        session: Optional[ServiceFoundrySession],
    ):
        self.session = session
        self.host = None
        if self.session:
            self.host = self.session.profile.server_config.api_server

    @classmethod
    def get_client(
        cls, auth_required: bool = True, profile_name: str = DEFAULT_PROFILE_NAME
    ) -> "ServiceFoundryServiceClient":
        # Would be ok to prefer auth token from API instead of local session file
        if auth_required:
            session = get_session(profile_name=profile_name)
            return cls(session=session)
        else:
            # TODO (chiragjn): All usages should be made to handle session=None
            instance = cls(session=None)
            # Try to get this inside __init__, maybe profile shouldn't live inside session?
            instance.host = _get_profile(
                name=DEFAULT_PROFILE_NAME
            ).server_config.api_server
            return instance

    def check_and_refresh_session(self):
        decoded = self.session.decode()
        expiry_second = decoded["exp"]
        if expiry_second - time.time() < REFRESH_ACCESS_TOKEN_IN_SEC:
            logger.info(
                f"Going to refresh the access token {expiry_second - time.time()}."
            )
            self.session.refresh_access_token()

    def _get_header(self):
        return {"Authorization": f"Bearer {self.session.access_token}"}

    def list_workspace(self):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/workspace"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def create_workspace(self, cluster_id, name):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/workspace"
        res = requests.post(
            url,
            json={"name": name, "clusterId": cluster_id},
            headers=self._get_header(),
        )
        return request_handling(res)

    def remove_workspace(self, workspace_id, force=False):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/workspace/{workspace_id}"
        force = json.dumps(
            force
        )  # this dumb conversion is required because `params` just casts as str
        res = requests.delete(url, headers=self._get_header(), params={"force": force})
        return request_handling(res)

    def get_workspace_by_name(self, workspace_name, cluster_id):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/workspace"
        res = requests.get(
            url,
            headers=self._get_header(),
            params={"name": workspace_name, "clusterId": cluster_id},
        )
        return request_handling(res)

    def get_workspace(self, workspace_id):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/workspace/{workspace_id}"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def get_workspace_by_fqn(self, workspace_fqn: str) -> List[Dict[str, Any]]:
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/workspace"
        res = requests.get(
            url,
            headers=self._get_header(),
            params={"fqn": workspace_fqn},
        )
        return request_handling(res)

    def list_applications(self, workspace_id: str = None):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/applications"
        params = {}
        if workspace_id:
            params["workspaceId"] = workspace_id
        res = requests.get(url=url, params=params, headers=self._get_header())
        return request_handling(res)

    def create_cluster(
        self, name, region, aws_account_id, cluster_name, ca_data, server_url
    ):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/cluster"
        res = requests.post(
            url,
            json={
                "id": name,
                "region": region,
                "authData": {
                    "awsAccountID": aws_account_id,
                    "clusterName": cluster_name,
                    "caData": ca_data,
                    "serverUrl": server_url,
                },
            },
            headers=self._get_header(),
        )
        return request_handling(res)

    def list_cluster(self):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/cluster"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def get_cluster(self, cluster_id):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/cluster/{cluster_id}"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def remove_cluster(self, cluster_id):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/cluster/{cluster_id}"
        res = requests.delete(url, headers=self._get_header())
        return request_handling(res)

    def get_presigned_url(self, space_name, service_name, env):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/deployment/code-upload-url"
        res = requests.post(
            url,
            json={
                "workspaceFqn": space_name,
                "serviceName": service_name,
                "stage": env,
            },
            headers=self._get_header(),
        )
        return request_handling(res)

    def generate_presigned_url_to_download(
        self, s3_bucket: str, s3_key: str
    ) -> PresignedUrl:
        url = f"{self.host}/{VERSION_PREFIX}/deployment/code-download-url"
        res = requests.post(
            url,
            json={"s3Key": s3_key, "s3Bucket": s3_bucket},
            headers=self._get_header(),
        )
        uri = "s3://" + s3_bucket + "/" + s3_key.strip("/")
        presigned_url = request_handling(res)["presignedUrl"]
        return PresignedUrl(presigned_url=presigned_url, uri=uri)

    def upload_code_package(
        self, workspace_fqn: str, component_name: str, package_local_path: str
    ) -> PresignedUrl:
        http_response = self.get_presigned_url(
            space_name=workspace_fqn, service_name=component_name, env="default"
        )
        upload_package_to_s3(metadata=http_response, package_file=package_local_path)

        return self.generate_presigned_url_to_download(
            s3_bucket=http_response["s3Bucket"], s3_key=http_response["s3Key"]
        )

    def deploy_application(
        self, workspace_id: str, application: Application
    ) -> Deployment:
        data = {
            "workspaceId": workspace_id,
            "name": application.name,
            "manifest": application.dict(exclude_none=True),
        }
        url = f"{self.host}/{VERSION_PREFIX}/deployments"
        deploy_response = requests.post(url, json=data, headers=self._get_header())
        response = request_handling(deploy_response)
        return Deployment.parse_obj(response["deployment"])

    def create_secret_group(self, name):
        self.check_and_refresh_session()
        url = f"{self.host}/{VERSION_PREFIX}/secret-group/"
        res = requests.post(url, headers=self._get_header(), json={"name": name})
        return request_handling(res)

    def delete_secret_group(self, id):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/secret-group/{id}"
        res = requests.delete(url, headers=self._get_header())
        return request_handling(res)

    def get_secret_group(self, id):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/secret-group/{id}"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def create_secret(self, secret_group_id, key, value):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/secret/"
        res = requests.post(
            url,
            headers=self._get_header(),
            json={"secretGroupId": secret_group_id, "key": key, "value": value},
        )
        return request_handling(res)

    def delete_secret(self, id):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/secret/{id}"
        res = requests.delete(url, headers=self._get_header())
        return request_handling(res)

    def get_secret(self, id):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/secret/{id}"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def get_secrets_in_group(self, secret_group_id):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/secret/list-by-secret-group/{secret_group_id}"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def get_secret_groups(self):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/secret-group/findAll"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def _get_log_print_line(self, log: dict):
        time_str = log["time"]
        time_obj = parser.parse(time_str)
        if not time_obj.tzinfo:
            time_obj = time_obj.replace(tzinfo=timezone.utc)
        local_time = time_obj.astimezone(tzlocal())
        local_time_str = local_time.isoformat()
        return f'[{local_time_str}] {log["log"].strip()}'

    def _tail_logs(
        self,
        tail_logs_url: str,
        query_dict: dict,
        # NOTE: Rather making this printer callback an argument,
        # we should have global printer callback
        # which will be initialized based on the running env (cli, lib, notebook)
        subscribe_message: str,
        callback=OutputCallBack(),
        wait=False,
    ):
        self.check_and_refresh_session()
        sio = socketio.Client(request_timeout=60)
        callback.print_line("Waiting for the task to start...")

        @sio.on(subscribe_message)
        def logs(data):
            try:
                _log = json.loads(data)
                callback.print_line(self._get_log_print_line(_log["body"]))
            except Exception:
                pass

        sio.connect(tail_logs_url, transports="websocket")

        # TODO: We should have have a timeout here. `emit` does
        # not support timeout. Explore `sio.call`.

        sio.emit(
            subscribe_message,
            json.dumps(query_dict),
        )
        if wait:
            sio.wait()

    def tail_build_logs(
        self, build_response: BuildResponse, callback=OutputCallBack(), wait=False
    ):
        self._tail_logs(
            tail_logs_url=build_response.tailLogsUrl,
            query_dict={
                "pipelineRunName": build_response.name,
                "startTs": build_response.logsStartTs,
            },
            callback=callback,
            wait=wait,
            subscribe_message=BUILD_LOGS_SUBSCRIBE_MESSAGE,
        )

    def tail_logs_for_deployment(
        self,
        deployment_fqn: str,
        start_ts: int,
        limit: int,
        callback=OutputCallBack(),
        wait=True,
    ):
        self._tail_logs(
            tail_logs_url=urljoin(
                self.host, f"/?type={DEPLOYMENT_LOGS_SUBSCRIBE_MESSAGE}"
            ),
            query_dict={
                "deploymentFqn": deployment_fqn,
                "startTs": start_ts,
                "limit": limit,
            },
            callback=callback,
            wait=wait,
            subscribe_message=DEPLOYMENT_LOGS_SUBSCRIBE_MESSAGE,
        )

    def fetch_deployment_logs(
        self,
        deployment_fqn: str,
        end_ts: Optional[int],
        limit: Optional[int],
        start_ts: Optional[int],
        callback=OutputCallBack(),
    ):
        params = {
            "deploymentFqn": deployment_fqn,
        }
        if start_ts:
            params["startTs"] = start_ts
        if end_ts:
            params["endTs"] = end_ts
        if limit:
            params["limit"] = limit

        query_url = f"{self.host}/v1/logs"
        self.check_and_refresh_session()
        res = requests.post(url=query_url, json=params, headers=self._get_header())
        logs_list = request_handling(res)
        for log in logs_list["logs"]:
            callback.print_line(self._get_log_print_line(log))

    def get_authorization_for_resource(self, resource_type, resource_id):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/authorize/{resource_type}/{resource_id}"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def create_authorization(self, resource_id, resource_type, user_id, role):
        # @TODO instead of user_id pass emailID. Need to be done once API is available on auth.
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/authorize"
        res = requests.post(
            url,
            headers=self._get_header(),
            json={
                "resourceId": resource_id,
                "resourceType": resource_type,
                "userName": user_id,
                "userType": "USER",
                "role": role,
            },
        )
        return request_handling(res)

    def delete_authorization(self, id):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/authorize/{id}"
        res = requests.delete(url, headers=self._get_header())
        return request_handling(res)

    def update_authorization(self, id, role):
        self.check_and_refresh_session()

        url = f"{self.host}/{VERSION_PREFIX}/authorize"
        res = requests.patch(
            url, headers=self._get_header(), json={"id": id, "role": role}
        )
        return request_handling(res)

    @staticmethod
    def get_tenant_info(api_server_host: str, tenant_hostname: str):
        res = requests.get(
            url=f"{api_server_host}/{VERSION_PREFIX}/tenant-id",
            params={"hostName": tenant_hostname},
        )
        return request_handling(res)
