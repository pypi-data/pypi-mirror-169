import uuid
import logging
from datetime import datetime
from flask import Flask

from traffic_guardian_core.persistency import write_proxy_rules_form_json, read_proxy_rules_form_json, \
    get_proxy_rules_json_filename

FORMAT = "[%(asctime)s] %(message)s"
logging.basicConfig(format=FORMAT)
logger = logging.getLogger()


app = Flask(__name__)


@app.route("/addNewProxyRule", methods=['PUT'])
def add_new_rule():
    from flask import request

    request_data = request.get_json()

    rule_id = str(uuid.uuid4())

    proxy_rules = read_proxy_rules_form_json(get_proxy_rules_json_filename())

    if request_data["response_json_mock_body"] is not None:
        json_mock_body = request_data["response_json_mock_body"]
    else:
        json_mock_body = None

    proxy_rules[rule_id] =  {
        "rule_uri_regex": request_data["rule_uri_regex"],
        "rule_http_method": request_data["rule_http_method"],
        "mocked_status_code": request_data["mocked_status_code"],
        "response_json_body": json_mock_body,
        "creation_time": str(datetime.now().time())
    }

    write_proxy_rules_form_json(get_proxy_rules_json_filename(), proxy_rules)
    logger.info(f"Rule {rule_id} has been sucessfully added")
    return {"rule_token": rule_id}, 201


@app.route("/deleteProxyRule/<rule_id>", methods=['DELETE'])
def delete_existing_rule(rule_id: str):
    proxy_rules = read_proxy_rules_form_json(get_proxy_rules_json_filename())
    if rule_id not in proxy_rules.keys():
        logger.info(f"Rule {rule_id} does not exist!")
        return {"message": f"Rule {rule_id} does not exist!"}, 400
    else:
        proxy_rules.pop(rule_id)
        write_proxy_rules_form_json(get_proxy_rules_json_filename(), proxy_rules)
        logger.info(f"Rule {rule_id} has been sucessfully removed")
        return {"message": f"Rule {rule_id} has been sucessfully removed"}, 202


@app.route("/getLastRequestDetailsForProxyRule/<rule_id>", methods=['GET'])
def get_details_about(rule_id: str):
    proxy_rules = read_proxy_rules_form_json(get_proxy_rules_json_filename())
    if rule_id not in proxy_rules.keys():
        logger.info(f"Rule {rule_id} does not exist!")
        return {"message": f"Rule {rule_id} does not exist!"}, 400
    else:
        proxy_rule = proxy_rules[rule_id]
        if "last_request_done_for_rule" in proxy_rule.keys():
            logger.info(f"Rule {rule_id} last request executed details returned")
            return proxy_rule["last_request_done_for_rule"], 200
        else:
            logger.info(f"Rule {rule_id} doesn't have any requests intercepted yet!")
            return { "uri": "", "headers": {} }, 200


@app.route("/deleteAllProxyRules", methods=['DELETE'])
def delete_all_existing_proxy_rules():
    write_proxy_rules_form_json(get_proxy_rules_json_filename(), {})
    logger.info(f"All rules has been sucessfully removed")
    return {"message": f"All rules has been sucessfully removed"}, 202