# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['jptranstokenizer', 'jptranstokenizer.mainword', 'jptranstokenizer.subword']

package_data = \
{'': ['*']}

install_requires = \
['SudachiTra>=0.1.7,<0.2.0',
 'pyknp>=0.6.1,<0.7.0',
 'sentencepiece>=0.1.96,<0.2.0',
 'spacy>=3.2.0,<4.0.0',
 'transformers>=4.7.0,<5.0.0']

setup_kwargs = {
    'name': 'jptranstokenizer',
    'version': '0.0.4',
    'description': 'Japanese tokenizer with transformers library',
    'long_description': '<div id="top"></div>\n\n<h1 align="center">jptranstokenizer: Japanese Tokenzier for transformers</h1>\n\n<p align="center">\n  <img alt="Python" src="https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue">\n  <a href="https://pypi.python.org/pypi/jptranstokenizer">\n    <img alt="pypi" src="https://img.shields.io/pypi/v/jptranstokenizer.svg">\n  </a>\n  <a href="https://github.com/retarfi/jptranstokenizer#licenses">\n    <img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-brightgreen">\n  </a>\n  <a href="https://github.com/retarfi/jptranstokenizer/releases">\n    <img alt="GitHub release" src="https://img.shields.io/github/v/release/retarfi/jptranstokenizer.svg">\n  </a>\n</p>\n\nThis is a repository for japanese tokenizer with HuggingFace library.\n\n**issue は日本語でも大丈夫です。**\n\n\n<!-- TABLE OF CONTENTS -->\n<details>\n  <summary>Table of Contents</summary>\n  <ol>\n    <li>\n      <a href="#usage">Usage</a>\n    </li>\n    <li><a href="#roadmap">Roadmap</a></li>\n    <li>\n      <a href="#citation">Citation</a>\n      <ul>\n        <li><a href="#this-implementation">This Implementation</a></li>\n      </ul>\n    </li>\n    <li><a href="#licenses">Licenses</a></li>\n    <li><a href="#related-work">Related Work</a></li>\n  </ol>\n</details>\n\n\n## Usage\n\nTo be added\n\n\n<!-- ROADMAP -->\n\n## Roadmap\n\n\nSee the [open issues](https://github.com/retarfi/language-pretraining/issues) for a full list of proposed features (and known issues).\n\n## Citation\n\n\n**There will be another paper for this pretrained model.\nBe sure to check here again when you cite.**\n\n### This Implementation\n\n```\n@misc{suzuki-2022-github,\n  author = {Masahiro Suzuki},\n  title = {jptranstokenizer: Japanese Tokenzier for transformers},\n  year = {2022},\n  publisher = {GitHub},\n  journal = {GitHub repository},\n  howpublished = {\\url{https://github.com/retarfi/jptranstokenizer}}}\n```\n\n## Licenses\n\nThe codes in this repository are distributed under the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0).\n\n\n## Related Work\n- Pretrained Japanese BERT models (containing Japanese tokenizer)\n  - Autor NLP Lab. in Tohoku University\n  - https://github.com/cl-tohoku/bert-japanese\n- SudachiTra\n  - Author Works Applications\n  - https://github.com/WorksApplications/SudachiTra\n- UD_Japanese-GSD\n  - Author megagonlabs\n  - https://github.com/megagonlabs/UD_Japanese-GSD\n- Juman++\n  - Author Kurohashi Lab. in Universyti of Kyoto\n  - https://github.com/ku-nlp/jumanpp\n',
    'author': 'Masahiro Suzuki',
    'author_email': 'msuzuki9609@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
