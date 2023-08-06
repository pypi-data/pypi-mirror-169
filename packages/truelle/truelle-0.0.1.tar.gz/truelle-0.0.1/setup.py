# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['truelle']

package_data = \
{'': ['*']}

install_requires = \
['parsel>=1.6.0,<2.0.0', 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'truelle',
    'version': '0.0.1',
    'description': 'A tiny web scraping library',
    'long_description': '# Truelle\n\n\n\nTruelle - "trowel" in french - is a tiny web scraping library, inspired by the great [Scrapy](https://scrapy.org/) framework, \ndepending only on [Requests](https://requests.readthedocs.io/en/latest/), and [Parsel](https://github.com/scrapy/parsel) libraries.\n\nTruelle only offers a sequential request processing, and returns items directly\nIt\'s intended to be embedded in tiny scripts. Spiders aims to be compatible with Scrapy spider and easily switch to a Scrapy.\n\n## Install\n\n    pip install truelle\n\n## Get started\n\n1. Create a Spider\n\n```python\nfrom truelle import Spider\n\nclass MySpider(Spider):\n    start_urls = [ "https://truelle.io" ]\n    \n    def parse(self, response: Response):\n        for title in response.css("h1::text").getall():\n            yield { "title": title }\n            \nspider = MySpider() \n```\n\n2. Then get your items back...\n\n... in vanilla Python:\n           \n```python\nfor item in spider.crawl():\n    do_something(item)\n```\n\n... in a Pandas dataframe:\n\n```python\nimport pandas as pd\nmy_df = pd.DataFrame(spider.crawl())\n```\n\n## Custom settings\n\n```python\ndef custom_fingerprint(request):\n    return "test"\n\ncustom_settings = {\n    "HTTP_CACHE_ENABLED": True,\n    "REQUEST_FINGERPRINTER": custom_fingerprint,\n    "HTTP_PROXY": "http://myproxy:8080",\n    "HTTPS_PROXY": "http://myproxy:8080",\n    "DOWNLOAD_DELAY": 2\n}\n\nspider.crawl(settings=custom_settings)\n```\n',
    'author': 'Jonathan Geslin',
    'author_email': 'jonathan.geslin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
