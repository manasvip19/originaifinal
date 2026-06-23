async function loadAnalysisData() {
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

    if (!result || !result.analysis) {
        const fallbackText = 'No analysis data is available. Please upload a research paper from the Analyzer page first.';
        document.querySelectorAll('#investor-report p').forEach(element => {
            if (element.id) element.innerText = fallbackText;
        });
        return;
    }

    const report = result.analysis.investor_report || {};
    const startup = result.analysis.startup || {};
    const market = result.analysis.market || {};
    const scores = result.analysis.scores || {};

    const mappings = {
        'executive-summary': report.executive_summary,
        'research-overview': report.research_overview,
        'key-discovery': report.key_discovery,
        'startup-opportunity': report.startup_opportunity,
        'problem-solved': report.problem_solved,
        'solution': report.solution,
        'industry': report.industry || result.analysis.industry || 'Unknown',
        'target-market': report.target_market || startup.target_market || 'Not available',
        'market-size': report.market_size,
        'tam': report.tam,
        'sam': report.sam,
        'som': report.som,
        'business-model': report.business_model,
        'revenue-model': report.revenue_model,
        'go-to-market-plan': report.go_to_market_plan,
        'competition-analysis': report.competition_analysis,
        'risk-assessment': report.risk_analysis,
        'technology-readiness': report.technology_readiness,
        'commercialization-readiness': report.commercialization_readiness,
        'funding-readiness': report.funding_readiness,
        'expected-roi': report.expected_roi,
        'investment-recommendation': report.investment_recommendation,
        'final-verdict': report.final_verdict
    };

    Object.entries(mappings).forEach(([id, value]) => {
        const element = document.getElementById(id);
        if (element) {
            element.innerText = value || 'Not available';
        }
    });

    const title = document.querySelector('.hero h1');
    if (title && startup.name) {
        title.textContent = `${startup.name} Investor Report`;
    }
}

function downloadReport() {
    let result = null;
    try {
        result = JSON.parse(localStorage.getItem('originai_result') || 'null');
    } catch (error) {
        console.warn(error);
    }

    if (!result || !result.analysis) {
        return;
    }

    const report = result.analysis.investor_report || {};
    const blob = new Blob([JSON.stringify(report, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'originai-investor-report.json';
    document.body.appendChild(a);
    a.click();
    URL.revokeObjectURL(url);
    a.remove();
}

function downloadStartupSummary() {
    let result = null;
    try {
        result = JSON.parse(localStorage.getItem('originai_result') || 'null');
    } catch (error) {
        console.warn(error);
    }

    if (!result || !result.analysis) {
        return;
    }

    const summary = {
        research_summary: result.analysis.research_summary,
        key_discovery: result.analysis.key_discovery,
        industry: result.analysis.industry,
        startup: result.analysis.startup,
        market: result.analysis.market,
        scores: result.analysis.scores
    };
    const blob = new Blob([JSON.stringify(summary, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'originai-startup-summary.json';
    document.body.appendChild(a);
    a.click();
    URL.revokeObjectURL(url);
    a.remove();
}

function exportReportPdf() {
    let result = null;
    try {
        result = JSON.parse(localStorage.getItem('originai_result') || 'null');
    } catch (error) {
        console.warn(error);
    }

    if (!result || !result.analysis) {
        return;
    }

    const report = result.analysis.investor_report || {};
    const startup = result.analysis.startup || {};
    const { jsPDF } = window.jspdf;
    const pdf = new jsPDF({ unit: 'pt', format: 'letter' });
    const margin = 40;
    let y = 40;
    const lineHeight = 16;

    pdf.setFontSize(18);
    pdf.text('OriginAI Investor Report', margin, y);
    y += 26;
    pdf.setFontSize(12);
    pdf.text(`Startup: ${startup.name || 'N/A'}`, margin, y);
    y += 18;
    pdf.text(`Industry: ${report.industry || result.analysis.industry || 'N/A'}`, margin, y);
    y += 24;

    const sections = [
        { title: 'Executive Summary', text: report.executive_summary },
        { title: 'Problem Solved', text: report.problem_solved },
        { title: 'Solution', text: report.solution },
        { title: 'Industry', text: report.industry || result.analysis.industry },
        { title: 'Target Market', text: report.target_market },
        { title: 'Market Size', text: `${report.market_size || 'N/A'} • TAM ${report.tam || 'N/A'} • SAM ${report.sam || 'N/A'} • SOM ${report.som || 'N/A'}` },
        { title: 'Business Model', text: report.business_model },
        { title: 'Revenue Model', text: report.revenue_model },
        { title: 'Go-To-Market Strategy', text: report.go_to_market_plan },
        { title: 'Competitive Landscape', text: report.competition_analysis },
        { title: 'Risk Analysis', text: report.risk_analysis },
        { title: 'Technology Readiness', text: report.technology_readiness },
        { title: 'Commercialization Readiness', text: report.commercialization_readiness },
        { title: 'Funding Readiness', text: report.funding_readiness },
        { title: 'Expected ROI', text: report.expected_roi },
        { title: 'Investment Recommendation', text: report.investment_recommendation },
        { title: 'Final Verdict', text: report.final_verdict }
    ];

    sections.forEach(section => {
        pdf.setFontSize(14);
        pdf.text(section.title, margin, y);
        y += 18;
        pdf.setFontSize(11);
        const text = section.text || 'Not available';
        const lines = pdf.splitTextToSize(text, 520);
        pdf.text(lines, margin, y);
        y += lines.length * lineHeight + 12;
        if (y > 740) {
            pdf.addPage();
            y = 40;
        }
    });

    pdf.save('originai-investor-report.pdf');
}

function printReport() {
    window.print();
}

window.addEventListener('DOMContentLoaded', () => {
    loadAnalysisData();
    const downloadButton = document.querySelector('.btn-secondary[onclick="downloadAnalysis()"]');
    if (downloadButton) {
        downloadButton.addEventListener('click', downloadAnalysis);
    }
});

function downloadAnalysis() {
    let result = null;
    try {
        result = JSON.parse(localStorage.getItem('originai_result') || 'null');
    } catch (error) {
        console.warn(error);
    }

    if (!result || !result.analysis) {
        return;
    }

    const blob = new Blob([JSON.stringify(result.analysis, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'originai-analysis.json';
    document.body.appendChild(a);
    a.click();
    URL.revokeObjectURL(url);
    a.remove();
}
