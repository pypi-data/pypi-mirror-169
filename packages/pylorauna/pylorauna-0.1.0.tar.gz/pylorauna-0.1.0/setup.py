# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pylorauna']

package_data = \
{'': ['*']}

install_requires = \
['gql[all]>=3.4.0,<4.0.0']

setup_kwargs = {
    'name': 'pylorauna',
    'version': '0.1.0',
    'description': "API Wrapper for the Lorauna API. Lorauna refers to the 'Sauna Lorrainebad' in Bern, CH",
    'long_description': "# Sauna Lorrainebad API Wrapper 🧖🏽\u200d♀️\nIn Bern, CH there's a super sweet sauna down at the Aare.  \nTheir current capacity can be seen on their [website](https://saunalorrainebad.ch) or through this little API wrapper.\n\n## Example usage\n```python\nfrom pylorauna.lorauna import LoraunaClient\n\nclient = LoraunaClient()\ndata = client.get_data()\nprint(data.capacity_message)\n# $ Mir hei no bis Endi Oktober Summerpouse.\n```",
    'author': 'Elia Bieri',
    'author_email': 'contact@eliabieri.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
