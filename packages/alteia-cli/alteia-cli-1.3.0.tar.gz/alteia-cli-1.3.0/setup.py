# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['alteia_cli', 'alteia_cli.custom_analytics', 'alteia_cli.plugins']

package_data = \
{'': ['*'], 'alteia_cli.custom_analytics': ['share/*']}

install_requires = \
['alteia>=2,<3.0.0',
 'click_spinner>=0.1.8,<0.2.0',
 'jsonschema>=3.0.0,<5.0.0',
 'pyinquirer>=1.0.3,<2.0.0',
 'pyyaml>=5.0.0,<7.0.0',
 'semver>=2.13.0,<3.0.0',
 'tabulate>=0.8.9',
 'typer>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['alteia = alteia_cli.main:app']}

setup_kwargs = {
    'name': 'alteia-cli',
    'version': '1.3.0',
    'description': 'CLI for Alteia',
    'long_description': '# `alteia`\n\nCLI for Alteia Platform.\n\n**Usage**:\n\n```console\n$ alteia [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `-p, --profile TEXT`: Alteia CLI Profile  [env var: ALTEIA_CLI_PROFILE; default: default]\n* `--version`: Display the CLI version and exit\n* `--verbose`: Display more info during the run\n* `--install-completion`: Install completion for the current shell.\n* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `analytics`: Interact with analytics.\n* `configure`: Configure platform credentials.\n* `credentials`: Interact with Docker registry credentials.\n* `products`: Interact with products.\n\n## `alteia analytics`\n\nInteract with analytics.\n\n**Usage**:\n\n```console\n$ alteia analytics [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `create`: Create a new analytic.\n* `delete`: Delete an analytic.\n* `list`: List the analytics.\n* `share`: Share an analytic\n* `unshare`: Unshare an analytic\n\n### `alteia analytics create`\n\nCreate a new analytic.\n\n**Usage**:\n\n```console\n$ alteia analytics create [OPTIONS]\n```\n\n**Options**:\n\n* `--description PATH`: Path of the Analytic description (YAML file).  [required]\n* `--company TEXT`: Company identifier.\n* `--help`: Show this message and exit.\n\n### `alteia analytics delete`\n\nDelete an analytic.\n\n**Usage**:\n\n```console\n$ alteia analytics delete [OPTIONS] ANALYTIC_NAME\n```\n\n**Arguments**:\n\n* `ANALYTIC_NAME`: [required]\n\n**Options**:\n\n* `--version TEXT`: Version range of the analytic in SemVer format. If not provided, all the versions will be deleted.\n* `--help`: Show this message and exit.\n\n### `alteia analytics list`\n\nList the analytics.\n\n**Usage**:\n\n```console\n$ alteia analytics list [OPTIONS]\n```\n\n**Options**:\n\n* `-n, --limit INTEGER RANGE`: Max number of analytics returned.  [default: 100]\n* `--all`: If set, display all kinds of analytics (otherwise only custom analytics are displayed).  [default: False]\n* `--help`: Show this message and exit.\n\n### `alteia analytics share`\n\nShare an analytic \n\n**Usage**:\n\n```console\n$ alteia analytics share [OPTIONS] ANALYTIC_NAME\n```\n\n**Arguments**:\n\n* `ANALYTIC_NAME`: [required]\n\n**Options**:\n\n* `--version TEXT`: Range of versions in SemVer format. If not provided, all the versions will be shared.\n* `--company TEXT`: Identifier of the company to share the analytic with.\n\nWhen providing the identifier of the root company of your domain,\nthe analytic is shared with all the companies of the domain\n(equivalent to using the --domain option)\n* `--domain / --no-domain`: To share the analytic with the root company of your domain.\n\nThis has the effect to share the analytic with all the\ncompanies of your domain and is equivalent to using the\n--company option providing the id of the root company.  [default: False]\n* `--help`: Show this message and exit.\n\n### `alteia analytics unshare`\n\nUnshare an analytic \n\n**Usage**:\n\n```console\n$ alteia analytics unshare [OPTIONS] ANALYTIC_NAME\n```\n\n**Arguments**:\n\n* `ANALYTIC_NAME`: [required]\n\n**Options**:\n\n* `--version TEXT`: Range of versions in SemVer format. If not provided, all the versions will be unshared.\n* `--company TEXT`: Identifier of the company to unshare the analytic with.\n* `--domain / --no-domain`: To unshare the analytic with the root company of your domain.\n\nThis is equivalent to using the --company option providing\nthe id of the root company.\nNote that if you specifically shared the analytic with a company\nof your domain, the analytic will still be shared with that company.  [default: False]\n* `--help`: Show this message and exit.\n\n## `alteia configure`\n\nConfigure platform credentials.\n\nYou can configure multiples credential profiles by specifying\na different profile name for each one.\n\n**Usage**:\n\n```console\n$ alteia configure [OPTIONS] [PROFILE]\n```\n\n**Arguments**:\n\n* `[PROFILE]`: Alteia CLI Profile to configure  [env var: ALTEIA_CLI_PROFILE;default: default]\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n## `alteia credentials`\n\nInteract with Docker registry credentials.\n\n**Usage**:\n\n```console\n$ alteia credentials [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `create`: Create a new credential entry.\n* `delete`: Delete a credential entry by its name.\n* `list`: List the existing credentials.\n\n### `alteia credentials create`\n\nCreate a new credential entry.\n\n**Usage**:\n\n```console\n$ alteia credentials create [OPTIONS]\n```\n\n**Options**:\n\n* `--filepath PATH`: Path of the Credential JSON file.  [required]\n* `--company TEXT`: Company identifier.\n* `--help`: Show this message and exit.\n\n### `alteia credentials delete`\n\nDelete a credential entry by its name.\n\n**Usage**:\n\n```console\n$ alteia credentials delete [OPTIONS] NAME\n```\n\n**Arguments**:\n\n* `NAME`: [required]\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n### `alteia credentials list`\n\nList the existing credentials.\n\n**Usage**:\n\n```console\n$ alteia credentials list [OPTIONS]\n```\n\n**Options**:\n\n* `--company TEXT`: Company identifier.\n* `--help`: Show this message and exit.\n\n## `alteia products`\n\nInteract with products.\n\n**Usage**:\n\n```console\n$ alteia products [OPTIONS] COMMAND [ARGS]...\n```\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n**Commands**:\n\n* `cancel`: Cancel a running product.\n* `list`: List the products\n* `logs`: Retrieve the logs of a product.\n\n### `alteia products cancel`\n\nCancel a running product.\n\n**Usage**:\n\n```console\n$ alteia products cancel [OPTIONS] PRODUCT_ID\n```\n\n**Arguments**:\n\n* `PRODUCT_ID`: [required]\n\n**Options**:\n\n* `--help`: Show this message and exit.\n\n### `alteia products list`\n\nList the products \n\n**Usage**:\n\n```console\n$ alteia products list [OPTIONS]\n```\n\n**Options**:\n\n* `-n, --limit INTEGER RANGE`: Max number of products returned  [default: 10]\n* `--analytic TEXT`: Analytic name\n* `--company TEXT`: Company identifier\n* `--status [pending|processing|available|rejected|failed]`: Product status\n* `--all`: If set, display also the products from platform analytics (otherwise only products from custom analytics are displayed).  [default: False]\n* `--help`: Show this message and exit.\n\n### `alteia products logs`\n\nRetrieve the logs of a product.\n\n**Usage**:\n\n```console\n$ alteia products logs [OPTIONS] PRODUCT_ID\n```\n\n**Arguments**:\n\n* `PRODUCT_ID`: [required]\n\n**Options**:\n\n* `-f, --follow`: Follow logs.  [default: False]\n* `--help`: Show this message and exit.\n\n----\n*Generated with `python -m typer_cli alteia_cli/main.py utils docs --name alteia`*\n',
    'author': 'Alteia Backend Team',
    'author_email': 'backend-team@alteia.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
