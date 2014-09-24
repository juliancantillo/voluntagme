#!/usr/bin/env bash

#Install packages

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >> /etc/apt/sources.list.d/postgresql.list'
apt-get update

apt-get -y install python-software-properties
apt-get install -y libpq-dev
apt-get install -y postgresql-9.3 postgresql-server-dev-9.3 postgresql-9.3-postgis-2.1 libpq-dev
apt-get install -y python-dev libjpeg-dev zlib1g-dev
apt-get install -y python-virtualenv virtualenvwrapper
apt-get install binutils libproj-dev gdal-bin
apt-get install php5-cli php5-pgsql


echo "Configure Postgres DATABASE"
sudo -u postgres psql postgres -U postgres -c "CREATE ROLE db_user WITH LOGIN ENCRYPTED PASSWORD 'password' CREATEDB CREATEROLE REPLICATION SUPERUSER"
sudo -u postgres psql postgres -U postgres -c "CREATE DATABASE my_db"
sudo -u postgres psql my_db -U postgres -c "CREATE EXTENSION postgis"
sudo -u postgres psql my_db -U postgres -c "CREATE EXTENSION postgis_topology"
sudo -u postgres psql postgres -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE my_db TO db_user"


echo "listen_addresses = '*' " >> /etc/postgresql/9.3/main/postgresql.conf
echo "host    all    all    all    password" >> /etc/postgresql/9.3/main/pg_hba.conf
sudo service postgresql restart

echo "Configure Virtualenv"
#Create and activate the virtualenv
cd /home/vagrant/
mkdir .virtualenvs
cd .virtualenvs
virtualenv env
source env/bin/activate

#Install the python requirements (inside the virtualenv)
cd /vagrant/
echo "Installing requirments for python"
pip install -r requirements/local.txt

chown vagrant.vagrant /home/vagrant/.virtualenvs

cd my_project
#Initialize the DB from the Django project models
python manage.py migrate

echo "Project setup finished."
