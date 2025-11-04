<?php
/**
 * Footer Template
 *
 * @package BWNA_Theme
 */
?>

    </div><!-- #content -->

    <footer id="colophon" class="site-footer">

        <?php if (is_active_sidebar('footer-1') || is_active_sidebar('footer-2') || is_active_sidebar('footer-3')) : ?>
            <div class="footer-widgets">
                <div class="container">
                    <div class="footer-widgets-inner">
                        <?php for ($i = 1; $i <= 3; $i++) : ?>
                            <?php if (is_active_sidebar('footer-' . $i)) : ?>
                                <div class="footer-column">
                                    <?php dynamic_sidebar('footer-' . $i); ?>
                                </div>
                            <?php endif; ?>
                        <?php endfor; ?>
                    </div>
                </div>
            </div>
        <?php endif; ?>

        <div class="site-info">
            <div class="container">
                <div class="site-info-inner">

                    <?php if (has_nav_menu('footer')) : ?>
                        <nav class="footer-navigation">
                            <?php
                            wp_nav_menu(array(
                                'theme_location' => 'footer',
                                'menu_id'        => 'footer-menu',
                                'depth'          => 1,
                                'container'      => false,
                            ));
                            ?>
                        </nav>
                    <?php endif; ?>

                    <div class="copyright">
                        <p>
                            &copy; <?php echo date('Y'); ?>
                            <a href="<?php echo esc_url(home_url('/')); ?>">
                                <?php bloginfo('name'); ?>
                            </a>
                        </p>
                    </div>

                </div>
            </div>
        </div>

    </footer>

</div><!-- #page -->

<?php wp_footer(); ?>
</body>
</html>
