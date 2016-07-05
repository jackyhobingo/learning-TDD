Provisioning a new site
=======================

## needed packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

e.g.,, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx virtual machine setting

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Upstart works

* see gunicorn-upstart.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## data structure
Assume we have a user account at /home/username

/home/username
--site
   --SITENAME
     --database
     --source
     --static
     --virtualenv

