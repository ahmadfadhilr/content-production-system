# Database Schema for Content Ideation System

This database tracks and ranks content ideas for Fadhil's personal brand content system.
It supports the 10-stage content production pipeline described in the project.

## Database Files

- `database/schema.sql` - SQL schema definition
- `scripts/content_ideas.py` - Python utilities for database operations
- `scripts/ranking.py` - Ranking and filtering logic
- `README.md` - Database documentation

## 1. Schema Definition (`database/schema.sql`)

```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Main content ideas table
CREATE TABLE content_ideas (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title TEXT NOT NULL,
    pillar ENUM('business_model_finance', 'revenue_growth', 'operations_leadership') NOT NULL,
    concept_type ENUM('decision_note', 'operating_playbook') NOT NULL,
    audience_problem TEXT NOT NULL,
    target_search_volume INTEGER,
    gap_classification ENUM('empty', 'shallow', 'deep') NOT NULL,
    evidence_type ENUM('primary_data', 'secondary_research', 'tertiary') NOT NULL,
    reference_sources TEXT,
    estimated_days_to_produce INTEGER,
    created_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status ENUM('ready', 'improve', 'wait', 'gapped', 'merged') NOT NULL,
    reason TEXT,
    
    -- Calculated fields
    p_score INTEGER,  -- Raw search volume score
    g_score INTEGER,  -- Raw gap score
    b_score INTEGER,  -- Raw evidence score
    k_score INTEGER,  -- Raw capacity score
    total_score INTEGER GENERATED ALWAYS AS (
        (p_score * 2) + (g_score * 2) + b_score + k_score
    ) STORED
);

-- Supporting tables
CREATE TABLE gap_analysis (
    level VARCHAR(20) PRIMARY KEY,
    score_value INTEGER NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE evidence_sources (
    source_id VARCHAR(20) PRIMARY KEY,
    source_type ENUM('primary', 'secondary', 'tertiary') NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE ranking_criteria (
    criterion VARCHAR(20) PRIMARY KEY,
    weight INTEGER NOT NULL,
    description TEXT NOT NULL
);

-- Indexes for performance
CREATE INDEX idx_content_ideas_status ON content_ideas(status);
CREATE INDEX idx_content_ideas_pillar ON content_ideas(pillar);
CREATE INDEX idx_content_ideas_total_score ON content_ideas(total_score DESC);
CREATE INDEX idx_content_ideas_created_date ON content_ideas(created_date);

-- Insert initial gap analysis data
INSERT INTO gap_analysis (level, score_value, description) VALUES
('empty', 5, 'No local video content covers this angle'),
('shallow', 3, 'Exists but limited duration or lacks numerical analysis'),
('deep', 1, 'Well-covered with comprehensive analysis');

-- Insert initial evidence sources
INSERT INTO evidence_sources (source_id, source_type, description) VALUES
('Cugini2017', 'secondary', 'Academic research on customer profitability'),
('Lueg2024', 'secondary', 'Value-based pricing implementation study'),
('Dawes2009', 'secondary', 'Price elasticity in service businesses'),
('Ascarza2016', 'secondary', 'Churn prevention effectiveness study'),
('TheCPJ2018', 'secondary', 'Professional services margin benchmarks');

-- Insert ranking criteria
INSERT INTO ranking_criteria (criterion, weight, description) VALUES
('search_volume', 2, 'Market demand based on YouTube search volume'),
('gap', 2, 'Market opportunity based on content gap analysis'),
('evidence', 1, 'Quality and type of evidence supporting the concept'),
('capacity', 1, 'Estimated production effort and resources required');
```

## 2. Python Utilities (`scripts/content_ideas.py`)

```python
#!/usr/bin/env python3
"""
Database utilities for the content ideation system.
Provides functions to manage content ideas, ranking, and filtering.
"""

import os
import sys
import uuid
from datetime import datetime
from typing import List, Dict, Optional, Tuple
import json

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class ContentIdea:
    """Represents a content idea with all its metadata and calculations."""
    
    def __init__(self, title: str, pillar: str, concept_type: str, 
                 audience_problem: str, target_search_volume: int = 0,
                 gap_classification: str = 'shallow',
                 evidence_type: str = 'secondary_research',
                 reference_sources: str = '', estimated_days_to_produce: int = 2,
                 reason: str = ''):
        self.id = str(uuid.uuid4())
        self.title = title
        self.pillar = pillar
        self.concept_type = concept_type
        self.audience_problem = audience_problem
        self.target_search_volume = target_search_volume
        self.gap_classification = gap_classification
        self.evidence_type = evidence_type
        self.reference_sources = reference_sources
        self.estimated_days_to_produce = estimated_days_to_produce
        self.reason = reason
        self.created_date = datetime.now()
        
        # Calculate scores
        self.p_score = self._calculate_p_score(target_search_volume)
        self.g_score = self._calculate_g_score(gap_classification)
        self.b_score = self._calculate_b_score(evidence_type)
        self.k_score = self._calculate_k_score(estimated_days_to_produce)
        self.total_score = (self.p_score * 2) + (self.g_score * 2) + self.b_score + self.k_score
        
        self.status = self._determine_status()
    
    def _calculate_p_score(self, search_volume: int) -> int:
        """Calculate search volume score (0-5)."""
        if search_volume >= 100000:
            return 5
        elif search_volume >= 10000:
            return 3
        elif search_volume >= 1000:
            return 1
        return 0
    
    def _calculate_g_score(self, gap: str) -> int:
        """Calculate gap score (1-5)."""
        scores = {
            'empty': 5,
            'shallow': 3,
            'deep': 1
        }
        return scores.get(gap, 3)
    
    def _calculate_b_score(self, evidence: str) -> int:
        """Calculate evidence score (1-5)."""
        scores = {
            'primary_data': 5,
            'secondary_research': 3,
            'tertiary': 1
        }
        return scores.get(evidence, 1)
    
    def _calculate_k_score(self, days: int) -> int:
        """Calculate capacity score (1-5)."""
        if days <= 2:
            return 5
        elif days <= 4:
            return 3
        elif days <= 7:
            return 1
        return 0
    
    def _determine_status(self) -> str:
        """Determine idea status based on scores and evidence."""
        if self.total_score >= 18 and self.evidence_type in ['primary_data', 'secondary_research']:
            return 'ready'
        elif self.total_score >= 18:
            return 'wait'
        elif self.gap_classification == 'deep':
            return 'gapped'
        elif self.total_score >= 16:
            return 'improve'
        else:
            return 'wait'
    
    def to_dict(self) -> Dict:
        """Convert idea to dictionary for storage."""
        return {
            'id': self.id,
            'title': self.title,
            'pillar': self.pillar,
            'concept_type': self.concept_type,
            'audience_problem': self.audience_problem,
            'target_search_volume': self.target_search_volume,
            'gap_classification': self.gap_classification,
            'evidence_type': self.evidence_type,
            'reference_sources': self.reference_sources,
            'estimated_days_to_produce': self.estimated_days_to_produce,
            'created_date': self.created_date.isoformat(),
            'reason': self.reason,
            'p_score': self.p_score,
            'g_score': self.g_score,
            'b_score': self.b_score,
            'k_score': self.k_score,
            'total_score': self.total_score,
            'status': self.status
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'ContentIdea':
        """Create idea from dictionary."""
        idea = cls(
            title=data['title'],
            pillar=data['pillar'],
            concept_type=data['concept_type'],
            audience_problem=data['audience_problem'],
            target_search_volume=data.get('target_search_volume', 0),
            gap_classification=data.get('gap_classification', 'shallow'),
            evidence_type=data.get('evidence_type', 'secondary_research'),
            reference_sources=data.get('reference_sources', ''),
            estimated_days_to_produce=data.get('estimated_days_to_produce', 2),
            reason=data.get('reason', '')
        )
        # Override calculated fields if present in data
        for field in ['id', 'created_date', 'p_score', 'g_score', 'b_score', 
                     'k_score', 'total_score', 'status']:
            if field in data and hasattr(idea, field):
                setattr(idea, field, data[field])
        return idea
class ContentIdeasManager:
    """Manages content ideas and their lifecycle."""
    
    def __init__(self, db_path: str = 'database/content_ideas.db'):
        self.db_path = db_path
        self._ensure_directory()
        self._initialize_database()
    
    def _ensure_directory(self):
        """Ensure database directory exists."""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
    
    def _initialize_database(self):
        """Initialize database with tables if they don't exist."""
        import sqlite3
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create tables
        cursor.executescript('''
            CREATE TABLE IF NOT EXISTS content_ideas (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                pillar TEXT NOT NULL,
                concept_type TEXT NOT NULL,
                audience_problem TEXT NOT NULL,
                target_search_volume INTEGER,
                gap_classification TEXT NOT NULL,
                evidence_type TEXT NOT NULL,
                reference_sources TEXT,
                estimated_days_to_produce INTEGER,
                created_date TEXT NOT NULL,
                reason TEXT,
                p_score INTEGER,
                g_score INTEGER,
                b_score INTEGER,
                k_score INTEGER,
                total_score INTEGER,
                status TEXT NOT NULL
            );
            
            CREATE INDEX IF NOT EXISTS idx_status ON content_ideas(status);
            CREATE INDEX IF NOT EXISTS idx_pillar ON content_ideas(pillar);
            CREATE INDEX IF NOT EXISTS idx_total_score ON content_ideas(total_score DESC);
        ''')
        
        conn.commit()
        conn.close()
    
    def add_idea(self, idea: ContentIdea) -> str:
        """Add a new content idea to the database."""
        import sqlite3
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        idea_dict = idea.to_dict()
        
        cursor.execute('''
            INSERT INTO content_ideas (
                id, title, pillar, concept_type, audience_problem,
                target_search_volume, gap_classification, evidence_type,
                reference_sources, estimated_days_to_produce, created_date,
                reason, p_score, g_score, b_score, k_score, total_score, status
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            idea_dict['id'], idea_dict['title'], idea_dict['pillar'],
            idea_dict['concept_type'], idea_dict['audience_problem'],
            idea_dict['target_search_volume'], idea_dict['gap_classification'],
            idea_dict['evidence_type'], idea_dict['reference_sources'],
            idea_dict['estimated_days_to_produce'], idea_dict['created_date'],
            idea_dict['reason'], idea_dict['p_score'], idea_dict['g_score'],
            idea_dict['b_score'], idea_dict['k_score'], idea_dict['total_score'],
            idea_dict['status']
        ))
        
        conn.commit()
        conn.close()
        return idea.id
    
    def get_idea(self, idea_id: str) -> Optional[ContentIdea]:
        """Get a content idea by ID."""
        import sqlite3
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM content_ideas WHERE id = ?', (idea_id,))
        row = cursor.fetchone()
        
        conn.close()
        
        if row is None:
            return None
        
        columns = [desc[0] for desc in cursor.description]
        idea_dict = dict(zip(columns, row))
        return ContentIdea.from_dict(idea_dict)
    
    def get_all_ideas(self, status_filter: Optional[str] = None) -> List[ContentIdea]:
        """Get all content ideas, optionally filtered by status."""
        import sqlite3
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        if status_filter:
            cursor.execute('SELECT * FROM content_ideas WHERE status = ? ORDER BY total_score DESC', 
                         (status_filter,))
        else:
            cursor.execute('SELECT * FROM content_ideas ORDER BY total_score DESC')
        
        ideas = []
        for row in cursor.fetchall():
            columns = [desc[0] for desc in cursor.description]
            idea_dict = dict(zip(columns, row))
            ideas.append(ContentIdea.from_dict(idea_dict))
        
        conn.close()
        return ideas
    
    def update_idea(self, idea_id: str, updates: Dict) -> bool:
        """Update an existing content idea."""
        import sqlite3
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Recalculate scores if needed
        if 'target_search_volume' in updates or 'gap_classification' in updates or \
           'evidence_type' in updates or 'estimated_days_to_produce' in updates:
            
            current_idea = self.get_idea(idea_id)
            if current_idea:
                if 'target_search_volume' in updates:
                    current_idea.target_search_volume = updates['target_search_volume']
                if 'gap_classification' in updates:
                    current_idea.gap_classification = updates['gap_classification']
                if 'evidence_type' in updates:
                    current_idea.evidence_type = updates['evidence_type']
                if 'estimated_days_to_produce' in updates:
                    current_idea.estimated_days_to_produce = updates['estimated_days_to_produce']
                
                current_idea.p_score = current_idea._calculate_p_score(current_idea.target_search_volume)
                current_idea.g_score = current_idea._calculate_g_score(current_idea.gap_classification)
                current_idea.b_score = current_idea._calculate_b_score(current_idea.evidence_type)
                current_idea.k_score = current_idea._calculate_k_score(current_idea.estimated_days_to_produce)
                current_idea.total_score = (current_idea.p_score * 2) + (current_idea.g_score * 2) + \
                                           current_idea.b_score + current_idea.k_score
                current_idea.status = current_idea._determine_status()
        
        # Update other fields
        set_clause = ', '.join([f'{k} = ?' for k in updates.keys()])
        values = list(updates.values())
        
        cursor.execute(f'UPDATE content_ideas SET {set_clause} WHERE id = ?', values + [idea_id])
        
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    
    def delete_idea(self, idea_id: str) -> bool:
        """Delete a content idea."""
        import sqlite3
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM content_ideas WHERE id = ?', (idea_id,))
        
        conn.commit()
        conn.close()
        return cursor.rowcount > 0
    
    def get_statistics(self) -> Dict:
        """Get database statistics."""
        import sqlite3
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        stats = {}
        
        # Total ideas
        cursor.execute('SELECT COUNT(*) FROM content_ideas')
        stats['total_ideas'] = cursor.fetchone()[occupied]
        
        # Ideas by status
        cursor.execute('SELECT status, COUNT(*) FROM content_ideas GROUP BY status')
        stats['ideas_by_status'] = {
            row[0]: row[1] for row in cursor.fetchall()
        }
        
        # Ideas by pillar
        cursor.execute('SELECT pillar, COUNT(*) FROM content_ideas GROUP BY pillar')
        stats['ideas_by_pillar'] = {
            row[0]: row[1] for row in cursor.fetchall()
        }
        
        # Average scores
        cursor.execute('SELECT 
            AVG(p_score), AVG(g_score), AVG(b_score), AVG(k_score), AVG(total_score)
            FROM content_ideas')
        avg_scores = cursor.fetchone()
        stats['average_scores'] = {
            'p_score': avg_scores[0],
            'g_score': avg_scores[1],
            'b_score': avg_scores[2],
            'k_score': avg_scores[3],
            'total_score': avg_scores[4]
        }
        
        conn.close()
        return stats
```

## 3. Ranking Script (`scripts/ranking.py`)

```python
#!/usr/bin/env python3
"""
Content idea ranking and filtering script.
Provides various views and analytics for content ideas.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from scripts.content_ideas import ContentIdeasManager, ContentIdea

def print_ranking(ideas: List[ContentIdea], title: str = "Ranking"):
    """Print ranking of content ideas."""
    print(f"\n{title}")
    print("=" * 80)
    print(f"{'#':>3} | {'Title':<50} | {'Pillar':>10} | {'Score':>6} | {'Status':>10}")
    print("-" * 80)
    
    for i, idea in enumerate(ideas, 1):
        print(f"{i:>3} | {idea.title[:47]:<50} | {idea.pillar:>10} | "
              f"{idea.total_score:>6} | {idea.status:>10}")
    
    print()
    
    # Ready ideas
    ready_ideas = [idea for idea in ideas if idea.status == 'ready']
    if ready_ideas:
        print(f"Ready to produce ({len(ready_ideas)}):")
        for idea in ready_ideas[:5]:  # Show top 5
            print(f"  • {idea.title}")
    
    print()

def print_idea_details(idea: ContentIdea):
    """Print detailed information about a content idea."""
    print(f"\nContent Idea Details")
    print("=" * 80)
    print(f"ID: {idea.id}")
    print(f"Title: {idea.title}")
    print(f"Pillar: {idea.pillar}")
    print(f"Concept Type: {idea.concept_type}")
    print(f"\nAudience Problem:")
    print(f"  {idea.audience_problem}")
    print(f"\nMetrics:")
    print(f"  Search Volume: {idea.target_search_volume:,} (score: {idea.p_score}/5)")
    print(f"  Gap Classification: {idea.gap_classification} (score: {idea.g_score}/5)")
    print(f"  Evidence Type: {idea.evidence_type} (score: {idea.b_score}/5)")
    print(f"  Estimated Production Time: {idea.estimated_days_to_produce} days (score: {idea.k_score}/5)")
    print(f"  Total Score: {idea.total_score}/30")
    print(f"\nStatus: {idea.status}")
    if idea.reason:
        print(f"\nReason: {idea.reason}")
    if idea.reference_sources:
        print(f"\nReference Sources: {idea.reference_sources}")
    
    print()

def main():
    """Main script entry point."""
    manager = ContentIdeasManager()
    
    # Parse command line arguments
    show_all = "--all" in sys.argv
    show_detail = "--detail" in sys.argv
    show_ready_only = "--ready-only" in sys.argv
    
    # Get ideas based on filters
    if show_ready_only:
        ideas = [idea for idea in manager.get_all_ideas() if idea.status == 'ready']
        title = "Ready to Produce (Score ≥18, Evidence ≥ Secondary)"
    elif show_all:
        ideas = manager.get_all_ideas()
        title = "All Content Ideas"
    else:
        ideas = manager.get_all_ideas()
        title = "Content Ideas Ranking"
    
    if show_detail:
        # Show details for each idea
        for idea in ideas:
            print_idea_details(idea)
    else:
        # Show ranking
        print_ranking(ideas, title)
    
    # Show statistics
    stats = manager.get_statistics()
    print(f"\nStatistics")
    print("=" * 80)
    print(f"Total Ideas: {stats.get('total_ideas', 0)}")
    print(f"\nBy Status:")
    for status, count in stats.get('ideas_by_status', {}).items():
        print(f"  {status}: {count}")
    
    print(f"\nBy Pillar:")
    for pillar, count in stats.get('ideas_by_pillar', {}).items():
        print(f"  {pillar}: {count}")
    
    print(f"\nAverage Scores:")
    for criterion, score in stats.get('average_scores', {}).items():
        print(f"  {criterion}: {score:.2f}")

if __name__ == "__main__":
    main()
```

## 4. Database Documentation (`database/README.md`)

# Database Structure

This database supports the content ideation workflow for Fadhil's personal brand content system.

## Tables

### 1. Content Ideas (`content_ideas`)

| Column | Type | Description |
|--------|------|-------------|
| `id` | UUID | Unique identifier |
| `title` | TEXT | Content idea title |
| `pillar` | ENUM | Content pillar (business_model_finance, revenue_growth, operations_leadership) |
| `concept_type` | ENUM | Type of concept (decision_note, operating_playbook) |
| `audience_problem` | TEXT | Problem statement for target audience |
| `target_search_volume` | INTEGER | YouTube search volume for validation |
| `gap_classification` | ENUM | Gap analysis (empty, shallow, deep) |
| `evidence_type` | ENUM | Evidence quality (primary_data, secondary_research, tertiary) |
| `reference_sources` | TEXT | Source references |
| `estimated_days_to_produce` | INTEGER | Estimated production time in days |
| `created_date` | TIMESTAMP | Record creation timestamp |
| `reason` | TEXT | Additional context or rationale |
| `p_score` | INTEGER | Search volume score (0-5) |
| `g_score` | INTEGER | Gap score (1-5) |
| `b_score` | INTEGER | Evidence score (1-5) |
| `k_score` | INTEGER | Capacity score (0-5) |
| `total_score` | INTEGER | Total calculated score (0-30) |
| `status` | ENUM | Current status (ready, improve, wait, gapped, merged) |

### 2. Gap Analysis (`gap_analysis`)

Reference table for gap classification criteria.

| Column | Type | Description |
|--------|------|-------------|
| `level` | VARCHAR | Gap level (empty, shallow, deep) |
| `score_value` | INTEGER | Numerical score for gap level |
| `description` | TEXT | Detailed description of gap level |

### 3. Evidence Sources (`evidence_sources`)

Reference table for evidence quality standards.

| Column | Type | Description |
|--------|------|-------------|
| `source_id` | VARCHAR | Source identifier |
| `source_type` | ENUM | Evidence type (primary, secondary, tertiary) |
| `description` | TEXT | Source description and criteria |

### 4. Ranking Criteria (`ranking_criteria`)

Reference table for scoring weights.

| Column | Type | Description |
|--------|------|-------------|
| `criterion` | VARCHAR | Criterion name (search_volume, gap, evidence, capacity) |
| `weight` | INTEGER | Weight multiplier |
| `description` | TEXT | Criterion description |

## Scoring System

### Formula

**Total Score = (p_score × 2) + (g_score × 2) + b_score + k_score**

### Score Ranges

| Criterion | Score 5 | Score 3 | Score 1 |
|-----------|---------|---------|---------|
| **Search Volume (p)** | ≥ 100,000 | 10,000-99,999 | < 10,000 |
| **Gap (g)** | Empty (no local content) | Shallow (limited scope) | Deep (saturated market) |
| **Evidence (b)** | Primary data (own data) | Secondary research (journals, reports) | Tertiary (opinions) |
| **Capacity (k)** | ≤ 2 days | 4 days | 7+ days |

### Status Definitions

| Status | Criteria |
|--------|----------|
| **ready** | Score ≥18 AND evidence ≥ secondary_research |
| **improve** | Score 16-17 OR needs improvement in one criterion |
| **wait** | Score ≥18 but evidence = tertiary OR score <16 |
| **gapped** | Gap = deep (market saturated) |
| **merged** | Duplicate of existing idea |

## Database Operations

### Python Scripts

1. **`scripts/content_ideas.py`** - Core database operations
   - Add, retrieve, update, delete ideas
   - Calculate scores and determine status
   - Database initialization and management

2. **`scripts/ranking.py`** - Ranking and filtering
   - Display idea rankings
   - Filter by status or criteria
   - Show statistics and analytics

### Command Line Usage

```bash
# Show ranking of all ideas
python3 scripts/ranking.py

# Show only ready ideas
python3 scripts/ranking.py --ready-only

# Show all ideas including hidden ones
python3 scripts/ranking.py --all

# Show detailed information for an idea
python3 scripts/ranking.py --detail
```

## Integration with Content Pipeline

### Stage 1: Ideation
1. Use `scripts/ranking.py` to evaluate and rank ideas
2. Filter ideas based on readiness criteria
3. Select top ideas for production

### Stage 2: Packaging
1. Retrieve selected ideas using their IDs
2. Access full details including evidence sources
3. Prepare materials for content development

### Stage 3: Research
1. Use evidence sources for validation
2. Cross-reference with ranking criteria
3. Update ideas with new research findings

### Stage 4: Production
1. Use idea details to guide content creation
2. Reference evidence sources in content
3. Document findings and outcomes

### Stage 5: Evaluation
1. Track idea performance after production
2. Update database with new data
3. Recalculate scores based on actual results

## Best Practices

1. **Never modify existing ideas** - Only add new ones
2. **Always calculate scores automatically** - Don't manually set scores
3. **Use evidence_type for quality** - Prioritize primary and secondary evidence
4. **Review gap classification regularly** - Market conditions change
5. **Document all decisions** - Use the `reason` field effectively

## Maintenance

### Daily
- Check ranking of ready ideas
- Review new ideas as they're added

### Weekly
- Analyze statistics and trends
- Update evidence sources with new research
- Review and refine ranking criteria

### Monthly
- Clean up old or irrelevant ideas
- Update gap analysis based on new market data
- Review and adjust scoring weights if needed

## Backup and Recovery

The database stores all ideas persistently. For backup:
1. Export the SQLite database file
2. Consider regular backups of the `database/content_ideas.db` file
3. Maintain version history using the creation dates

## Scaling

For large-scale operations:
1. Use database indexes for performance
2. Implement periodic archiving of old ideas
3. Consider sharding by pillar if dealing with thousands of ideas
4. Add caching for frequently accessed ideas

This database structure provides a robust foundation for managing and ranking content ideas while supporting the entire content production workflow from ideation to evaluation.