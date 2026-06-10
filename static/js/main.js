// ================================
// ORIGIN AI MAIN JS
// ================================

document.addEventListener("DOMContentLoaded", () => {

    initCursorGlow();
    initNavbar();
    initCounters();
    initPipelineAnimation();
    initFloatingCards();

});

// ================================
// CURSOR SPOTLIGHT
// ================================

function initCursorGlow() {

    const glow = document.querySelector(".cursor-glow");

    if (!glow) return;

    document.addEventListener("mousemove", (e) => {

        glow.style.left = e.clientX + "px";
        glow.style.top = e.clientY + "px";

    });
}

// ================================
// NAVBAR SCROLL EFFECT
// ================================

function initNavbar() {

    const navbar = document.querySelector(".navbar");

    if (!navbar) return;

    window.addEventListener("scroll", () => {

        if (window.scrollY > 50) {

            navbar.style.background =
                "rgba(5,8,22,0.92)";

            navbar.style.backdropFilter =
                "blur(30px)";

            navbar.style.borderBottom =
                "1px solid rgba(255,255,255,0.15)";

        } else {

            navbar.style.background =
                "rgba(5,8,22,0.65)";

        }

    });

}

// ================================
// COUNTER ANIMATION
// ================================

function initCounters() {

    const counters =
        document.querySelectorAll(".metric h3");

    counters.forEach(counter => {

        const targetText =
            counter.innerText;

        const target =
            parseInt(
                targetText.replace(/\D/g, "")
            );

        let current = 0;

        const increment =
            target / 100;

        const updateCounter = () => {

            current += increment;

            if (current < target) {

                counter.innerText =
                    Math.floor(current) + "+";

                requestAnimationFrame(updateCounter);

            } else {

                counter.innerText =
                    targetText;
            }
        };

        updateCounter();

    });

}

// ================================
// PIPELINE ANIMATION
// ================================

function initPipelineAnimation() {

    const steps =
        document.querySelectorAll(
            ".pipeline-step"
        );

    if (!steps.length) return;

    let activeIndex = 0;

    setInterval(() => {

        steps.forEach(step => {

            step.classList.remove("active");

        });

        steps[activeIndex]
            .classList.add("active");

        activeIndex++;

        if (activeIndex >= steps.length) {

            activeIndex = 0;
        }

    }, 1500);

}

// ================================
// FLOATING CARDS
// ================================

function initFloatingCards() {

    const cards =
        document.querySelectorAll(
            ".floating-card"
        );

    cards.forEach(card => {

        card.addEventListener(
            "mousemove",
            (e) => {

                const rect =
                    card.getBoundingClientRect();

                const x =
                    e.clientX - rect.left;

                const y =
                    e.clientY - rect.top;

                const rotateY =
                    ((x / rect.width) - 0.5) * 20;

                const rotateX =
                    ((y / rect.height) - 0.5) * -20;

                card.style.transform =
                    `
                    perspective(1000px)
                    rotateX(${rotateX}deg)
                    rotateY(${rotateY}deg)
                    scale(1.04)
                    `;
            }
        );

        card.addEventListener(
            "mouseleave",
            () => {

                card.style.transform =
                    `
                    perspective(1000px)
                    rotateX(0deg)
                    rotateY(0deg)
                    scale(1)
                    `;
            }
        );

    });

}
// ======================================
// AGENT NETWORK EFFECT
// ======================================

const agentCards =
document.querySelectorAll(".agent-card");

agentCards.forEach(card => {

    card.addEventListener("mouseenter", () => {

        card.style.boxShadow =
        "0 0 50px rgba(0,245,212,0.4)";

    });

    card.addEventListener("mouseleave", () => {

        card.style.boxShadow =
        "none";

    });

});
// =====================================
// PIPELINE STAGES ANIMATION
// =====================================

const stages =
document.querySelectorAll(".pipeline-stage");

let currentStage = 0;

setInterval(() => {

    stages.forEach(stage => {

        stage.style.boxShadow = "none";

    });

    stages[currentStage].style.boxShadow =
        "0 0 45px rgba(0,245,212,.35)";

    currentStage++;

    if (currentStage >= stages.length) {

        currentStage = 0;
    }

}, 1200);
// ===============================
// MARKET BAR ANIMATION
// ===============================

const bars =
document.querySelectorAll(".bar");

bars.forEach((bar, index) => {

    const finalHeight =
        bar.style.height;

    bar.style.height = "0%";

    setTimeout(() => {

        bar.style.transition =
            "1s ease";

        bar.style.height =
            finalHeight;

    }, index * 150);

});
// ====================================
// RADAR DATA
// ====================================

const radarData = {

    "Healthcare":
    "Opportunities: 421 | Growth: +32%",

    "Energy":
    "Opportunities: 302 | Growth: +28%",

    "Agriculture":
    "Opportunities: 198 | Growth: +21%",

    "Robotics":
    "Opportunities: 367 | Growth: +31%",

    "FinTech":
    "Opportunities: 287 | Growth: +19%",

    "ClimateTech":
    "Opportunities: 255 | Growth: +35%",

    "Cybersecurity":
    "Opportunities: 314 | Growth: +27%",

    "Education":
    "Opportunities: 176 | Growth: +16%"
};

const radarNodes =
document.querySelectorAll(".radar-node");

const industryName =
document.getElementById("industryName");

const industryStats =
document.getElementById("industryStats");

radarNodes.forEach(node => {

    node.addEventListener("mouseenter", () => {

        const industry =
        node.innerText;

        industryName.innerText =
        industry;

        industryStats.innerText =
        radarData[industry];

    });

});