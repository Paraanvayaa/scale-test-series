import json

with open('iit_analysis_summary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for iit, stats in data.items():
    print('==============================')
    print(f'IIT: {iit}')
    print(f'Years: {stats["years"]}')
    print(f'Total Questions: {stats["total_questions"]}')
    print(f'Subjects: {stats["subject_counts"]}')
    print(f'Question Types: {stats["q_type_counts"]}')
    print(f'Physics Topics: {stats["topic_distribution"]["Physics"]}')
    print(f'Chemistry Topics: {stats["topic_distribution"]["Chemistry"]}')
    print(f'Math Topics: {stats["topic_distribution"]["Mathematics"]}')
    print(f'Avg Word Count: {stats["avg_word_count"]}')
    print(f'Diagram Count: {stats["diagram_count"]}')
    print(f'Multi-concept Count: {stats["multi_concept_count"]}')
    print(f'P1 vs P2: {stats["p1_vs_p2"]}')

