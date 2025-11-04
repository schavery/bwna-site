<?php
/**
 * 404 Template
 *
 * @package BWNA_Theme
 */

get_header(); ?>

<main id="main-content" class="site-main container">

    <section class="error-404 not-found">
        <header class="page-header">
            <h1 class="page-title"><?php _e('Page Not Found', 'bwna-theme'); ?></h1>
        </header>

        <div class="page-content">
            <p><?php _e('The page you are looking for might have been removed, had its name changed, or is temporarily unavailable.', 'bwna-theme'); ?></p>

            <h2><?php _e('Try searching:', 'bwna-theme'); ?></h2>
            <?php get_search_form(); ?>

            <h2><?php _e('Recent Posts:', 'bwna-theme'); ?></h2>
            <ul>
                <?php
                wp_list_pages(array(
                    'title_li' => '',
                    'number'   => 5,
                ));
                ?>
            </ul>
        </div>
    </section>

</main>

<?php get_footer(); ?>
