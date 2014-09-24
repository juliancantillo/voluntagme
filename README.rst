Django Vagrant Base Project
==============================

This is a Django Project integrated with Vagrant to run a development instance using PostgreSQL and python-virtualenv.


Requirements:
-------------
Install Vagrant:
https://www.vagrantup.com/downloads.html

Install Virtualbox
https://www.virtualbox.org/wiki/Downloads

Install GIT:
http://git-scm.com/downloads



Getting up and running with Vagrant
-----------------------------------
Open a console a go to you project directory:


.. sourcecode:: bash

    vagrant up



It will install everything you need and will have installed:

* Python
* Python virtualenv
* Django
* Django libraries required for project
* PostgreSQL 9.3
* Will create a virtualenv called env
* It will create the initial database.


Run the Development server
-----------------------------------------

.. sourcecode:: bash

    cd /vagrant/my_project/
    workon env
    python manage.py runserver 0.0.0.0:8000

