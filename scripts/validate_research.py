#!/usr/bin/env python3
"""Validate research records, generated views, CSV, and cross-links."""
import csv,json,re,html,tempfile,shutil,subprocess,sys
from pathlib import Path
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parents[1]
def validate(root=ROOT):
 data=json.loads((root/'data/papers.json').read_text());papers=data['papers'];ids=[p['id'] for p in papers];errors=[]
 def check(ok,message):
  if not ok:errors.append(message)
 check(len(ids)==len(set(ids)),'Duplicate research ID')
 check(len({p['url'] for p in papers})==len(papers),'Duplicate original publication URL')
 dois=[p['doi'].lower() for p in papers if p['doi']]
 check(len(dois)==len(set(dois)),'Duplicate publication DOI')
 games={g['id'] for g in json.loads((root/'data/games.json').read_text())['games']}
 for p in papers:
  for key in ['id','title','authors','venue','summary_en','summary_zh','publication_type','topic','url','discovery_source','checked_at','metadata_basis']:check(bool(p.get(key)),f'{p["id"]}: missing {key}')
  check(p['publication_type'] in data['publication_types'],'Unknown publication type')
  check(p['topic'] in data['topics'],'Unknown topic')
  check(isinstance(p['year'],int) and 1900<=p['year']<=2100,'Invalid year')
  for k in ['url','discovery_source']:check(urlsplit(p[k]).scheme=='https' and bool(urlsplit(p[k]).netloc),'Invalid source URL')
  check(not p['doi'] or bool(re.fullmatch(r'10\.\d{4,9}/\S+',p['doi'])),'Invalid DOI')
  check(not re.search('[\u4e00-\u9fff]',p['summary_en']),'Chinese text in English summary')
  check(set(p['related_game_ids'])<=games,'Unknown game cross-link')
  check(set(p.get('related_paper_ids',[]))<=set(ids),'Unknown related paper')
 for lang in ['', 'en/']:
  s=(root/lang/'research.html').read_text()
  for p in papers:check(s.count(f'id="{p["id"]}"')==1,f'{lang}: missing/duplicate article {p["id"]}')
  if lang:check(not re.search('[\u4e00-\u9fff]',re.sub(r'<a href="../research.html">中文</a>','',s)),'Chinese content in English page')
  check('research.html' in (root/lang/'index.html').read_text(),'Missing home navigation')
 with (root/'data/papers.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
 check(len(rows)==len(papers),'CSV count differs')
 for p,row in zip(papers,rows):
  for k,v in p.items():check(row[k]==(json.dumps(v,ensure_ascii=False) if isinstance(v,list) else str(v)),f'CSV differs: {p["id"]}/{k}')
 return errors
if __name__=='__main__':
 errors=validate()
 if errors:print('\n'.join(errors));sys.exit(1)
 print('Research data, bilingual pages, CSV and cross-links valid.')
