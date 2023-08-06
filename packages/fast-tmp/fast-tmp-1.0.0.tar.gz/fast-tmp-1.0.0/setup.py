# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fast_tmp',
 'fast_tmp.admin',
 'fast_tmp.amis',
 'fast_tmp.amis.forms',
 'fast_tmp.conf',
 'fast_tmp.contrib',
 'fast_tmp.contrib.auth',
 'fast_tmp.depends',
 'fast_tmp.jinja_extension',
 'fast_tmp.site',
 'fast_tmp.utils',
 'fast_tmp.utils.tortoise_dantic',
 'fastapi_cli',
 'fastapi_cli.tpl.app.{{cookiecutter.app_name}}',
 'fastapi_cli.tpl.app.{{cookiecutter.app_name}}.routes',
 'fastapi_cli.tpl.project.{{cookiecutter.project_slug}}',
 'fastapi_cli.tpl.project.{{cookiecutter.project_slug}}.tests',
 'fastapi_cli.tpl.project.{{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}',
 'fastapi_cli.tpl.project.{{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}.apps',
 'fastapi_cli.tpl.project.{{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}.apps.api',
 'fastapi_cli.tpl.project.{{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}.apps.api.v1',
 'fastapi_cli.tpl.project.{{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}.apps.api.v1.endpoints',
 'fastapi_cli.tpl.project.{{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}.enums']

package_data = \
{'': ['*'],
 'fast_tmp.admin': ['templates/*'],
 'fastapi_cli': ['tpl/app/*',
                 'tpl/project/*',
                 'tpl/static/*',
                 'tpl/static/static/*'],
 'fastapi_cli.tpl.project.{{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}': ['static/*',
                                                                                         'static/amis/*']}

install_requires = \
['asgiref>=3.5.2,<4.0.0',
 'cookiecutter>=2.1.1,<3.0.0',
 'fastapi[all]>=0.85.0,<0.86.0',
 'python-jose>=3.3.0,<4.0.0',
 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['fast-tmp = fastapi_cli:main']}

setup_kwargs = {
    'name': 'fast-tmp',
    'version': '1.0.0',
    'description': 'fastapi tortoise amis admin',
    'long_description': 'None',
    'author': 'Chise1',
    'author_email': 'chise123@live.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Chise1/fast-tmp',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
