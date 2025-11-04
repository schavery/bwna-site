<?php
/**
 * BWNA Theme Functions
 *
 * @package BWNA_Theme
 * @since 1.0.0
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

/**
 * Theme Setup
 */
function bwna_theme_setup() {
    // Add theme support
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('html5', array(
        'search-form',
        'comment-form',
        'comment-list',
        'gallery',
        'caption',
        'style',
        'script'
    ));
    add_theme_support('custom-logo');
    add_theme_support('responsive-embeds');
    add_theme_support('align-wide');

    // Register navigation menus
    register_nav_menus(array(
        'primary' => __('Primary Menu', 'bwna-theme'),
        'footer' => __('Footer Menu', 'bwna-theme'),
    ));

    // Add image sizes
    add_image_size('bwna-featured', 1200, 600, true);
    add_image_size('bwna-thumbnail', 400, 300, true);
}
add_action('after_setup_theme', 'bwna_theme_setup');

/**
 * Enqueue Scripts and Styles
 */
function bwna_enqueue_assets() {
    // Main stylesheet
    wp_enqueue_style('bwna-style', get_stylesheet_uri(), array(), '1.0.0');

    // Custom CSS (if needed)
    if (file_exists(get_template_directory() . '/assets/css/custom.css')) {
        wp_enqueue_style('bwna-custom', get_template_directory_uri() . '/assets/css/custom.css', array('bwna-style'), '1.0.0');
    }

    // Main JavaScript
    if (file_exists(get_template_directory() . '/assets/js/main.js')) {
        wp_enqueue_script('bwna-main', get_template_directory_uri() . '/assets/js/main.js', array('jquery'), '1.0.0', true);
    }
}
add_action('wp_enqueue_scripts', 'bwna_enqueue_assets');

/**
 * Register Widget Areas
 */
function bwna_widgets_init() {
    // Sidebar
    register_sidebar(array(
        'name'          => __('Sidebar', 'bwna-theme'),
        'id'            => 'sidebar-1',
        'description'   => __('Add widgets here to appear in your sidebar.', 'bwna-theme'),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
        'after_widget'  => '</section>',
        'before_title'  => '<h2 class="widget-title">',
        'after_title'   => '</h2>',
    ));

    // Footer widgets
    $footer_columns = 3;
    for ($i = 1; $i <= $footer_columns; $i++) {
        register_sidebar(array(
            'name'          => sprintf(__('Footer %d', 'bwna-theme'), $i),
            'id'            => 'footer-' . $i,
            'description'   => sprintf(__('Footer column %d', 'bwna-theme'), $i),
            'before_widget' => '<div id="%1$s" class="widget %2$s">',
            'after_widget'  => '</div>',
            'before_title'  => '<h3 class="widget-title">',
            'after_title'   => '</h3>',
        ));
    }
}
add_action('widgets_init', 'bwna_widgets_init');

/**
 * Custom Excerpt Length
 */
function bwna_excerpt_length($length) {
    return 30;
}
add_filter('excerpt_length', 'bwna_excerpt_length');

/**
 * Custom Excerpt More
 */
function bwna_excerpt_more($more) {
    return '...';
}
add_filter('excerpt_more', 'bwna_excerpt_more');

/**
 * Add Mailchimp shortcode support for embedded forms
 */
function bwna_mailchimp_embed($atts) {
    $atts = shortcode_atts(array(
        'src' => '',
        'width' => '100%',
        'height' => '500',
    ), $atts);

    if (empty($atts['src'])) {
        return '';
    }

    return sprintf(
        '<div class="mailchimp-embed"><iframe src="%s" width="%s" height="%s" frameborder="0" scrolling="no"></iframe></div>',
        esc_url($atts['src']),
        esc_attr($atts['width']),
        esc_attr($atts['height'])
    );
}
add_shortcode('mailchimp', 'bwna_mailchimp_embed');

/**
 * Add support for oEmbed
 */
function bwna_enable_oembed() {
    add_filter('oembed_result', 'bwna_wrap_oembed', 10, 3);
}
add_action('init', 'bwna_enable_oembed');

function bwna_wrap_oembed($html, $url, $args) {
    return '<div class="embed-responsive">' . $html . '</div>';
}

/**
 * Include additional theme files
 */
// require_once get_template_directory() . '/inc/customizer.php';
// require_once get_template_directory() . '/inc/template-tags.php';
