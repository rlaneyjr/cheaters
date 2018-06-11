# Atom

### Key shorcuts

>>> keymap.cson

```cson

'atom-workspace atom-text-editor:not([mini])':

  # Comment Line
  'alt-1': 'editor:toggle-line-comments'

  # Color Picker
  'alt-2': 'color-picker:open'

  # Beautify
  'alt-4': 'atom-beautify:beautify-editor'

  # Git
  'alt-5': 'git-history:show-file-history'
  'alt-6': 'git-diff-details:toggle-git-diff-details'


  # Css number increase
  'alt-up': 'emmet:increment-number-by-1'
  'alt-down': 'emmet:decrement-number-by-1'

  # Move up and down
  'ctrl-shift-up': 'editor:move-line-up'
  'ctrl-shift-down': 'editor:move-line-down'

  'alt-z': 'tree-view:toggle'

  # Split multi-selections
  'ctrl-shift-L': 'editor:split-selections-into-lines'


'atom-text-editor.autocomplete-active':
  'enter': 'autocomplete-plus:confirm'

```


### Styles

>>> styles.less

```less

/* Mini map scroll bar hide */
atom-text-editor .vertical-scrollbar,
atom-text-editor::shadow .vertical-scrollbar {
  opacity: 0;
  width: 0;
}


/* Square Dots for pigments */
atom-text-editor::shadow pigments-markers::shadow pigments-color-marker.dot,
pigments-markers::shadow pigments-color-marker.dot,
pigments-color-marker.dot {
  width: 1em;
  height: 1em;
  margin-top: 0.15em;
  border-radius: 0px;
  vertical-align: bottom;
}


/* highlight-selected */
atom-text-editor, atom-text-editor::shadow {
  atom-text-editor .highlight.highlight-selected .region {
    position: absolute;
    pointer-events: none;
    z-index: -1;
  }
  .highlights {

    // Box
    .highlight-selected .region {
      border: 2px dotted;
      border-color: #ff538c;
      // background-color: rgba(245, 245, 245, 0.35);
      // padding: 5px;
    }
    // Background
    .highlight-selected.background .region {
      background-color: rgba(155, 149, 0, 0.6);
    }
    // Light theme box (set in settings)
    .highlight-selected.light-theme .region {
      border-color: rgba(255, 128, 64, 0.4);
    }
    // Light theme background (set in settings)
    .highlight-selected.light-theme.background .region {
      background-color: rgba(255, 128, 64, 0.2);
    }
  }
}

/* Find highlight */
atom-text-editor::shadow .highlight.find-result .region {
  border: 2px dotted;
  border-color: #ff538c;
  background: yellow;
}
atom-text-editor::shadow .highlight.current-result .region,
atom-text-editor::shadow .highlight.current-result ~ .highlight.selection .region {
  border: 2px dotted;
  border-color: #ff538c;
  background: yellow;
}

```

### Toolbar

```json
[
  {
    "type"    : "button",
    "icon"    : "three-bars",
    "callback": "tree-view:toggle",
    "tooltip" : "Toggle tree-view (Alt z)"
  },
  {
    "type"    : "spacer"
  },


  {
    "type"    : "button",
    "icon"    : "document",
    "callback": "application:new-file",
    "tooltip" : "New File",
    "iconset" : "ion"
  },
  {
    "type"    : "button",
    "icon"    : "folder",
    "callback": "application:open-file",
    "tooltip" : "Open...",
    "iconset" : "ion"
  },
  {
    "type"    : "button",
    "icon"    : "archive",
    "callback": "core:save",
    "tooltip" : "Save",
    "iconset" : "ion"
  },
  {
    "type"    : "spacer"
  },


  {
    "type"    : "button",
    "icon"    : "search",
    "callback": "find-and-replace:show",
    "tooltip" : "find-and-replace:show",
    "iconset" : "ion"
  },
  {
    "type"    : "button",
    "icon"    : "shuffle",
    "callback": "find-and-replace:show-replace",
    "tooltip" : "Replace in Buffer",
    "iconset" : "ion"
  },
  {
    "type"    : "spacer"
  },


  {
    "type"    : "button",
    "icon"    : "octoface",
    "callback": "git-control:toggle",
    "tooltip" : "Git Control",
    "style"   : {
      "color" : "#ec5959"
    }
  },
  {
    "type"    : "button",
    "icon"    : "history",
    "callback": "git-history:show-file-history",
    "tooltip" : "Git File history (Alt 5)"
  },
  {
    "type"    : "button",
    "icon"    : "list-alt",
    "iconset" : "fa",
    "callback": "git-log:show",
    "tooltip" : "Git Log"
  },
  {
    "type"    : "button",
    "icon"    : "mirror",
    "callback": "git-difftool:diff-file",
    "tooltip" : "Git Diff File"
  },
  {
    "type"    : "spacer"
  },

  
  {
    "type"    : "button",
    "icon"    : "comment-o",
    "iconset" : "fa",
    "callback": "editor:toggle-line-comments",
    "tooltip" : "Comment Line (Alt 1)"
  },
  {
    "type"    : "button",
    "icon"    : "eyedropper",
    "iconset" : "fa",
    "callback": "color-picker:open",
    "tooltip" : "Color Pickers(Alt 2)"
  },
  {
    "type"    : "button",
    "icon"    : "sort-alpha-asc",
    "callback": "sort-lines:sort",
    "tooltip" : "Sort Lines - F5",
    "iconset" : "fa"
  },
  {
    "type"    : "button",
    "icon"    : "magic",
    "callback": "beautify-editor",
    "tooltip" : "Beautify (Alt 4)",
    "iconset" : "fa"
  },
  {
    "type"    : "button",
    "icon"    : "css3",
    "callback": "css-comb:run",
    "tooltip" : "Sort css",
    "iconset" : "fa"
  },
  {
    "type"    : "spacer"
  },


  {
    "type"    : "button",
    "icon"    : "markdown",
    "callback": "markdown-preview:toggle",
    "tooltip" : "Markdown Preview"
  },
  {
    "type"    : "button",
    "icon"    : "cloud-upload",
    "callback": "remote-ftp:toggle",
    "tooltip" : "Remote FTP",
    "iconset" : "fa"
  },
  {
    "type"    : "spacer"
  },

  {
    "type"    : "button",
    "icon"    : "columns",
    "iconset" : "fa",
    "callback": ["pane:split-right"]
  },
  {
    "type"    : "spacer"
  },
  {
    "type"    : "button",
    "icon"    : "gear",
    "callback": "settings-view:open",
    "tooltip" : "Settings"
  },
  {
    "type"    : "spacer"
  },
  {
    "type"    : "button",
    "icon"    : "xxxxxxxxxx",
    "callback": "axxxxxxxxx",
    "tooltip" : "Nxxxxxxe",
    "iconset" : "xxxxxx"
  }
]

```
