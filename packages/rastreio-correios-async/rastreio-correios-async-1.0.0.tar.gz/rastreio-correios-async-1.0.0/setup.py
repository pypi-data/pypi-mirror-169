# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rastreio_correios']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0']

setup_kwargs = {
    'name': 'rastreio-correios-async',
    'version': '1.0.0',
    'description': 'Programa não oficial de rastreio de encomendas dos correios.',
    'long_description': '# 🐍 Rastreador de Encomendas\n\n## Esse programa tem como seu intuito fazer o rastreio de encomendas dos correios\n\n- Rastreio de encomendas\n\n## Como utilizar?\n\n```Python\nfrom asyncio import run\n\nfrom rastreio_correios import Rastreio\n\n\nasync def main():\n    rastreio = Rastreio()\n    resultado = await rastreio.rastrear()\n    print(resultado)\n\n\nrun(main())\n```\n\n### O que usamos na infraestrutura?\n\n- [Utilizamos a linguagem Python](https://www.python.org/)\n',
    'author': 'Diaszano',
    'author_email': 'lucasdiiassantos@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
