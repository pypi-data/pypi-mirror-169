# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['vestas_azure']

package_data = \
{'': ['*']}

install_requires = \
['adlfs>=2022.7.0,<2023.0.0',
 'azure-identity>=1.10.0,<2.0.0',
 'azure-keyvault-secrets>=4.5.1,<5.0.0',
 'azure-servicebus>=7.7.0,<8.0.0',
 'jsonformatter>=0.3.1,<0.4.0',
 'pyarrow>=8.0.0,<9.0.0',
 'pydantic>=1.9.1,<2.0.0',
 'python-dotenv>=0.20.0,<0.21.0']

setup_kwargs = {
    'name': 'vestas-azure',
    'version': '0.1.10rc2',
    'description': '',
    'long_description': '# Vestas Azure\n\nThe `vestas-azure` package holds Azure related utility functions and objects developed in a Vestas context.\n\n## Getting started\n\nThe package is hosted on our internal [JFrog Artifactory](http://pswiki.vestas.net:8090/display/PB/API%3A+Python+client). Please make sure you have configured it correctly before proceeding.\n\n### Installation\n\nInstall the package via pip,\n\n```\npip install vestas-azure\n```\n\nor [Poetry](https://python-poetry.org/),\n\n```\npoetry add vestas-azure \n```\n\n### Configuration\n\nThe configuration is performed via environment variables,\n\n```bash\nVAZ_BLOB_STORAGE_CONTAINER=resources\nVAZ_BLOB_STORAGE_ACCOUNT_NAME=mapublic\nVAZ_BLOB_STORAGE_ACCOUNT_KEY=REDACTED\nVAZ_SERVICE_BUS_CONNECTION_STR=REDACTED\n```\n\nPlease see `.env.example` for a complete list of configuration options. For local development purposes, injection using `dot-env` is recommended.\n\n## Development\n\nMake sure that `Python` and [Poetry](https://python-poetry.org/) are installed and setup correctly, see [this guide](http://pswiki.vestas.net:8090/display/CERB/How+to+Python) for details. Create a new environment with all dependencies,\n\n    poetry install\n\nand install the git commit hooks,\n\n\tmake git_setup\n\nThis will enable `black`, `mypy` and `flake8`, which will inform you about any issues before committing.  These tools are enabled in the pipelines, so if they aren\'t run at submit time, the pipelines will fail.\n\n### Running tests\n\n```\nmake test\n```\n\n### Linking to Azure\n\nThe linking to Azure (e.g. which storage account to use, which default container, ...) can be specified via environment variables, or using a `.env` file. To link to the public test storage account, simply run\n\n```\nmake .env\n```\n\nto generate a `.env` file from the bundled `.env.example` file. If a `.env` doesn\'t exist already when tests are run, it is generated automatically from `.env.example`.\n\n## Documentation\n\n### Data access abstraction\n\nThe `vestas_azure.file_container` modules provides an abstraction for data access in terms of the `FileContainer` interface. Presently, the following backends have been implemented,\n\n- A `DiskContainer` that stores data in a folder on disk\n- An `AzureContainer` that stores data in an Azure Blob Storage container\n- A `DictContainer` that stores data in a Python dictionary, i.e. in-memory\n\nUsing the `FileContainer` interface abstraction for data access, code will work with all of these backends.\n\n#### Monkey patches applied\n\nImporting the module will patch the following functions if available:\n\n- `PIL.Image.save`\n- `pandas.DataFrame.to_excel`\n- `pandas.read_excel`\n\nThese patches allow these functions to interact with the abstraction.\n\n#### DiskContainer\n\nNo configuration is necessary, just point at the folder you want to use as a temporary storage,\n\n```python\nfrom vestas_azure import DiskContainer\n\ndc = DiskContainer(wd="/tmp/myFolder")\ndc.write("test_file.txt", b"TestContent")\nassert dc.read("test_file.txt") == b"TestContent"\n```\n\n#### AzureContainer\n\nTo use an Azure Blob Storage container, it is necessary to provide the name of the target container, the account name, and the account key. In addition to specifying them when instantiating the `AzureContainer` object, they can be provided via environment variables. Azure connections can be set on instantiation, e.g.\n\n```python\nfrom vestas_azure import AzureContainer\n\nazc = AzureContainer(\n    container_name="sadvpsetc",\n    account_name="MyAccount",\n    account_key="MyAccountKey",\n)\nazc.write("test_file.txt", b"TestContent")\nassert azc.read("test_file.txt") == b"TestContent"\n```\n\nInstantiating the AzureContainer without specifying connection details will then cause a fallback to the configuration set via environment variables,\n\n```python\nfrom vestas_azure import AzureContainer\n\nazc = AzureContainer()\nazc.write("test_file.txt", b"TestContent")\nassert azc.read("test_file.txt") == b"TestContent"\n```\n\n#### DictContainer\n\nNo configuration is necessary,\n\n```python\nfrom vestas_azure import DictContainer\n\ndc = DictContainer()\ndc.write("test_file.txt", b"TestContent")\nassert dc.read("test_file.txt") == b"TestContent"\n```\n\n#### DataframeContainer\n\nThe `vestas_azure.dataframe_container` submodule provides convenience methods for reading and writing Pandas dataframes. When provided with a `FileContainer` object, the `DataFrameContainer` allows reading and writing dataframes to the underlying backend. Data is written and read back in the given `file_format`.\n\n### Blob storage\n\nThe `vestas_azure.blob_storage` submodule contains several utility functions for working with blob storages. In addition to functions helping with authentication and getting clients, the following functions are available,\n\n| function            | purpose                                       |\n|---------------------|-----------------------------------------------|\n| upload_dir          | Upload an entire directory to a container     |\n| download_dir        | Download an entire directory from a container |\n| duplicate_container | Copy all files in one container to another    |\n\n### Logging\n\nThe `vestas_azure.logging` module holds a range of logging utility functions (e.g. for adding custom logging levels, custom formatters etc.). In addition, an `AzureServiceBusLogHandler` class is included, which redirects logs to an Azure Service Bus (configured via the `VAZ_SERVICE_BUS_CONNECTION_STRING` settings). Similarly, an `AzureServiceBusLogReceiver` class is included for collecting the logs. For an example of how this works in practice, take a look at the [gemini level b source code](https://vestas.visualstudio.com/Gemini/_git/gemini-level-b).\n\n### Config\n\nThe `vestas_azure.config` module provides an `AzureConfig` object for settings configuration via pydantic. For some library/project `some_vestas_stuff`, the intended use is to create a `some_vestas_stuff/config.py` module with content like\n\n```python\nfrom typing import Optional\nfrom pydantic import BaseSettings, Field\nfrom vestas_azure import protected_load_dotenv, AzureConfig\n\n\nclass SvsSettings(BaseSettings):\n    FOO: Optional[str] = Field(default="bar")\n    SECRET_FOO: Optional[str] = Field(default="my_key_vault|secret_foo")\n\n    class Config:\n        env_prefix = "SVS_"\n\n\ndef _parse_settings():\n    _settings = SvsSettings()\n    # NOTE: Extra settings parsing/loading logic can be put here.\n    return _settings\n\n\nprotected_load_dotenv()  # load env variables\ncfg = AzureConfig(parse_settings=_parse_settings)  # parse settings\nsettings: SvsSettings = cfg.settings  # make available as module level \'settings\' attribute\n```\n\nwhich would then make the setting(s) available across the project similar to the use in `vestas-azure`, i.e.\n\n```python\nfrom some_vestas_stuff.config import settings\n\nprint(settings.FOO)  # will output "bar"\nprint(settings.SECRET_FOO)  # will output the content of the secret named "secret_foo" in the "my_key_vault" Azure Key Vault\n```\n\nNote that the special syntax \'KEY_VAULT_NAME|SECRET_NAME\' can be used to pull secrets from Azure Key Vaults.\n',
    'author': 'Emil Haldrup Eriksen',
    'author_email': 'emher@vestas.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4',
}


setup(**setup_kwargs)
