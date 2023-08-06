# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    J_SECURITY_CHECK = "/j_security_check"
    DATASERVICE_CLIENT_TOKEN = "/dataservice/client/token"
    DATASERVICE_DEVICE = "/dataservice/device"
    DATASERVICE_DEVICE_MONITOR = "/dataservice/device/monitor"
    DATASERVICE_DEVICE_COUNTERS = "/dataservice/device/counters"
    DATASERVICE_STATISTICS_INTERFACE = "/dataservice/statistics/interface"
    DATASERVICE_TEMPLATE_FEATURE = "/dataservice/template/feature"
    DATASERVICE_TEMPLATE_FEATURE_TYPES = "/dataservice/template/feature/types"
    DATASERVICE_TEMPLATE_POLICY_VEDGE_DEVICES = "/dataservice/template/policy/vedge/devices"
    DATASERVICE_TEMPLATE_POLICY_LIST = "/dataservice/template/policy/list"
