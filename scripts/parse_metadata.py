import json

with open('metadata.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('TITLE:', data.get('title'))
print('UPLOAD DATE:', data.get('upload_date'))
print('DURATION (s):', data.get('duration'))
print('\n--- CHAPTERS ---')
for c in data.get('chapters', []) or []:
    st = c.get('start_time', 0)
    et = c.get('end_time', 0)
    print(f"{int(st//3600):02d}:{int((st%3600)//60):02d}:{int(st%60):02d} - {int(et//3600):02d}:{int((et%3600)//60):02d}:{int(et%60):02d} | {c.get('title')}")

print('\n--- DESCRIPTION ---')
print(data.get('description', ''))
