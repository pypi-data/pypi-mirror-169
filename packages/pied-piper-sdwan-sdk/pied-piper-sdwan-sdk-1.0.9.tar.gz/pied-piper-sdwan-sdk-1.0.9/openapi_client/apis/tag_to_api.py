import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.authentication_api import AuthenticationApi
from openapi_client.apis.tags.sdwan_fabric_devices_api import SDWANFabricDevicesApi
from openapi_client.apis.tags.sdwan_device_template_api import SDWANDeviceTemplateApi
from openapi_client.apis.tags.sdwan_device_policy_api import SDWANDevicePolicyApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.SDWAN_FABRIC_DEVICES: SDWANFabricDevicesApi,
        TagValues.SDWAN_DEVICE_TEMPLATE: SDWANDeviceTemplateApi,
        TagValues.SDWAN_DEVICE_POLICY: SDWANDevicePolicyApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.SDWAN_FABRIC_DEVICES: SDWANFabricDevicesApi,
        TagValues.SDWAN_DEVICE_TEMPLATE: SDWANDeviceTemplateApi,
        TagValues.SDWAN_DEVICE_POLICY: SDWANDevicePolicyApi,
    }
)
