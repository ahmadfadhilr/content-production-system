# Content Ideation System - Quick Start Guide

This system implements a data-driven workflow for identifying, ranking, and managing content ideas for a personal brand content production system.

## Getting Started

### 1. Initialize the Database
```bash
python3 scripts/init_database.py
```

This will:
- Create the SQLite database file (`database.db`)
- Set up all necessary tables
- Populate reference data (gap analysis, evidence sources)

### 2. Run the Ideation Workflow
```bash
python3 scripts/run_ideation.py
```

This will:
- Generate sample content ideas based on the 01-ideasi.md methodology
- Add ideas to the database
- Display rankings and statistics

### 3. View Rankings
```bash
python3 scripts/ranking.py
```

View all content ideas sorted by their total score:

```
# | Title                                              | Pillar | Score | Status
#1 | Margin per Lini Layanan di Bisnis Jasa       | 1      | 28    | Siap
#2 | Harga Jual Layanan Jasa untuk Bisnis yang Waktu Orang-nya Terbatas | 1      | 24    | Siap
#3 | Kenaikan Harga dan Siapa yang Benar-Benar Pergi | 1      | 20    | Perbaiki
...
```

### 4. View Ready Ideas Only
```bash
python3 scripts/ranking.py --ready-only
```

Shows only ideas that are ready for production (score ≥18 with sufficient evidence).

### 5. View Detailed Information
```bash
python3 scripts/ranking.py --detail
```

Shows detailed information about each content idea including:
- Full title and description
- Scores for each criterion (search volume, gap, evidence, capacity)
- Status and any additional context

## Database Schema

The database stores content ideas with the following key fields:

| Field | Description |
|-------|-------------|
| `id` | Unique identifier |
| `title` | Content idea title |
| `pillar` | Content pillar (business_model_finance, revenue_growth, operations_leadership) |
| `concept_type` | Concept type (decision_note, operating_playbook) |
| `audience_problem` | Problem statement for target audience |
| `target_search_volume` | YouTube search volume for demand validation |
| `gap_classification` | Gap analysis (empty, shallow, deep) |
| `evidence_type` | Evidence quality (primary_data, secondary_research, tertiary) |
| `estimated_days_to_produce` | Production time estimate |
| `p_score`, `g_score`, `b_score`, `k_score` | Individual scores |
| `total_score` | Total calculated score (0-30) |
| `status` | Current status (ready, improve, wait, gapped, merged) |

## Scoring System

### Formula
**Total Score = (p_score × 2) + (g_score × 2) + b_score + k_score**

### Score Ranges

| Criterion | Score 5 | Score 3 | Score 1 |
|-----------|---------|---------|---------|
| **Search Volume** | ≥ 100,000 | 10,000-99,999 | < 10,000 |
| **Gap** | Empty | Shallow | Deep |
| **Evidence** | Primary data | Secondary research | Tertiary |
| **Capacity** | ≤ 2 days | 4 days | 7+ days |

### Status Definitions

| Status | Criteria |
|--------|----------|
| **ready** | Score ≥18 AND evidence ≥ secondary_research |
| **improve** | Score 16-17 OR needs improvement |
| **wait** | Score ≥18 but evidence = tertiary OR score <16 |
| **gapped** | Gap = deep (market saturated) |
| **merged** | Duplicate of existing idea |

## Example Output

### Basic Ranking
```
Content Ideas Ranking:

# | Title                                              | Pillar | Score | Status
--------------------------------------------------------
#1 | Margin per Lini Layanan di Bisnis Jasa       | 1      | 28    | Siap
#2 | Harga Jual Layanan Jasa untuk Bisnis yang Waktu Orang-nya Terbatas | 1      | 24    | Siap
#3 | Kenaikan Harga dan Siapa yang Benar-Benar Pergi | 1      | 20    | Perbaiki
...

Total ideas in database: 5
Ideas ready for production: 2
```

### Ready Ideas Only
```
Content Ideas Ranking:

# | Title                                              | Pillar | Score | Status
--------------------------------------------------------
#1 | Margin per Lini Layanan di Bisnis Jasa       | 1      | 28    | Siap
#2 | Harga Jual Layanan Jasa untuk Bisnis yang Waktu Orang-nya Terbatas | 1      | 24    | Siap

Ready to produce (2):
  • Margin per Lini Layanan di Bisnis Jasa
  • Harga Jual Layanan Jasa untuk Bisnis yang Waktu Orang-nya Terbatas
```

## Priority Concepts for Entrepreneurs

Based on the scoring system, the system identifies these priority concepts:

1. **Value Proposition Clarity** - Clear understanding of what you sell and why
2. **Customer Acquisition Channels** - Effective ways to reach customers
3. **Unit Economics** - Understanding profit per unit
4. **Pricing Strategy** - Setting the right price
5. **Cash Flow Management** - Ensuring enough liquidity
6. **Team Management** - Hiring and managing people effectively
7. **Operational Scalability** - Systems to grow without losing quality
8. **Risk Assessment** - Identifying and managing business risks

These concepts are ranked by their importance to entrepreneurs and their potential impact on business success.

## Troubleshooting

### Database Not Initialized
```bash
# Reinitialize the database
python3 scripts/init_database.py

# Then run the ideation workflow
python3 scripts/run_ideation.py
```

### No Ideas in Database
```bash
# Run the ideation workflow to populate the database
python3 scripts/run_ideation.py
```

### Ranking Script Errors
```bash
# Ensure the database exists
python3 scripts/init_database.py

# Then run ranking
python3 scripts/ranking.py
```

## Next Steps

1. **Initialize the database** using `init_database.py`
2. **Run the ideation workflow** using `run_ideation.py`
3. **View rankings** using `ranking.py`
4. **Analyze results** and select ideas for production
5. **Update ideas** with real-world performance data as they are produced

This system provides a complete foundation for managing content ideas through the entire production pipeline, from ideation to evaluation and optimization.