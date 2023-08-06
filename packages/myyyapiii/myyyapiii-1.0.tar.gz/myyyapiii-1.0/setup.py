from setuptools import setup
from distutils.command.install import INSTALL_SCHEMES

for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

with open('DESCRIPTION.txt') as file:
      desc = file.read()

with open('requirements.txt') as f:
    required = f.readlines()

req = [x.strip() for x in required]

setup(name='myyyapiii',
      version='1.0',
      description='A small api that uses fastapi-users',
      url = "https://github.com/ladejavu/python-dev/tree/docker",
      author='sundus_ladejavu',
      author_email='sundus.khalid@ladejavu.com',
      long_description=desc,
      install_requires=req,
      license='MIT',
      packages=['venv', 'app', 'alembic'],
      keywords='api',
      package_dir={'': 'venv', 'venv': 'venv/app', 'venv': 'venv/alembic'},
      data_files=[('', ['DESCRIPTION.txt', 'requirements.txt'])]
      )

