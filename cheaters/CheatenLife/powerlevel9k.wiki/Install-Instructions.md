There are two steps to start using this theme:

1. [Install the Powerlevel9k Theme](#step-1-install-powerlevel9k)
 1. [Vanilla ZSH Install](#option-1-install-for-vanilla-zsh)
 2. [Oh-My-ZSH Install](#option-2-install-for-oh-my-zsh)
 3. [Prezto Install](#option-3-install-for-prezto)
 4. [Antigen Install](#option-4-install-for-antigen)
 5. [Zplug Install](#option-5-install-for-zplug)
 6. [Zgen Install](#option-6-install-for-zgen)
 7. [Antibody Install](#option-7-install-for-antibody)
 8. [ZPM Install](#option-8-install-for-zpm)
 9. [ZIM Install](#option-9-install-for-zim)
2. [Install Powerline-Patched Fonts](#step-2-install-powerline-fonts)

To get the most out of Powerlevel9k, you need to install both the theme as well
as Powerline-patched fonts, if you don't have them installed already. If you
cannot install Powerline-patched fonts for some reason, follow the instructions
below for a `compatible` install.

No configuration is necessary post-installation if you like the default
settings, but there is plenty of segment configuration available if you are
interested.

#### Step 1: Install Powerlevel9k
There are several ways to install and use the Powerlevel9k theme: vanilla ZSH,
Oh-My-Zsh, Prezto, Antigen, Zgen, Antibody, ZPM and ZIM. Do **one** of the following, depending on how you use ZSH.

##### Option 1: Install for Vanilla ZSH

If you just use a vanilla ZSH install, simply clone this repository and
reference it in your `~/.zshrc`:

    $ git clone https://github.com/bhilburn/powerlevel9k.git ~/powerlevel9k
    $ echo 'source  ~/powerlevel9k/powerlevel9k.zsh-theme' >> ~/.zshrc

##### Option 2: Install for Oh-My-ZSH

To install this theme for use in
[Oh-My-Zsh](https://github.com/robbyrussell/oh-my-zsh), clone this repository
into your OMZ `custom/themes` directory.

    $ git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k

You then need to select this theme in your `~/.zshrc`:

    ZSH_THEME="powerlevel9k/powerlevel9k"

##### Option 3: Install for Prezto

To install this theme for use in Prezto, clone this repository into your
[Prezto](https://github.com/sorin-ionescu/prezto) `prompt/external` directory.

    $ git clone https://github.com/bhilburn/powerlevel9k.git  ~/.zprezto/modules/prompt/external/powerlevel9k
    $ ln -s ~/.zprezto/modules/prompt/external/powerlevel9k/powerlevel9k.zsh-theme ~/.zprezto/modules/prompt/functions/prompt_powerlevel9k_setup

You then need to select this theme in your `~/.zpreztorc`:

    zstyle ':prezto:module:prompt' theme 'powerlevel9k'

Please note if you plan to set a `POWERLEVEL9K_MODE` to use a specific font, [as described in this section of the Wiki](https://github.com/bhilburn/powerlevel9k/wiki/Install-Instructions#option-2-install-awesome-powerline-fonts), you must set the `MODE` **before** `prezto` is loaded.

##### Option 4: Install for antigen

To install this theme for use in [antigen](https://github.com/zsh-users/antigen), just add this
in your `~/.zshrc`:

    antigen theme bhilburn/powerlevel9k powerlevel9k
    antigen apply

Note that you should define any customizations at the top of your `.zshrc`
(i.e. setting the `POWERLEVEL9K_*` variables) in your `.zshrc`.

##### Option 5: Install for Zplug

To install this theme for use in [Zplug](https://github.com/b4b4r07/zplug), just add this 
in your `~/.zshrc`:

    zplug "bhilburn/powerlevel9k", use:powerlevel9k.zsh-theme

Note that you should define any customizations at the top of your `.zshrc`
(i.e. setting the `POWERLEVEL9K_*` variables) in your `.zshrc`.

##### Option 6: Install for Zgen

To install this theme for use in [zgen](https://github.com/tarjoilija/zgen), just add this 
in your `~/.zshrc`:

    zgen load bhilburn/powerlevel9k powerlevel9k

Note that you should define any customizations at the top of your .zshrc
(i.e. setting the `POWERLEVEL9K_*` variables) in your `.zshrc`.

##### Option 7: Install for Antibody

To install this theme for use in [Antibody](https://github.com/caarlos0/antibody), just add this 
in your `~/.zshrc`:

    antibody bundle bhilburn/powerlevel9k

Note that you should define any customizations at the top of your `.zshrc`
(i.e. setting the `POWERLEVEL9K_*` variables) in your `.zshrc`.

##### Option 8: Install for ZPM

To install this theme for use in [ZPM](https://github.com/horosgrisa/ZPM), just add this 
in your `~/.zshrc`:

    Plug bhilburn/powerlevel9k
    source ~/.local/share/zpm/plugins/powerlevel9k/powerlevel9k.zsh-theme

Note that you should define any customizations at the top of your `.zshrc`
(i.e. setting the `POWERLEVEL9K_*` variables) in your `.zshrc`.

##### Option 9: Install for ZIM

To install this theme for use in ZIM, clone this repository into your
[ZIM](https://github.com/Eriner/zim) `prompt/external-themes` directory.

    $ git clone https://github.com/bhilburn/powerlevel9k.git ~/.zim/modules/prompt/external-themes/powerlevel9k
    $ ln -s ~/.zim/modules/prompt/external-themes/powerlevel9k/powerlevel9k.zsh-theme ~/.zim/modules/prompt/functions/prompt_powerlevel9k_setup

Add this in your `~/.zshrc`:

    POWERLEVEL9K_INSTALLATION_PATH=~/.zim/modules/prompt/external-themes/powerlevel9k/powerlevel9k.zsh-theme

You then need to select this theme in your `~/.zim`:

    zprompt_theme='powerlevel9k'

Note that you should define any customizations at the top of your `.zshrc` just below `POWERLEVEL9K_INSTALLATION_PATH`
(i.e. setting the `POWERLEVEL9K_*` variables) in your `.zshrc`.

#### Step 2: Install Powerline Fonts
Technically, you don't *have* to install Powerline fonts. If you are using
a font that has some of the basic glyphs we need, you can use the theme in
`compatible` mode - see the third option, below.

To get the most out of theme, though, you'll want Powerline-patched fonts. There
are two varieties of these: 'Powerline Fonts' and 'Awesome Powerline
Fonts'. The latter includes additional glyphs that aren't required for a normal
install.

Do one of the following:

##### Option 1: Install Powerline Fonts

You can find the [installation instructions for Powerline Fonts here]
(https://powerline.readthedocs.org/en/latest/installation/linux.html#fonts-installation).
You can also find the raw font files [in this Github
repository](https://github.com/powerline/fonts) if you want to manually install
them for your OS.

After you have installed Powerline fonts, make the default font in your terminal
emulator the Powerline font you want to use.

This is the default mode for `Powerlevel9k`, and no further configuration is
necessary.

**N.B.:** If Powerlevel9k is not working properly, it is almost always the case
that the fonts were not properly installed, or you have not configured your
terminal to use a Powerline-patched font!

##### Option 2: Install Awesome Powerline Fonts

Alternatively, you can install [Awesome Terminal
Fonts](https://github.com/gabrielelana/awesome-terminal-fonts), which provide
a number of additional glyphs.

**Note:** This setting must be set before you source/apply the theme

You then need to indicate that you wish to use the additional glyphs by defining
the following in your `~/.zshrc`:

    POWERLEVEL9K_MODE='awesome-fontconfig'

If you chose to use [already patched fonts](https://github.com/gabrielelana/awesome-terminal-fonts/tree/patching-strategy/patched), use instead :

    POWERLEVEL9K_MODE='awesome-patched'

Note that if you prefer flat segment transitions, you can use the following with
`Awesome Powerline Fonts` installed:

    POWERLEVEL9K_MODE='flat'

Which looks like this:

![](https://cloud.githubusercontent.com/assets/1544760/7981324/76d0eb5a-0aae-11e5-9608-d662123d0b0a.png)

##### Option 3: Compatible Mode

This option is best if you prefer not to install additional fonts. This option
will work out-of-the-box if your your terminal font supports the segment
separator characters `\uE0B0` (left segment separator) and `\uE0B2` (right
segment separator).

All you need to do to in this case is install the `Powerlevel9k` theme itself,
as explained above, and then define the following in your `~/.zshrc`:

    POWERLEVEL9K_MODE='compatible'

Note that depending on your terminal font, this may still not render
appropriately. This configuration should be used as a back-up.