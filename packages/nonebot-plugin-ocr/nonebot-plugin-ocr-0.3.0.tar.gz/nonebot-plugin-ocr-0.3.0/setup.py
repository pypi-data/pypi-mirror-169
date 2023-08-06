# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_ocr', 'nonebot_plugin_ocr.bot', 'nonebot_plugin_ocr.ocr']

package_data = \
{'': ['*']}

install_requires = \
['diskcache>=5.4.0,<6.0.0',
 'httpx>=0.23.0,<0.24.0',
 'nonebot-adapter-onebot>=2.1.3,<3.0.0',
 'nonebot2>=2.0.0-beta.5,<3.0.0',
 'tomli>=2.0.1,<3.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-ocr',
    'version': '0.3.0',
    'description': 'OCR plugin for nonebot2',
    'long_description': '# nonebot-plugin-ocr\nOCR plugin for nonebot2\n',
    'author': 'NewYearPrism',
    'author_email': 'None',
    'maintainer': 'NewYearPrism',
    'maintainer_email': 'None',
    'url': 'https://github.com/NewYearPrism/nonebot-plugin-ocr',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
