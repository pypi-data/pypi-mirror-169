# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['schnitsum']

package_data = \
{'': ['*']}

install_requires = \
['torch>=1.12.1,<2.0.0', 'transformers>=4.22.2,<5.0.0']

setup_kwargs = {
    'name': 'schnitsum',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Schnitsum: Easy to use neural network based summarization models\n\nThis package enables to generate summaries of you documents of interests.\n\nCurrently, we support following models,\n\n- [BART (large)](https://aclanthology.org/2020.acl-main.703) fine-tuned on computer science papers (ref. [SciTLDR](https://aclanthology.org/2020.findings-emnlp.428)).\n  - Model name: `sobamchan/bart-large-scitldr`\n\nwe are planning to expand coverage soon to other domains, languages, models soon.\n\n\n# Installation\n\n```bash\npip install schnitsum  # or poetry add schnitsum\n```\n\nThis will let you generate summaries with CPUs only, if you want to utilize your GPUs, please follow the instruction by PyTorch, [here](https://pytorch.org/get-started/locally/).\n\n\n# Usage\n\n```py3\nfrom schnitsum import SchnitSum\nmodel = SchnitSum("sobamchan/bart-large-scitldr")\n\ndocs = [\n    "Document you want to summarize."\n]\n\nsummaries = model(docs)\nprint(summaries)\n```\n',
    'author': 'sobamchan',
    'author_email': 'oh.sore.sore.soutarou@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
