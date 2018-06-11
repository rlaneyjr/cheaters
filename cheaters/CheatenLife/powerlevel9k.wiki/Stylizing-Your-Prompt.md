You can configure the look and feel of your prompt easily with some built-in
options.

#### Double-Lined Prompt

By default, `powerlevel9k` is a single-lined prompt. If you would like to have
the segments display on one line, and print the command prompt below it, simply
define `POWERLEVEL9K_PROMPT_ON_NEWLINE` in your `~/.zshrc`:
```zsh
POWERLEVEL9K_PROMPT_ON_NEWLINE=true
```

If you want the right prompt to appear on the newline as well, simply
define `POWERLEVEL9K_RPROMPT_ON_NEWLINE` as well in your `~/.zshrc`:
```zsh
POWERLEVEL9K_PROMPT_ON_NEWLINE=true
POWERLEVEL9K_RPROMPT_ON_NEWLINE=true
```
Here is an example of a double-lined prompt where the `RPROMPT` is drawn on the newline:

![](http://bhilburn.org/content/images/2015/03/double-line.png)

You can customize the icons used to draw the multi-line prompt by setting the
following variables in your `~/.zshrc`:
```zsh
POWERLEVEL9K_MULTILINE_FIRST_PROMPT_PREFIX="↱"
POWERLEVEL9K_MULTILINE_SECOND_PROMPT_PREFIX="↳ "
```

#### Disable Right Prompt

If you do not want a right prompt, you can completely disable it by setting:
```zsh
POWERLEVEL9K_DISABLE_RPROMPT=true
```

#### Light Color Theme

If you prefer to use "light" colors, simply set `POWERLEVEL9K_COLOR_SCHEME`
to `light` in your `~/.zshrc`, and you're all set!
```zsh
POWERLEVEL9K_COLOR_SCHEME='light'
```
The 'light' color scheme works well for ['Solarized
Light'](https://github.com/altercation/solarized) users. Check it out:

![](http://bhilburn.org/content/images/2015/03/solarized-light.png)

#### Icon Customization

Each icon in your prompt can be customized by specifying an appropriately named variable. 

Simply prefix the name of the icon from the segment with 'POWERLEVEL9K', and export this as an environment variable set to the font codepoint (glyph code) you would like to use.

As an example, if you wanted to use a different glyph for the segment separators, you can easily do that with this:
```zsh
POWERLEVEL9K_LEFT_SEGMENT_SEPARATOR=$'\uE0B1'
POWERLEVEL9K_RIGHT_SEGMENT_SEPARATOR=$'\uE0B3'
```
We provide a function that will print every icon name in the theme. To get a full list of icons just type `get_icon_names` in your terminal.

If you want to dump all of the icons you are using, shown in random colors, add the special segment `icons_test` to your prompt:
```zsh
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(icons_test)
```
This special prompt does not work on the right side, as it would be too long,
and ZSH hides it automatically. Please note that the output depends on
your `POWERLEVEL9K_MODE` settings.

#### Segment Color Customization

For each segment in your prompt, you can specify a foreground and background
color by setting them in your `~/.zshrc`. Use the segment names from the [Available Prompt Segments](https://github.com/bhilburn/powerlevel9k/blob/master/README.md#available-prompt-segments) section of the `README.md`. For example, to change the appearance of the `time` segment, you would use:
```zsh
POWERLEVEL9K_TIME_FOREGROUND='red'
POWERLEVEL9K_TIME_BACKGROUND='blue'
```
Note that you can also use a colorcode value. Example:
```zsh
POWERLEVEL9K_VCS_FOREGROUND='021' # Dark blue
```
For a full list of supported colors, run this little code in your terminal:

```zsh
for code ({000..255}) print -P -- "$code: %F{$code}This is how your text would look like%f"
```

#### Special Segment Colors

Some segments have state. For example, if you become root, or modify a file in your version
control system, segments try to reflect this fact by changing the color.
For these segments you still can modify the color to your needs by setting a variable like 
`POWERLEVEL9K_<name-of-segment>_<state>_BACKGROUND`.
Segments with state are:

| Segment        | States                                              |
|----------------|-----------------------------------------------------|
| battery        | `LOW`, `CHARGING`, `CHARGED`, `DISCONNECTED`        |
| context        | `DEFAULT`, `ROOT`                                   |
| dir            | `HOME`, `HOME_SUBFOLDER`, `DEFAULT`                 |
| load           | `CRITICAL`, `WARNING`, `DEFAULT`                    |
| rspec_stats    | `STATS_GOOD`, `STATS_AVG`, `STATS_BAD`              |
| status         | `ERROR`, `OK` (note: only, if verbose is not false) |
| symfony2_tests | `TESTS_GOOD`, `TESTS_AVG`, `TESTS_BAD`              |
| vcs            | `CLEAN`, `UNTRACKED`, `MODIFIED`                    |
| vi_mode        | `NORMAL`, `INSERT`                                  |

Example:
```zsh
# Advanced `vcs` color customization
POWERLEVEL9K_VCS_CLEAN_FOREGROUND='blue'
POWERLEVEL9K_VCS_CLEAN_BACKGROUND='black'
POWERLEVEL9K_VCS_UNTRACKED_FOREGROUND='yellow'
POWERLEVEL9K_VCS_UNTRACKED_BACKGROUND='black'
POWERLEVEL9K_VCS_MODIFIED_FOREGROUND='red'
POWERLEVEL9K_VCS_MODIFIED_BACKGROUND='black'
```

#### Visual Identifiers For Segments

Most segment have a so called "visual identifier" which is an icon or string that serves as a "logo" for the segment. This identifier is displayed on the left side for left configured segments and on the right for right configured segments.

Let's assume you have configured the `load` segment. This segment can have different states (`CRITICAL`, `WARNING` and `NORMAL`). Now, we want to display the segment in black and white and colorize only the visual identifier.
```zsh
# Segment in black and white
POWERLEVEL9K_LOAD_CRITICAL_BACKGROUND="black"
POWERLEVEL9K_LOAD_CRITICAL_FOREGROUND="white"
POWERLEVEL9K_LOAD_WARNING_BACKGROUND="black"
POWERLEVEL9K_LOAD_WARNING_FOREGROUND="white"
POWERLEVEL9K_LOAD_NORMAL_BACKGROUND="black"
POWERLEVEL9K_LOAD_NORMAL_FOREGROUND="white"
# Colorize only the visual identifier
POWERLEVEL9K_LOAD_CRITICAL_VISUAL_IDENTIFIER_COLOR="red"
POWERLEVEL9K_LOAD_WARNING_VISUAL_IDENTIFIER_COLOR="yellow"
POWERLEVEL9K_LOAD_NORMAL_VISUAL_IDENTIFIER_COLOR="green"
```
#### Glue Segments Together

It is possible to display two segments as one, by adding `_joined` to your segment definition. The segments are always joined with their predecessor, so be sure that this is always visible. Otherwise you may get unwanted results. For example, if you want to join `status` and `background_jobs` in your right prompt together, set:
```zsh
POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status background_jobs_joined)
```
This works with every segment, even with custom ones and with conditional ones.