Ckanext-OpenRefine ([español](/LEEME.md))
============

CKAN Extension for adding Open Refine analysis into your dataset resources. 

##Dependencies

- [Requests](python-requests.org)

##Installation / Setup
This section is a step by step guide to install the project. An ordered list is recommended.

1. Install the CKAN extension to your local environment.
  ```sh
  (pyenv) $ pip install -e git+https://github.com/CodeandoMexico/ckanext-openrefine.git@master#egg=ckanext-widgets
  ```

2. Activate the plugin in your ``config.ini`` by adding the extension.
  ```sh
  ckan.plugins =  openrefine
  ```

##Questions or issues?
We keep the project's conversation in our issues page [issues](https://github.com/CodeandoMexico/ckanext-openrefine/issues). If you have any other question you can reach us at <equipo@codeandomexico.org>.

##Contribute
We want this project to be the result of a community effort. You can collaborate with [code](https://github.com/CodeandoMexico/ckanext-openrefine/pulls), [ideas](https://github.com/CodeandoMexico/ckanext-openrefine/issues) and [bugs](https://github.com/CodeandoMexico/ckanext-openrefine/issues). Read our [CONTRIBUTE](/CONTRIBUTE.md) file.

##Core Team
This project is an initiative of [Codeando México](http://www.codeandomexico.org).

The core team:
- [Noé Domínguez Porras](https://github.com/poguez)
- [Miguel Angel Gordian](https://github.com/zoek1)

##License
Section to add the license. The default license is AGPL-3.0. Might vary depending of the project. Example:

Available under the license: GNU Affero General Public License (AGPL) v3.0. Read the document [LICENSE](/LICENSE) for more information

Created by [Codeando México](http://www.codeandomexico.org), 2014.

![alt text](http://blog.codeandomexico.org/images/logo.png "Codeando México")
