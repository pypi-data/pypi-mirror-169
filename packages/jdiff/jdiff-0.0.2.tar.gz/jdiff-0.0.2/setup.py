# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jdiff', 'jdiff.utils']

package_data = \
{'': ['*']}

install_requires = \
['deepdiff>=5.5.0,<6.0.0', 'jmespath>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'jdiff',
    'version': '0.0.2',
    'description': 'A light-weight library to compare structured output from network devices show commands.',
    'long_description': '# jdiff\n\n`jdiff` is a lightweight Python library allowing you to examine structured data. `jdiff` provides an interface to intelligently compare--via key presense/absense and value comparison--JSON data objects\n\nOur primary use case is the examination of structured data returned from networking devices, such as:\n\n* Compare the operational state of network devices pre and post change\n* Compare operational state of a device vs a "known healthy" state\n* Compare state of similar devices, such as a pair of leafs or a pair of backbone routers\n* Compare operational state of a component (interface, vrf, bgp peering, etc.) migrated from one device to another\n\nHowever, the library fits other use cases where structured data needs to be operated on.\n\n## Installation \n\nInstall from PyPI:\n\n```\npip install jdiff\n```\n\n## Intelligent Comparison\n\nThe library provides the ability to ask more intelligent questions of a given data structure. Comparisons of data such as "Is my pre change state the same as my post change state", is not that interesting of a comparison. The library intends to ask intelligent questions _like_:\n\n* Is the route table within 10% of routes before and after a change?\n* Is all of the interfaces that were up before the change, still up?\n* Are there at least 10k sessions of traffic on my firewall?\n* Is there there at least 2 interfaces up within lldp neighbors?\n\n## Technical Overview\n\nThe library heavily relies on [JMESPath](https://jmespath.org/) for traversing the JSON object and finding the values to be evaluated. More on that [here](#customized-jmespath).\n\n`jdiff` has been developed around diffing and testing structured data returned from Network APIs and libraries (such as TextFSM) but is equally useful when working or dealing with data returned from APIs.\n\n## Documentation\n\nDocumentation is hosted on Read the Docs at [jdiff Documentation](https://jdiff.readthedocs.io/).\n',
    'author': 'Network to Code, LLC',
    'author_email': 'info@networktocode.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/networktocode/jdiff',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
