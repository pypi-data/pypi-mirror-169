# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['available']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'dom-available',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Is \'domain.x\' Available?\n\n> IN WHOIS WE TRUST\n\nMy cheap way of checking whether a domain is available to be purchased or not (powered by [whois](https://github.com/domainr/whois)).\n\n#### Disclaimer\nThis package _might not_ be able to check the available for _every_ possible domain TLD, since `whois` does not work with some TLDs. In the future, I might include options to call different APIs (Gandi API, Domainr, etc.).\n\n### Example\n\n```Python\npackage main\n\nfrom available.checker import safe_domain\n\ndomain := "dreamdomain.io"\navailable, isBadTld = safe_domain(domain)\n\nif available :\n        print("[+] Success!")\n        \n```',
    'author': 'Aman Jha',
    'author_email': 'amanjha22@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
