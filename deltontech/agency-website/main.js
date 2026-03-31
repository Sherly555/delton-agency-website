// main.js - Vanilla JS
document.addEventListener('DOMContentLoaded', () => {
    // Register GSAP ScrollTrigger
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger, TextPlugin);
    } else {
        console.error("GSAP not loaded");
    }

    // Hero Animations
    if (document.querySelector('.gsap-hero-fade')) {
        gsap.from(".gsap-hero-fade > *:not(h1)", {
            y: 30,
            opacity: 0,
            duration: 0.8,
            stagger: 0.2,
            ease: "power3.out"
        });

        const heroH1 = document.querySelector('.gsap-hero-fade h1');
        if (heroH1) {
            heroH1.innerHTML = `<span class="type-word1"></span><br/><span class="gradient-text type-word2"></span><span class="type-word3"></span><span class="inline-block w-1.5 h-10 md:h-14 bg-[#DC2626] ml-2 animate-pulse align-middle"></span>`;
            
            const tl = gsap.timeline({ delay: 0.2, repeat: -1, repeatDelay: 25.6 });
            tl.to('.type-word1', { duration: 1.6, text: "We Build Digital ", ease: "none" })
              .to('.type-word2', { duration: 1.2, text: "Experiences", ease: "none" })
              .to('.type-word3', { duration: 1.6, text: " That Matter", ease: "none" });
        }
    }

    if (document.querySelector('.gsap-hero-image')) {
        gsap.from(".gsap-hero-image", {
            scale: 0.9,
            opacity: 0,
            duration: 1,
            delay: 0.4,
            ease: "power3.out"
        });
    }

    // Scroll Animations for generic elements
    if (typeof gsap !== 'undefined') {
        gsap.utils.toArray('.glass.p-8').forEach(card => {
            gsap.from(card, {
                scrollTrigger: {
                    trigger: card,
                    start: "top bottom-=100",
                    toggleActions: "play none none reverse"
                },
                y: 50,
                opacity: 0,
                duration: 0.6,
                ease: "power2.out"
            });
        });
    }

    // Mobile menu toggle
    const menuBtn = document.querySelector('header button');
    const nav = document.querySelector('header nav');

    if (menuBtn && nav) {
        menuBtn.addEventListener('click', () => {
            nav.classList.toggle('hidden');
            nav.classList.toggle('flex');
            nav.classList.toggle('flex-col');
            nav.classList.toggle('absolute');
            nav.classList.toggle('top-full');
            nav.classList.toggle('left-0');
            nav.classList.toggle('w-full');
            nav.classList.toggle('bg-dark/95');
            nav.classList.toggle('p-6');
            nav.classList.toggle('backdrop-blur-xl');
            nav.classList.toggle('min-h-[90vh]');
        });
    }
});
