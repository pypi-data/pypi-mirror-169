# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python3_markdown_extension_graphviz']

package_data = \
{'': ['*']}

install_requires = \
['Markdown>=3.4.1,<4.0.0']

setup_kwargs = {
    'name': 'python3-markdown-extension-graphviz',
    'version': '0.1.0',
    'description': '',
    'long_description': 'Note: Forked to fix errors with latest version of Python-Markdown and migrate to\nusing Poetry.\n\n# Markdown Inline Graphviz (for Python 3)\n\nThis is just a continuation of the great job of Steffen Prince in [sprin/markdown-inline-graphviz](https://github.com/sprin/markdown-inline-graphviz),\nin order to get it work with pip3. If you use python 2, please use the original extension instead.\n\nA Python Markdown extension that replaces inline Graphviz definitions with\ninline SVGs or PNGs!\n\nWhy render the graphs inline? No configuration! Works with any\nPython-Markdown-based static site generator, suche originas\n[MkDocs](http://www.mkdocs.org/), [Pelican](http://blog.getpelican.com/), and\n[Nikola](https://getnikola.com/) out of the box without configuring an output\ndirectory.\n\n# Installation\n\n    $ pip3 install markdown_inline_graphviz_extension --user\n\n# Usage\n\nActivate the `markdown_inline_graphviz` extension. For example, with Mkdocs, you add a\nstanza to mkdocs.yml:\n\n```yaml\nmarkdown_extensions:\n  - markdown_inline_graphviz\n```\n\nTo use it in your Markdown doc, with SVG output:\n\n    ```graphviz dot attack_plan.svg\n    digraph G {\n        rankdir=LR\n        Earth [peripheries=2]\n        Mars\n        Earth -> Mars\n    }\n    ```\n\nor with PNG:\n\n    ```graphviz dot attack_plan.png\n    digraph G {\n        rankdir=LR\n        Earth [peripheries=2]\n        Mars\n        Earth -> Mars\n    }\n    ```\n\nAlternatively you can still using `{%` legacy notation but its not recommended.\n\n```\n{% dot attack_plan.svg\n    digraph G {\n        rankdir=LR\n        Earth [peripheries=2]\n        Mars\n        Earth -> Mars\n    }\n%}\n```\n\nSupported graphviz commands: dot, neato, fdp, sfdp, twopi, circo.\n\n# Credits\n\nInspired by [jawher/markdown-dot](https://github.com/jawher/markdown-dot),\nwhich renders the dot graph to a file instead of inline.\n\nForked from [sprin/markdown-inline-graphviz](https://github.com/sprin/markdown-inline-graphviz)\n\n# License\n\n[MIT License](http://www.opensource.org/licenses/mit-license.php)\n',
    'author': 'Manuel Brea',
    'author_email': 'm.brea.carreras@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
