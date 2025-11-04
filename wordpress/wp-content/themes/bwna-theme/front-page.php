<?php
/**
 * Front Page Template
 * This will be customized to match the Wix homepage layout
 *
 * @package BWNA_Theme
 */

get_header(); ?>

<main id="main-content" class="site-main">

    <?php
    // Display static front page content if set
    if (have_posts()) :
        while (have_posts()) : the_post();
    ?>

            <div class="front-page-content">

                <div class="hero-section">
                    <div class="container">
                        <?php if (has_post_thumbnail()) : ?>
                            <div class="hero-image">
                                <?php the_post_thumbnail('full'); ?>
                            </div>
                        <?php endif; ?>

                        <div class="hero-content">
                            <?php the_title('<h1 class="hero-title">', '</h1>'); ?>
                        </div>
                    </div>
                </div>

                <div class="page-content container">
                    <?php the_content(); ?>
                </div>

            </div>

    <?php
        endwhile;
    endif;
    ?>

    <!-- Additional homepage sections will be added based on scraped design -->

</main>

<?php get_footer(); ?>
