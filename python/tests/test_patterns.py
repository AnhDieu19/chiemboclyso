"""Test integrated patterns and brightness"""
from chart import generate_birth_chart
from interpretation import generate_overall_interpretation

chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
interp = generate_overall_interpretation(chart)

print("=" * 60)
print("TỬ VI NAM PHÁI - TEST PATTERNS & BRIGHTNESS")
print("=" * 60)

# Test patterns
patterns = interp.get('patterns', [])
print(f"\n📋 Patterns found: {len(patterns)}")
for p in patterns:
    print(f"  • {p['name']} ({p['nature']})")
    print(f"    → {p['meaning'][:60]}...")

# Test patterns summary
summary = interp.get('patterns_summary', {})
print(f"\n📊 Summary: {summary.get('overall', 'N/A')}")
print(f"   Cát: {summary.get('cat_count', 0)}, Hung: {summary.get('hung_count', 0)}")

# Test fortune with patterns
print(f"\n🔮 Fortune:\n{interp.get('fortune', 'N/A')}")

print("\n" + "=" * 60)
print("✅ Test completed!")
