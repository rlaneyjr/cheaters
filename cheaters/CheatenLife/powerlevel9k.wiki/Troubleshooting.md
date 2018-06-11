Here are some fixes to some common problems.

#### Gaps Between Segments

You can see this issue in the screenshot, below:

![](http://bhilburn.org/content/images/2014/12/font_issue.png)

Thankfully, this is easy to fix. This happens if you have successfully installed
Powerline fonts, but did not make a Powerline font the default font in your
terminal emulator (e.g., 'terminator', 'gnome-terminal', 'konsole', etc.,).

#### Segment Colors are Wrong

If the color display within your terminal seems off, it's possible you are using
a reduced color set. You can check this by invoking `echotc Co` in your
terminal, which should yield `256`. If you see something different, try setting
`xterm-256color` in your `~/.zshrc`:

    TERM=xterm-256color

#### Segment Separators are Wrong Color

If the segment separators in your prompt are a different shade than the segments themselves, like this:

![](https://raw.githubusercontent.com/wiki/bhilburn/powerlevel9k/images/terminal.png)


then the issue is your terminal emulator. This issue is most common in OSX's default `Terminal` application. If you are on OSX, you will need to use an alternative emulator, like [iTerm2](https://www.iterm2.com/) to see the proper colors.

#### Strange Characters in Prompt

If your prompt shows strange character like this:

![](https://cloud.githubusercontent.com/assets/1544760/9156161/e0e584e6-3ed0-11e5-897a-2318a8e32d35.png)

it is most likely that you set `POWERLEVEL9K_MODE="awesome-patched"`, but
did not install an [awesome-font](https://github.com/gabrielelana/awesome-terminal-fonts). For most other modes, you need a [powerline-patched](https://github.com/powerline/fonts) font.

#### Strange Character / Segment Spacing

If your prompt looks like this:

![](https://cloud.githubusercontent.com/assets/1775878/13372667/ed7b7514-dd4d-11e5-9a8a-b7a8b1f07e1f.png)

It's likely you are using [iTerm2](https://www.iterm2.com/) and have "Double-Width Characters" enabled. Be sure this setting is **disabled**.

![](https://cloud.githubusercontent.com/assets/1775878/13372685/f8a0ef90-dd4e-11e5-9321-92f007dedf76.png)