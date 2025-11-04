/**
 * BWNA Theme Main JavaScript
 *
 * @package BWNA_Theme
 */

(function($) {
    'use strict';

    // Mobile menu toggle
    const menuToggle = $('.menu-toggle');
    const primaryMenu = $('#primary-menu');

    menuToggle.on('click', function() {
        const expanded = $(this).attr('aria-expanded') === 'true' || false;
        $(this).attr('aria-expanded', !expanded);
        primaryMenu.toggleClass('toggled');
        $('body').toggleClass('menu-open');
    });

    // Close mobile menu when clicking outside
    $(document).on('click', function(e) {
        if (!$(e.target).closest('.main-navigation').length) {
            menuToggle.attr('aria-expanded', 'false');
            primaryMenu.removeClass('toggled');
            $('body').removeClass('menu-open');
        }
    });

    // Close mobile menu on ESC key
    $(document).on('keydown', function(e) {
        if (e.key === 'Escape') {
            menuToggle.attr('aria-expanded', 'false');
            primaryMenu.removeClass('toggled');
            $('body').removeClass('menu-open');
        }
    });

    // Smooth scroll for anchor links
    $('a[href*="#"]:not([href="#"])').on('click', function() {
        if (location.pathname.replace(/^\//, '') === this.pathname.replace(/^\//, '') &&
            location.hostname === this.hostname) {
            let target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html, body').animate({
                    scrollTop: target.offset().top - 80
                }, 800);
                return false;
            }
        }
    });

    // Add class to header on scroll
    let lastScroll = 0;
    const header = $('#masthead');

    $(window).on('scroll', function() {
        const currentScroll = $(this).scrollTop();

        if (currentScroll > 100) {
            header.addClass('scrolled');
        } else {
            header.removeClass('scrolled');
        }

        lastScroll = currentScroll;
    });

    // Responsive embeds
    function responsiveEmbeds() {
        $('iframe[src*="youtube"], iframe[src*="vimeo"], iframe[src*="mailchimp"]').each(function() {
            if (!$(this).parent().hasClass('embed-responsive')) {
                $(this).wrap('<div class="embed-responsive"></div>');
            }
        });
    }

    // Run on load
    responsiveEmbeds();

    // Lazy load images (simple version)
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });

        document.querySelectorAll('img.lazy').forEach(function(img) {
            imageObserver.observe(img);
        });
    }

})(jQuery);
