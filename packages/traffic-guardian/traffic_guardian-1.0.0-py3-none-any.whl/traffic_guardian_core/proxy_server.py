import json
import re
from twisted.web import proxy, http

from traffic_guardian_core.persistency import read_proxy_rules_form_json, get_proxy_rules_json_filename, \
    write_proxy_rules_form_json


def get_sorted_proxy_rules_from_newest_to_oldest():
    proxy_rules = read_proxy_rules_form_json(get_proxy_rules_json_filename())
    if len(proxy_rules.keys()) != 0:
        return reversed(sorted(proxy_rules, key=lambda id: proxy_rules[id]["creation_time"]))
    else:
        return []


class TrafficGuardianProxyRequest(proxy.ProxyRequest):
    def process(self):
        try:
            proxy_rules = read_proxy_rules_form_json(get_proxy_rules_json_filename())
            print(f"Reveived request {self.method} {self.uri}")
            if len(proxy_rules.keys()) != 0:

                proxy_rule_id = None
                proxy_rule = None
                for rule_id in get_sorted_proxy_rules_from_newest_to_oldest():
                    rule = proxy_rules[rule_id]
                    pattern = re.compile(rule["rule_uri_regex"])
                    print(f"checking rule {rule_id}")
                    if pattern.match(self.uri.decode('utf-8')):
                        print(f"rule chosen {rule_id}, {rule}")
                        proxy_rule_id = rule_id
                        proxy_rule = rule
                        break

                print(f'Request being mocked with {proxy_rule["mocked_status_code"]} status code '
                      f'matched with method {rule["rule_http_method"]} and regex {proxy_rule["rule_uri_regex"]}'
                      f'using {proxy_rule_id} rule!')

                raw_headers = self.getAllHeaders()
                decoded_headers = { key.decode('utf-8'): raw_headers[key].decode('utf-8') for key in raw_headers}

                proxy_rule["last_request_done_for_rule"] = {
                    "uri": self.uri.decode('utf-8'),
                    "headers": decoded_headers
                }
                proxy_rules[rule_id] = proxy_rule
                write_proxy_rules_form_json(get_proxy_rules_json_filename(), proxy_rules)

                self.setResponseCode(proxy_rule["mocked_status_code"])
                if rule["response_json_body"] is not None:
                    self.setHeader("content-type", b'application/json')
                    self.write(bytes(json.dumps(rule["response_json_body"]), 'utf-8'))
                self.finish()
            else:
                proxy.ProxyRequest.process(self)
        except KeyError:
            print("HTTPS is not supported at the moment!")


class TrafficGuardianProxy(proxy.Proxy):
    requestFactory = TrafficGuardianProxyRequest


class TrafficGuardianProxyFactory(http.HTTPFactory):
    def buildProtocol(self, addr):
        return TrafficGuardianProxy()
