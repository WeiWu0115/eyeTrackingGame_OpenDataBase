#!/usr/bin/env python3
"""Regenerate CSV files and counts after editing the bilingual JSON records."""
import collections
import csv
import html
import json
from pathlib import Path
import re
from validate_catalog import CATEGORIES

ROOT=Path(__file__).resolve().parents[1]
ROLE_ZH={'Gaze control':'眼控操作','Gaze assistance':'眼动辅助','Gaze-responsive':'注视响应','Blink detection':'眨眼检测','Multimodal':'多模态交互','Measurement only':'眼动测量'}
def sync(root=ROOT):
    root=Path(root);data=json.loads((root/'en/data/games.json').read_text())['games'];related=json.loads((root/'en/data/related-training.json').read_text())['entries']
    cats=collections.Counter(x['category'] for x in data);tags=collections.Counter(t for x in data for t in x['tags']);roles=collections.Counter(x['eye_role'] for x in data);main_ids={x['id'] for x in data};related_ids={x['id'] for x in related};shared=sorted(main_ids&related_ids)
    for language,directory in [('zh',root),('en',root/'en')]:
        for stem,key in [('games','games'),('related-training','entries')]:
            p=directory/'data'/f'{stem}.json';doc=json.loads(p.read_text());records=doc[key]
            if stem=='related-training':doc['shared_main_collection_ids']=shared;p.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
            fields=list(dict.fromkeys(k for g in records for k in g))
            with (directory/'data'/f'{stem}.csv').open('w',encoding='utf-8-sig',newline='') as f:
                w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
                for g in records:w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in g.items()})
        p=directory/'data/review-method.json';doc=json.loads(p.read_text());doc.update(total_entries=len(data),primary_category_counts=dict(cats),overlapping_tag_counts=dict(tags),gaze_role_counts=dict(roles),shared_main_and_related_ids=shared,unique_records_across_collections=len(main_ids|related_ids),related_training_games=sum(x['entry_type']=='Game' for x in related),related_research_frameworks=sum(x['entry_type']=='Research environment' for x in related));p.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
        p=directory/'review.html';s=p.read_text();tables=[]
        for counter,labels in [(cats,CATEGORIES),(roles,ROLE_ZH)]:tables.append(''.join('<tr><td>'+html.escape(k if language=='en' else labels[k])+'</td><td>'+str(v)+'</td></tr>' for k,v in counter.items()))
        pos=iter(tables);s=re.sub(r'<tbody>.*?</tbody>',lambda m:'<tbody>'+next(pos)+'</tbody>',s,count=2,flags=re.S)
        s=re.sub(r'(collection contains )\d+( records)',rf'\g<1>{len(data)}\2',s);s=re.sub(r'(目录收录 )\d+( 条)',rf'\g<1>{len(data)}\2',s)
        if language=='en':s=re.sub(r'Overlapping tags cover .*? records\.',f'Overlapping tags cover {tags["Commercial"]} commercial, {tags["Steam"]} Steam, {tags["Indie"]} indie, {tags["Awarded"]} award-winning, {tags["Accessibility"]} accessibility, {tags["Research"]} research, {tags["Training"]} training, and {tags["VR"]} VR records.',s)
        else:s=re.sub(r'交叉标签覆盖.*?。',f'交叉标签覆盖商业 {tags["Commercial"]}、Steam {tags["Steam"]}、独立 {tags["Indie"]}、获奖 {tags["Awarded"]}、无障碍 {tags["Accessibility"]}、研究 {tags["Research"]}、学习训练 {tags["Training"]} 与 VR {tags["VR"]}。',s)
        p.write_text(s)
        p=directory/'README.md';s=p.read_text();s=re.sub(r'\b\d+ records (in the main collection|covering games)',lambda m:str(len(data))+' records '+m[1],s);s=re.sub(r'(Main collection — )\d+( records)',rf'\g<1>{len(data)}\2',s);s=re.sub(r'(\| \*\*Total\*\* \| \*\*)\d+(\*\* \|)',rf'\g<1>{len(data)}\2',s)
        for cat in CATEGORIES:s=re.sub(r'(\| '+re.escape(cat)+r' \| )\d+( \|)',lambda m:m[1]+str(cats[cat])+m[2],s)
        for tag,phrase in [('Steam','records with Steam sources'),('Research','research-related records'),('Training','training records')]:s=re.sub(r'\b\d+ '+phrase,str(tags[tag])+' '+phrase,s)
        p.write_text(s)
    print(f'Synchronized exports and counts: {len(data)} main records; {len(related)} related records; {len(shared)} shared record(s).')
if __name__=='__main__': sync()
