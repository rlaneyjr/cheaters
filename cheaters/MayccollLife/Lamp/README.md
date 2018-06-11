Cambair Carpeta WWWW

>>> httpd.conf
    \wamp\bin\apache\Apache2.2.21\conf\httpd.conf

    --- <Directory "D:/PortableApps/wamp/www/">
    +++ <Directory "D:/www/">

    --- DocumentRoot "D:/PortableApps/wamp/www/"
    +++ DocumentRoot "D:/www/"

    --- #LoadModule rewrite_module modules/mod_rewrite.so
    +++ LoadModule rewrite_module modules/mod_rewrite.so


/* ::::::: Config PHP
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: */

>>> php.ini
    \wamp\bin\apache\Apache2.2.21\bin\php.ini

    --- max_execution_time = 30
    +++ max_execution_time = 300

    --- memory_limit = 128M
    +++ memory_limit = 512M

    --- upload_max_filesize = 2M
    +++ upload_max_filesize = 256M

    --- post_max_size = 8M
    +++ post_max_size = 256M

    --- realpath_cache_size = 16k
    +++ realpath_cache_size = 24M

    --- realpath_cache_ttl = 120
    +++ realpath_cache_ttl = 36000

/* ::::::: Configurar URL virtual
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: */

::: host
    C:\Windows\System32\drivers\etc\host
    127.0.0.1   www.EJEMPLO.com

>>> httpd.conf

    --- #Include conf/extra/httpd-vhosts.conf
    +++ Include conf/extra/httpd-vhosts.conf

>>> httpd-vhosts.conf
    \wamp\bin\apache\apache2.4.2\conf\extra\httpd-vhosts.conf

    <VirtualHost *:80>
        DocumentRoot "D:\www\ejemplo"
        ServerName www.ejemplo.com
    </VirtualHost>


/* :::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: */
