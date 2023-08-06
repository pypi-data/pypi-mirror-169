# DeviceServer.DevicesApi

All URIs are relative to *http://localhost/DeviceServer*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_devices**](DevicesApi.md#get_devices) | **GET** /Devices | GET list of devices
[**get_devices_button**](DevicesApi.md#get_devices_button) | **GET** /Devices/Button/{device_id} | GET state of button
[**get_devices_device_id_ports**](DevicesApi.md#get_devices_device_id_ports) | **GET** /Devices/{device_id}/Ports | GET all ports for device
[**get_devices_index**](DevicesApi.md#get_devices_index) | **GET** /Devices/{device_id} | GET single device
[**get_devices_leds**](DevicesApi.md#get_devices_leds) | **GET** /Devices/{device_id}/Leds/{led_index} | GET state of LED
[**get_devices_port**](DevicesApi.md#get_devices_port) | **GET** /Devices/{device_id}/Ports/{port_index} | GET status of port
[**get_port**](DevicesApi.md#get_port) | **GET** /Ports/{port_index} | GET status of port
[**put_devices_leds_index**](DevicesApi.md#put_devices_leds_index) | **PUT** /Devices/{device_id}/Leds/{led_index} | PUT state of LED
[**put_devices_ports**](DevicesApi.md#put_devices_ports) | **PUT** /Devices/{device_id}/Ports/{port_index} | PUT state of port
[**put_devices_ports_pulse**](DevicesApi.md#put_devices_ports_pulse) | **PUT** /Devices/{device_id}/Ports/{port_index}/Pulse | PUT port into state for period of time
[**put_ports**](DevicesApi.md#put_ports) | **PUT** /Ports/{port_index} | PUT state of port
[**put_ports_pulse**](DevicesApi.md#put_ports_pulse) | **PUT** /Ports/{port_index}/Pulse | PUT port into state for period of time


# **get_devices**
> list[Device] get_devices()

GET list of devices

Returns list of devices

### Example

```python
from __future__ import print_function
import time
import DeviceServer
from DeviceServer.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/DeviceServer
# See configuration.py for a list of all supported configuration parameters.
configuration = DeviceServer.Configuration(
    host = "http://localhost/DeviceServer"
)


# Enter a context with an instance of the API client
with DeviceServer.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = DeviceServer.DevicesApi(api_client)
    
    try:
        # GET list of devices
        api_response = api_instance.get_devices()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->get_devices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Device]**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_button**
> InlineResponse200 get_devices_button(device_id, button_index)

GET state of button

Returns state of the selected devices button

### Example

```python
from __future__ import print_function
import time
import DeviceServer
from DeviceServer.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/DeviceServer
# See configuration.py for a list of all supported configuration parameters.
configuration = DeviceServer.Configuration(
    host = "http://localhost/DeviceServer"
)


# Enter a context with an instance of the API client
with DeviceServer.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = DeviceServer.DevicesApi(api_client)
    device_id = 'device_id_example' # str | UUID of device
button_index = 56 # int | index of the button on tha device (1-100)

    try:
        # GET state of button
        api_response = api_instance.get_devices_button(device_id, button_index)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->get_devices_button: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| UUID of device | 
 **button_index** | **int**| index of the button on tha device (1-100) | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_device_id_ports**
> list[Port] get_devices_device_id_ports(device_id)

GET all ports for device

returns a list of all ports attached to a device

### Example

```python
from __future__ import print_function
import time
import DeviceServer
from DeviceServer.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/DeviceServer
# See configuration.py for a list of all supported configuration parameters.
configuration = DeviceServer.Configuration(
    host = "http://localhost/DeviceServer"
)


# Enter a context with an instance of the API client
with DeviceServer.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = DeviceServer.DevicesApi(api_client)
    device_id = 'device_id_example' # str | UUID of device

    try:
        # GET all ports for device
        api_response = api_instance.get_devices_device_id_ports(device_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->get_devices_device_id_ports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| UUID of device | 

### Return type

[**list[Port]**](Port.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_index**
> Device get_devices_index(device_id)

GET single device

Gets information for a single device

### Example

```python
from __future__ import print_function
import time
import DeviceServer
from DeviceServer.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/DeviceServer
# See configuration.py for a list of all supported configuration parameters.
configuration = DeviceServer.Configuration(
    host = "http://localhost/DeviceServer"
)


# Enter a context with an instance of the API client
with DeviceServer.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = DeviceServer.DevicesApi(api_client)
    device_id = 'device_id_example' # str | UUID of device

    try:
        # GET single device
        api_response = api_instance.get_devices_index(device_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->get_devices_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| UUID of device | 

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_leds**
> InlineResponse200 get_devices_leds(device_id, led_index)

GET state of LED

Returns state of selected led on selected device

### Example

```python
from __future__ import print_function
import time
import DeviceServer
from DeviceServer.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/DeviceServer
# See configuration.py for a list of all supported configuration parameters.
configuration = DeviceServer.Configuration(
    host = "http://localhost/DeviceServer"
)


# Enter a context with an instance of the API client
with DeviceServer.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = DeviceServer.DevicesApi(api_client)
    device_id = 'device_id_example' # str | UUID of device
led_index = 56 # int | Index of LED

    try:
        # GET state of LED
        api_response = api_instance.get_devices_leds(device_id, led_index)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->get_devices_leds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| UUID of device | 
 **led_index** | **int**| Index of LED | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_port**
> Port get_devices_port(device_id, port_index)

GET status of port

returns status of ports

### Example

```python
from __future__ import print_function
import time
import DeviceServer
from DeviceServer.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/DeviceServer
# See configuration.py for a list of all supported configuration parameters.
configuration = DeviceServer.Configuration(
    host = "http://localhost/DeviceServer"
)


# Enter a context with an instance of the API client
with DeviceServer.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = DeviceServer.DevicesApi(api_client)
    device_id = 'device_id_example' # str | UUID of device
port_index = 56 # int | Index of port

    try:
        # GET status of port
        api_response = api_instance.get_devices_port(device_id, port_index)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->get_devices_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| UUID of device | 
 **port_index** | **int**| Index of port | 

### Return type

[**Port**](Port.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_port**
> Port get_port(port_index)

GET status of port

status of port

### Example

```python
from __future__ import print_function
import time
import DeviceServer
from DeviceServer.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/DeviceServer
# See configuration.py for a list of all supported configuration parameters.
configuration = DeviceServer.Configuration(
    host = "http://localhost/DeviceServer"
)


# Enter a context with an instance of the API client
with DeviceServer.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = DeviceServer.DevicesApi(api_client)
    port_index = 56 # int | Index of port

    try:
        # GET status of port
        api_response = api_instance.get_port(port_index)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DevicesApi->get_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port_index** | **int**| Index of port | 

### Return type

[**Port**](Port.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_devices_leds_index**
> put_devices_leds_index(device_id, led_index, state)

PUT state of LED

Set led at index on selected device

### Example

```python
from __future__ import print_function
import time
import DeviceServer
from DeviceServer.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/DeviceServer
# See configuration.py for a list of all supported configuration parameters.
configuration = DeviceServer.Configuration(
    host = "http://localhost/DeviceServer"
)


# Enter a context with an instance of the API client
with DeviceServer.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = DeviceServer.DevicesApi(api_client)
    device_id = 'device_id_example' # str | UUID of device
led_index = 56 # int | Index of LED
state = True # bool | True = LED on, False = LED off

    try:
        # PUT state of LED
        api_instance.put_devices_leds_index(device_id, led_index, state)
    except ApiException as e:
        print("Exception when calling DevicesApi->put_devices_leds_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| UUID of device | 
 **led_index** | **int**| Index of LED | 
 **state** | **bool**| True &#x3D; LED on, False &#x3D; LED off | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_devices_ports**
> put_devices_ports(device_id, port_index, state)

PUT state of port

Set State of Port 

### Example

```python
from __future__ import print_function
import time
import DeviceServer
from DeviceServer.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/DeviceServer
# See configuration.py for a list of all supported configuration parameters.
configuration = DeviceServer.Configuration(
    host = "http://localhost/DeviceServer"
)


# Enter a context with an instance of the API client
with DeviceServer.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = DeviceServer.DevicesApi(api_client)
    device_id = 'device_id_example' # str | UUID of device
port_index = 56 # int | Index of port
state = 56 # int | state id to switch to, 1 or more

    try:
        # PUT state of port
        api_instance.put_devices_ports(device_id, port_index, state)
    except ApiException as e:
        print("Exception when calling DevicesApi->put_devices_ports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| UUID of device | 
 **port_index** | **int**| Index of port | 
 **state** | **int**| state id to switch to, 1 or more | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_devices_ports_pulse**
> put_devices_ports_pulse(device_id, port_index, time, state)

PUT port into state for period of time

Pulse port from one state to another for a period of time in seconds

### Example

```python
from __future__ import print_function
import time
import DeviceServer
from DeviceServer.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/DeviceServer
# See configuration.py for a list of all supported configuration parameters.
configuration = DeviceServer.Configuration(
    host = "http://localhost/DeviceServer"
)


# Enter a context with an instance of the API client
with DeviceServer.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = DeviceServer.DevicesApi(api_client)
    device_id = 'device_id_example' # str | UUID of device
port_index = 56 # int | Index of port
time = 3.4 # float | time in seconds to press for 0.1 = 100ms
state = 56 # int | state to switch to

    try:
        # PUT port into state for period of time
        api_instance.put_devices_ports_pulse(device_id, port_index, time, state)
    except ApiException as e:
        print("Exception when calling DevicesApi->put_devices_ports_pulse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | [**str**](.md)| UUID of device | 
 **port_index** | **int**| Index of port | 
 **time** | **float**| time in seconds to press for 0.1 &#x3D; 100ms | 
 **state** | **int**| state to switch to | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_ports**
> put_ports(port_index, state)

PUT state of port

Set State of Port 

### Example

```python
from __future__ import print_function
import time
import DeviceServer
from DeviceServer.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/DeviceServer
# See configuration.py for a list of all supported configuration parameters.
configuration = DeviceServer.Configuration(
    host = "http://localhost/DeviceServer"
)


# Enter a context with an instance of the API client
with DeviceServer.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = DeviceServer.DevicesApi(api_client)
    port_index = 56 # int | Index of port
state = 56 # int | state id to switch to, 1 or more

    try:
        # PUT state of port
        api_instance.put_ports(port_index, state)
    except ApiException as e:
        print("Exception when calling DevicesApi->put_ports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port_index** | **int**| Index of port | 
 **state** | **int**| state id to switch to, 1 or more | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_ports_pulse**
> put_ports_pulse(port_index, time, state)

PUT port into state for period of time

Pulse port from one state to another for a period of time in seconds

### Example

```python
from __future__ import print_function
import time
import DeviceServer
from DeviceServer.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/DeviceServer
# See configuration.py for a list of all supported configuration parameters.
configuration = DeviceServer.Configuration(
    host = "http://localhost/DeviceServer"
)


# Enter a context with an instance of the API client
with DeviceServer.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = DeviceServer.DevicesApi(api_client)
    port_index = 56 # int | Index of port
time = 3.4 # float | time in seconds to press for 0.1 = 100ms
state = 56 # int | state to switch to

    try:
        # PUT port into state for period of time
        api_instance.put_ports_pulse(port_index, time, state)
    except ApiException as e:
        print("Exception when calling DevicesApi->put_ports_pulse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port_index** | **int**| Index of port | 
 **time** | **float**| time in seconds to press for 0.1 &#x3D; 100ms | 
 **state** | **int**| state to switch to | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

