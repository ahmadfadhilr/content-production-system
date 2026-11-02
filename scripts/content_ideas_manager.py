#!/usr/bin/env python3
"""
Simple content idea management system for ranking and storing content ideas.
"""

import os
import sys
import uuid
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime

# Define the database path
db_path = Path(__file__).parent.parent / "database.db"

class ContentIdea:
    """Represents a content idea with its metadata and calculated scores."""
    
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
        self.created_date = datetime.now().isoformat()
        
        # Calculate scores using the ranking system
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
        """Convert idea to dictionary for database storage."""
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
            'created_date': self.created_date,
            'reason': self.reason,
            'p_score': self.p_score,
            'g_score': self.g_score,
            'b_score': self.b_score,
            'k_score': self.k_score,
            'total_score': self.total_score,
            'status': self.status
        }
class ContentIdeasManager:
    """Manages content ideas and their lifecycle."""
    
    def __init__(self):
        self.db_path = Path(__file__).parent.parent / "database.db"
        self._ensure_database_exists()
    
    def _ensure_database_exists(self):
        """Initialize the database with schema if it doesn't exist."""
        # Create parent directory if it doesn't exist
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
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
            )
        ''')
        
        # Create indexes
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_content_ideas_status ON content_ideas(status)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_content_ideas_pillar ON content_ideas(pillar)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_content_ideas_total_score ON content_ideas(total_score DESC)')
        
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
    
    def get_all_ideas(self, status_filter: Optional[str] = None) -> List[Dict]:
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
            ideas.append(dict(zip(columns, row)))
        
        conn.close()
        return ideas
    
    def get_statistics(self) -> Dict:
        """Get database statistics."""
        import sqlite3
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        stats = {}
        
        # Total ideas
        cursor.execute('SELECT COUNT(*) FROM content_ideas')
        stats['total_ideas'] = cursor.fetchone()[0]
        
        # Ideas by status
        cursor.execute('SELECT status, COUNT(*) FROM content_ideas GROUP BY status')
        stats['ideas_by_status'] = {
            row[0]: row[1] for row in cursor.fetchall()
        }
        
        conn.close()
        return stats

# Create the manager instance for import
manager = ContentIdeasManager()