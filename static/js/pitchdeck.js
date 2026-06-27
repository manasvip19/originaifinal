async function loadPitchDeck() {
    let result = null;
    try {
        result = JSON.parse(localStorage.getItem('originai_result') || 'null');
    } catch (error) {
        console.warn('local storage parse failed', error);
    }

    if (!result || !result.analysis) {
        try {
            const response = await fetch('/api/analysis/latest');
            if (response.ok) {
                result = await response.json();
            }
        } catch (error) {
            console.warn('fetch latest analysis failed', error);
        }
    }

    const container = document.getElementById('deck-slides');
    if (!container) return;

    if (!result || !result.analysis) {
        const noDeck = (window.i18n && typeof i18n.t === 'function') ? i18n.t('pitchdeck.no_deck') : 'No pitch deck available';
        const uploadFirst = (window.i18n && typeof i18n.t === 'function') ? i18n.t('pitchdeck.upload_first') : 'Upload a PDF and run analysis first.';
        container.innerHTML = `<div class="card"><h3>${noDeck}</h3><p>${uploadFirst}</p></div>`;
        return;
    }

    const analysis = result.analysis;
    const startup = analysis.startup || {};
    const market = analysis.market || {};
    const scores = analysis.scores || {};
    const report = analysis.investor_report || {};

    const slides = [
        {
            title: 'Cover',
            content: `${startup.name || 'Research Venture'} — ${startup.tagline || 'Research-led commercialization for the next generation of enterprise products.'}`
        },
        {
            title: 'Problem',
            content: startup.problem || 'Research teams struggle to turn complex discoveries into investor-ready products and commercial value.'
        },
        {
            title: 'Solution',
            content: startup.solution || 'A commercialization engine that converts research findings into scalable market-ready offerings and investor decks.'
        },
        {
            title: 'Technology',
            content: startup.technology_highlight || report.solution || 'A technology platform designed for rapid validation, integration and commercialization of breakthrough research.'
        },
        {
            title: 'Market',
            content: `Total addressable market: ${market.market_size || 'N/A'}, growth: ${market.growth_rate || 'N/A'}, TAM ${market.tam || 'N/A'}, SAM ${market.sam || 'N/A'}, SOM ${market.som || 'N/A'}`
        },
        {
            title: 'Competition',
            content: startup.competitive_advantage || report.competition_analysis || 'Differentiates through research-first product strategy, faster go-to-market, and specialized industry execution.'
        },
        {
            title: 'Business Model',
            content: startup.business_model || 'Subscription SaaS with enterprise licensing, data monetization, and managed services.'
        },
        {
            title: 'Revenue',
            content: startup.revenue_streams ? startup.revenue_streams.join(', ') : report.revenue_model || 'Subscription, licensing, and professional services.'
        },
        {
            title: 'Financials',
            content: `Opportunity score: ${scores.investment_score || 'N/A'} / 100, Funding readiness: ${scores.funding_readiness_score || 'N/A'} / 100, Investor interest: ${scores.investor_interest_score || 'N/A'} / 100.`
        },
        {
            title: 'Roadmap',
            content: startup.growth_strategy || 'Pilot, validate, partner, and scale into adjacent markets while securing enterprise adoption.'
        },
        {
            title: 'Funding Ask',
            content: startup.funding_strategy || 'Raise capital to accelerate product development, validate commercial pilots, and scale customer acquisition.'
        },
        {
            title: 'Vision',
            content: startup.vision || 'To turn research breakthroughs into the next generation of market-leading startups.'
        },
        {
            title: 'Conclusion',
            content: report.final_verdict || 'This opportunity is positioned for early-stage investors seeking research-backed, high-growth commercialization potential.'
        }
    ];

    const slideLabel = (window.i18n && typeof i18n.t === 'function') ? i18n.t('slide.slide_number') : 'Slide';
    container.innerHTML = slides.map((slide, index) => `
        <div class="card slide-card">
            <div class="slide-number">${slideLabel} ${index + 1}</div>
            <h3>${slide.title}</h3>
            <p>${slide.content}</p>
        </div>
    `).join('');
}

function downloadPitchDeck() {
    let result = null;
    try {
        result = JSON.parse(localStorage.getItem('originai_result') || 'null');
    } catch (error) {
        console.warn(error);
    }

    if (!result || !result.analysis) return;

    const analysis = result.analysis;
    const startup = analysis.startup || {};
    const market = analysis.market || {};
    const scores = analysis.scores || {};
    const report = analysis.investor_report || {};
    const { jsPDF } = window.jspdf;
    const pdf = new jsPDF({ unit: 'pt', format: 'letter' });
    const margin = 40;
    let y = 40;

    const slides = [
        { title: 'Cover', text: `${startup.name || 'Research Venture'} — ${startup.tagline || 'Research-led commercialization for market impact.'}` },
        { title: 'Problem', text: startup.problem || 'Research discoveries are not reaching investors fast enough due to commercialization gaps.' },
        { title: 'Solution', text: startup.solution || 'A structured product and go-to-market framework that converts research into scalable startup ventures.' },
        { title: 'Technology', text: startup.technology_highlight || 'A research-first technology platform that accelerates product-market fit and commercialization.' },
        { title: 'Market', text: `Market size: ${market.market_size || 'N/A'}, TAM: ${market.tam || 'N/A'}, SAM: ${market.sam || 'N/A'}, SOM: ${market.som || 'N/A'}, Growth: ${market.growth_rate || 'N/A'}` },
        { title: 'Competition', text: startup.competitive_advantage || 'Differentiates with research-backed IP, a targeted commercialization path, and strong early adoption strategy.' },
        { title: 'Business Model', text: startup.business_model || 'Subscription SaaS with enterprise licensing and strategic services.' },
        { title: 'Revenue', text: startup.revenue_streams ? startup.revenue_streams.join(', ') : report.revenue_model || 'Subscription, licensing, and services.' },
        { title: 'Financials', text: `Opportunity score ${scores.investment_score || 'N/A'} / 100, Funding readiness ${scores.funding_readiness_score || 'N/A'} / 100, Investor interest ${scores.investor_interest_score || 'N/A'} / 100.` },
        { title: 'Roadmap', text: startup.growth_strategy || 'Validate pilots, expand into enterprise verticals, and scale commercialization.' },
        { title: 'Funding Ask', text: startup.funding_strategy || 'Raise earliest capital to complete commercialization milestones and build market traction.' },
        { title: 'Vision', text: startup.vision || 'To convert high-impact research into enduring companies that lead the next wave of innovation.' },
        { title: 'Conclusion', text: report.final_verdict || 'This pitch deck supports a compelling investment case for research commercialization.' }
    ];

    pdf.setFontSize(18);
    pdf.text('OriginAI Pitch Deck', margin, y);
    y += 30;

    slides.forEach(slide => {
        pdf.setFontSize(14);
        pdf.text(slide.title, margin, y);
        y += 20;
        pdf.setFontSize(11);
        const lines = pdf.splitTextToSize(slide.text, 520);
        pdf.text(lines, margin, y);
        y += lines.length * 16 + 18;
        if (y > 720) {
            pdf.addPage();
            y = 40;
        }
    });

    pdf.save('originai-pitch-deck.pdf');
}

function printDeck() {
    window.print();
}

window.addEventListener('DOMContentLoaded', loadPitchDeck);
document.addEventListener('i18n:changed', loadPitchDeck);
