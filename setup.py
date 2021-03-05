from os.path import abspath, dirname, join, normpath
from setuptools import find_packages, setup

setup(
    name='onelogin-flask-oidc',
    version='1.0',
    install_requires=[
        'Flask>=1.1.2',
        'flask-oidc>=1.4.0'
    ],
    author='Mel Hall',
    author_email="mel@melhall.dev",
    zip_safe=False,
    include_package_data=True,    
    url='https://github.com/datamel/onelogin-flask-oidc',
    description='An app to demonstrate using OneLogin OpenID Connect (OIDC) with Flask.'
)
