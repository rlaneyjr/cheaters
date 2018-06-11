Brimir - Install Ubuntu trusty 14.04
====================================



#### Install Dependencies

```bash
    $
    sudo apt-get update
    sudo apt-get install -y git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties libffi-dev libmysqlclient-dev libpcre3-dev nginx mysql-client mysql-server
```

#### Install Ruby

```bash
    $
    sudo apt-get remove --purge ruby
    cd
    wget http://ftp.ruby-lang.org/pub/ruby/2.2/ruby-2.2.1.tar.gz
    tar -xzvf ruby-2.2.1.tar.gz
    cd ruby-2.2.1/
    ./configure
    make
    sudo make install
    ruby -v
    echo "gem: --no-ri --no-rdoc" > ~/.gemrc
```

#### Isntall Postgresql

```bash
    $
    sudo apt-get install -y postgresql
    sudo apt-get install -y postgresql-server-dev-9.3

    export LANGUAGE=en_US.UTF-8
    export LANG=en_US.UTF-8
    export LC_ALL=en_US.UTF-8
    sudo locale-gen en_US.UTF-8
    sudo dpkg-reconfigure locales
    sudo pg_createcluster 9.3 main --start

    sudo /etc/init.d/postgresql start

    sudo -u postgres createuser -D -P someuser
    sudo -u postgres createdb -O someuser somedb
    psql -d somedb -U someuser -W

    sudo vim /etc/postgresql/9.4/main/pg_hba.conf

    ---
    local   all             all                                     peer
    +++
    local   all             all                                     md5

    sudo service postgresql restart

```

#### Install Nginx with passenger

```bash
    $
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 561F9B9CAC40B2F7
    sudo vim /etc/apt/sources.list.d/passenger.list
```

```txt
    +++
    deb https://oss-binaries.phusionpassenger.com/apt/passenger trusty main
```

```bash
    $
    sudo chown root: /etc/apt/sources.list.d/passenger.list
    sudo chmod 600 /etc/apt/sources.list.d/passenger.list
    sudo apt-get update
    sudo apt-get install -y nginx-extras passenger
    sudo rm /usr/bin/ruby
    sudo ln -s /usr/local/bin/ruby /usr/bin/ruby
```

#### Set up nginx

```bash
    sudo vim /etc/nginx/nginx.conf
```

```txt
    +++
    passenger_root /usr/lib/ruby/vendor_ruby/phusion_passenger/locations.ini;
    passenger_ruby /usr/local/bin/ruby;
```

```bash
    sudo vim /etc/nginx/sites-available/default
```

```txt
    +++
    # listen 80 default_server;
    # listen [::]:80 default_server ipv6only=on;
```

```bash
    sudo vim /etc/nginx/sites-available/brimir
```

```txt
    +++
    server {
        listen 80 default_server;
        server_name www.mydomain.com;
        passenger_enabled on;
        passenger_app_env production;
        root /home/rails/brimir/public;
    }
```

```bash
    $
    sudo ln -s /etc/nginx/sites-available/brimir /etc/nginx/sites-enabled/brimir
    sudo nginx -s reload
    sudo service nginx restart
```


#### Clone repo

```bash
    $
    git clone https://github.com/ivaldi/brimir.git

    sudo gem install bundler
```

#### Config (important)

```bash
    $
    sudo vim config/environments/production.rb
```

```txt
    +++
    config.action_mailer.default_options = { from: 'brimir@yoururl.com' }

    config.action_mailer.default_url_options = { host: 'brimir.yoururl.com' }
```

#### For Mysql

```bash
    $
    sudo vim config/database.yml
```

```txt
    +++
    adapter: mysql2
```

```bash
    $
    sudo bundle install --without sqlite postgresql development test --deployment

    sudo sed -i "s/<%= ENV\[\"SECRET_KEY_BASE\"\] %>/`bin/rake secret`/g" config/secrets.yml

    rake db:schema:load RAILS_ENV=production

    sudo rake assets:precompile RAILS_ENV=production

    bin/rails console production

    u = User.new({ email: 'admin@admin.com', password: 'admin123', password_confirmation: 'admin123' }); u.agent = true; u.save!
```



#### Errors

bundle install

- Json - Wrong ruby version use 2+
- Mysql - sudo apt-get install libmysqlclient-dev
- any other - sudo gem install bundler

- sudo sed -i "s/<%= ENV\[\"SECRET_KEY_BASE\"\] %>/`bin/rake secret`/g" config/secrets.yml

    sudo apt-get install -y nodejs

- rake assets:precompile RAILS_ENV=production

    vim config/initializers/devise.rb

Crash create ticket

    $ bundle exec rake secret
    $ sudo vim config/secrets.yml
