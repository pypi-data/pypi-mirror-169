# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['archetypes', 'archetypes.algorithms', 'archetypes.visualization']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.6.0,<4.0.0',
 'numpy>=1.23.3,<2.0.0',
 'scikit-learn>=1.1.2,<2.0.0',
 'scipy>=1.9.1,<2.0.0']

setup_kwargs = {
    'name': 'archetypes',
    'version': '0.3.0',
    'description': 'A scikit-learn compatible Python package for archetypal analysis',
    'long_description': '# Archetypes\n![PyPI](https://img.shields.io/pypi/v/archetypes)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/archetypes)\n[![Python package](https://github.com/aleixalcacer/archetypes/actions/workflows/python-package.yml/badge.svg)](https://github.com/aleixalcacer/archetypes/actions/workflows/python-package.yml)\n![PyPI - License](https://img.shields.io/pypi/l/archetypes)\n[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](CODE_OF_CONDUCT.md)\n\n**archetypes** is a [scikit-learn](https://scikit-learn.org) compatible Python package for archetypal analysis.\n\n\n## Installation\n\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install archetypes.\n\n```bash\npip install archetypes\n```\n\n\n## Usage\n\n```python\nimport archetypes as arch\nimport numpy as np\n\nX = np.random.normal(0, 1, (100, 2))\n\naa = arch.AA(n_archetypes=4)\n\nX_trans = aa.fit_transform(X)\n\n```\n\n## Contributing\n\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n\n## License\n\nDistributed under the BSD 3-Clause License. See [LICENSE](LICENSE) for more information.\n',
    'author': 'Aleix Alcacer',
    'author_email': 'aleixalcacer@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
