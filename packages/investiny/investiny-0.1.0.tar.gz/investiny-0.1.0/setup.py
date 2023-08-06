# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['investiny']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.0,<0.24.0']

setup_kwargs = {
    'name': 'investiny',
    'version': '0.1.0',
    'description': '`investpy` but made tiny.',
    'long_description': '# 🤏🏻 `investpy` but made tiny\n\nSuuuuuuuper simple and tiny `investpy` replacement while I try to fix it! Here I\'ll try\nto add more or less the same functionality that was developed for `investpy` while keeping this\npackage tiny and up-to-date, as some solutions just work temporarily.\n\nEveryone using `investiny` please go thank @ramakrishnamekala129 for proposing this solution\nthat seems to be stable and working fine so far (fingers crossed!). Also take the chance to explore\nany other solution proposed by the `investpy` users at https://github.com/alvarobartt/investpy/issues.\n\nI\'m currently waiting to have a conversation with Investing.com so as to see whether we can get\nto some sort of an agreement in order to keep `investpy` alive.\n\nIn the meantime you can follow me at https://twitter.com/alvarobartt as I post updates there, and\nI highly appreciate your feedback.\n\n@adelRosal, an `investpy` user created a change.org site so as to show some support, so please sign\nthe petition as it may be useful towards the continuity of `investpy` at https://www.change.org/p/support-from-investing-com-for-the-continuity-of-investpy-library\n\nFinally, remember that `investiny` is super simple and tiny and shouldn\'t be considered reliable, it\'s\nworking fine so far, but it may be discontinued, so please use it carefully.\n\n## 🤏🏻 Usage\n\n```python\nfrom investiny import historical_data\n\ndata = historical_data(investing_id=6408, from_date="09/01/2022", to_date="10/01/2022") # Returns AAPL historical data as JSON (without date)\n```\n\n## 🔮 TODOs\n\n- [ ] Add Search API as also available https://tvc4.investing.com/.../search?limit=30&query=USD&type=&exchange= (thanks again @ramakrishnamekala129)\n- [ ] Add error basic error handling\n',
    'author': 'Alvaro Bartolome',
    'author_email': 'alvarobartt@yahoo.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/alvarobartt/investiny',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
