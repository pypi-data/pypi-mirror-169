import requests
import json

config = {
    "http_proxy_govenor_host": "localhost",
    "http_proxy_govenor_port": 9090
}


def set_config(host, port):
    """
    This function is to set up the host and port on which traffic_guardian proxy server is run
    :param host:
    :param port:
    :return:
    """
    config['http_proxy_govenor_host'] = host
    config['http_proxy_govenor_port'] = port


def __get_base_url():
    return f"http://{config['http_proxy_govenor_host']}:{config['http_proxy_govenor_port']}"


def __buildUrl(endpoint):
    return __get_base_url() + endpoint


def __getDefaultHeaders():
    return {
        'Content-Type': 'application/json'
    }


class ProxyRule:
    def __init__(self, rule_uri_regex: str, rule_http_method: str, mocked_status_code: int,
                 mocked_json_body: dict = None):
        """
        Example usage:
        ProxyRule(
            f"^http://api.sms.com/sms.do",
            "POST",
            200,
            {
                "count": 1,
                "list": [
                    {
                        "id": "12312312kjhkjhk3123lkjlk123",
                        "points": 0.16,
                        "number": "48123456789",
                        "date_sent": 1664224086,
                        "submitted_number": "481234567689",
                        "status": "QUEUE",
                        "error": None,
                        "idx": None,
                        "parts": 1
                    }
                ]
            }
        )
        :param rule_uri_regex: this should be a regex sting that is used by re.match() function to parse URI
        :param rule_http_method: this should be HTTP method of intercepted requedst
        :param mocked_status_code: this should be status code that should be used in mocked response
        :param mocked_json_body: this is optional and should be a dict that will be turned to JSON body and returned in mocked response
        """
        self.rule_uri_regex = rule_uri_regex
        self.rule_http_method = rule_http_method
        self.mocked_status_code = mocked_status_code
        self.mocked_json_body = mocked_json_body

    def get_json(self):
        return json.dumps({
            "rule_uri_regex": self.rule_uri_regex,
            "rule_http_method": self.rule_http_method,
            "mocked_status_code": self.mocked_status_code,
            "response_json_mock_body": self.mocked_json_body
        })


def add_rule(rule: ProxyRule) -> str:
    """
    Function used to create new rules to the proxy server as an input it takes instance of a ProxyRule class
    and on output it returns unique identifier of created rule
    :param rule:
    :return: unique identifier of created rule as str
    """
    payload = rule.get_json()

    url = __buildUrl("/addNewProxyRule")
    headers = __getDefaultHeaders()

    response = requests.put(url, headers=headers, data=payload)
    return response.json()["rule_token"]


def remove_rule(rule_id):
    """
    Function that removes the proxy rule added earlier using rule_id as and argument
    :param rule_id:
    """
    url = __buildUrl(f"/deleteProxyRule/{rule_id}")
    headers = __getDefaultHeaders()
    response = requests.delete(url, headers=headers)


def remove_all_proxy_rules():
    """
    Function removes all existing rules
    """
    url = __buildUrl("/deleteAllProxyRules")
    headers = __getDefaultHeaders()
    response = requests.delete(url, headers=headers)


def get_last_request_intercepted_by_proxy_rule(rule_id):
    """
    Function that returns URI and headers of last intercepted request by the rule
     of which identifier is passed as a parameter
    :param rule_id:
    :return: {
                    "uri": "http:example.uri/param=123?,
                    "headers": {
                        "Content-Type": "application/json
                    }
            }
    """
    url = __buildUrl(f"/getLastRequestDetailsForProxyRule/{rule_id}")
    headers = __getDefaultHeaders()
    response = requests.get(url, headers=headers)
    return response.json()


def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer


@parametrized
def with_proxy_rule(func, proxyRule: ProxyRule):
    """
    Decorator that will automatically add rule, execute test function and after all will remove rule

    Example usage:

    @traffic_guardian.with_proxy_rule(
        ProxyRule(
            f"^http://api.sms.com/sms.do",
            "POST",
            503
        )
    )
    def test_api_negative_scenario_with_decorator():
        pass

    :param func:
    :param proxyRule: this is an instance of ProxyRule class with specific proxy rule to be used by proxy server
    """
    def wrapper(*args, **kwargs):
        rule_id = add_rule(proxyRule)
        func(*args, **kwargs)
        remove_rule(rule_id)

    return wrapper
