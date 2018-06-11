If you have a special configuration show it here!

#### Rules

1. Provide an awesome screenshot.
2. Provide your configuration.
3. Share your color scheme & font.

#### Configurations

##### tunnckoCore configuration:

![Charlike Mike Reagent zsh theme screenshot](https://cloud.githubusercontent.com/assets/5038030/15469159/0fc514f4-20f1-11e6-9145-a6b8f8b1bebe.png)

Almost the default config. Font is `SourceCodePro+Powerline+Awesome Regular 12`

```sh
POWERLEVEL9K_MODE='awesome-patched'
POWERLEVEL9K_SHORTEN_DIR_LENGTH=2
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(os_icon dir vcs)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status nvm node_version)

POWERLEVEL9K_OS_ICON_BACKGROUND="white"
POWERLEVEL9K_OS_ICON_FOREGROUND="blue"
POWERLEVEL9K_DIR_HOME_FOREGROUND="white"
POWERLEVEL9K_DIR_HOME_SUBFOLDER_FOREGROUND="white"
POWERLEVEL9K_DIR_DEFAULT_FOREGROUND="white"
```

OS is ArchLinux, terminal is `gnome-terminal`, theme is `Use colors from system theme` which is `Arc-Dark`, and the pallete is built-in `Tango`.

##### bhilburn's configuration:

![Ben Hilburn's configuration screenshot](https://cloud.githubusercontent.com/assets/569571/12149820/af22eb06-b45a-11e5-99b3-8a383659fc5f.png)

This is the default theme configuration with no additional settings.

Color scheme is `Eighties-Dark` from [Gnome-Terminal Base16 Colors Themes](https://github.com/chriskempson/base16-gnome-terminal). Font is `DejaVu Sans Mono for Powerline Book`, 10pt.

##### tacolizard's configuration:

![screenshot](http://i.imgur.com/2sLVZ3R.png)

```
#DISABLE_AUTO_TITLE="true"

POWERLEVEL9K_BATTERY_CHARGING='yellow'
POWERLEVEL9K_BATTERY_CHARGED='green'
POWERLEVEL9K_BATTERY_DISCONNECTED='$DEFAULT_COLOR'
POWERLEVEL9K_BATTERY_LOW_THRESHOLD='10'
POWERLEVEL9K_BATTERY_LOW_COLOR='red'
POWERLEVEL9K_BATTERY_ICON='\uf1e6 '
POWERLEVEL9K_MULTILINE_FIRST_PROMPT_PREFIX=''
POWERLEVEL9K_MULTILINE_SECOND_PROMPT_PREFIX='\uf0da'
#POWERLEVEL9K_VCS_GIT_ICON='\ue60a'

POWERLEVEL9K_VCS_MODIFIED_BACKGROUND='yellow'
POWERLEVEL9K_VCS_UNTRACKED_BACKGROUND='yellow'
#POWERLEVEL9K_VCS_UNTRACKED_ICON='?'


POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(status os_icon battery context dir vcs)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(time background_jobs ram virtualenv rbenv rvm)

POWERLEVEL9K_SHORTEN_STRATEGY="truncate_middle"
POWERLEVEL9K_SHORTEN_DIR_LENGTH=4

#POWERLEVEL9K_CUSTOM_TIME_FORMAT="%D{\uf017 %H:%M:%S}"
POWERLEVEL9K_TIME_FORMAT="%D{\uf017 %H:%M \uf073 %d.%m.%y}"

POWERLEVEL9K_STATUS_VERBOSE=false

POWERLEVEL9K_PROMPT_ON_NEWLINE=true
```

Colorscheme is Solarized Dark for gnome terminal. Font is Input Mono Regular patched with font-awesome

##### dritter's configuration:

![bildschirmfoto 2015-09-28 um 23 58 47](https://cloud.githubusercontent.com/assets/1544760/10149938/0740fcae-663d-11e5-89cf-86a54c693a44.png)
```zsh
POWERLEVEL9K_MODE='awesome-patched'
POWERLEVEL9K_SHORTEN_DIR_LENGTH=3
POWERLEVEL9K_SHORTEN_STRATEGY="truncate_middle"
POWERLEVEL9K_STATUS_VERBOSE=false
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(status os_icon load context dir vcs)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(time)
POWERLEVEL9K_SHOW_CHANGESET=true
POWERLEVEL9K_CHANGESET_HASH_LENGTH=6
```
Used font is 13pt `SourceCodePro+Powerline+Awesome+Regular`.

Used color scheme is: [Solarized Darcula](https://github.com/mbadolato/iTerm2-Color-Schemes/blob/master/schemes/Solarized%20Darcula.itermcolors)

##### Kayant's configuration:

![Anthony's configuration screenshot](https://cloud.githubusercontent.com/assets/569571/12373633/b73e0de8-bc34-11e5-80af-38d512280601.png)

```zsh
POWERLEVEL9K_MODE='awesome-patched'
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(os_icon root_indicator context dir vcs)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status time)
POWERLEVEL9K_PROMPT_ON_NEWLINE=true
POWERLEVEL9K_STATUS_VERBOSE=false
POWERLEVEL9K_TIME_FORMAT="%D{%H:%M \uE868  %d.%m.%y}"
export DEFAULT_USER="$USER"
```

The font is 10pt `SourceCodePro+Powerline+Awesome+Regular`, with the [Base 16 Google Dark](https://github.com/chriskempson/base16-gnome-terminal) color scheme.

##### giladgo's configuration:

![screen shot 2015-09-29 at 09 58 36](https://cloud.githubusercontent.com/assets/1915716/10157373/44017de4-6692-11e5-9c0f-0854eb882b8c.png)

```zsh
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(context dir node_version vcs)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(longstatus history time)
POWERLEVEL9K_TIME_FORMAT="%D{%H:%M:%S %d/%m/%Y}"
POWERLEVEL9K_NODE_VERSION_BACKGROUND='022'
```

The font is 16pt `Inconsolata for Powerline`, with the [Solarized Dark](https://github.com/mbadolato/iTerm2-Color-Schemes/blob/master/schemes/Solarized%20Dark.itermcolors) color scheme.

##### natemccurdy's configuration:

![nate powerlevel9k gif](http://i.imgur.com/wyBVZQy.gif)

```zsh
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(time context dir vcs)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status rbenv)
POWERLEVEL9K_STATUS_VERBOSE=false
POWERLEVEL9K_SHORTEN_STRATEGY="truncate_middle"
POWERLEVEL9K_SHORTEN_DIR_LENGTH=3
```

Font is 14pt `Iconsolata for Powerline` with [Solarized Dark](https://github.com/mbadolato/iTerm2-Color-Schemes/blob/master/schemes/Solarized%20Dark.itermcolors) iterm2 colors.

##### rjorgenson's configuration:

![rjorgenson powerlevel9k](https://camo.githubusercontent.com/271270ea1d1d922b273047e87dda206b95e80e5b/687474703a2f2f692e696d6775722e636f6d2f4c634c31566e502e706e67)

Font is [SourceCodePro+Powerline+Awesome Regular at 10pt](https://github.com/stefano-meschiari/dotemacs/blob/master/SourceCodePro%2BPowerline%2BAwesome%2BRegular.ttf) with [Solarized Dark](http://ethanschoonover.com/solarized) color scheme.

```zsh
POWERLEVEL9K_MODE='awesome-patched'
POWERLEVEL9K_PROMPT_ON_NEWLINE=true
POWERLEVEL9K_MULTILINE_FIRST_PROMPT_PREFIX="%{%F{249}%}\u250f"
POWERLEVEL9K_MULTILINE_SECOND_PROMPT_PREFIX="%{%F{249}%}\u2517%{%F{default}%} "
POWERLEVEL9K_SHORTEN_DIR_LENGTH=4
POWERLEVEL9K_SHORTEN_STRATEGY="truncate_middle"
POWERLEVEL9K_OS_ICON_BACKGROUND="black"
POWERLEVEL9K_OS_ICON_FOREGROUND="249"
POWERLEVEL9K_TODO_BACKGROUND="black"
POWERLEVEL9K_TODO_FOREGROUND="249"
POWERLEVEL9K_DIR_HOME_BACKGROUND="black"
POWERLEVEL9K_DIR_HOME_FOREGROUND="249"
POWERLEVEL9K_DIR_HOME_SUBFOLDER_BACKGROUND="black"
POWERLEVEL9K_DIR_HOME_SUBFOLDER_FOREGROUND="249"
POWERLEVEL9K_DIR_DEFAULT_BACKGROUND="black"
POWERLEVEL9K_DIR_DEFAULT_FOREGROUND="249"
POWERLEVEL9K_STATUS_OK_BACKGROUND="black"
POWERLEVEL9K_STATUS_OK_FOREGROUND="green"
POWERLEVEL9K_STATUS_ERROR_BACKGROUND="black"
POWERLEVEL9K_STATUS_ERROR_FOREGROUND="red"
POWERLEVEL9K_NVM_BACKGROUND="black"
POWERLEVEL9K_NVM_FOREGROUND="249"
POWERLEVEL9K_NVM_VISUAL_IDENTIFIER_COLOR="green"
POWERLEVEL9K_RVM_BACKGROUND="black"
POWERLEVEL9K_RVM_FOREGROUND="249"
POWERLEVEL9K_RVM_VISUAL_IDENTIFIER_COLOR="red"
POWERLEVEL9K_LOAD_CRITICAL_BACKGROUND="black"
POWERLEVEL9K_LOAD_WARNING_BACKGROUND="black"
POWERLEVEL9K_LOAD_NORMAL_BACKGROUND="black"
POWERLEVEL9K_LOAD_CRITICAL_FOREGROUND="249"
POWERLEVEL9K_LOAD_WARNING_FOREGROUND="249"
POWERLEVEL9K_LOAD_NORMAL_FOREGROUND="249"
POWERLEVEL9K_LOAD_CRITICAL_VISUAL_IDENTIFIER_COLOR="red"
POWERLEVEL9K_LOAD_WARNING_VISUAL_IDENTIFIER_COLOR="yellow"
POWERLEVEL9K_LOAD_NORMAL_VISUAL_IDENTIFIER_COLOR="green"
POWERLEVEL9K_RAM_BACKGROUND="black"
POWERLEVEL9K_RAM_FOREGROUND="249"
POWERLEVEL9K_RAM_ELEMENTS=(ram_free)
POWERLEVEL9K_BATTERY_LOW_BACKGROUND="black"
POWERLEVEL9K_BATTERY_CHARGING_BACKGROUND="black"
POWERLEVEL9K_BATTERY_CHARGED_BACKGROUND="black"
POWERLEVEL9K_BATTERY_DISCONNECTED_BACKGROUND="black"
POWERLEVEL9K_BATTERY_LOW_FOREGROUND="249"
POWERLEVEL9K_BATTERY_CHARGING_FOREGROUND="249"
POWERLEVEL9K_BATTERY_CHARGED_FOREGROUND="249"
POWERLEVEL9K_BATTERY_DISCONNECTED_FOREGROUND="249"
POWERLEVEL9K_BATTERY_LOW_VISUAL_IDENTIFIER_COLOR="red"
POWERLEVEL9K_BATTERY_CHARGING_VISUAL_IDENTIFIER_COLOR="yellow"
POWERLEVEL9K_BATTERY_CHARGED_VISUAL_IDENTIFIER_COLOR="green"
POWERLEVEL9K_BATTERY_DISCONNECTED_VISUAL_IDENTIFIER_COLOR="249"
POWERLEVEL9K_TIME_BACKGROUND="black"
POWERLEVEL9K_TIME_FOREGROUND="249"
POWERLEVEL9K_TIME_FORMAT="%D{%H:%M:%S} \UE12E"
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=('status' 'os_icon' 'todo' 'context' 'dir' 'vcs')
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=('nvm' 'rvm' 'load' 'ram_joined' 'battery' 'time')
```

##### sevenfoxes's configuration:
![sevenfoxes powerlevel9k](http://i.imgur.com/EaYpPff.png)

```zsh
prompt_zsh_showStatus () {
  state=`osascript -e 'tell application "Spotify" to player state as string'`;
  if [ $state = "playing" ]; then
    artist=`osascript -e 'tell application "Spotify" to artist of current track as string'`;
    track=`osascript -e 'tell application "Spotify" to name of current track as string'`;

    echo -n "$artist - $track";
  fi
}

POWERLEVEL9K_PROMPT_ON_NEWLINE=true
POWERLEVEL9K_RPROMPT_ON_NEWLINE=true
POWERLEVEL9K_MODE='awesome-patched'
POWERLEVEL9K_SHORTEN_DIR_LENGTH=3
POWERLEVEL9K_SHORTEN_STRATEGY="truncate_middle"
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(root_indicator dir nvm vcs)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status zsh_showStatus)
POWERLEVEL9K_NVM_BACKGROUND='28'
POWERLEVEL9K_NVM_FOREGROUND='15'
POWERLEVEL9K_TIME_FORMAT="%D{%H:%M \uE868  %d.%m}"
```
Used font is 13pt `SourceCodePro+Powerline+Awesome+Regular`.
Used color scheme is: [Neutron](https://github.com/mbadolato/iTerm2-Color-Schemes/blob/master/schemes/Neutron.itermcolors)

To get the Currently playing Spotify track to work:
OSX
```zsh
brew install shpotify
```

Linux (use this function instead of the one listed above)
Depends: [spotify-cli](https://github.com/johnelse/spotify-cli)
```zsh
prompt_zsh_showStatus () {
  state=`spotify-cli now-playing`;
  if [ $state = "Spotify service not found - is it running?" ]; then
    
  else
    artist=`spotify-cli now-playing | grep "spotify_artist_name" | cut -d'=' -f2`
    track=`spotify-cli now-playing | grep "spotify_track_name" | cut -d'=' -f2`

    echo -n "$artist - $track";
  fi
}
```


##### Falkor's configuration:
![Falkor powerlevel9k](https://github.com/Falkor/dotfiles/blob/master/screenshots/screenshot_falkor_iterm.png)

~~~zsh
# See also https://github.com/Falkor/dotfiles/blob/master/oh-my-zsh/
# Font taken from https://github.com/stefano-meschiari/dotemacs/blob/master/SourceCodePro%2BPowerline%2BAwesome%2BRegular.ttf
#
POWERLEVEL9K_MODE='awesome-patched'

# Disable dir/git icons
POWERLEVEL9K_HOME_ICON=''
POWERLEVEL9K_HOME_SUB_ICON=''
POWERLEVEL9K_FOLDER_ICON=''

DISABLE_AUTO_TITLE="true"

POWERLEVEL9K_VCS_GIT_ICON=''
POWERLEVEL9K_VCS_STAGED_ICON='\u00b1'
POWERLEVEL9K_VCS_UNTRACKED_ICON='\u25CF'
POWERLEVEL9K_VCS_UNSTAGED_ICON='\u00b1'
POWERLEVEL9K_VCS_INCOMING_CHANGES_ICON='\u2193'
POWERLEVEL9K_VCS_OUTGOING_CHANGES_ICON='\u2191'

POWERLEVEL9K_VCS_MODIFIED_BACKGROUND='yellow'
POWERLEVEL9K_VCS_UNTRACKED_BACKGROUND='yellow'
#POWERLEVEL9K_VCS_UNTRACKED_ICON='?'

POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(status os_icon context dir vcs)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(background_jobs virtualenv rbenv rvm time)

POWERLEVEL9K_SHORTEN_STRATEGY="truncate_middle"
POWERLEVEL9K_SHORTEN_DIR_LENGTH=4

POWERLEVEL9K_TIME_FORMAT="%D{%H:%M \uE868  %d.%m.%y}"

POWERLEVEL9K_STATUS_VERBOSE=false
export DEFAULT_USER="$USER"
~~~

* Font is [Source Code Pro + Powerline Awesome Regular](https://github.com/stefano-meschiari/dotemacs/blob/master/SourceCodePro%2BPowerline%2BAwesome%2BRegular.ttf) at 14pt (for bot Regular and Non-ASCII font)
* Color scheme is [Darkside](https://github.com/mbadolato/iTerm2-Color-Schemes/blob/master/schemes/Darkside.itermcolors)


#### letientai299's configuration
Two lines prompt with time segment on the second line left promt.

![letientai299 terminal theme](https://raw.githubusercontent.com/letientai299/dotfiles/master/images/terminal.png)

```bash
POWERLEVEL9K_SHORTEN_DIR_LENGTH=2
POWERLEVEL9K_MODE='awesome-patched'
POWERLEVEL9K_PROMPT_ON_NEWLINE=true

POWERLEVEL9K_VCS_GIT_ICON=''
POWERLEVEL9K_VCS_STAGED_ICON='\u00b1'
POWERLEVEL9K_VCS_UNTRACKED_ICON='\u25CF'
POWERLEVEL9K_VCS_UNSTAGED_ICON='\u00b1'
POWERLEVEL9K_VCS_INCOMING_CHANGES_ICON='\u2193'
POWERLEVEL9K_VCS_OUTGOING_CHANGES_ICON='\u2191'

POWERLEVEL9K_RAM_BACKGROUND="black"
POWERLEVEL9K_RAM_FOREGROUND="249"
POWERLEVEL9K_RAM_ELEMENTS=(ram_free)

POWERLEVEL9K_MULTILINE_FIRST_PROMPT_PREFIX="\n"
POWERLEVEL9K_MULTILINE_SECOND_PROMPT_PREFIX="%K{white}%F{black} `date +%T` \UE12E %f%k%F{white}%f "

POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(context dir vcs)
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status nvm rvm background_jobs ram battery)
```

* Font is [Source Code Pro + Powerline Awesome Regular](https://github.com/stefano-meschiari/dotemacs/blob/master/SourceCodePro%2BPowerline%2BAwesome%2BRegular.ttf) at 14pt (for bot Regular and Non-ASCII font). Copied from Falkor's config.
* The color scheme is [aci](https://github.com/Mayccoll/Gogh/blob/master/content/themes.md#aci) from [Mayccoll/Gogh](https://github.com/Mayccoll/Gogh)

### Tritlo's configuration

![Tritlo's terminal theme](http://i.imgur.com/rNjW58X.png)

Powerelevel9k is loaded with `zgen` and `prezto` (with `zgen` being bootstrapped if it is not found, so a fresh install can be made with `rm -rf .zgen`) as follows:
```sh
# Keep powerlevel9k in distinct file
source ~/.powerlevel9k

# === ZGEN stuff ===
if [ !  -f ~/.zgen/zgen.zsh ]; then
    echo "Zgen not found, bootstrapping."
    mkdir -p ~/.zgen
    curl -L https://raw.githubusercontent.com/tarjoilija/zgen/master/zgen.zsh > ~/.zgen/zgen.zsh
fi

source ~/.zgen/zgen.zsh
if ! zgen saved; then
    # Bootstrap fonts

    # Load skwp theme, in case powerlevel9k doesn't work.
    zgen prezto prompt theme 'skwp'
    zgen prezto syntax-highlighting color 'yes'

    # prezto and modules
    zgen prezto

    zgen prezto git
    zgen prezto command-not-found
    zgen prezto syntax-highlighting
    zgen prezto history-substring-search
    zgen prezto completion
    zgen prezto fasd

    zgen load tarruda/zsh-autosuggestions
    if [[ ! $TERM =~ linux ]];
    then
        zgen load bhilburn/powerlevel9k powerlevel9k.zsh-theme
    fi

    prompt skwp
fi
```

Powerlevel9k is then configured as follows:
```sh

    POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(os_icon context time dir)
    POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status vcs ip battery docker_machine)
    POWERLEVEL9K_PROMPT_ON_NEWLINE=true
    POWERLEVEL9K_RPROMPT_ON_NEWLINE=true
    POWERLEVEL9K_BATTERY_ICON="B"
    POWERLEVEL9K_MULTILINE_FIRST_PROMPT_PREFIX=""

    local user_symbol="$"
    if [[ $(print -P "%#") =~ "#" ]]; then
        user_symbol = "#"
    fi

    POWERLEVEL9K_MULTILINE_SECOND_PROMPT_PREFIX="%{%B%F{yellow}%K{blue}%} $user_symbol%{%b%f%k%F{blue}%} %{%f%}"

    POWERLEVEL9K_SHOW_CHANGESET=true
    POWERLEVEL9K_CHANGESET_HASH_LENGTH=6
    POWERLEVEL9K_TIME_FORMAT="%D{%F %T}"
```

* The font is [Pragmata Pro](http://www.fsd.it/shop/fonts/pragmatapro/)
* The terminal is iTerm 3.
* The colour scheme is [Molokai](https://github.com/mbadolato/iTerm2-Color-Schemes#molokai)
