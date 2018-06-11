# Installation

NetBox requires following system dependencies:

* python2.7
* python-dev
* python-pip
* libxml2-dev
* libxslt1-dev
* libffi-dev
* graphviz
* libpq-dev
* libssl-dev

```
# sudo apt-get install -y python2.7 python-dev python-pip libxml2-dev libxslt1-dev libffi-dev graphviz libpq-dev libssl-dev
```

You may opt to install NetBox either from a numbered release or by cloning the master branch of its repository on GitHub.

## Option A: Download a Release

Download the [latest stable release](https://github.com/digitalocean/netbox/releases) from GitHub as a tarball or ZIP archive and extract it to your desired path. In this example, we'll use `/opt/netbox`.

```
# wget https://github.com/digitalocean/netbox/archive/vX.Y.Z.tar.gz
# tar -xzf vX.Y.Z.tar.gz -C /opt
# cd /opt/
# ln -s netbox-X.Y.Z/ netbox
# cd /opt/netbox/
```

## Option B: Clone the Git Repository

Create the base directory for the NetBox installation. For this guide, we'll use `/opt/netbox`.

```
# mkdir -p /opt/netbox/
# cd /opt/netbox/
```

If `git` is not already installed, install it:

```
# sudo apt-get install -y git
```

Next, clone the **master** branch of the NetBox GitHub repository into the current directory:

```
# git clone -b master https://github.com/digitalocean/netbox.git .
Cloning into '.'...
remote: Counting objects: 1994, done.
remote: Compressing objects: 100% (150/150), done.
remote: Total 1994 (delta 80), reused 0 (delta 0), pack-reused 1842
Receiving objects: 100% (1994/1994), 472.36 KiB | 0 bytes/s, done.
Resolving deltas: 100% (1495/1495), done.
Checking connectivity... done.
```

## Install Python Packages

Install the required Python packages using pip. (If you encounter any compilation errors during this step, ensure that you've installed all of the system dependencies listed above.)

```
# sudo pip install -r requirements.txt
```

# Configuration

Move into the NetBox configuration directory and make a copy of `configuration.example.py` named `configuration.py`.

```
# cd netbox/netbox/
# cp configuration.example.py configuration.py
```

Open `configuration.py` with your preferred editor and set the following variables:
 
* ALLOWED_HOSTS
* DATABASE
* SECRET_KEY

## ALLOWED_HOSTS

This is a list of the valid hostnames by which this server can be reached. You must specify at least one name or IP address.

Example:

```
ALLOWED_HOSTS = ['netbox.example.com', '192.0.2.123']
```

## DATABASE

This parameter holds the database configuration details. You must define the username and password used when you configured PostgreSQL. If the service is running on a remote host, replace `localhost` with its address.

Example:

```
DATABASE = {
    'NAME': 'netbox',               # Database name
    'USER': 'netbox',               # PostgreSQL username
    'PASSWORD': 'J5brHrAXFLQSif0K', # PostgreSQL password
    'HOST': 'localhost',            # Database server
    'PORT': '',                     # Database port (leave blank for default)
}
```

## SECRET_KEY

Generate a random secret key of at least 50 alphanumeric characters. This key must be unique to this installation and must not be shared outside the local system.

You may use the script located at `netbox/generate_secret_key.py` to generate a suitable key.

!!! note
    In the case of a highly available installation with multiple web servers, `SECRET_KEY` must be identical among all servers in order to maintain a persistent user session state.

# Run Database Migrations

Before NetBox can run, we need to install the database schema. This is done by running `./manage.py migrate` from the `netbox` directory (`/opt/netbox/netbox/` in our example):

```
# cd /opt/netbox/netbox/
# ./manage.py migrate
Operations to perform:
  Apply all migrations: dcim, sessions, admin, ipam, utilities, auth, circuits, contenttypes, extras, secrets, users
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  ...
```

If this step results in a PostgreSQL authentication error, ensure that the username and password created in the database match what has been specified in `configuration.py`

# Create a Super User

NetBox does not come with any predefined user accounts. You'll need to create a super user to be able to log into NetBox:

```
# ./manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password: 
Password (again): 
Superuser created successfully.
```

# Collect Static Files

```
# ./manage.py collectstatic

You have requested to collect static files at the destination
location as specified in your settings:

    /opt/netbox/netbox/static

This will overwrite existing files!
Are you sure you want to do this?

Type 'yes' to continue, or 'no' to cancel: yes
```

# Load Initial Data (Optional)

NetBox ships with some initial data to help you get started: RIR definitions, common devices roles, etc. You can delete any seed data that you don't want to keep.

!!! note
    This step is optional. It's perfectly fine to start using NetBox without using this initial data if you'd rather create everything from scratch.

```
# ./manage.py loaddata initial_data
Installed 43 object(s) from 4 fixture(s)
```

# Test the Application

At this point, NetBox should be able to run. We can verify this by starting a development instance:

```
# ./manage.py runserver 0.0.0.0:8000 --insecure
Performing system checks...

System check identified no issues (0 silenced).
June 17, 2016 - 16:17:36
Django version 1.9.7, using settings 'netbox.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.
```

Now if we navigate to the name or IP of the server (as defined in `ALLOWED_HOSTS`) we should be greeted with the NetBox home page. Note that this built-in web service is for development and testing purposes only. It is not suited for production use.

!!! warning
    If the test service does not run, or you cannot reach the NetBox home page, something has gone wrong. Do not proceed with the rest of this guide until the installation has been corrected.
