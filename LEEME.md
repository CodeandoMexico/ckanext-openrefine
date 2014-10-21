Repo Guidelines ([english](/README.md))
============

Repo Guidelines es un conjunto de recomendaciones que ayudan a estructurar un proyecto antes de liberarlo a la comunidad de código abierto.

##Dependencias

- (Requests)[python-requests.org]

##Instalación / Configuraci�

1. Instala la extensión de CKAN en tu entorno local.
  ```sh
  (pyenv) $ pip install -e git+https://github.com/CodeandoMexico/ckanext-openrefine.git@master#egg=ckanext-widgets
  ```

2. Activa el plugin en tu archivo ``config.ini`` agregando la extensión.
  ```sh
  ckan.plugins =  openrefine
  ```

##¿Preguntas o problemas? 
Mantenemos la conversación del proyecto en nuestra página de problemas [issues] (https://github.com/CodeandoMexico/repo-guidelines/issues). Si usted tiene cualquier otra pregunta, nos puede contactar por correo <equipo@codeandomexico.org>.

##Contribuye

Queremos que este proyecto sea el resultado de un esfuerzo de la comunidad. Usted puede colaborar con [código](https://github.com/CodeandoMexicockanext-openrefine/pulls), [ideas](https://github.com/CodeandoMexico/ckanext-openrefine/issues) and [bugs](https://github.com/CodeandoMexico/ckanext-openrefine/issues). Lea nuestro archivo [CONTRIBUYE](/CONTRIBUYE.md).

##Core Team

Este proyecto es una iniciativa de [Codeando México](http://www.codeandomexico.org).
El core team:
- [Noé Domínguez Porras](https://github.com/poguez)
- [Miguel Angel Gordian](https://github.com/zoek1)

##Licencia
Sección para agregar la licencia. La licencia por defecto es AGPL-3.0. Puede variar en función del proyecto. Ejemplo:

_Available under the license: GNU Affero General Public License (AGPL) v3.0. Read the document [LICENSE](/LICENSE) for more information_

Creado por [Codeando México](http://www.codeandomexico.org), 2014.

![alt text](http://blog.codeandomexico.org/images/logo.png "Codeando México")
