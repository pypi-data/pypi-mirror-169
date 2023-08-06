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


class CLIHarness:
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
        kwarg_cli = [
            f"--{re.sub('_', '-', k.removesuffix('_'))}={v}"
            for k, v in all_kwargs.items()
            if v is not None
        ]
        command = ["chalk", *args, *kwarg_cli]
        if self._dry:
            print(command)
            return ""

        return subprocess.check_output(command).decode("UTF-8")

    @staticmethod
    def _parse(output: str, model: Type[T]) -> T:
        return model.parse_obj(json_loads(output))

    def apply_await(
            self,
            force: Optional[bool] = None,
    ) -> CLIApply:
        return self._parse(self._chalk("apply", await_=True, force=force), CLIApply)

    def version(self) -> CLIVersion:
        return self._parse(self._chalk("version"), CLIVersion)

    def version_tag_only(self) -> str:
        return self._chalk("version", tag_only=True)

    def whoami(self) -> CLIWhoAmI:
        return self._parse(self._chalk("whoami"), CLIWhoAmI)

    def token(self) -> CLIToken:
        return self._parse(self._chalk("token"), CLIToken)


if __name__ == "__main__":
    # harness = CLIHarness(dry=True)
    # harness.apply_await(force=True)
    harness = CLIHarness(dry=False)
    version = harness.version()
    assert version.version == "v0.4.5"
    version = harness.version_tag_only()
    assert version == "v0.4.5"
    me = harness.whoami()
    print(me)
