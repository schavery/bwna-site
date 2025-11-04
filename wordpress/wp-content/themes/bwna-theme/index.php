<?php
/**
 * Main Index Template
 *
 * @package BWNA_Theme
 */

get_header(); ?>

<main id="main-content" class="site-main container">

    <?php if (have_posts()) : ?>

        <div class="posts-grid">
            <?php while (have_posts()) : the_post(); ?>

                <article id="post-<?php the_ID(); ?>" <?php post_class(); ?>>

                    <?php if (has_post_thumbnail()) : ?>
                        <div class="post-thumbnail">
                            <a href="<?php the_permalink(); ?>">
                                <?php the_post_thumbnail('bwna-featured'); ?>
                            </a>
                        </div>
                    <?php endif; ?>

                    <header class="entry-header">
                        <h2 class="entry-title">
                            <a href="<?php the_permalink(); ?>">
                                <?php the_title(); ?>
                            </a>
                        </h2>

                        <div class="entry-meta">
                            <span class="posted-on">
                                <?php echo get_the_date(); ?>
                            </span>
                        </div>
                    </header>

                    <div class="entry-summary">
                        <?php the_excerpt(); ?>
                    </div>

                    <footer class="entry-footer">
                        <a href="<?php the_permalink(); ?>" class="read-more">
                            <?php _e('Read More', 'bwna-theme'); ?>
                        </a>
                    </footer>

                </article>

            <?php endwhile; ?>
        </div>

        <?php
        // Pagination
        the_posts_pagination(array(
            'prev_text' => __('Previous', 'bwna-theme'),
            'next_text' => __('Next', 'bwna-theme'),
        ));
        ?>

    <?php else : ?>

        <div class="no-posts">
            <h1><?php _e('Nothing Found', 'bwna-theme'); ?></h1>
            <p><?php _e('Sorry, no posts matched your criteria.', 'bwna-theme'); ?></p>
        </div>

    <?php endif; ?>

</main>

<?php
get_sidebar();
get_footer();
