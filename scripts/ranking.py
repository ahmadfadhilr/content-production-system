#!/usr/bin/env python3
"""
Content idea management and ranking script.
This is the main CLI tool for managing content ideas and their ranking.
"""

import os
import sys
from pathlib import Path
from typing import List, Dict, Optional

# Add the current directory to the path so we can import from scripts
sys.path.append(str(Path(__file__).parent))

from content_ideas_manager import ContentIdeasManager
def print_ranking(ideas: List[Dict], title: str = "Ranking"):
    """Print ranking of content ideas."""
    print(f"\n{title}")
    print("=" * 80)
    print(f"{'#':>3} | {'Title':<50} | {'Pillar':>10} | {'Score':>6} | {'Status':>10}")
    print("-" * 80)
    
    for i, idea in enumerate(ideas, 1):
        print(f"{i:>3} | {idea['title'][:47]:<50} | {idea['pillar']:>10} | "
              f"{idea['total_score']:>6} | {idea['status']:>10}")
    
    print()
    
    # Show ready ideas
    ready_ideas = [idea for idea in ideas if idea['status'] == 'ready']
    if ready_ideas:
        print(f"Ready to produce ({len(ready_ideas)}):")
        for idea in ready_ideas[:5]:
            print(f"  • {idea['title']}")
    
    print()

def print_idea_details(idea: Dict):
    """Print detailed information about a content idea."""
    print(f"\nContent Idea Details")
    print("=" * 80)
    print(f"ID: {idea['id']}")
    print(f"Title: {idea['title']}")
    print(f"Pillar: {idea['pillar']}")
    print(f"Concept Type: {idea['concept_type']}")
    print(f"\nAudience Problem:")
    print(f"  {idea['audience_problem']}")
    print(f"\nMetrics:")
    print(f"  Search Volume: {idea['target_search_volume']:,} (score: {idea['p_score']}/5)")
    print(f"  Gap Classification: {idea['gap_classification']} (score: {idea['g_score']}/5)")
    print(f"  Evidence Type: {idea['evidence_type']} (score: {idea['b_score']}/5)")
    print(f"  Estimated Production Time: {idea['estimated_days_to_produce']} days (score: {idea['k_score']}/5)")
    print(f"  Total Score: {idea['total_score']}/30")
    print(f"\nStatus: {idea['status']}")
    if idea['reason']:
        print(f"\nReason: {idea['reason']}")
    if idea['reference_sources']:
        print(f"\nReference Sources: {idea['reference_sources']}")
    
    print()

def main():
    """Main script entry point."""
    # Initialize the content ideas manager
    manager = ContentIdeasManager()
    
    # Parse command line arguments
    show_all = "--all" in sys.argv
    show_detail = "--detail" in sys.argv
    show_ready_only = "--ready-only" in sys.argv
    
    # Get ideas based on filters
    if show_ready_only:
        ideas = manager.get_all_ideas(status_filter="ready")
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
    print("\nStatistics")
    print("=" * 80)
    stats = manager.get_statistics()
    
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