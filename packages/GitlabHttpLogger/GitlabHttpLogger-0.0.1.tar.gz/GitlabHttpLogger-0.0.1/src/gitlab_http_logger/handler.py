#! /usr/bin/python3
# -*- coding: utf-8 -*-

import json
import logging
from typing import List, Optional, Union

import requests


def convert_record_severity(record_level: int) -> str:
    """Convert a Python logging level to a one understood by GitLab.

    Args:
        record_level (int): The logging level ID.

    Returns:
        The name of the level as understood by gitlab.
    """
    if record_level < 10:  # NOTSET
        return "unknown"
    if record_level < 20:  # DEBUG
        return "info"
    if record_level < 30:  # INFO
        return "low"
    if record_level < 40:  # WARNING
        return "medium"
    if record_level < 50:  # ERROR
        return "high"
    else:  # CRITICAL
        return "critical"


class GitlabHTTPHandler(logging.Handler):

    def __init__(self, webhook_url: str, auth_key: str, title: Optional[str] = None,
                 monitoring_tool: Optional[str] = None,
                 hosts: Optional[Union[str, List[str]]] = None,
                 gitlab_environment_name: Optional[str] = None):
        logging.Handler.__init__(self)
        self.webhook_url = webhook_url
        self.auth_key = auth_key
        self.static_data = {}
        if title is not None:
            self.static_data["title"] = title
        if monitoring_tool is not None:
            self.static_data["monitoring_tool"] = monitoring_tool
        if hosts is not None:
            self.static_data["hosts"] = hosts
        if gitlab_environment_name is not None:
            self.static_data["gitlab_environment_name"] = gitlab_environment_name

    def emit(self, record: logging.LogRecord):
        data = {
            "description": record.msg,
            "start_time": record.created,
            "end_time": record.msecs,
            "severity": convert_record_severity(record.levelno),
            "service": record.processName,
            "lineno": record.lineno,
            "funcName": record.funcName,
        }
        # Create a new dictionary by merging data and self.static_data and send it.
        self.__send_package({**data, **self.static_data})

    def __send_package(self, data: dict):
        requests.post(
            url=self.webhook_url,
            headers={
                "Authorization": "Bearer " + self.auth_key,
                "Content-Type": "application/json",
            },
            data=json.dumps(data),
        )
