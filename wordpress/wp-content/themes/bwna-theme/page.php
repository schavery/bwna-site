<?php
/**
 * Page Template
 *
 * @package BWNA_Theme
 */

get_header(); ?>

<main id="main-content" class="site-main container">

    <?php while (have_posts()) : the_post(); ?>

        <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>

            <header class="entry-header">
                <?php the_title('<h1 class="entry-title">', '</h1>'); ?>
            </header>

            <?php if (has_post_thumbnail()) : ?>
                <div class="post-thumbnail">
                    <?php the_post_thumbnail('bwna-featured'); ?>
                </div>
            <?php endif; ?>

            <div class="entry-content">
                <?php
                the_content();

                wp_link_pages(array(
                    'before' => '<div class="page-links">' . __('Pages:', 'bwna-theme'),
                    'after'  => '</div>',
                ));
                ?>
            </div>

        </article>

    <?php endwhile; ?>

</main>

<?php get_footer(); ?>
