from __future__ import print_function
import logicmonitor_sdk
from logicmonitor_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: LMv1
configuration = logicmonitor_sdk.Configuration()
configuration.company = 'lmnishulsharma'
configuration.access_id = 'f29A56Y9QUmkez62rMHa'
configuration.access_key = 't4)qi9]I6_XPNQ7z)^PuD=])-H3tw9TQy}ww}5QQ'

# create an instance of the API class
api_instance = logicmonitor_sdk.LMApi(logicmonitor_sdk.ApiClient(configuration))

body = {
    "name": "awstest2"
}

try:
    # add device group
    api_response = api_instance.add_device_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LMApi->addDeviceGroup: %s\n" % e)

