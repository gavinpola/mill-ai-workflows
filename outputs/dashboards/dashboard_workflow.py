#!/usr/bin/env python3
"""
Mill Customer Data Dashboard Workflow

This workflow takes raw customer food waste data (in various formats) and
automatically generates customized dashboards and insights.

The key insight: every customer's data is different, but the workflow is the same.
This script demonstrates how to:
1. Ingest and normalize various data formats
2. Automatically detect data types and structures
3. Generate appropriate visualizations
4. Create a customized dashboard output

Usage:
    python dashboard_workflow.py --input data.csv --output dashboard.html
    python dashboard_workflow.py --demo  # Run with sample data
"""

import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path
import random
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from enum import Enum

# Check for required libraries, install if missing
try:
    import pandas as pd
    import numpy as np
except ImportError:
    print("Installing required libraries...")
    import subprocess
    subprocess.check_call(["pip", "install", "pandas", "numpy"])
    import pandas as pd
    import numpy as np


class DataType(Enum):
    """Types of data customers might provide"""
    WEIGHT_TIMESERIES = "weight_timeseries"      # Weight measurements over time
    ITEM_COUNTS = "item_counts"                   # Counts of wasted items
    COST_DATA = "cost_data"                       # Dollar values of waste
    CATEGORY_BREAKDOWN = "category_breakdown"     # Waste by category
    LOCATION_DATA = "location_data"               # Waste by location/store
    IMAGE_METADATA = "image_metadata"             # Metadata from waste images
    MIXED = "mixed"                               # Combination of above


@dataclass
class DataProfile:
    """Profile of the ingested data"""
    data_type: DataType
    date_range: tuple
    num_records: int
    columns: List[str]
    has_location: bool
    has_category: bool
    has_cost: bool
    has_weight: bool
    quality_score: float  # 0-1, based on completeness
    recommended_charts: List[str]


@dataclass
class Insight:
    """A generated insight from the data"""
    title: str
    description: str
    metric: str
    value: Any
    trend: str  # "up", "down", "stable"
    importance: str  # "high", "medium", "low"
    recommendation: str


class DataIngestor:
    """Handles various input formats and normalizes to standard structure"""

    SUPPORTED_FORMATS = ['.csv', '.json', '.xlsx', '.parquet']

    def __init__(self, file_path: Optional[str] = None):
        self.file_path = file_path
        self.raw_data = None
        self.normalized_data = None
        self.profile = None

    def ingest(self, file_path: Optional[str] = None) -> pd.DataFrame:
        """Ingest data from file and return normalized DataFrame"""
        path = file_path or self.file_path

        if path is None:
            raise ValueError("No file path provided")

        suffix = Path(path).suffix.lower()

        if suffix == '.csv':
            self.raw_data = pd.read_csv(path)
        elif suffix == '.json':
            self.raw_data = pd.read_json(path)
        elif suffix == '.xlsx':
            self.raw_data = pd.read_excel(path)
        elif suffix == '.parquet':
            self.raw_data = pd.read_parquet(path)
        else:
            raise ValueError(f"Unsupported format: {suffix}")

        self.normalized_data = self._normalize(self.raw_data)
        self.profile = self._profile_data(self.normalized_data)

        return self.normalized_data

    def ingest_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Ingest data directly from a DataFrame"""
        self.raw_data = df
        self.normalized_data = self._normalize(df)
        self.profile = self._profile_data(self.normalized_data)
        return self.normalized_data

    def _normalize(self, df: pd.DataFrame) -> pd.DataFrame:
        """Normalize column names and data types"""
        # Standardize column names
        df.columns = [c.lower().strip().replace(' ', '_') for c in df.columns]

        # Detect and parse date columns
        date_patterns = ['date', 'time', 'timestamp', 'datetime', 'day']
        for col in df.columns:
            if any(p in col for p in date_patterns):
                try:
                    df[col] = pd.to_datetime(df[col])
                except:
                    pass

        # Detect and convert numeric columns
        for col in df.columns:
            if df[col].dtype == 'object':
                try:
                    df[col] = pd.to_numeric(df[col].str.replace('[$,]', '', regex=True))
                except:
                    pass

        return df

    def _profile_data(self, df: pd.DataFrame) -> DataProfile:
        """Analyze data and create a profile"""
        columns = list(df.columns)

        # Detect what's in the data
        has_location = any(c in columns for c in ['location', 'store', 'site', 'warehouse', 'location_id'])
        has_category = any(c in columns for c in ['category', 'type', 'item_type', 'food_type', 'waste_category'])
        has_cost = any(c in columns for c in ['cost', 'value', 'price', 'amount', 'dollars'])
        has_weight = any(c in columns for c in ['weight', 'pounds', 'kg', 'lbs', 'mass', 'weight_lbs'])

        # Find date column
        date_col = None
        for col in columns:
            if df[col].dtype == 'datetime64[ns]':
                date_col = col
                break

        date_range = (None, None)
        if date_col:
            date_range = (df[date_col].min(), df[date_col].max())

        # Determine data type
        if has_weight and date_col:
            data_type = DataType.WEIGHT_TIMESERIES
        elif has_cost:
            data_type = DataType.COST_DATA
        elif has_category:
            data_type = DataType.CATEGORY_BREAKDOWN
        elif has_location:
            data_type = DataType.LOCATION_DATA
        else:
            data_type = DataType.MIXED

        # Calculate quality score
        completeness = 1 - (df.isnull().sum().sum() / (len(df) * len(df.columns)))
        quality_score = min(1.0, completeness)

        # Recommend charts based on data
        charts = []
        if date_col:
            charts.append("time_series")
        if has_location:
            charts.append("location_comparison")
            charts.append("location_heatmap")
        if has_category:
            charts.append("category_breakdown")
            charts.append("category_treemap")
        if has_weight or has_cost:
            charts.append("trend_analysis")
            charts.append("distribution")
        if has_location and (has_weight or has_cost):
            charts.append("location_ranking")

        return DataProfile(
            data_type=data_type,
            date_range=date_range,
            num_records=len(df),
            columns=columns,
            has_location=has_location,
            has_category=has_category,
            has_cost=has_cost,
            has_weight=has_weight,
            quality_score=quality_score,
            recommended_charts=charts
        )


class InsightGenerator:
    """Generates insights from the data"""

    def __init__(self, df: pd.DataFrame, profile: DataProfile):
        self.df = df
        self.profile = profile

    def generate_all_insights(self) -> List[Insight]:
        """Generate all applicable insights"""
        insights = []

        # Always generate summary insight
        insights.append(self._summary_insight())

        # Conditional insights based on data
        if self.profile.has_weight:
            insights.extend(self._weight_insights())
        if self.profile.has_cost:
            insights.extend(self._cost_insights())
        if self.profile.has_category:
            insights.extend(self._category_insights())
        if self.profile.has_location:
            insights.extend(self._location_insights())
        if self.profile.date_range[0]:
            insights.extend(self._trend_insights())

        return insights

    def _summary_insight(self) -> Insight:
        """Generate summary insight"""
        return Insight(
            title="Data Overview",
            description=f"Analyzed {self.profile.num_records:,} records across {len(self.profile.columns)} data fields",
            metric="Records",
            value=self.profile.num_records,
            trend="stable",
            importance="high",
            recommendation="Review the detailed breakdown below for actionable insights"
        )

    def _weight_insights(self) -> List[Insight]:
        """Generate weight-related insights"""
        insights = []
        weight_col = self._find_column(['weight', 'pounds', 'kg', 'lbs', 'weight_lbs'])

        if weight_col:
            total_weight = self.df[weight_col].sum()
            avg_weight = self.df[weight_col].mean()

            insights.append(Insight(
                title="Total Waste Weight",
                description=f"Total recorded food waste across all data",
                metric="Total lbs",
                value=f"{total_weight:,.0f}",
                trend="down" if total_weight < avg_weight * len(self.df) * 0.9 else "stable",
                importance="high",
                recommendation="Focus reduction efforts on highest-weight categories"
            ))

        return insights

    def _cost_insights(self) -> List[Insight]:
        """Generate cost-related insights"""
        insights = []
        cost_col = self._find_column(['cost', 'value', 'price', 'amount', 'dollars'])

        if cost_col:
            total_cost = self.df[cost_col].sum()

            insights.append(Insight(
                title="Total Waste Value",
                description=f"Dollar value of recorded food waste",
                metric="Total $",
                value=f"${total_cost:,.0f}",
                trend="stable",
                importance="high",
                recommendation="Target high-value items for immediate reduction"
            ))

        return insights

    def _category_insights(self) -> List[Insight]:
        """Generate category-related insights"""
        insights = []
        cat_col = self._find_column(['category', 'type', 'item_type', 'food_type', 'waste_category'])
        weight_col = self._find_column(['weight', 'pounds', 'kg', 'lbs', 'weight_lbs'])

        if cat_col and weight_col:
            top_category = self.df.groupby(cat_col)[weight_col].sum().idxmax()
            top_value = self.df.groupby(cat_col)[weight_col].sum().max()

            insights.append(Insight(
                title="Top Waste Category",
                description=f"'{top_category}' is the largest contributor to food waste",
                metric="Category waste",
                value=f"{top_value:,.0f} lbs",
                trend="stable",
                importance="high",
                recommendation=f"Deep dive into {top_category} to identify reduction opportunities"
            ))

        return insights

    def _location_insights(self) -> List[Insight]:
        """Generate location-related insights"""
        insights = []
        loc_col = self._find_column(['location', 'store', 'site', 'warehouse', 'location_id'])
        weight_col = self._find_column(['weight', 'pounds', 'kg', 'lbs', 'weight_lbs'])

        if loc_col and weight_col:
            location_totals = self.df.groupby(loc_col)[weight_col].sum()
            best = location_totals.idxmin()
            worst = location_totals.idxmax()
            variance = (location_totals.max() - location_totals.min()) / location_totals.mean() * 100

            insights.append(Insight(
                title="Location Variance",
                description=f"'{worst}' wastes {variance:.0f}% more than '{best}'",
                metric="Variance",
                value=f"{variance:.0f}%",
                trend="stable",
                importance="high",
                recommendation=f"Investigate best practices at {best} and replicate"
            ))

        return insights

    def _trend_insights(self) -> List[Insight]:
        """Generate trend-related insights"""
        insights = []
        date_col = self._find_date_column()
        weight_col = self._find_column(['weight', 'pounds', 'kg', 'lbs', 'weight_lbs'])

        if date_col and weight_col:
            # Weekly trend
            weekly = self.df.set_index(date_col).resample('W')[weight_col].sum()
            if len(weekly) >= 2:
                change = (weekly.iloc[-1] - weekly.iloc[0]) / weekly.iloc[0] * 100
                trend = "down" if change < -5 else ("up" if change > 5 else "stable")

                insights.append(Insight(
                    title="Weekly Trend",
                    description=f"Waste has {'decreased' if change < 0 else 'increased'} {abs(change):.1f}% over the period",
                    metric="Change",
                    value=f"{change:+.1f}%",
                    trend=trend,
                    importance="medium",
                    recommendation="Continue monitoring weekly trends for sustained improvement"
                ))

        return insights

    def _find_column(self, candidates: List[str]) -> Optional[str]:
        """Find first matching column from candidates"""
        for col in self.df.columns:
            if any(c in col.lower() for c in candidates):
                return col
        return None

    def _find_date_column(self) -> Optional[str]:
        """Find datetime column"""
        for col in self.df.columns:
            if self.df[col].dtype == 'datetime64[ns]':
                return col
        return None


class DashboardGenerator:
    """Generates HTML dashboard from data and insights"""

    def __init__(self, df: pd.DataFrame, profile: DataProfile, insights: List[Insight], customer_name: str = "Customer"):
        self.df = df
        self.profile = profile
        self.insights = insights
        self.customer_name = customer_name

    def generate(self) -> str:
        """Generate complete HTML dashboard"""
        return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{self.customer_name} - Food Waste Dashboard | Mill</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {{
            --mill-green: #1a472a;
            --mill-light: #2d5a3d;
            --mill-accent: #4a7c59;
            --bg-light: #f8f9fa;
            --text-dark: #333;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: var(--bg-light);
            color: var(--text-dark);
            line-height: 1.6;
        }}
        .header {{
            background: linear-gradient(135deg, var(--mill-green) 0%, var(--mill-light) 100%);
            color: white;
            padding: 30px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .header h1 {{ font-size: 1.8em; font-weight: 600; }}
        .header .meta {{ opacity: 0.9; font-size: 0.9em; }}
        .container {{ max-width: 1400px; margin: 0 auto; padding: 30px; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }}
        .card {{
            background: white;
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }}
        .card h3 {{
            color: var(--mill-green);
            margin-bottom: 15px;
            font-size: 1.1em;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .metric-card {{
            text-align: center;
            padding: 30px;
        }}
        .metric-value {{
            font-size: 2.5em;
            font-weight: 700;
            color: var(--mill-green);
            line-height: 1.2;
        }}
        .metric-label {{
            color: #666;
            font-size: 0.9em;
            margin-top: 5px;
        }}
        .trend-up {{ color: #e74c3c; }}
        .trend-down {{ color: #27ae60; }}
        .trend-stable {{ color: #95a5a6; }}
        .insight-card {{
            border-left: 4px solid var(--mill-accent);
        }}
        .insight-card .importance-high {{ border-left-color: #e74c3c; }}
        .insight-card .importance-medium {{ border-left-color: #f39c12; }}
        .insight-card .recommendation {{
            background: var(--bg-light);
            padding: 12px;
            border-radius: 6px;
            margin-top: 15px;
            font-size: 0.9em;
        }}
        .chart-container {{ height: 300px; position: relative; }}
        .data-quality {{
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 15px;
            background: var(--bg-light);
            border-radius: 8px;
            margin-bottom: 20px;
        }}
        .quality-bar {{
            flex: 1;
            height: 8px;
            background: #ddd;
            border-radius: 4px;
            overflow: hidden;
        }}
        .quality-fill {{
            height: 100%;
            background: linear-gradient(90deg, var(--mill-green), var(--mill-accent));
            width: {self.profile.quality_score * 100}%;
        }}
        .section-title {{
            font-size: 1.3em;
            color: var(--mill-green);
            margin: 30px 0 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid var(--mill-accent);
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #eee;
        }}
        th {{ background: var(--bg-light); font-weight: 600; }}
        .footer {{
            text-align: center;
            padding: 30px;
            color: #888;
            font-size: 0.85em;
        }}
    </style>
</head>
<body>
    <div class="header">
        <div>
            <h1>{self.customer_name} Food Waste Dashboard</h1>
            <div class="meta">Generated by Mill AI Workflow | {datetime.now().strftime('%B %d, %Y')}</div>
        </div>
        <div style="text-align: right;">
            <div style="font-size: 0.9em; opacity: 0.9;">Data Period</div>
            <div style="font-weight: 600;">{self._format_date_range()}</div>
        </div>
    </div>

    <div class="container">
        <div class="data-quality">
            <span>Data Quality:</span>
            <div class="quality-bar"><div class="quality-fill"></div></div>
            <span>{self.profile.quality_score * 100:.0f}%</span>
        </div>

        <h2 class="section-title">Key Metrics</h2>
        <div class="grid">
            {self._generate_metric_cards()}
        </div>

        <h2 class="section-title">Insights & Recommendations</h2>
        <div class="grid">
            {self._generate_insight_cards()}
        </div>

        <h2 class="section-title">Visualizations</h2>
        <div class="grid">
            {self._generate_charts()}
        </div>

        <h2 class="section-title">Data Summary</h2>
        <div class="card">
            {self._generate_data_table()}
        </div>
    </div>

    <div class="footer">
        <p>Powered by Mill | Outsmarting Food Waste Together</p>
        <p style="margin-top: 5px;">This dashboard was automatically generated from your data using Mill's AI workflow system.</p>
    </div>

    {self._generate_chart_scripts()}
</body>
</html>"""

    def _format_date_range(self) -> str:
        """Format the date range for display"""
        if self.profile.date_range[0] and self.profile.date_range[1]:
            start = self.profile.date_range[0].strftime('%b %d, %Y')
            end = self.profile.date_range[1].strftime('%b %d, %Y')
            return f"{start} - {end}"
        return "All Time"

    def _generate_metric_cards(self) -> str:
        """Generate HTML for metric cards"""
        cards = []

        # Total records
        cards.append(f"""
        <div class="card metric-card">
            <div class="metric-value">{self.profile.num_records:,}</div>
            <div class="metric-label">Total Records</div>
        </div>
        """)

        # Weight total if available
        weight_col = self._find_column(['weight', 'pounds', 'kg', 'lbs', 'weight_lbs'])
        if weight_col:
            total = self.df[weight_col].sum()
            cards.append(f"""
            <div class="card metric-card">
                <div class="metric-value">{total:,.0f}</div>
                <div class="metric-label">Total Pounds Wasted</div>
            </div>
            """)

        # Cost total if available
        cost_col = self._find_column(['cost', 'value', 'price', 'amount', 'dollars'])
        if cost_col:
            total = self.df[cost_col].sum()
            cards.append(f"""
            <div class="card metric-card">
                <div class="metric-value">${total:,.0f}</div>
                <div class="metric-label">Total Waste Value</div>
            </div>
            """)

        # Location count if available
        loc_col = self._find_column(['location', 'store', 'site', 'warehouse', 'location_id'])
        if loc_col:
            count = self.df[loc_col].nunique()
            cards.append(f"""
            <div class="card metric-card">
                <div class="metric-value">{count}</div>
                <div class="metric-label">Locations Tracked</div>
            </div>
            """)

        return '\n'.join(cards)

    def _generate_insight_cards(self) -> str:
        """Generate HTML for insight cards"""
        cards = []
        for insight in self.insights[:6]:  # Limit to 6 insights
            trend_class = f"trend-{insight.trend}"
            trend_icon = {"up": "", "down": "", "stable": ""}[insight.trend]

            cards.append(f"""
            <div class="card insight-card">
                <h3>{insight.title}</h3>
                <p>{insight.description}</p>
                <p style="margin-top: 10px;">
                    <strong>{insight.metric}:</strong>
                    <span class="{trend_class}">{insight.value} {trend_icon}</span>
                </p>
                <div class="recommendation">
                    <strong>Recommendation:</strong> {insight.recommendation}
                </div>
            </div>
            """)

        return '\n'.join(cards)

    def _generate_charts(self) -> str:
        """Generate HTML for chart containers"""
        charts = []

        # Category breakdown if available
        cat_col = self._find_column(['category', 'type', 'item_type', 'food_type', 'waste_category'])
        if cat_col:
            charts.append("""
            <div class="card">
                <h3>Waste by Category</h3>
                <div class="chart-container">
                    <canvas id="categoryChart"></canvas>
                </div>
            </div>
            """)

        # Location comparison if available
        loc_col = self._find_column(['location', 'store', 'site', 'warehouse', 'location_id'])
        if loc_col:
            charts.append("""
            <div class="card">
                <h3>Waste by Location</h3>
                <div class="chart-container">
                    <canvas id="locationChart"></canvas>
                </div>
            </div>
            """)

        # Time series if available
        if self.profile.date_range[0]:
            charts.append("""
            <div class="card">
                <h3>Waste Over Time</h3>
                <div class="chart-container">
                    <canvas id="timeChart"></canvas>
                </div>
            </div>
            """)

        return '\n'.join(charts) if charts else '<div class="card"><p>No charts available for this data format.</p></div>'

    def _generate_chart_scripts(self) -> str:
        """Generate JavaScript for Chart.js charts"""
        scripts = ['<script>']

        cat_col = self._find_column(['category', 'type', 'item_type', 'food_type', 'waste_category'])
        weight_col = self._find_column(['weight', 'pounds', 'kg', 'lbs', 'weight_lbs'])
        loc_col = self._find_column(['location', 'store', 'site', 'warehouse', 'location_id'])

        # Category chart
        if cat_col and weight_col:
            cat_data = self.df.groupby(cat_col)[weight_col].sum().sort_values(ascending=False).head(10)
            labels = [str(l) for l in cat_data.index.tolist()]
            values = cat_data.values.tolist()

            scripts.append(f"""
            new Chart(document.getElementById('categoryChart'), {{
                type: 'doughnut',
                data: {{
                    labels: {json.dumps(labels)},
                    datasets: [{{
                        data: {json.dumps(values)},
                        backgroundColor: [
                            '#1a472a', '#2d5a3d', '#4a7c59', '#6b9b7a', '#8cba9b',
                            '#acd9bc', '#cce8d4', '#e5f4eb', '#f0f9f4', '#f8fcfa'
                        ]
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{ legend: {{ position: 'right' }} }}
                }}
            }});
            """)

        # Location chart
        if loc_col and weight_col:
            loc_data = self.df.groupby(loc_col)[weight_col].sum().sort_values(ascending=False).head(10)
            labels = [str(l) for l in loc_data.index.tolist()]
            values = loc_data.values.tolist()

            scripts.append(f"""
            new Chart(document.getElementById('locationChart'), {{
                type: 'bar',
                data: {{
                    labels: {json.dumps(labels)},
                    datasets: [{{
                        label: 'Waste (lbs)',
                        data: {json.dumps(values)},
                        backgroundColor: '#1a472a'
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{ legend: {{ display: false }} }},
                    scales: {{ y: {{ beginAtZero: true }} }}
                }}
            }});
            """)

        # Time series chart
        date_col = self._find_date_column()
        if date_col and weight_col:
            time_data = self.df.set_index(date_col).resample('D')[weight_col].sum().fillna(0)
            labels = [d.strftime('%Y-%m-%d') for d in time_data.index.tolist()]
            values = time_data.values.tolist()

            scripts.append(f"""
            new Chart(document.getElementById('timeChart'), {{
                type: 'line',
                data: {{
                    labels: {json.dumps(labels)},
                    datasets: [{{
                        label: 'Daily Waste (lbs)',
                        data: {json.dumps(values)},
                        borderColor: '#1a472a',
                        backgroundColor: 'rgba(26, 71, 42, 0.1)',
                        fill: true,
                        tension: 0.3
                    }}]
                }},
                options: {{
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {{ legend: {{ display: false }} }},
                    scales: {{ y: {{ beginAtZero: true }} }}
                }}
            }});
            """)

        scripts.append('</script>')
        return '\n'.join(scripts)

    def _generate_data_table(self) -> str:
        """Generate HTML table with data summary"""
        # Get summary by category or location
        cat_col = self._find_column(['category', 'type', 'item_type', 'food_type', 'waste_category'])
        weight_col = self._find_column(['weight', 'pounds', 'kg', 'lbs', 'weight_lbs'])
        cost_col = self._find_column(['cost', 'value', 'price', 'amount', 'dollars'])

        if cat_col and (weight_col or cost_col):
            agg_cols = {}
            if weight_col:
                agg_cols[weight_col] = 'sum'
            if cost_col:
                agg_cols[cost_col] = 'sum'

            summary = self.df.groupby(cat_col).agg(agg_cols).sort_values(
                weight_col if weight_col else cost_col, ascending=False
            ).head(15)

            rows = []
            for idx, row in summary.iterrows():
                cols = [f"<td>{idx}</td>"]
                if weight_col:
                    cols.append(f"<td>{row[weight_col]:,.0f} lbs</td>")
                if cost_col:
                    cols.append(f"<td>${row[cost_col]:,.0f}</td>")
                rows.append(f"<tr>{''.join(cols)}</tr>")

            headers = ["<th>Category</th>"]
            if weight_col:
                headers.append("<th>Total Weight</th>")
            if cost_col:
                headers.append("<th>Total Cost</th>")

            return f"""
            <table>
                <thead><tr>{''.join(headers)}</tr></thead>
                <tbody>{''.join(rows)}</tbody>
            </table>
            """

        return "<p>Data table not available for this format.</p>"

    def _find_column(self, candidates: List[str]) -> Optional[str]:
        """Find first matching column"""
        for col in self.df.columns:
            if any(c in col.lower() for c in candidates):
                return col
        return None

    def _find_date_column(self) -> Optional[str]:
        """Find datetime column"""
        for col in self.df.columns:
            if self.df[col].dtype == 'datetime64[ns]':
                return col
        return None


def generate_sample_data() -> pd.DataFrame:
    """Generate realistic sample food waste data"""
    np.random.seed(42)

    # Date range: last 30 days
    dates = pd.date_range(end=datetime.now(), periods=30, freq='D')

    # Locations
    locations = ['Store #101', 'Store #205', 'Store #312', 'Store #427', 'Store #533']

    # Categories with realistic distributions
    categories = {
        'Produce': 0.30,
        'Bakery': 0.20,
        'Deli/Prepared': 0.18,
        'Dairy': 0.12,
        'Meat/Seafood': 0.10,
        'Frozen': 0.05,
        'Other': 0.05
    }

    records = []
    for date in dates:
        for location in locations:
            # Each location generates 5-15 waste records per day
            n_records = random.randint(5, 15)
            for _ in range(n_records):
                category = random.choices(
                    list(categories.keys()),
                    weights=list(categories.values())
                )[0]

                # Weight varies by category
                base_weight = {
                    'Produce': 25, 'Bakery': 15, 'Deli/Prepared': 20,
                    'Dairy': 10, 'Meat/Seafood': 12, 'Frozen': 8, 'Other': 5
                }[category]
                weight = max(1, np.random.normal(base_weight, base_weight * 0.3))

                # Cost roughly $2-5 per pound depending on category
                cost_per_lb = random.uniform(2, 5)
                cost = weight * cost_per_lb

                # Location variance - Store #427 is best, #312 is worst
                location_multiplier = {
                    'Store #101': 1.0, 'Store #205': 0.9, 'Store #312': 1.4,
                    'Store #427': 0.6, 'Store #533': 1.1
                }[location]
                weight *= location_multiplier
                cost *= location_multiplier

                records.append({
                    'date': date,
                    'location': location,
                    'category': category,
                    'weight_lbs': round(weight, 1),
                    'cost_dollars': round(cost, 2)
                })

    return pd.DataFrame(records)


def main():
    parser = argparse.ArgumentParser(description="Mill Customer Data Dashboard Workflow")
    parser.add_argument('--input', '-i', help='Input data file (csv, json, xlsx, parquet)')
    parser.add_argument('--output', '-o', default='dashboard.html', help='Output HTML file')
    parser.add_argument('--customer', '-c', default='Sample Customer', help='Customer name for dashboard')
    parser.add_argument('--demo', action='store_true', help='Run with demo data')
    args = parser.parse_args()

    print("Mill Customer Data Dashboard Workflow")
    print("=" * 40)

    # Get data
    if args.demo or not args.input:
        print("\nGenerating sample data...")
        df = generate_sample_data()
        customer_name = "Demo Grocery Chain"
    else:
        print(f"\nLoading data from {args.input}...")
        ingestor = DataIngestor(args.input)
        df = ingestor.ingest()
        customer_name = args.customer

    # Ingest and profile
    print("Profiling data...")
    ingestor = DataIngestor()
    df = ingestor.ingest_dataframe(df)
    profile = ingestor.profile

    print(f"  - Records: {profile.num_records:,}")
    print(f"  - Columns: {', '.join(profile.columns)}")
    print(f"  - Data type: {profile.data_type.value}")
    print(f"  - Quality score: {profile.quality_score:.0%}")

    # Generate insights
    print("\nGenerating insights...")
    generator = InsightGenerator(df, profile)
    insights = generator.generate_all_insights()
    print(f"  - Generated {len(insights)} insights")

    # Generate dashboard
    print("\nGenerating dashboard...")
    dashboard = DashboardGenerator(df, profile, insights, customer_name)
    html = dashboard.generate()

    # Write output
    output_path = Path(args.output)
    output_path.write_text(html)
    print(f"\nDashboard saved to: {output_path.absolute()}")

    # Also save insights as JSON
    insights_path = output_path.with_suffix('.insights.json')
    insights_data = [asdict(i) for i in insights]
    insights_path.write_text(json.dumps(insights_data, indent=2, default=str))
    print(f"Insights saved to: {insights_path}")

    print("\nDone!")


if __name__ == "__main__":
    main()
