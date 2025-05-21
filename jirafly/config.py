from enum import Enum
from pathlib import Path

import yaml
from pydantic import BaseModel


class TeamMember(BaseModel, frozen=True):
    gitlab_nickname: str
    jira_id: str
    name: str
    slack_handle: str


class GitlabRepo(BaseModel, frozen=True):
    project: str
    branch: str


class Gitlab(BaseModel, frozen=True):
    checked_repos: list[GitlabRepo]


class Jira(BaseModel, frozen=True):
    url: str
    user: str
    project: str
    filter_extension: str = ""


class OpenAI(BaseModel, frozen=True):
    model: str


class Prompts(BaseModel, frozen=True):
    echo: str
    morning_report: str = ""
    sprint_review: str = ""


class Config(BaseModel, frozen=True):
    team_name: str
    team: list[TeamMember]
    gitlab: Gitlab
    jira: Jira
    openai: OpenAI
    prompts: Prompts


def parse_config(config_path: Path) -> Config:
    """
    Parses YAML configuration from specified path.
    """
    with open(config_path, "r", encoding="utf-8") as f:
        return Config(**yaml.safe_load(f))
