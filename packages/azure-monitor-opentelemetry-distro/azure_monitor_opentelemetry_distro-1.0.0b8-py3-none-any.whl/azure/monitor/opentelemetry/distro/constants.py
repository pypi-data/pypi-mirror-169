import socket
from os import environ

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License in the project root for
# license information.
# --------------------------------------------------------------------------

STATUS_LOGGER_NAME = "azure.monitor.opentelemetry.diagnostics.status_logger"
DIAGNOSTIC_LOGGER_NAME = "opentelemetry"
# TODO change for commit
# LOGGER_PATH_LINUX = "/var/log/applicationinsights"
LOGGER_PATH_LINUX = ""
DIAGNOSTIC_LOGGER_FILE_NAME = "applicationinsights-extension.log"
STATUS_LOGGER_FILE_NAME = "status_python.json"
OPERATION = "Startup"
DEFAULT_IKEY_VALUE = "unknown"
MACHINE_NAME = socket.gethostname()


def default_env_var(var_name, default_val=""):
    try:
        return environ[var_name]
    except KeyError:
        return default_val


def get_customer_ikey():
    try:
        environ["APPLICATIONINSIGHTS_CONNECTION_STRING"].split(";")[0].split("=")[1]
    except KeyError:
        return DEFAULT_IKEY_VALUE


SITE_NAME = default_env_var("WEBSITE_SITE_NAME")
SUBSCRIPTION_ID = default_env_var("WEBSITE_OWNER_NAME")
EXTENSION_VERSION = default_env_var(
    "ApplicationInsightsAgent_EXTENSION_VERSION", "disabled"
)
CUSTOMER_IKEY = get_customer_ikey()
