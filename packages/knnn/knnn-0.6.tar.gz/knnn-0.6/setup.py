from setuptools import setup, find_packages

setup(
    name='knnn',
    version='0.6',
    license='MIT',
    author="ON",
    author_email='email@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'scikit-learn',
      ],

)