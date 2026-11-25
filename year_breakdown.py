import json

with open('iit_analysis_summary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for iit, stats in data.items():
    print(f'*** {iit} Year-by-Year ***')
    for yr in sorted(stats['year_profiles'].keys()):
        ydata = stats['year_profiles'][yr]
        print(f'  Year {yr}: Total={ydata["total_q"]}, Types={dict(ydata["q_types"])}')

