"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""
import requests
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('ctm360-cyna')

error_msg = {
    400: "Bad Request -- Your request is invalid.",
    401: "Unauthorized -- Wrong Credentials provided.",
    403: "Access Denied -- The data requested is hidden for administrators only.",
    404: "Not Found -- The specified data could not be found.",
    405: "Method Not Allowed -- You tried to access a API Endpoint with an invalid method.",
    406: "Not Acceptable -- You requested a format that isn't json.",
    410: "Gone -- The data requested has been removed from our servers.",
    429: "Too Many Requests -- You're requesting too frequently! Slow down!",
    500: "Internal Server Error -- We had a problem with our server. Try again later.",
    503: "Service Unavailable -- We're temporarily offline for maintenance. Please try again later.",
    'time_out': 'The request timed out while trying to connect to the remote server',
    'ssl_error': 'SSL certificate validation failed'
}


class CTM360:
    def __init__(self, config):
        self.base_url = config.get('server','').strip('/')
        if not self.base_url.startswith('https://') and not self.base_url.startswith('http://'):
            self.base_url = 'https://{0}'.format(self.base_url)
        self.api_key = config.get('api_key')
        self.verify_ssl = config.get('verify_ssl')

    def make_rest_call(self, endpoint, query_params={}, req_params={}, method='GET'):
        service_endpoint = '{0}{1}'.format(self.base_url, endpoint)
        logger.info('Request URL {}'.format(service_endpoint))

        try:
            headers = {'api-key': self.api_key}
            response = requests.request(
                method=method,
                url=service_endpoint,
                headers=headers,
                verify=self.verify_ssl,
                params=query_params,
                data=req_params
            )

            if response.ok:
                if response.status_code == 204:
                    return {"status": "success", "message": "No content returned"}
                return response.json()
            if error_msg[response.status_code]:
                raise ConnectorError('{}'.format(
                    error_msg[response.status_code]))
            response.raise_for_status()
        except requests.exceptions.SSLError as e:
            logger.exception('{}'.format(e))
            raise ConnectorError('{}'.format(error_msg['ssl_error']))
        except requests.exceptions.ConnectionError as e:
            logger.exception('{}'.format(e))
            raise ConnectorError('{}'.format(error_msg['time_out']))
        except Exception as e:
            logger.exception('{}'.format(e))
            raise ConnectorError('{}'.format(e))


def _check_health(config):
    ctm = CTM360(config)
    resp = ctm.make_rest_call(endpoint='/api/v1/news')
    if resp:
        logger.info('connector available')
        return True
    return False

def filter_params(params):
    filtered_params = {k: v for k,
                       v in params.items() if v is not None and v != ''}
    return filtered_params


def get_cyber_news(config, params):
    ctm = CTM360(config)
    query_params = {
        'size': params.get('size'),
        'start_date': params.get('start_date'),
        'end_date': params.get('end_date'),
        'fields': params.get('fields'),
        'search_after': params.get('search_after')
    }
    query_params = filter_params(query_params)
    return  ctm.make_rest_call(endpoint='/api/v1/news', method='GET', query_params=query_params)


operations = {
    'get_cyber_news': get_cyber_news
}
