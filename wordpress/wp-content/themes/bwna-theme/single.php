<?php
/**
 * Single Post Template
 *
 * @package BWNA_Theme
 */

get_header(); ?>

<main id="main-content" class="site-main container">

    <?php while (have_posts()) : the_post(); ?>

        <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>

            <header class="entry-header">
                <?php the_title('<h1 class="entry-title">', '</h1>'); ?>

                <div class="entry-meta">
                    <span class="posted-on">
                        <time datetime="<?php echo get_the_date('c'); ?>">
                            <?php echo get_the_date(); ?>
                        </time>
                    </span>

                    <?php if (has_category()) : ?>
                        <span class="cat-links">
                            <?php _e('in', 'bwna-theme'); ?>
                            <?php the_category(', '); ?>
                        </span>
                    <?php endif; ?>
                </div>
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

            <?php if (has_tag()) : ?>
                <footer class="entry-footer">
                    <div class="tags-links">
                        <?php the_tags('<span class="tags-label">' . __('Tags:', 'bwna-theme') . '</span> ', ', '); ?>
                    </div>
                </footer>
            <?php endif; ?>

        </article>

        <?php
        // Post navigation
        the_post_navigation(array(
            'prev_text' => '<span class="nav-subtitle">' . __('Previous:', 'bwna-theme') . '</span> %title',
            'next_text' => '<span class="nav-subtitle">' . __('Next:', 'bwna-theme') . '</span> %title',
        ));
        ?>

    <?php endwhile; ?>

</main>

<?php
get_sidebar();
get_footer();
