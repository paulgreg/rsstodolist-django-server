rsstodolist-server
==================

rsstodolist-server is a django port of the Google App Engine rsstodolist application (http://rsstodolist.appspot.com).
Same functionality are expected but It can be host on your server.

Pre-requisites
--------------

Have python and django (1.5) installed and eventually mysql or another database (you could also use sqlite).
You better install django using pip :

    pip install Django==1.5.5

If you’ll use mysql as database, you’ll need the following command on Debian / Ubuntu to build the mysql client :

    apt-get install python-dev
    apt-get install libmysqlclient-dev
    pip install mysql-python

Then create a database and a dedicated user, for mysql :

    mysql -u root -p
    create database rsstodolist;
    grant all privileges on rsstodolist.* to 'rsstodolist'@'localhost' identified by 'CHANGEME';

You can then try to login using :

    mysql -u rsstodolist -p

Then, you’ll have to change database information in rsstodolist\settings.py file (use settings.py.dist as example).


You should then create database table by :

    python manage.py syncdb


Run
----

You can then run the project using :

    python manage.py runserver


Deploy
------

Follow the Django deployement guide to deploy the application : https://docs.djangoproject.com/en/dev/howto/deployment/

Serve `src/Feeds/static` as static files in `/static` directory

