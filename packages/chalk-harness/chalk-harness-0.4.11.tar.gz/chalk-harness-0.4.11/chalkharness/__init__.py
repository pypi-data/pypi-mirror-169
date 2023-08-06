import re
import subprocess
from datetime import datetime
from json import loads as json_loads
from typing import Optional, TypeVar, Type

from pydantic import BaseModel


class CLIVersion(BaseModel):
    version: str
    platform: str
    sha1: str
    at: datetime


class CLIWhoAmI(BaseModel):
    user: str


class CLIToken(BaseModel):
    token: str


class CLIDeploymentComplete(BaseModel):
    id: str
    creator: str
    environmentId: str
    status: str
    isPreview: bool


class CLIApply(BaseModel):
    deployment_id: str
    deployment_url: str
    status: str
    response: Optional[CLIDeploymentComplete]


T = TypeVar("T")


class ChalkCLIHarness:
    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        environment: Optional[str] = None,
        json: bool = True,
        dry: bool = False,
    ):
        self._client_id = client_id
        self._client_secret = client_secret
        self._environment = environment
        self._json = json
        self._dry = dry

    def _chalk(self, *args, **kwargs):
        all_kwargs = dict(
            client_id=self._client_id,
            client_secret=self._client_secret,
            environment=self._environment,
            json=self._json,
        )
        all_kwargs.update(kwargs)

        def format_key(k: str) -> str:
            return re.sub("_", "-", k.removesuffix("_"))

        kwarg_cli = [
            f"--{format_key(k)}={v}" if v is not True else f"--{format_key(k)}"
            for k, v in all_kwargs.items()
            if v is not None
        ]
        command = ["chalk", *args, *kwarg_cli]
        if self._dry:
            print(command)
            return command

        return subprocess.check_output(command).decode("UTF-8")

    def _parse(self, output: str, model: Type[T]) -> T:
        if self._dry:
            return output
        return model.parse_obj(json_loads(output))

    def _chalk_parse(self, model: Type[T], *args, **kwargs) -> T:
        return self._parse(self._chalk(*args, **kwargs), model)

    def apply_await(self, force: Optional[bool] = None) -> CLIApply:
        return self._chalk_parse(CLIApply, "apply", await_=True, force=force)

    def version(self) -> CLIVersion:
        return self._chalk_parse(CLIVersion, "version")

    def version_tag_only(self) -> str:
        return self._chalk("version", tag_only=True)

    def whoami(self) -> CLIWhoAmI:
        return self._chalk_parse(CLIWhoAmI, "whoami")

    def token(self) -> CLIToken:
        return self._chalk_parse(CLIToken, "token")
