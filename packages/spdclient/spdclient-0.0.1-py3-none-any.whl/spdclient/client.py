from uuid import uuid4
import httpx
import logging
from time import time

logger = logging.getLogger(__name__)


class SPDClient:
    def __init__(self, host=None, port=None, username=None, password=None, is_https=False):
        self.host = host or '127.0.0.1'
        self.port = port or 6800
        self.is_https = is_https
        self.url = f"http{'s' if is_https else ''}://{host}:{port}"
        if username is not None and password is not None:
            self.url = (
                f"http{'s' if is_https else ''}://{username}:{password}@{host}:{port}"
            )
            log_url = f"http{'s' if is_https else ''}://*****:*****@{host}:{port}"
            logger.debug(f"Server URL: {log_url}")
        else:
            logger.debug(f"Server URL: {self.url}")

    def daemon_status(self):
        with httpx.Client() as client:
            response = client.get(self.url + "/daemonstatus.json")
            try:
                return response.json()
            except Exception as e:
                return {
                    "status_code": response.status_code,
                    "status": "error",
                    "message": str(e),
                }

    def add_version(self, project:str, egg:str, version:str=None):
        formdata = {
            "project": project,
            "version": version or str(int(time())),
        }
        logger.debug(f"/addversion.json formdata: {formdata}")
        logger.debug(f"/addversion.json egg file: {egg}")

        files = {"egg": open(egg, "rb")}
        with httpx.Client() as client:
            response = client.post(
                self.url + "/addversion.json", data=formdata, files=files
            )
            try:
                return response.json()
            except Exception as e:
                logger.exception(e, exc_info=True)
                return {
                    "status_code": response.status_code,
                    "status": "error",
                    "message": str(e),
                }

    def schedule(
        self,
        project: str,
        spider: str,
        setting: dict = None,
        jobid: str = None,
        priority: float = None,
        version: str = None,
        spider_args: dict = None,
    ):
        formdata = {
            "project": project,
            "spider": spider,
            "jobid": jobid or uuid4(),
            "priority": priority or 0,
        }
        if setting is not None:
            settings_list = []
            for k, v in setting.items():
                settings_str = f"{k}={v}"
                settings_list.append(settings_str)
            formdata["setting"] = settings_list
        if version is not None:
            formdata["_version"] = version
        if spider_args is not None:
            formdata.update(spider_args)

        logger.debug(f"/schedule.json formdata: {formdata}")
        with httpx.Client() as client:
            response = client.post(self.url + "/schedule.json", data=formdata)
            try:
                return response.json()
            except Exception as e:
                logger.exception(e, exc_info=True)
                return {
                    "status_code": response.status_code,
                    "status": "error",
                    "message": str(e),
                }

    def cancel(self, project:str, job:str):
        with httpx.Client() as client:
            data = {"project": project, "job": job}
            response = client.post(self.url + "/cancel.json", data=data)
            try:
                return response.json()
            except Exception as e:
                logger.exception(e, exc_info=True)
                return {
                    "status_code": response.status_code,
                    "status": "error",
                    "message": str(e),
                }

    def list_projects(self):
        with httpx.Client() as client:
            response = client.get(self.url + "/listprojects.json")
            try:
                return response.json()
            except Exception as e:
                return {
                    "status_code": response.status_code,
                    "status": "error",
                    "message": str(e),
                }

    def list_versions(self, project):
        with httpx.Client() as client:
            params = {"project": project}
            response = client.get(self.url + "/listversions.json", params=params)
            try:
                return response.json()
            except Exception as e:
                return {
                    "status_code": response.status_code,
                    "status": "error",
                    "message": str(e),
                }

    def list_spiders(self, project:str, version:str=None):
        params = {"project": project}
        with httpx.Client() as client:
            if version is not None:
                params["version"] = version
            response = client.get(self.url + "/listspiders.json", params=params)
            try:
                return response.json()
            except Exception as e:
                return {
                    "status_code": response.status_code,
                    "status": "error",
                    "message": str(e),
                }

    def list_jobs(self, project:str=None):
        with httpx.Client() as client:
            params = {}
            if project is not None:
                params["project"] = project
            response = client.get(self.url + "/listjobs.json", params=params)
            try:
                return response.json()
            except Exception as e:
                return {
                    "status_code": response.status_code,
                    "status": "error",
                    "message": str(e),
                }

    def delversion(self, project: str, version: str):
        with httpx.Client() as client:
            data = {"project": project, "version": version}
            response = client.post(self.url + "/delversion.json", data=data)
            try:
                return response.json()
            except Exception as e:
                return {
                    "status_code": response.status_code,
                    "status": "error",
                    "message": str(e),
                }

    def delproject(self, project: str):
        with httpx.Client() as client:
            data = {
                "project": project,
            }
            response = client.post(self.url + "/delproject.json", data=data)
            try:
                return response.json()
            except Exception as e:
                return {
                    "status_code": response.status_code,
                    "status": "error",
                    "message": str(e),
                }
