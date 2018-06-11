Utils
=====


Linux
-----

### Processs

```bash
  $ top -bn 1
```

### Apache folder pass

- http://www.htaccesstools.com/htpasswd-generator/

- http://www.htpasswdgenerator.net/

.htaccess

```bash
AuthName "intranet"
    AuthType Basic
    AuthUserFile PATH/intranet/.htpasswds
    Require valid-user
```

.htpasswds

```bash
USERLOGIN:$apr1$oxwfvojdrWgKVX4gqBRBRLsmSojCo71
```
