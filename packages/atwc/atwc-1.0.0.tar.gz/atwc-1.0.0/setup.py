# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['atwc']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.1,<4.0.0']

setup_kwargs = {
    'name': 'atwc',
    'version': '1.0.0',
    'description': "Python interface to TWC's API",
    'long_description': '# aTWC - Python interface to Teamwork Cloud\n\nPython interface to NoMagic/CATIA Teamwork Cloud Server.\n\n[Teamwork Cloud](https://www.3ds.com/products-services/catia/products/no-magic/teamwork-cloud/) server is a central\nrepository service to store and retrieve [Cameo](https://www.3ds.com/products-services/catia/products/no-magic/cameo-systems-modeler/)\nand [MagicDraw](https://www.3ds.com/products-services/catia/products/no-magic/magicdraw/) models.\n\nTWC exposes a REST API that allows interaction with the stored models.\n\nThis library has been primarily written as interface abstraction for\nArchimedes Exhibitions GmbH\'s Cameo Collaborator Publisher service, hence it\'s\nnot intended as a general-purpose solution.\n\naTWC is developed and maintained by [Archimedes Exhibitions GmbH](https://www.archimedes-exhibitions.de). \n\n## Installation\n\n```bash\n$ pip3 install atwc\n```\n\n## Usage example\n\n```python\nimport asyncio\nimport atwc\n\n\nasync def main():\n    client = atwc.client.Client(\'https://twc.local:8111/osmc/\', \'user\', \'password\')\n\n    async with client.create_session():\n        browser = atwc.browsers.ResourceBrowser(client)\n        await browser.fetch()\n\n        print(\'MagicDraw resources:\')\n        for resource in browser.md_resources:\n            print(f\'  {await browser.get_category_path(resource)}/\'\n                  f\'{resource["dcterms:title"]}\')\n\n\nasyncio.run(main())\n```\n\n## Running the examples\n\nCopy the file `config.py.dist` into `config.py` in the `examples` folder:\n\n```bash\n$ cd examples\n$ cp config.py.dist config.py\n```\n\nEdit the file `config.py` and replace the placeholders for all the entries.\n\nMore information can be found in the docstring of each script.\n',
    'author': 'Marco Fagiolini',
    'author_email': 'mfx@amdx.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/amdx/atwc',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
