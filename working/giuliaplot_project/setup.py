from setuptools import setup, find_packages

setup(name='giuliaplot_project',
      description='Decorator for plots created for the scientific computing class',
      author='Giulia Rancati Cattaneo',
      author_email='g.rancaticattaneo@campus.unimib.it',
      version='0.0.3',
      packages=find_packages(),
      install_requires=['numpy', 'matplotlib'])

