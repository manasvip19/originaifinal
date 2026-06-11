// ======================================
// DASHBOARD DYNAMIC BINDING
// ======================================

async function loadAnalysis() {
    let result = null;

    try {
        result = JSON.parse(localStorage.getItem("originai_result") || "null");
    } catch (error) {
        console.warn("localStorage parse failed", error);
    }

    if (!result || !result.analysis) {
        try {
            const response = await fetch("/api/analysis/latest");
            if (response.ok) {
                result = await response.json();
            }
        } catch (error) {
            console.warn("Failed to fetch latest analysis", error);
        }
    }

    if (!result || !result.analysis) {
        return;
    }

    const analysis = result.analysis;
    const startup = analysis.startup || {};
    const market = analysis.market || {};
    const scores = analysis.scores || {};

    const mappings = [
        { id: "startup-name", value: startup.name || ((window.i18n && typeof i18n.t === 'function') ? i18n.t('dashboard.default_research_opportunity') : "Research Opportunity") },
        { id: "industry", value: analysis.industry || ((window.i18n && typeof i18n.t === 'function') ? i18n.t('dashboard.default_industry') : "Technology") },
        { id: "score", value: scores.investment_score || 0 },
        { id: "summary-text", value: analysis.research_summary || ((window.i18n && typeof i18n.t === 'function') ? i18n.t('dashboard.default_summary') : "Research summary will appear here after analysis.") },
        { id: "discovery-text", value: analysis.key_discovery || ((window.i18n && typeof i18n.t === 'function') ? i18n.t('dashboard.default_discovery') : "Key discovery will appear here.") },
        { id: "commercial-potential", value: `${scores.commercial_potential || 0} / 100` },
        { id: "risk-score", value: `Risk score: ${scores.risk_score || "--"}` },
        { id: "revenue-model", value: startup.revenue_streams ? startup.revenue_streams.join(", ") : startup.business_model || "--" },
        { id: "funding-readiness", value: `${scores.funding_readiness_score || 0} / 100` },
        { id: "tech-readiness", value: `${scores.technology_readiness_level || 0} / 10` },
        { id: "market-intelligence", value: market.market_size || "--" },
        { id: "innovation-score", value: `${scores.innovation_level || 0} / 100` },
        { id: "tam-value", value: market.tam || "--" },
        { id: "sam-value", value: market.sam || "--" },
        { id: "competition-value", value: startup.competitive_advantage || "--" },
        { id: "risk-value", value: `${scores.risk_score || "--"}` },
        { id: "competition-intelligence", value: startup.competitive_advantage || "--" },
        { id: "scalability-intelligence", value: `${scores.scalability_score || 0} / 100` },
        { id: "commercialization-readiness-score", value: `${scores.commercialization_readiness_score || 0} / 100` },
        { id: "funding-readiness-score", value: `${scores.funding_readiness_score || 0} / 100` },
        { id: "investor-interest-score", value: `${scores.investor_interest_score || 0} / 100` },
        { id: "market-timing-score", value: `${scores.market_timing_score || 0} / 100` },
        { id: "startup-success-probability", value: scores.startup_success_probability || "Unknown" },
        { id: "unicorn-potential-score", value: `${scores.unicorn_potential_score || 0} / 100` }
    ];

    mappings.forEach(item => {
        const element = document.getElementById(item.id);
        if (element && item.value !== undefined && item.value !== null) {
            element.innerText = item.value;
        }
    });

    const scoreValue = document.querySelector(".score-value");
    const target = Number(scores.investment_score || 0);
    animateScore(scoreValue, target);
    renderOpportunityFeed(analysis);
}

function animateScore(element, target) {
    if (!element) return;
    let count = 0;
    const finalTarget = Math.min(Math.max(target, 0), 100);
    const increment = Math.max(1, Math.floor(finalTarget / 60));
    const timer = setInterval(() => {
        count += increment;
        if (count >= finalTarget) {
            element.innerText = finalTarget;
            clearInterval(timer);
            return;
        }
        element.innerText = count;
    }, 15);
}

function renderOpportunityFeed(analysis) {
    const feed = document.getElementById("opportunity-feed");
    if (!feed) return;

    const startup = analysis.startup || {};
    const entries = [
        {
            title: startup.name || "Research Opportunity",
            subtitle: analysis.industry || "Industry"
        },
        {
            title: startup.problem || "Problem statement",
            subtitle: "Problem"
        },
        {
            title: startup.solution || "Solution overview",
            subtitle: "Solution"
        },
        {
            title: startup.business_model || "Business model",
            subtitle: "Model"
        }
    ];

    feed.innerHTML = entries.map(item => `
        <div class="feed-card">
            <h3>${item.title}</h3>
            <span>${item.subtitle}</span>
        </div>
    `).join("");
}

async function loadHistory() {
    const list = document.getElementById("recent-analyses");
    if (!list) return;

    try {
        const response = await fetch("/api/analysis/history");
        if (!response.ok) {
            list.innerHTML = "<p>No recent analyses available.</p>";
            return;
        }

        const history = await response.json();
        if (!history.length) {
            list.innerHTML = "<p>No recent analyses available.</p>";
            return;
        }

        list.innerHTML = history.slice(0, 4).map(entry => {
            const name = entry.analysis.startup?.name || entry.filename || "Research Opportunity";
            const industry = entry.analysis.industry || "Unknown";
            const timestamp = new Date(entry.timestamp).toLocaleDateString();
            return `<div class="history-card"><strong>${name}</strong><span>${industry}</span><small>${timestamp}</small></div>`;
        }).join("");
    } catch (error) {
        list.innerHTML = "<p>Unable to load recent analyses.</p>";
    }
}

// ======================================
// INITIAL ANIMATIONS
// ======================================

const bars = document.querySelectorAll(".bar");
bars.forEach(bar => {
    const finalHeight = bar.style.height;
    bar.style.height = "0%";
    setTimeout(() => {
        bar.style.transition = "1.2s ease";
        bar.style.height = finalHeight;
    }, 300);
});

const feedCards = document.querySelectorAll(".feed-card");
feedCards.forEach((card, index) => {
    card.style.opacity = "0";
    card.style.transform = "translateY(40px)";
    setTimeout(() => {
        card.style.transition = ".6s ease";
        card.style.opacity = "1";
        card.style.transform = "translateY(0)";
    }, index * 150);
});

// ======================================
// CARD TILT EFFECT
// ======================================

const cards = document.querySelectorAll(".card");
cards.forEach(card => {
    card.addEventListener("mousemove", e => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const rotateY = ((x / rect.width) - 0.5) * 10;
        const rotateX = ((y / rect.height) - 0.5) * -10;
        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.02)`;
    });

    card.addEventListener("mouseleave", () => {
        card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale(1)`;
    });
});

loadAnalysis();
loadHistory();
document.addEventListener('i18n:changed', () => {
    loadAnalysis();
    loadHistory();
});
