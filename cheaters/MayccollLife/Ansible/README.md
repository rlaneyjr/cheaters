Ansible
=======

## CI

```bash
  $
  ansible-playbook bootstrap.yml
```

## Run local

```yml
---
- hosts: all
  tasks:
    - shell: echo "hello world"
```

```bash
  ansible-playbook -i "localhost," -c local playbook.yml
```

## Tanks

- **Ensure a locale exists.**
 
```yml
# ··············································································
    # ###  Ensure a locale exists.
# ··············································································

    - name      : Fix locale es_CO.UTF-8
      locale_gen:
        name    : es_CO.UTF-8
        state   : present

    - name      : Fix locale en_US.UTF-8
      locale_gen:
        name    : en_US.UTF-8
        state   : present

```

- **Install ZSH**

```yml
# ··············································································
    # ### Install zsh
# ··············································································

    - name      : remove folders
      file      :
        state   : absent
        path    : "{{ item }}"
      with_items:
        - "{{ home }}/.zshrc"
        - "{{ home }}/.oh-my-zsh"
        - "{{ home }}/.antigen"
        - "{{ home }}/antigen.zshrc"
        - "{{ home }}/.zshrc"

# ··· Install ZSH
    - name      : Install ZSH
      apt       :
        pkg     : zsh
        state   : latest

    - name      : Set zsh as default shell
      user      :
        name    : "{{ owner }}"
        shell   : /bin/zsh


# ··· Install Oh-My-ZSH
    - name      : Install Oh-My-ZSH
      git       :
        repo    : https://github.com/robbyrussell/oh-my-zsh.git
        dest    : "{{ home }}/.oh-my-zsh"

    - name      : Install Oh-My-ZSH - Change permissions
      file      :
        path    : "{{ home }}/.oh-my-zsh"
        owner   : "{{ owner }}"
        group   : "{{ group }}"
        state   : directory
        recurse : yes


# ··· Create file .zshrc
    - name      : Create file .zshrc
      get_url   :
        url     : "https://raw.githubusercontent.com/Mayccoll/Linux/master/files/zshrc"
        dest    : "{{ home }}/.zshrc"

    - name      : Change .zshrc owner and group
      file      :
        path    : "{{ home }}/.zshrc"
        owner   : "{{ owner }}"
        group   : "{{ group }}"
        mode    : 0644

# ··· Install Antigen
    - name      : Install Antigen
      git       :
        repo    : https://github.com/zsh-users/antigen.git
        dest    : "{{ home }}/.antigen"

    - name      : Install Antigen - Change permissions
      file      :
        path    : "{{ home }}/.antigen"
        owner   : "{{ owner }}"
        group   : "{{ group }}"
        state   : directory
        recurse : yes


# ··· Install Oh-My-ZSH Plugin
    - name      : Install Syntax Higbhtlighting
      git       :
        repo    : https://github.com/zsh-users/zsh-syntax-highlighting.git
        dest    : "{{ home }}/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting"

    - name      : Install Syntax Higbhtlighting - Change permissions
      file      :
        path    : "{{ home }}/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting"
        owner   : "{{ owner }}"
        group   : "{{ group }}"
        state   : directory
        recurse : yes


# ··· Add antigen to .zshrc
    - name      : Get Antigen config file
      get_url   :
        url     : "https://raw.githubusercontent.com/Mayccoll/Linux/master/files/antigen.zshrc"
        dest    : "{{ home }}/antigen.zshrc"

    - name      : Add antigen config file to .zshrc
      shell     : "cat {{ home }}/antigen.zshrc >> {{ home }}/.zshrc"

    - name      : Remove antigen.zshrc
      file      :
        state   : absent
        path    : "{{ home }}/antigen.zshrc"


# ··· Install Terminal Fonts
    - name      : Install Terminal Fonts
      git       :
        repo    : http://github.com/gabrielelana/awesome-terminal-fonts.git
        dest    : "{{ home }}/awesome-terminal-fonts"
        version : patching-strategy

    - name      : Install Terminal Fonts - Change permissions
      file      :
        path    : "{{ home }}/awesome-terminal-fonts"
        owner   : "{{ owner }}"
        group   : "{{ group }}"
        state   : directory
        recurse : yes

    - name      : Install Terminal Fonts - Copy Fonts
      shell     : "cp {{ home }}/awesome-terminal-fonts/patched/*.ttf /usr/local/share/fonts"

    - name      : Install Terminal Fonts - Install fontconfig
      apt       :
        pkg     : fontconfig
        state   : latest

    - name      : Install Terminal Fonts - Update cache
      shell     : fc-cache -fv

    - name      : Install Terminal Fonts - Remove Folder
      file      :
        state   : absent
        path    : "{{ home }}/awesome-terminal-fonts"# ··············································································
    # ### Install zsh
# ··············································································

    - name      : remove folders
      file      :
        state   : absent
        path    : "{{ item }}"
      with_items:
        - "{{ home }}/.zshrc"
        - "{{ home }}/.oh-my-zsh"
        - "{{ home }}/.antigen"
        - "{{ home }}/antigen.zshrc"
        - "{{ home }}/.zshrc"

# ··· Install ZSH
    - name      : Install ZSH
      apt       :
        pkg     : zsh
        state   : latest

    - name      : Set zsh as default shell
      user      :
        name    : "{{ owner }}"
        shell   : /bin/zsh


# ··· Install Oh-My-ZSH
    - name      : Install Oh-My-ZSH
      git       :
        repo    : https://github.com/robbyrussell/oh-my-zsh.git
        dest    : "{{ home }}/.oh-my-zsh"

    - name      : Install Oh-My-ZSH - Change permissions
      file      :
        path    : "{{ home }}/.oh-my-zsh"
        owner   : "{{ owner }}"
        group   : "{{ group }}"
        state   : directory
        recurse : yes


# ··· Create file .zshrc
    - name      : Create file .zshrc
      get_url   :
        url     : "https://raw.githubusercontent.com/Mayccoll/Linux/master/files/zshrc"
        dest    : "{{ home }}/.zshrc"

    - name      : Change .zshrc owner and group
      file      :
        path    : "{{ home }}/.zshrc"
        owner   : "{{ owner }}"
        group   : "{{ group }}"
        mode    : 0644

# ··· Install Antigen
    - name      : Install Antigen
      git       :
        repo    : https://github.com/zsh-users/antigen.git
        dest    : "{{ home }}/.antigen"

    - name      : Install Antigen - Change permissions
      file      :
        path    : "{{ home }}/.antigen"
        owner   : "{{ owner }}"
        group   : "{{ group }}"
        state   : directory
        recurse : yes


# ··· Install Oh-My-ZSH Plugin
    - name      : Install Syntax Higbhtlighting
      git       :
        repo    : https://github.com/zsh-users/zsh-syntax-highlighting.git
        dest    : "{{ home }}/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting"

    - name      : Install Syntax Higbhtlighting - Change permissions
      file      :
        path    : "{{ home }}/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting"
        owner   : "{{ owner }}"
        group   : "{{ group }}"
        state   : directory
        recurse : yes


# ··· Add antigen to .zshrc
    - name      : Get Antigen config file
      get_url   :
        url     : "https://raw.githubusercontent.com/Mayccoll/Linux/master/files/antigen.zshrc"
        dest    : "{{ home }}/antigen.zshrc"

    - name      : Add antigen config file to .zshrc
      shell     : "cat {{ home }}/antigen.zshrc >> {{ home }}/.zshrc"

    - name      : Remove antigen.zshrc
      file      :
        state   : absent
        path    : "{{ home }}/antigen.zshrc"


# ··· Install Terminal Fonts
    - name      : Install Terminal Fonts
      git       :
        repo    : http://github.com/gabrielelana/awesome-terminal-fonts.git
        dest    : "{{ home }}/awesome-terminal-fonts"
        version : patching-strategy

    - name      : Install Terminal Fonts - Change permissions
      file      :
        path    : "{{ home }}/awesome-terminal-fonts"
        owner   : "{{ owner }}"
        group   : "{{ group }}"
        state   : directory
        recurse : yes

    - name      : Install Terminal Fonts - Copy Fonts
      shell     : "cp {{ home }}/awesome-terminal-fonts/patched/*.ttf /usr/local/share/fonts"

    - name      : Install Terminal Fonts - Install fontconfig
      apt       :
        pkg     : fontconfig
        state   : latest

    - name      : Install Terminal Fonts - Update cache
      shell     : fc-cache -fv

    - name      : Install Terminal Fonts - Remove Folder
      file      :
        state   : absent
        path    : "{{ home }}/awesome-terminal-fonts"
  ```
  
## Playbook Recipies

```yml
---
- hosts: vagrant
  remote_user: vagrant
  sudo: yes


  vars:
    mysqlUser:         root
    mysqlPass:         vagrant
    dbUser:            admin
    dbPass:            vagrant
    dbName:            wordpress
    wordpressPath:     /home/vagrant/www
    vhostTemplatePath: templates/vhost.conf
    mysqlTemplatePath: templates/mysql


  tasks:

    - name: Add my user
      user:
        name:             {{ user_name }}
        password:         {{ user_pass }}
        shell:            /bin/bash
        groups:           sudo
        append:           yes
        generate_ssh_key: yes
        ssh_key_bits:     2048
        state:            present


    - name: Add my workstation user's public key to the new user
      authorized_key:
        user:  "{{ user_name }}"
        key:   "{{ lookup('file', 'certificates/id_rsa.pub') }}"
        state: present


    - name: Change SSH port
      lineinfile:
        dest: /etc/ssh/sshd_config
        regexp: "^Port"
        line: "Port 60022"
        state: present


    - name: Remove root SSH access
      lineinfile:
        dest: /etc/ssh/sshd_config
        regexp: "^PermitRootLogin"
        line: "PermitRootLogin no"
        state: present


    - name: Remove password SSH access
      lineinfile:
        dest: /etc/ssh/sshd_config
        regexp: "^PasswordAuthentication"
        line: "PasswordAuthentication no"
        state: present


    - name: Install unzip
      apt: pkg=unzip state=latest update_cache=yes


    - name: Install MySQL client, server and related libraries
      apt: pkg={{ item }} state=latest
      with_items:
        - mysql-client
        - mysql-server
        - python-mysqldb

      - name: Start MySQL service
        service:
          name: "mysql"
          state: started
          enabled: yes


      - name: Setup MySQL root password
        mysql_user:
          name: "root"
          password: "{{ mysqlPass }}"
          host: "{{ item }}"
          state: present
        with_items:
          - "{{ ansible_hostname }}"
          - 127.0.0.1
          - ::1
          - localhost


      - name: Setup MySQL creds for root user
        template:
          src: "{{ mysqlTemplatePath }}"
          dest: "/root/.my.cnf"
          owner: "root"
          mode: 0600


      - name: Delete blank MySQL users
        mysql_user:
          name: ""
          host: "{{ item }}"
          state: absent
        with_items:
          - "{{ ansible_hostname }}"
          - 127.0.0.1
          - ::1
          - localhost


      - name: Drop MySQL test database
        mysql_db: name=test state=absent


      - name: Setup empty database for WordPress
        mysql_db:
          name: "{{ dbName }}"
          encoding: "utf8"
          collation: "utf8_unicode_ci"
          state: "present"
          login_user: "root"
          login_password: "{{ mysqlPass }}"


      - name: Setup MySQL user for WordPress
        mysql_user:
          name: "{{ dbUser }}"
          password: "{{ dbPass }}"
          host: "localhost"
          priv: "wordpress.*:ALL"
          state: "present"

    - name: Install PHP and its modules
      apt: pkg={{ item }} state=latest
      with_items:
        - php5
        - php5-cli
        - php5-curl
        - php5-gd
        - php5-imagick
        - php5-mysql
        - php5-xmlrpc


    - name: Install Apache and its modules
      apt: pkg={{ item }} state=latest
      with_items:
        - apache2
        - libapache2-mod-php5


    - name: Activate mod_rewrite
      apache2_module: name=rewrite state=present





    - name: Put "vagrant" user in www-data group
      user:
        name: "vagrant"
        groups: "www-data"
        append: yes

###
    - name: Unzip WordPress
      unarchive:
        src: ../wordpress.zip
        dest: "{{ wordpressPath }}"

####
    - name: Symlink web root to unzipped WordPress
      file:
        src: "{{ wordpressPath }}/wordpress"
        dest: "/var/www/wordpress"
        state: "link"


    - name: Copy virtual host setup over
      template:
        src: "{{ vhostTemplatePath }}"
        dest: /etc/apache2/sites-available/


    - name: Activate virtual host
      command: a2ensite vhost


    - name: Deactivate default vhost
      command: a2dissite 000-default


    - name: Ensure Apache is running
      service: name=apache2 state=restarted enabled=yes


    - name: Install git
      action: apt pkg=git state=installed


    - name: Install git-core
      action: apt pkg=git-core state=installed

````
