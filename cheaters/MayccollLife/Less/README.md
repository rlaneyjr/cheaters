# less


### links

```less
// .links ( @color, @hover, @visited, @active, @text-deco );
@import "https://raw.githubusercontent.com/Mayccoll/Utils/master/Less/links.less";

a {
  .links ( #6cc000, #d43838, #00bac0, #c0008a, false );
}
```



### Clear Fix

```less
@import "https://raw.githubusercontent.com/Mayccoll/Utils/master/Less/clear.fix.less";

.myClass {
  .clear-fix;
}
```



### Media


```less
@import "https://raw.githubusercontent.com/Mayccoll/Utils/master/Less/media.less";

@media @phone {
    background-color: rgb(134, 160, 217);
}
```

- **Options**

```
    @media @phone-p
    @media @phone-l
    @media @ipad
    @media @ipad-p
    @media @ipad-l
    @media @laptop
    @media @desktops
    @media @screen
    @media @screen-hd
    @media @screen-full-hd
```

### Hide Text

```less
/**
 * :::::: Hide Text
 */
.hide-text () {
  text-indent: 100%;
  white-space: nowrap;
  overflow: hidden;
  display: block;
}
```

### Reset Doted links

```less
/**
 * ::::::: Reset Doted links
 */
.resetDots () {
  a,
  a:active,
  a:focus {
    outline: none;
  }
  input::-moz-focus-inner {
    border: 0;
  }
  :focus,
  :active {
    outline: 0;
  }
}
/* ::::::: Call */
.resetDots;
```
