from setuptools import setup, find_packages

setup(
    name='retrieval',
    version='0.0.1dev0',
    author="Xing Han Lu",
    author_email="pypi@xinghanlu.com",
    url='https://github.com/xhluca/retrieval',
    description='Toolkit for dense neural retrieval. This project is currently under development, so please email the author for any question or access to the code repository, which will be open-sourced when released.',
    packages=find_packages(
        where='src',
        include=["retrieval"],
        exclude=[],
    ),
    install_requires=[
        # dependencies here
    ],
    extras_require={
        # For special installation, e.g. pip install retrieval[dev]
        'dev': ['black', 'twine']
    }
)