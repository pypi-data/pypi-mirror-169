.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/traffic_guardian.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/traffic_guardian
    .. image:: https://readthedocs.org/projects/traffic_guardian/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://traffic_guardian.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/traffic_guardian/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/traffic_guardian
    .. image:: https://img.shields.io/pypi/v/traffic_guardian.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/traffic_guardian/
    .. image:: https://img.shields.io/conda/vn/conda-forge/traffic_guardian.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/traffic_guardian
    .. image:: https://pepy.tech/badge/traffic_guardian/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/traffic_guardian
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/traffic_guardian

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

|

================
traffic_guardian
================


    Proxy server for intercepting HTTP traffic with python library to dynamically manage the proxy rules

Solution consists of two main components that are implemented inside `traffic_guardian_core` package:
 1. Proxy server based on `twisted` networking engine running by default on port 8080
 2. REST API to govern the proxy rules used for intercepting and mocking responses by default on port 9090

Based on REST API for governing the proxy rules python library has been developed inside `traffic_guardian` package.

Usage
=====
To install `traffic_guardian` use following command (assuming that you have `pip` installed):

.. code-block:: bash

    $ pip install traffic_guardian

To run the proxy server on default port (8080 for proxy server, 9090 for REST API to govern the proxy rules) use the following command:

.. code-block:: bash

    $ traffic_guardian

To check more help with the CLI tool use the following command

.. code-block:: bash

    $ traffic_guardian -h

Docs
====
Documentation to project is hosted on readthedocs.org under following link https://traffic-guardian.readthedocs.io/en/latest/



.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
