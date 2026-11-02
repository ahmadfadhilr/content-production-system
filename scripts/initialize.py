#!/usr/bin/env python3
"""
Script to initialize the database and add sample content ideas.
"""

import sqlite3
import uuid
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "database.db"

def main():
    """Main function to initialize database and add sample ideas."""
    print("Initializing database and adding sample content ideas...")
    
    # Connect to the database
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create tables if they don't exist
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
    
    # Check if we already have data
    cursor.execute('SELECT COUNT(*) FROM content_ideas')
    total = cursor.fetchone()[0]
    
    if total == 0:
        # Sample content ideas from the ideasi workflow
        sample_ideas = [
            {
                'id': str(uuid.uuid4()),
                'title': 'Margin per Lini Layanan di Bisnis Jasa',
                'pillar': 'business_model_finance',
                'concept_type': 'decision_note',
                'audience_problem': 'Pemilik bisnis jasa dengan 2-10 orang tim yang omzetnya naik tetapi uang di rekening tidak bertambah, sehingga ia tidak tahu lini mana yang sebenarnya membiayai lini lain.',
                'target_search_volume': 183822,
                'gap_classification': 'empty',
                'evidence_type': 'secondary_research',
                'reference_sources': 'Cugini2017; Lueg2024; TheCPJ2018',
                'estimated_days_to_produce': 2,
                'reason': 'Pasokan lokal kosong untuk menghitung margin per lini layanan.',
                'created_date': datetime.now().isoformat(),
                'p_score': 3,
                'g_score': 5,
                'b_score': 3,
                'k_score': 5,
                'total_score': 28,
                'status': 'ready'
            },
            {
                'id': str(uuid.uuid4()),
                'title': 'Harga Jual Layanan Jasa untuk Bisnis yang Waktu Orangnya Terbatas',
                'pillar': 'business_model_finance',
                'concept_type': 'decision_note',
                'audience_problem': 'Pemilik bisnis jasa dengan kapasitas orang yang terbatas ingin menetapkan harga yang mencerminkan kapasitas mereka tanpa kehilangan pendapatan.',
                'target_search_volume': 121915,
                'gap_classification': 'shallow',
                'evidence_type': 'secondary_research',
                'reference_sources': 'Hinterhuber2004; Avlonitis2007; Indounas2006',
                'estimated_days_to_produce': 2,
                'reason': 'Menargetkan bisnis jasa dengan batasan kapasitas orang yang sulit ditemukan di YouTube.',
                'created_date': datetime.now().isoformat(),
                'p_score': 3,
                'g_score': 3,
                'b_score': 3,
                'k_score': 5,
                'total_score': 24,
                'status': 'ready'
            },
            {
                'id': str(uuid.uuid4()),
                'title': 'Mengatur Tim 3-8 Orang: Peran, Ritme Rapat, Batas Wewenang',
                'pillar': 'operations_leadership',
                'concept_type': 'operating_playbook',
                'audience_problem': 'Pemilik bisnis dengan 3-8 orang yang mengeluh tim tidak jalan, padahal masalahnya bukan motivasi melainkan peran yang tidak pernah didefinisikan.',
                'target_search_volume': 81301,
                'gap_classification': 'shallow',
                'evidence_type': 'secondary_research',
                'reference_sources': 'Gallup2026; Nasrallah2015; Belloc2025',
                'estimated_days_to_produce': 3,
                'reason': 'Pasokan lokal membahas motivasi, bukan pembagian peran dan wewenang yang jelas.',
                'created_date': datetime.now().isoformat(),
                'p_score': 3,
                'g_score': 3,
                'b_score': 3,
                'k_score': 3,
                'total_score': 20,
                'status': 'ready'
            }
        ]
        
        # Insert sample ideas
        for idea in sample_ideas:
            cursor.execute('''
                INSERT INTO content_ideas (
                    id, title, pillar, concept_type, audience_problem,
                    target_search_volume, gap_classification, evidence_type,
                    reference_sources, estimated_days_to_produce, created_date,
                    reason, p_score, g_score, b_score, k_score, total_score, status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                idea['id'], idea['title'], idea['pillar'], idea['concept_type'],
                idea['audience_problem'], idea['target_search_volume'],
                idea['gap_classification'], idea['evidence_type'],
                idea['reference_sources'], idea['estimated_days_to_produce'],
                idea['created_date'], idea['reason'], idea['p_score'],
                idea['g_score'], idea['b_score'], idea['k_score'],
                idea['total_score'], idea['status']
            ))
        
        conn.commit()
        print(f'Successfully added {len(sample_ideas)} sample content ideas to the database.')
    else:
        print(f'Database already contains {total} content ideas.')
    
    conn.close()

if __name__ == "__main__":
    main()