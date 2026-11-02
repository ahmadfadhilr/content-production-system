#!/usr/bin/env python3
"""
Script to run the content ideation workflow and populate the database.
"""

import sys
from pathlib import Path
from datetime import datetime

# Add the current directory to the path
sys.path.append(str(Path(__file__).parent))

from content_ideas_manager import ContentIdea, ContentIdeasManager
def main():
    """Main function to run the ideation workflow."""
    print("Running Content Ideation Workflow...")
    
    # Initialize database manager
    manager = ContentIdeasManager()
    
    # Sample content ideas based on the workflow
    # These are examples that would come from running the 01-ideasi.md workflow
    
    sample_ideas = [
        ContentIdea(
            title="Margin per Lini Layanan di Bisnis Jasa",
            pillar="business_model_finance",
            concept_type="decision_note",
            audience_problem="Pemilik bisnis jasa dengan 2-10 orang tim yang omzetnya naik tetapi uang di rekening tidak bertambah, sehingga ia tidak tahu lini mana yang sebenarnya membiayai lini lain.",
            target_search_volume=183822,
            gap_classification="empty",
            evidence_type="secondary_research",
            reference_sources="Cugini2017; Lueg2024; TheCPJ2018",
            estimated_days_to_produce=2,
            reason="Pasokan lokal kosong untuk menghitung margin per lini layanan."
        ),
        ContentIdea(
            title="Harga Jual Layanan Jasa untuk Bisnis yang Waktu Orangnya Terbatas",
            pillar="business_model_finance",
            concept_type="decision_note",
            audience_problem="Pemilik bisnis jasa dengan kapasitas orang yang terbatas ingin menetapkan harga yang mencerminkan kapasitas mereka tanpa kehilangan pendapatan.",
            target_search_volume=121915,
            gap_classification="shallow",
            evidence_type="secondary_research",
            reference_sources="Hinterhuber2004; Avlonitis2007; Indounas2006",
            estimated_days_to_produce=2,
            reason="Menargetkan bisnis jasa dengan batasan kapasitas orang yang sulit ditemukan di YouTube."
        ),
        ContentIdea(
            title="Mengatur Tim 3-8 Orang: Peran, Ritme Rapat, Batas Wewenang",
            pillar="operations_leadership",
            concept_type="operating_playbook",
            audience_problem="Pemilik bisnis dengan 3-8 orang yang mengeluh tim tidak jalan, padahal masalahnya bukan motivasi melainkan peran yang tidak pernah didefinisikan.",
            target_search_volume=81301,
            gap_classification="shallow",
            evidence_type="secondary_research",
            reference_sources="Gallup2026; Nasrallah2015; Belloc2025",
            estimated_days_to_produce=3,
            reason="Pasokan lokal membahas motivasi, bukan pembagian peran dan wewenang yang jelas."
        ),
        ContentIdea(
            title="Kenaikan Harga dan Siapa yang Benar-Benar Pergi",
            pillar="business_model_finance",
            concept_type="decision_note",
            audience_problem="Pemilik bisnis yang ingin menaikkan harga tetapi tidak tahu siapa yang benar-benar akan pergi.",
            target_search_volume=17228,
            gap_classification="shallow",
            evidence_type="secondary_research",
            reference_sources="Dawes2009; Ascarza2016",
            estimated_days_to_produce=3,
            reason="Permintaan lemah, fokus pada mencari kueri pengganti atau video pendek."
        ),
        ContentIdea(
            title="Retensi per Kohort, Bukan Repeat Order Total",
            pillar="revenue_growth",
            concept_type="operating_playbook",
            audience_problem="Bisnis yang mengukur repeat order sebagai satu angka tanpa memisahkan pelanggan per bulan pertama kedatangan mereka.",
            target_search_volume=22466,
            gap_classification="shallow",
            evidence_type="secondary_research",
            reference_sources="Ascarza2016; JRetailing2026",
            estimated_days_to_produce=2,
            reason="Gap dangkal. Cari sudut lebih sempit seperti retensi per tutor atau per paket."
        ),
    ]
    
    # Add ideas to database
    added_count = 0
    for idea in sample_ideas:
        idea_id = manager.add_idea(idea)
        added_count += 1
        print(f"Added idea: {idea.title} (ID: {idea_id})")
    
    print(f"\nSuccessfully added {added_count} content ideas to the database.")
    
    # Show ranking
    print("\n" + "="*80)
    print("Content Ideas Ranking:")
    print("="*80)
    
    ideas = manager.get_all_ideas()
    print(f"{'#':>3} | {'Title':<50} | {'Pillar':>10} | {'Score':>6} | {'Status':>10}")
    print("-"*80)
    
    for i, idea in enumerate(ideas, 1):
        print(f"{i:>3} | {idea['title'][:47]:<50} | {idea['pillar']:>10} | "
              f"{idea['total_score']:>6} | {idea['status']:>10}")
    
    print(f"\nTotal ideas in database: {len(ideas)}")
    
    ready_ideas = [idea for idea in ideas if idea['status'] == 'ready']
    print(f"Ideas ready for production: {len(ready_ideas)}")

if __name__ == "__main__":
    main()