from setuptools import setup
required = []
with open('DESCRIPTION.txt') as file:
    long_description = file.read()

with open('requirements.txt') as f:
    required.append(f.read().splitlines())

setup(name='myapiii',
      version='1.0',
      description='A small api that uses fastapi-users',
      url = "https://github.com/ladejavu/python-dev/tree/docker",
      author='sundus_ladejavu',
      author_email='sundus.khalid@ladejavu.com',
      long_description=long_description,
      install_requires=required,
      license='MIT',
      packages=['venv'],
      keywords='api'
      )

