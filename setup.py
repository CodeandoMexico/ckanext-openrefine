from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(
    name='ckanext-openrefine',
    version=version,
    description="CKAN Extension for adding Open Refine analysis into your dataset resources.",
    long_description='''
    ''',
    classifiers=[],
    keywords='',
    author='Noe Dominguez Porras & Miguel Angel Gordian',
    author_email='datamx@codeandomexico.org',
    url='http://codeandomexico.org',
    license='AGPL 3.0',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.openrefine'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        openrefine=ckanext.openrefine.plugin:OpenRefinePlugin
    ''',
)
