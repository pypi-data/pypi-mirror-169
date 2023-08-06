import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.j_security_check import JSecurityCheck
from openapi_client.apis.paths.dataservice_client_token import DataserviceClientToken
from openapi_client.apis.paths.dataservice_device import DataserviceDevice
from openapi_client.apis.paths.dataservice_device_monitor import DataserviceDeviceMonitor
from openapi_client.apis.paths.dataservice_device_counters import DataserviceDeviceCounters
from openapi_client.apis.paths.dataservice_statistics_interface import DataserviceStatisticsInterface
from openapi_client.apis.paths.dataservice_template_feature import DataserviceTemplateFeature
from openapi_client.apis.paths.dataservice_template_feature_types import DataserviceTemplateFeatureTypes
from openapi_client.apis.paths.dataservice_template_policy_vedge_devices import DataserviceTemplatePolicyVedgeDevices
from openapi_client.apis.paths.dataservice_template_policy_list import DataserviceTemplatePolicyList

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.J_SECURITY_CHECK: JSecurityCheck,
        PathValues.DATASERVICE_CLIENT_TOKEN: DataserviceClientToken,
        PathValues.DATASERVICE_DEVICE: DataserviceDevice,
        PathValues.DATASERVICE_DEVICE_MONITOR: DataserviceDeviceMonitor,
        PathValues.DATASERVICE_DEVICE_COUNTERS: DataserviceDeviceCounters,
        PathValues.DATASERVICE_STATISTICS_INTERFACE: DataserviceStatisticsInterface,
        PathValues.DATASERVICE_TEMPLATE_FEATURE: DataserviceTemplateFeature,
        PathValues.DATASERVICE_TEMPLATE_FEATURE_TYPES: DataserviceTemplateFeatureTypes,
        PathValues.DATASERVICE_TEMPLATE_POLICY_VEDGE_DEVICES: DataserviceTemplatePolicyVedgeDevices,
        PathValues.DATASERVICE_TEMPLATE_POLICY_LIST: DataserviceTemplatePolicyList,
    }
)

path_to_api = PathToApi(
    {
        PathValues.J_SECURITY_CHECK: JSecurityCheck,
        PathValues.DATASERVICE_CLIENT_TOKEN: DataserviceClientToken,
        PathValues.DATASERVICE_DEVICE: DataserviceDevice,
        PathValues.DATASERVICE_DEVICE_MONITOR: DataserviceDeviceMonitor,
        PathValues.DATASERVICE_DEVICE_COUNTERS: DataserviceDeviceCounters,
        PathValues.DATASERVICE_STATISTICS_INTERFACE: DataserviceStatisticsInterface,
        PathValues.DATASERVICE_TEMPLATE_FEATURE: DataserviceTemplateFeature,
        PathValues.DATASERVICE_TEMPLATE_FEATURE_TYPES: DataserviceTemplateFeatureTypes,
        PathValues.DATASERVICE_TEMPLATE_POLICY_VEDGE_DEVICES: DataserviceTemplatePolicyVedgeDevices,
        PathValues.DATASERVICE_TEMPLATE_POLICY_LIST: DataserviceTemplatePolicyList,
    }
)
