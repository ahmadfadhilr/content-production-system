# Content Ideation System

This system implements a data-driven workflow for identifying, ranking, and managing content ideas for a personal brand content production system.

## Overview

The system follows a 10-stage content production pipeline, starting with Stage 1 (Ideation) which uses market research and gap analysis to identify the most valuable content ideas for production.

## Key Features

### 1. Database Schema

The database stores content ideas with the following structure:

- **id**: Unique identifier for each idea
- **title**: Content idea title
- **pillar**: Content pillar (business_model_finance, revenue_growth, operations_leadership)
- **concept_type**: Type of concept (decision_note, operating_playbook)
- **audience_problem**: Problem statement for target audience
- **target_search_volume**: YouTube search volume for demand validation
- **gap_classification**: Gap analysis (empty, shallow, deep)
- **evidence_type**: Evidence quality (primary_data, secondary_research, tertiary)
- **reference_sources**: Source references
- **estimated_days_to_produce**: Production time estimate
- **created_date**: Record creation date
- **reason**: Additional context
- **p_score**: Search volume score (0-5)
- **g_score**: Gap score (1-5)
- **b_score**: Evidence score (1-5)
- **k_score**: Capacity score (0-5)
- **total_score**: Total calculated score (0-30)
- **status**: Current status (ready, improve, wait, gapped, merged)

### 2. Scoring System

**Total Score Formula:** `(p_score × 2) + (g_score × 2) + b_score + k_score`

| Criterion | Score 5 | Score 3 | Score 1 |
|-----------|---------|---------|---------|
| **Search Volume (p)** | ≥ 100,000 | 10,000-99,999 | < 10,000 |
| **Gap (g)** | Empty (no local content) | Shallow (limited scope) | Deep (saturated market) |
| **Evidence (b)** | Primary data (own data) | Secondary research (journals, reports) | Tertiary (opinions) |
| **Capacity (k)** | ≤ 2 days | 4 days | 7+ days |

### 3. Idea Status

| Status | Criteria |
|--------|----------|
| **ready** | Score ≥18 AND evidence ≥ secondary_research |
| **improve** | Score 16-17 OR needs improvement in one criterion |
| **wait** | Score ≥18 but evidence = tertiary OR score <16 |
| **gapped** | Gap = deep (market saturated) |
| **merged** | Duplicate of existing idea |

## System Components

### 1. `init_database.py`
Initializes the SQLite database with tables and reference data.

**Usage:**
```bash
python3 init_database.py
```

### 2. `content_ideas_manager.py`
Core manager class for database operations:
- Add, retrieve, update, and delete ideas
- Calculate scores using the ranking system
- Determine idea status

### 3. `run_ideation.py`
Runs the content ideation workflow:
- Generates sample ideas based on the 01-ideasi.md methodology
- Adds ideas to the database
- Displays ranking and statistics

**Usage:**
```bash
python3 run_ideation.py
```

### 4. `ranking.py`
Command-line interface for:
- Viewing idea rankings
- Filtering by status
- Displaying detailed information
- Showing statistics and analytics

**Usage:**
```bash
# View all ideas
python3 ranking.py

# View only ready ideas
python3 ranking.py --ready-only

# View detailed information
python3 ranking.py --detail
```

## Workflow Integration

### Stage 1: Ideation (01-ideasi.md)

The ideation workflow follows these steps:

1. **Keyword Research (Step 1)**: Generate 15 keyword queries across three pillars
2. **Demand Measurement (Step 2)**: Measure search demand using YouTube data
3. **Supply Analysis (Step 3)**: Analyze content gaps and saturation
4. **Gap Filtering (Step 3b)**: Filter out ideas with deep gaps or insufficient demand
5. **Concept Formulation (Step 4)**: Develop specific concepts with target audiences
6. **Evidence Determination (Step 5)**: Identify and classify evidence sources
7. **Scoring and Ranking (Step 6)**: Calculate scores and rank ideas

### Database Operations

The system integrates with the 10-stage content production pipeline:

1. **Idea Storage**: All content ideas are stored in the database with full metadata
2. **Score Tracking**: Continuous scoring and status updates throughout the pipeline
3. **Filtering**: Ideas are filtered based on readiness criteria
4. **Retrieval**: Easy access to ideas for packaging and production stages

## Usage Examples

### 1. Initialize Database
```bash
python3 init_database.py
```

### 2. Generate and Add Ideas
```bash
python3 run_ideation.py
```

### 3. View Rankings
```bash
python3 ranking.py
```

### 4. View Ready Ideas
```bash
python3 ranking.py --ready-only
```

### 5. View Detailed Information
```bash
python3 ranking.py --detail
```

## Best Practices

### 1. Database Management
- Always use the `ContentIdeasManager` class for database operations
- Never manually modify database tables
- Use parameterized queries to prevent SQL injection

### 2. Idea Management
- Calculate scores automatically using the scoring system
- Regularly review and update idea statuses
- Maintain reference data (gap analysis, evidence sources)

### 3. Workflow Integration
- Use the ranking script to select ideas for production
- Update ideas with real-world performance data as they are produced
- Archive completed ideas when appropriate

## File Structure

```
content-production-system/
├── scripts/
│   ├── init_database.py          # Database initialization
│   ├── content_ideas_manager.py   # Core database operations
│   ├── run_ideation.py          # Content ideation workflow
│   └── ranking.py              # Ranking and filtering
├── database/
│   └── database.db              # SQLite database
└── database/
    └── README.md               # Database documentation
```

## Priority Concepts for Entrepreneurs

Based on the scoring system and market analysis, the top priority concepts include:

1. **Value Proposition Clarity** - Clear understanding of what you sell and why
2. **Customer Acquisition Channels** - Effective ways to reach customers
3. **Unit Economics** - Understanding profit per unit
4. **Pricing Strategy** - Setting the right price
5. **Cash Flow Management** - Ensuring enough liquidity
6. **Team Management** - Hiring and managing people effectively
7. **Operational Scalability** - Systems to grow without losing quality
8. **Risk Assessment** - Identifying and managing business risks

## Conclusion

This database system provides a robust foundation for managing and ranking content ideas through the entire content production pipeline. It ensures consistent evaluation, tracks performance over time, and integrates seamlessly with the 10-stage workflow described in the project documentation.

The scoring system, combined with market research and gap analysis, helps identify the most valuable content ideas that will resonate with both beginner and advanced entrepreneurs, supporting the goal of creating high-quality, impactful content for the personal brand.