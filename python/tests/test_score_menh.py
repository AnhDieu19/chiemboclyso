"""
Test script for score_menh() function
Compare with TalentFortuneAnalyzer.score_fortune() for consistency
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chart.chart_builder import generate_birth_chart
from analytics.multi_score_engine import MultiDimensionalScorer
from analytics.talent_fortune_engine import TalentFortuneAnalyzer


def test_score_menh():
    """Test score_menh() with sample charts"""
    
    test_cases = [
        {
            'name': 'Sample 1: 28/3/1994, giờ Mão',
            'day': 28, 'month': 3, 'year': 1994, 'hour': 3, 'gender': 'nam'
        },
        {
            'name': 'Sample 2: 19/5/1981, giờ Thân',
            'day': 19, 'month': 5, 'year': 1981, 'hour': 8, 'gender': 'nam'
        },
        {
            'name': 'Sample 3: 1/1/2000, giờ Tý',
            'day': 1, 'month': 1, 'year': 2000, 'hour': 0, 'gender': 'nu'
        },
    ]
    
    print("=" * 80)
    print("TEST SCORE_MENH() FUNCTION")
    print("=" * 80)
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"TEST CASE {i}: {test['name']}")
        print(f"{'='*80}")
        
        # Generate chart
        chart = generate_birth_chart(
            test['day'], test['month'], test['year'], 
            test['hour'], test['gender']
        )
        
        # Test MultiDimensionalScorer.score_menh()
        scorer = MultiDimensionalScorer(chart)
        menh_result = scorer.score_menh()
        
        # Test TalentFortuneAnalyzer.score_fortune() for comparison
        analyzer = TalentFortuneAnalyzer(chart)
        fortune_result = analyzer.score_fortune()
        
        # Display results
        print(f"\n📊 MultiDimensionalScorer.score_menh():")
        print(f"   Score: {menh_result['score']:.2f}")
        print(f"   Reasons ({len(menh_result['reasons'])}):")
        for r in menh_result['reasons'][:10]:  # Show first 10
            print(f"     - {r}")
        if len(menh_result['reasons']) > 10:
            print(f"     ... và {len(menh_result['reasons']) - 10} lý do khác")
        
        print(f"\n📊 TalentFortuneAnalyzer.score_fortune():")
        print(f"   Score: {fortune_result['score']:.2f}")
        print(f"   Factors ({len(fortune_result['factors'])}):")
        for f in fortune_result['factors'][:10]:  # Show first 10
            print(f"     - {f}")
        if len(fortune_result['factors']) > 10:
            print(f"     ... và {len(fortune_result['factors']) - 10} yếu tố khác")
        
        # Compare scores
        diff = abs(menh_result['score'] - fortune_result['score'])
        print(f"\n📈 Comparison:")
        print(f"   Score difference: {diff:.2f}")
        if diff < 1.0:
            print(f"   ✅ Scores are similar (difference < 1.0)")
        elif diff < 2.0:
            print(f"   ⚠️  Scores differ moderately (difference < 2.0)")
        else:
            print(f"   ❌ Scores differ significantly (difference >= 2.0)")
        
        # Show chart info
        print(f"\n📋 Chart Info:")
        print(f"   Cung Mệnh: {chart.get('menh_name', 'N/A')}")
        print(f"   Cung Thân: {chart.get('than_name', 'N/A')}")
        print(f"   Cục: {chart.get('cuc', {}).get('name', 'N/A')}")
        print(f"   Mệnh Chủ: {chart.get('menh_chu', 'N/A')}")
        print(f"   Thân Chủ: {chart.get('than_chu', 'N/A')}")
        
        # Show Chính Tinh tại Mệnh
        menh_idx = chart.get('menh_position')
        if menh_idx is not None:
            menh_pos = chart.get('positions', {}).get(menh_idx, {})
            chinh_tinh = [s.get('name', s) if isinstance(s, dict) else s 
                         for s in menh_pos.get('stars', []) 
                         if isinstance(s, dict) and s.get('name') in scorer.CHINH_TINH]
            if chinh_tinh:
                print(f"   Chính Tinh tại Mệnh: {', '.join(chinh_tinh)}")
            else:
                print(f"   Chính Tinh tại Mệnh: Vô Chính Diệu")


if __name__ == "__main__":
    test_score_menh()






