Redmine
=======


## Install plugins

```bash
  $
  cd installdir
  ./use_redmine
  cd apps/redmine/htdocs
  bundle install --without development test postgresql sqlite --no-deployment
  bundle install --without development test postgresql sqlite --deployment
  ruby bin/rake redmine:plugins RAILS_ENV=production
  ../../../../ctlscript.sh restart apache

```


### redmine_agile

  http://redminecrm.com/projects/agile/pages/1

### redmine_custom_css

```bash
  git clone git@github.com:martin-denizet/redmine_custom_css.gi
```


### redmine_custom_reports

```bash
  git clone git@github.com:nodecarter/redmine_custom_reports.git
```

### redmine_graphs

```bash
  ./use_redmine
  cd apps/redmine/htdocs/plugins
  git clone git://github.com/dmp/redmine-graphs-plugin.git redmine_graphs
  bundle exec rake redmine:plugins:migrate RAILS_ENV=production
  ../../../../ctlscript.sh restart apache
```

### redmine_ia_links_menu

```bash
  git clone git@github.com:Mayccoll/Redmine-links-Issue-Activity.git redmine_ia_links_menu
```

### redmine_issue_checklist

  http://www.redminecrm.com/projects/checklist/pages/1

### redmine_issue_templates

  https://bitbucket.org/akiko_pusu/redmine_issue_templates
  http://www.r-labs.org/projects/issue-template/wiki/About_en


### redmine_monitoring_controlling

  http://alexmonteiro.github.com/Redmine-Monitoring-Controlling

### redmine_screenshot_paste

  https://github.com/undx/redmine_screenshot_paste


### redmine_tags

  https://github.com/ixti/redmine_tags

### sidebar_hide

```bash
  git clone https://github.com/ries-tech/sidebar_hide.git
```
