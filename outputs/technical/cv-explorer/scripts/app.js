/**
 * Mill CV Explorer - Main Application
 * Interactive decision support tool for CV infrastructure design
 */

class CVExplorer {
  constructor() {
    this.options = [];
    this.criteria = [];
    this.presets = [];
    this.research = {};
    this.weights = {};
    this.radarCharts = {};

    this.init();
  }

  async init() {
    await this.loadData();
    this.initWeights();
    this.renderSliders();
    this.renderOptions();
    this.renderComparison();
    this.renderAccordion();
    this.renderResearch();
    this.bindEvents();
    this.updateRecommendation();
  }

  async loadData() {
    try {
      const [optionsRes, criteriaRes, researchRes] = await Promise.all([
        fetch('data/options.json'),
        fetch('data/criteria.json'),
        fetch('data/research.json')
      ]);

      const optionsData = await optionsRes.json();
      const criteriaData = await criteriaRes.json();
      const researchData = await researchRes.json();

      this.options = optionsData.options;
      this.criteria = criteriaData.criteria;
      this.presets = criteriaData.presets;
      this.research = researchData;
    } catch (error) {
      console.error('Error loading data:', error);
    }
  }

  initWeights() {
    // Initialize with balanced preset
    const balanced = this.presets.find(p => p.id === 'balanced');
    if (balanced) {
      this.weights = { ...balanced.weights };
    } else {
      this.criteria.forEach(c => {
        this.weights[c.id] = c.defaultWeight;
      });
    }
  }

  // Calculate weighted score for an option
  calculateScore(option) {
    return Object.keys(this.weights).reduce((sum, criterionId) => {
      const score = option.scores[criterionId] || 0;
      const weight = this.weights[criterionId];
      return sum + (score * weight);
    }, 0);
  }

  // Get ranked options
  getRankedOptions() {
    return this.options
      .map(option => ({
        ...option,
        weightedScore: this.calculateScore(option)
      }))
      .sort((a, b) => b.weightedScore - a.weightedScore);
  }

  // Render weight sliders
  renderSliders() {
    const container = document.getElementById('slidersContainer');
    if (!container) return;

    container.innerHTML = this.criteria.map(criterion => `
      <div class="slider-item" data-criterion="${criterion.id}">
        <div class="slider-header">
          <span class="slider-label">${criterion.label}</span>
          <span class="slider-value">${Math.round(this.weights[criterion.id] * 100)}%</span>
        </div>
        <input type="range" class="slider-input"
               min="0" max="50"
               value="${Math.round(this.weights[criterion.id] * 100)}"
               data-criterion="${criterion.id}">
        <p class="slider-description">${criterion.description}</p>
      </div>
    `).join('');
  }

  // Render option cards
  renderOptions() {
    const container = document.getElementById('optionsGrid');
    if (!container) return;

    const ranked = this.getRankedOptions();

    container.innerHTML = ranked.map((option, index) => {
      const isRecommended = index === 0;
      const badgeClass = option.badge || (isRecommended ? 'recommended' : '');
      const badgeText = option.badge ? option.badge.replace('-', ' ') : (isRecommended ? 'recommended' : '');

      return `
        <div class="option-card ${isRecommended ? 'recommended' : ''}" data-option="${option.id}">
          <div class="option-header">
            ${badgeText ? `<span class="option-badge ${badgeClass}">${badgeText}</span>` : '<span></span>'}
            <span class="option-rank">#${index + 1}</span>
          </div>
          <h3 class="option-title">${option.name}</h3>
          <p class="option-subtitle">${option.subtitle}</p>
          <div class="option-chart" id="chart-${option.id}"></div>
          <div class="option-metrics">
            <div class="metric">
              <span class="metric-value">${option.metrics.accuracyRange}</span>
              <span class="metric-label">Accuracy</span>
            </div>
            <div class="metric">
              <span class="metric-value">${option.metrics.frictionScore}</span>
              <span class="metric-label">Friction</span>
            </div>
            <div class="metric">
              <span class="metric-value">${option.metrics.costDelta}</span>
              <span class="metric-label">Cost</span>
            </div>
          </div>
          <div style="text-align: center; margin-top: var(--space-md);">
            <span class="option-score">${option.weightedScore.toFixed(2)}</span>
          </div>
        </div>
      `;
    }).join('');

    // Render radar charts for each option
    ranked.forEach(option => {
      this.renderRadarChart(option);
    });
  }

  // Render individual radar chart
  renderRadarChart(option) {
    const ctx = document.getElementById(`chart-${option.id}`);
    if (!ctx) return;

    // Destroy existing chart if it exists
    if (this.radarCharts[option.id]) {
      this.radarCharts[option.id].destroy();
    }

    const labels = this.criteria.map(c => c.shortLabel);
    const data = this.criteria.map(c => option.scores[c.id] || 0);

    this.radarCharts[option.id] = new Chart(ctx, {
      type: 'radar',
      data: {
        labels: labels,
        datasets: [{
          data: data,
          backgroundColor: 'rgba(26, 26, 26, 0.1)',
          borderColor: '#1a1a1a',
          borderWidth: 2,
          pointBackgroundColor: '#1a1a1a',
          pointRadius: 3
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false }
        },
        scales: {
          r: {
            min: 0,
            max: 5,
            ticks: {
              stepSize: 1,
              display: false
            },
            pointLabels: {
              font: { size: 10, family: "'Space Grotesk', sans-serif" },
              color: '#666666'
            },
            grid: { color: '#e5e5e5' },
            angleLines: { color: '#e5e5e5' }
          }
        }
      }
    });
  }

  // Render comparison views
  renderComparison() {
    this.renderParallelCoordinates();
    this.renderScatterPlot();
    this.renderMatrix();
  }

  // Render parallel coordinates chart
  renderParallelCoordinates() {
    const container = document.getElementById('parallelChart');
    if (!container) return;

    const ranked = this.getRankedOptions();
    const criteriaLabels = this.criteria.map(c => c.label);

    const traces = ranked.map((option, index) => {
      const values = this.criteria.map(c => option.scores[c.id] || 0);
      const opacity = index < 3 ? 1 : 0.3;

      return {
        type: 'scatter',
        mode: 'lines+markers',
        name: option.name,
        x: criteriaLabels,
        y: values,
        line: { width: 2 },
        marker: { size: 8 },
        opacity: opacity
      };
    });

    const layout = {
      showlegend: true,
      legend: { orientation: 'h', y: -0.2 },
      margin: { t: 20, b: 100, l: 50, r: 50 },
      yaxis: { range: [0, 5.5], title: 'Score' },
      font: { family: "'Space Grotesk', sans-serif" }
    };

    Plotly.newPlot(container, traces, layout, { responsive: true });
  }

  // Render scatter plot (cost vs accuracy)
  renderScatterPlot() {
    const container = document.getElementById('scatterChart');
    if (!container) return;

    const ranked = this.getRankedOptions();

    const trace = {
      type: 'scatter',
      mode: 'markers+text',
      x: ranked.map(o => o.scores.cost),
      y: ranked.map(o => o.scores.accuracy),
      text: ranked.map(o => o.name.replace('The ', '')),
      textposition: 'top center',
      marker: {
        size: ranked.map(o => o.weightedScore * 8),
        color: ranked.map((_, i) => i),
        colorscale: 'Viridis',
        showscale: false
      },
      hovertemplate: '<b>%{text}</b><br>Cost: %{x}<br>Accuracy: %{y}<extra></extra>'
    };

    const layout = {
      xaxis: { title: 'Cost Score (higher = cheaper)', range: [0.5, 5.5] },
      yaxis: { title: 'Accuracy Score', range: [0.5, 5.5] },
      margin: { t: 20, b: 60, l: 60, r: 20 },
      font: { family: "'Space Grotesk', sans-serif" }
    };

    Plotly.newPlot(container, [trace], layout, { responsive: true });
  }

  // Render score matrix
  renderMatrix() {
    const container = document.getElementById('matrixView');
    if (!container) return;

    const ranked = this.getRankedOptions();

    const getScoreClass = (score) => {
      if (score >= 4) return 'score-high';
      if (score >= 3) return 'score-medium';
      return 'score-low';
    };

    container.innerHTML = `
      <table class="matrix-table">
        <thead>
          <tr>
            <th>Option</th>
            ${this.criteria.map(c => `<th>${c.shortLabel}</th>`).join('')}
            <th>Weighted</th>
          </tr>
        </thead>
        <tbody>
          ${ranked.map(option => `
            <tr>
              <td><strong>${option.name}</strong><br><span style="color: #999; font-size: 0.75rem;">${option.subtitle}</span></td>
              ${this.criteria.map(c => `
                <td class="score-cell ${getScoreClass(option.scores[c.id])}">
                  ${option.scores[c.id]}
                </td>
              `).join('')}
              <td class="score-cell" style="font-weight: 700;">${option.weightedScore.toFixed(2)}</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    `;
  }

  // Render accordion details
  renderAccordion() {
    const container = document.getElementById('detailsAccordion');
    if (!container) return;

    const ranked = this.getRankedOptions();

    container.innerHTML = ranked.map(option => `
      <div class="accordion-item" data-option="${option.id}">
        <div class="accordion-header">
          <div>
            <h4>${option.name} <span class="subtitle">${option.subtitle}</span></h4>
          </div>
          <span class="accordion-toggle">▼</span>
        </div>
        <div class="accordion-content">
          <div class="accordion-section">
            <h5>How it works</h5>
            <p>${option.howItWorks}</p>
          </div>

          <div class="accordion-section">
            <h5>Why it's non-obvious</h5>
            <p>${option.whyNonObvious}</p>
          </div>

          <div class="accordion-section">
            <h5>Hardware bill of materials</h5>
            <table class="hardware-table">
              <thead>
                <tr>
                  <th>Component</th>
                  <th>Specification</th>
                  <th class="price">Price</th>
                </tr>
              </thead>
              <tbody>
                ${option.hardware.map(h => `
                  <tr>
                    <td>${h.component}</td>
                    <td>${h.spec}</td>
                    <td class="price">$${h.price}</td>
                  </tr>
                `).join('')}
                <tr style="font-weight: 600;">
                  <td colspan="2">Total</td>
                  <td class="price">$${option.hardware.reduce((sum, h) => sum + h.price, 0)}</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="accordion-section">
            <h5>Risk analysis</h5>
            <table class="risk-table">
              <thead>
                <tr>
                  <th>Risk</th>
                  <th>Probability</th>
                  <th>Impact</th>
                  <th>Mitigation</th>
                </tr>
              </thead>
              <tbody>
                ${option.risks.map(r => `
                  <tr>
                    <td>${r.risk}</td>
                    <td><span class="risk-badge ${r.probability.toLowerCase()}">${r.probability}</span></td>
                    <td><span class="risk-badge ${r.impact.toLowerCase()}">${r.impact}</span></td>
                    <td>${r.mitigation}</td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>

          <div class="accordion-section">
            <h5>Key metrics</h5>
            <p>
              <strong>Accuracy:</strong> ${option.metrics.accuracyRange}<br>
              <strong>User friction:</strong> ${option.metrics.frictionScore}<br>
              <strong>Cost range:</strong> ${option.metrics.costRange}<br>
              <strong>Cost delta vs baseline:</strong> ${option.metrics.costDelta}
            </p>
          </div>
        </div>
      </div>
    `).join('');
  }

  // Render research library
  renderResearch() {
    // Competitors
    const competitorsList = document.getElementById('competitorsList');
    if (competitorsList && this.research.competitors) {
      competitorsList.innerHTML = this.research.competitors.map(c => `
        <div class="research-item">
          <h4>${c.name}</h4>
          <p><strong>Accuracy:</strong> ${c.accuracy}</p>
          <p>${c.keyFindings}</p>
          <p class="source">Source: <a href="${c.url}" target="_blank">${c.source}</a></p>
        </div>
      `).join('');
    }

    // Benchmarks
    const benchmarksList = document.getElementById('benchmarksList');
    if (benchmarksList && this.research.benchmarks) {
      benchmarksList.innerHTML = this.research.benchmarks.map(b => `
        <div class="research-item">
          <h4>${b.metric}</h4>
          <p><strong>${b.value}</strong> on ${b.dataset}</p>
          <p class="source">Source: ${b.source}</p>
        </div>
      `).join('');
    }

    // Hardware
    const hardwareList = document.getElementById('hardwareList');
    if (hardwareList && this.research.hardware) {
      hardwareList.innerHTML = this.research.hardware.map(h => `
        <div class="research-item">
          <h4>${h.component}</h4>
          <p>${h.specs}</p>
          <p><strong>Price:</strong> ${h.price}</p>
          <p class="source">${h.notes}</p>
        </div>
      `).join('');
    }
  }

  // Update top recommendation
  updateRecommendation() {
    const ranked = this.getRankedOptions();
    const top = ranked[0];

    if (!top) return;

    document.getElementById('topScore').textContent = `${top.weightedScore.toFixed(2)} / 5.0`;
    document.getElementById('topName').textContent = top.name;
    document.getElementById('topSubtitle').textContent = top.subtitle;
    document.getElementById('topDescription').textContent = top.description;
    document.getElementById('topAccuracy').textContent = top.metrics.accuracyRange;
    document.getElementById('topFriction').textContent = top.metrics.frictionScore;
    document.getElementById('topCost').textContent = top.metrics.costRange;
    document.getElementById('topWhy').textContent = top.whyNonObvious;
  }

  // Bind all event listeners
  bindEvents() {
    // Slider changes
    document.querySelectorAll('.slider-input').forEach(slider => {
      slider.addEventListener('input', (e) => this.handleSliderChange(e));
    });

    // Preset buttons
    document.querySelectorAll('.preset-btn').forEach(btn => {
      btn.addEventListener('click', (e) => this.handlePresetClick(e));
    });

    // Tab buttons
    document.querySelectorAll('.tab-btn').forEach(btn => {
      btn.addEventListener('click', (e) => this.handleTabClick(e));
    });

    // Accordion headers
    document.querySelectorAll('.accordion-header').forEach(header => {
      header.addEventListener('click', (e) => this.handleAccordionClick(e));
    });

    // Option cards
    document.querySelectorAll('.option-card').forEach(card => {
      card.addEventListener('click', (e) => this.handleOptionClick(e));
    });

    // Export buttons
    document.getElementById('exportCsv')?.addEventListener('click', () => this.exportCsv());
    document.getElementById('exportPdf')?.addEventListener('click', () => this.exportSummary());

    // Navigation
    document.querySelectorAll('.nav-item').forEach(item => {
      item.addEventListener('click', (e) => this.handleNavClick(e));
    });

    // Scroll spy for navigation
    window.addEventListener('scroll', () => this.handleScroll());
  }

  handleSliderChange(e) {
    const criterionId = e.target.dataset.criterion;
    const value = parseInt(e.target.value) / 100;
    this.weights[criterionId] = value;

    // Update displayed value
    const valueSpan = e.target.parentElement.querySelector('.slider-value');
    if (valueSpan) {
      valueSpan.textContent = `${Math.round(value * 100)}%`;
    }

    // Update total
    const total = Object.values(this.weights).reduce((sum, w) => sum + w, 0);
    document.getElementById('weightsTotal').textContent = `${Math.round(total * 100)}%`;

    // Update preset buttons
    document.querySelectorAll('.preset-btn').forEach(btn => btn.classList.remove('active'));

    // Re-render
    this.renderOptions();
    this.renderComparison();
    this.updateRecommendation();
  }

  handlePresetClick(e) {
    const presetId = e.target.dataset.preset;
    const preset = this.presets.find(p => p.id === presetId);

    if (preset) {
      this.weights = { ...preset.weights };

      // Update sliders
      document.querySelectorAll('.slider-input').forEach(slider => {
        const criterionId = slider.dataset.criterion;
        const value = Math.round(this.weights[criterionId] * 100);
        slider.value = value;

        const valueSpan = slider.parentElement.querySelector('.slider-value');
        if (valueSpan) {
          valueSpan.textContent = `${value}%`;
        }
      });

      // Update total
      document.getElementById('weightsTotal').textContent = '100%';

      // Update active button
      document.querySelectorAll('.preset-btn').forEach(btn => btn.classList.remove('active'));
      e.target.classList.add('active');

      // Re-render
      this.renderOptions();
      this.renderComparison();
      this.updateRecommendation();
    }
  }

  handleTabClick(e) {
    const tab = e.target.dataset.tab;

    // Update buttons
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    e.target.classList.add('active');

    // Show/hide views
    document.getElementById('parallelChart').style.display = tab === 'parallel' ? 'block' : 'none';
    document.getElementById('scatterChart').style.display = tab === 'scatter' ? 'block' : 'none';
    document.getElementById('matrixView').style.display = tab === 'matrix' ? 'block' : 'none';

    // Resize Plotly charts if needed
    if (tab === 'parallel') {
      Plotly.Plots.resize(document.getElementById('parallelChart'));
    } else if (tab === 'scatter') {
      Plotly.Plots.resize(document.getElementById('scatterChart'));
    }
  }

  handleAccordionClick(e) {
    const item = e.target.closest('.accordion-item');
    if (item) {
      item.classList.toggle('open');
    }
  }

  handleOptionClick(e) {
    const optionId = e.target.closest('.option-card')?.dataset.option;
    if (optionId) {
      // Scroll to details and open accordion
      const accordion = document.querySelector(`.accordion-item[data-option="${optionId}"]`);
      if (accordion) {
        accordion.classList.add('open');
        accordion.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }
  }

  handleNavClick(e) {
    document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
    e.target.classList.add('active');
  }

  handleScroll() {
    const sections = document.querySelectorAll('section[id]');
    const scrollPos = window.scrollY + 100;

    sections.forEach(section => {
      if (section.offsetTop <= scrollPos && section.offsetTop + section.offsetHeight > scrollPos) {
        document.querySelectorAll('.nav-item').forEach(item => {
          item.classList.remove('active');
          if (item.getAttribute('href') === `#${section.id}`) {
            item.classList.add('active');
          }
        });
      }
    });
  }

  exportCsv() {
    const ranked = this.getRankedOptions();
    const headers = ['Rank', 'Name', 'Subtitle', ...this.criteria.map(c => c.label), 'Weighted Score'];

    const rows = ranked.map((option, index) => [
      index + 1,
      option.name,
      option.subtitle,
      ...this.criteria.map(c => option.scores[c.id]),
      option.weightedScore.toFixed(2)
    ]);

    const csv = [headers, ...rows].map(row => row.join(',')).join('\n');

    const blob = new Blob([csv], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'cv-explorer-comparison.csv';
    a.click();
    URL.revokeObjectURL(url);
  }

  exportSummary() {
    const ranked = this.getRankedOptions();
    const top = ranked[0];

    const summary = `
Mill Commercial CV Infrastructure Decision Summary
Generated: ${new Date().toISOString().split('T')[0]}

CRITERIA WEIGHTS
${this.criteria.map(c => `- ${c.label}: ${Math.round(this.weights[c.id] * 100)}%`).join('\n')}

TOP RECOMMENDATION: ${top.name}
Score: ${top.weightedScore.toFixed(2)} / 5.0

${top.subtitle}
${top.description}

Key Metrics:
- Accuracy: ${top.metrics.accuracyRange}
- Friction: ${top.metrics.frictionScore}
- Cost: ${top.metrics.costRange}

Why this option:
${top.whyNonObvious}

How it works:
${top.howItWorks}

ALL OPTIONS RANKED:
${ranked.map((o, i) => `${i + 1}. ${o.name} (${o.subtitle}) - ${o.weightedScore.toFixed(2)}`).join('\n')}

---
Mill AI Workflow System | Internal Use Only
    `.trim();

    const blob = new Blob([summary], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'cv-explorer-summary.txt';
    a.click();
    URL.revokeObjectURL(url);
  }
}

// Initialize on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  window.cvExplorer = new CVExplorer();
});
