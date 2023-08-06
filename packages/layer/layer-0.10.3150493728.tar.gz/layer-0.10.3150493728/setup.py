# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['layer',
 'layer.cache',
 'layer.clients',
 'layer.clients.protomappers',
 'layer.cloudpickle',
 'layer.config',
 'layer.contracts',
 'layer.decorators',
 'layer.exceptions',
 'layer.executables',
 'layer.executables.entrypoint',
 'layer.flavors',
 'layer.logged_data',
 'layer.logged_data.loggers',
 'layer.main',
 'layer.projects',
 'layer.runs',
 'layer.tracker',
 'layer.utils',
 'layer.utils.grpc']

package_data = \
{'': ['*']}

modules = \
['pyproject']
install_requires = \
['Jinja2',
 'aiohttp>=3.7.3,<3.8.0',
 'boto3>=1.16.24',
 'cryptography>=3.4.7',
 'humanize>=3.11.0',
 'layer-api==0.9.384528',
 'lazy_loader==0.1rc3',
 'mlflow-skinny>=1.25.0',
 'networkx>=2.5',
 'nvsmi>=0.4.2,<0.5.0',
 'pandas==1.3.5',
 'polling>=0.3.1',
 'psutil>=5.4.8',
 'pyarrow==9.0.0',
 'pyjwt>=2.0.0,<3.0.0',
 'requests>=2.23.0',
 'rich>=11',
 'wrapt>=1.13.3',
 'yarl>=1.6.3']

extras_require = \
{':python_version >= "3.7" and python_version < "3.8"': ['numpy<1.22']}

setup_kwargs = {
    'name': 'layer',
    'version': '0.10.3150493728',
    'description': 'Layer AI SDK',
    'long_description': '<!---\nCopyright 2022 Layer. All rights reserved.\n\nLicensed under the Apache License, Version 2.0 (the "License");\nyou may not use this file except in compliance with the License.\nYou may obtain a copy of the License at\n\n    http://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an "AS IS" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.\n-->\n\n<p align="center">\n    <br>\n    <a href="https://layer.ai">\n          <img src="https://app.layer.ai/assets/layer_wordmark_black.png" width="40%"\nalt="Layer"/>\n    </a>\n    <br>\n<p>\n<p align="center">\n    <a href="https://github.com/layerai/sdk/blob/main/LICENSE">\n        <img alt="License" src="https://img.shields.io/github/license/layerai/sdk.svg?color=blue">\n    </a>\n    <a href="https://docs.layer.ai">\n        <img alt="Documentation" src="https://img.shields.io/badge/docs-online-success">\n    </a>\n    <a href="https://github.com/layerai/sdk/actions/workflows/release.yml">\n        <img alt="Build" src="https://img.shields.io/github/workflow/status/layerai/sdk/Release">\n    </a>\n    <a href="https://pypi.python.org/pypi/layer">\n        <img alt="PyPI" src="https://img.shields.io/pypi/v/layer.svg">\n    </a>\n    <a href="https://github.com/layerai/.github/blob/main/CODE_OF_CONDUCT.md">\n        <img alt="Contributor Covenant" src="https://img.shields.io/badge/contributor%20covenant-v2.1%20adopted-blueviolet.svg">\n    </a>\n</p>\n\n## Layer - Metadata Store for Production ML\n\n![Layer - Metadata store for production ML](https://app.layer.ai/assets/layer_metadata_store.png)\n\n\n[Layer](https://layer.ai) helps you build, train and track all your machine learning project metadata including ML models and datasets with semantic versioning, extensive artifact logging and dynamic reporting with local↔cloud training\n\n**[Start for Free now!](https://app.layer.ai/login?returnTo=%2Fgetting-started)**\n\n## Getting Started\n\nInstall Layer:\n```shell\npip install layer --upgrade\n```\n\nLogin to your free account and initialize your project:\n```python\nimport layer\nlayer.login()\nlayer.init("my-first-project")\n```\n\nDecorate your training function to register your model to Layer:\n```python\nfrom layer.decorators import model\n\n@model("my-model")\ndef train():\n    from sklearn import datasets\n    from sklearn.svm import SVC\n    iris = datasets.load_iris()\n    clf = SVC()\n    clf.fit(iris.data, iris.target)\n    return clf\n\ntrain()\n```\n\nNow you can fetch your model from Layer:\n\n```python\nimport layer\n\nclf = layer.get_model("my-model:1.1").get_train()\nclf\n\n# > SVC()\n```\n\n[**🚀 Try in Google Colab now!**](https://colab.research.google.com/github/layerai/examples/blob/main/tutorials/add-models-to-layer/how_to_add_models_to_layer.ipynb)\n\n## Reporting bugs\nYou have a bug, a request or a feature? Let us know on [Slack](https://bit.ly/layercommunityslack) or [open an issue](https://github.com/layerai/sdk/issues/new/choose)\n\n## Contributing code\nDo you want to help us build the best metadata store? Check out the [Contributing Guide](https://github.com/layerai/sdk/blob/main/CONTRIBUTING.md)\n\n## Learn more\n- Join our [Slack Community ](https://bit.ly/layercommunityslack) to connect with other Layer users\n- Visit the [examples repo](https://github.com/layerai/examples) for more inspiration\n- Browse [Community Projects](https://layer.ai/community) to see more use cases\n- Check out the [Documentation](https://docs.layer.ai)\n- [Contact us](https://layer.ai/contact-us) for your questions\n',
    'author': 'Layer',
    'author_email': 'info@layer.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://layer.ai',
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
