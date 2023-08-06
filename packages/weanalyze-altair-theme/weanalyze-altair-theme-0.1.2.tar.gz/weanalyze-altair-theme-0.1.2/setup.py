# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['weanalyze_altair_theme']

package_data = \
{'': ['*']}

install_requires = \
['altair>=4.2.0,<5.0.0']

setup_kwargs = {
    'name': 'weanalyze-altair-theme',
    'version': '0.1.2',
    'description': "Weanalyze's theme for Altair charts.",
    'long_description': '# weanalyze-altair-theme <img align="right" src="https://raw.githubusercontent.com/weanalyze/weanalyze-altair-theme/master/assets/logo.svg" height="96" />\n\n[![PyPI](https://img.shields.io/pypi/v/weanalyze-altair-theme)](https://pypi.org/project/weanalyze-altair-theme/) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/weanalyze/weanalyze-altair-theme/master?labpath=demo.ipynb)\n\nWeAnalyze\'s theme for [Altair](https://github.com/altair-viz/altair) charts.\n\n## Sneak peek\n\n![Examples of charts with the weanalyze-altair-theme applied](https://raw.githubusercontent.com/weanalyze/weanalyze-altair-theme/master/assets/weanalyze_logo.svg)\n\n## Quickstart\n\n### Installation\n\nVia [pip](https://github.com/pypa/pip):\n\n```bash\npip install weanalyze-altair-theme\n```\n\n### Usage\n\n```python\nimport altair as alt\n\nalt.themes.enable("weanalyze")\n```\n',
    'author': 'jiandong',
    'author_email': 'jiandong@weanalyze.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
