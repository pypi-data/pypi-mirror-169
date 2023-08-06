import multiprocessing

from twisted.internet import reactor

from .proxy_rules_govenor import app
from .proxy_server import *


def run():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('proxy_server_port', default=8080,
                    nargs='?', type=int, help="Proxy server port by default set to 8080")
    ap.add_argument('proxy_rules_governor_port', default=9090,
                    nargs='?', type=int, help="Proxy rules governor REST API port by default set to 9090")
    ns = ap.parse_args()

    def start_proxy_server():
        reactor.listenTCP(ns.proxy_server_port, TrafficGuardianProxyFactory())
        reactor.run()

    def start_rules_govenor():
        app.run(port=ns.proxy_rules_governor_port)

    proxy_server_thread = multiprocessing.Process(target=start_proxy_server)
    rules_govenor_thread = multiprocessing.Process(target=start_rules_govenor)

    proxy_server_thread.start()
    rules_govenor_thread.start()