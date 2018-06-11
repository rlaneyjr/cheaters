## Functions

https://app.gistboxapp.com/library/label/1452193570913

## Wp-Cli

http://wp-cli.org/#install

```bash
    $
    curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \
    chmod +x wp-cli.phar && sudo mv wp-cli.phar /usr/local/bin/wp

    wp plugin install --activate all-in-one-wp-migration  admin-color-schemes
```

## Permissions

```bash
  $
  sudo chown -R www-data:www-data FOLDER/
  sudo find FOLDER/ -type d -exec chmod 755 {} \;
  sudo find FOLDER/ -type f -exec chmod 644 {} \;
```

## Plugins

#### Esentials

- [admin-color-schemes](https://wordpress.org/plugins/admin-color-schemes/)
- [admin-menu-editor](https://wordpress.org/plugins/admin-menu-editor/)
- [all-in-one-wp-migration](https://wordpress.org/plugins/all-in-one-wp-migration/)
- [better-wp-security](https://wordpress.org/plugins/better-wp-security/)
- [broken-link-checker](https://wordpress.org/plugins/broken-link-checker/)
- [custom-content-type-manager](https://wordpress.org/plugins/custom-content-type-manager/)
- [custom-login](https://wordpress.org/plugins/custom-login/)
- [flexible-posts-widget](https://wordpress.org/plugins/flexible-posts-widget/)
- [post-types-order](https://wordpress.org/plugins/post-types-order/)
- [regenerate-thumbnails](https://wordpress.org/plugins/regenerate-thumbnails/)
- [wp-maintenance-mode](https://wordpress.org/plugins/wp-maintenance-mode/)
- https://github.com/wp-sync-db/wp-sync-db

```bash
    $
    wp plugin install --activate  \
    admin-color-schemes \
    admin-menu-editor \
    all-in-one-wp-migration \
    better-wp-security
    broken-link-checker \
    custom-content-type-manager \
    custom-login \
    flexible-posts-widget \
    post-types-order \
    regenerate-thumbnails \
    wp-maintenance-mode
```
#### Development

- [debug-bar](https://wordpress.org/plugins/debug-bar/)



### Basics

- [advanced-menu-widget]()
- [carousel-without-jetpack]()
- [disable-comments]()
- [disable-wordpress-updates]()
- [easy-social-icons]()
- [external links]()
- [featured-video-plus]()
- [hc-custom-wp-admin-url]()
- [latest-tweets-widget]()
- [meta slider]()
- [ml-slider]()
- [ms-custom-login]()
- [open-external-links-in-a-new-window]()
- [quick-admin-color-scheme-picker]()
- [responsive-add-ons]()
- [restrict-categories]()
- [search-and-replace]()
- [sem-external-links]()
- [simple-basic-contact-form]()
- [simple-history]()
- [simple-responsive-slider]()
- [social-media-feather]()
- [the-events-calendar]()
- [theme-check]()
- [traffic-counter-widget]()
- [user-role-editor]()
- [video-list-manager]()
- [webmaster-user-role]()
- [wp-attachments]()
- [wp-db-backup]()
- [wp-media-library-categories]()
- [wp-optimize]()
- [wp-security-audit-log]()
- [wpfront-user-role-editor]()
- [yop-poll]()



### Child Theme

```css
/*
 Theme Name:     Foxy Child Theme
 Theme URI:      http://www.elegantthemes.com/gallery/foxy/
 Description:    Foxy Child Theme
 Author:         Elegant Themes
 Author URI:     http://www.elegantthemes.com
 Template:       Foxy
 Version:        1.0.0
*/

@import url("../Foxy/style.css");

/* =Theme customization starts here
------------------------------------------------------- */
```


### The Loop

```php
<?php
global $post;
$args = array(
  'posts_per_page'    => 5,
  'category'=> 59
);
$myposts = get_posts( $args );
foreach( $myposts as $post ) : setup_postdata($post);
  the_permalink();
  the_title();
  the_post_thumbnail('full');
  the_title();
endforeach;

```


### The Loop Custom Type

```php
<?php
	$arg = array(
		'post_type' 			=> 'producto',
		'category' 				=> 'hamburguesa',
		'posts_per_page'  => -1
	);
	$loop = new WP_Query( $arg );
?>
<?php while ( $loop->have_posts() ) : $loop->the_post(); ?>

	<h3><?php the_title(); ?></h3>

	<ul>
		<li><?php print_custom_field('product_desc'); ?></li>
		<li><?php print_custom_field('product_price'); ?></li>
	</ul>
	<img src="<?php print_custom_field('product_img:to_image_src'); ?>" /><br />

<?php endwhile; wp_reset_query();
```
