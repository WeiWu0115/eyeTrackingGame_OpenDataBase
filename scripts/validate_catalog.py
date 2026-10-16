#!/usr/bin/env python3
"""Validate the bilingual catalog using Python's standard library."""
import argparse
import collections
import csv
import datetime
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

CATEGORIES = {'Commercial games':'商业游戏','Indie & small games':'独立小游戏','Accessible gaze games':'无障碍眼控','Research prototypes':'研究原型','Training & serious games':'训练与严肃游戏','Research observation & datasets':'研究观察与数据集'}
ROLES = {'Gaze control','Gaze assistance','Gaze-responsive','Blink detection','Multimodal','Measurement only'}
TYPES = {'Game','Research prototype','Activity suite','Research environment'}
REQUIRED = ['id','title','category','genre','device','platform','interaction','description','features','sources','image_url','image_source','image_kind','image_credit','image_license','verified_at','tags','design_intent','eye_role','entry_type','genre_family']
HANDLE = re.compile(r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?\Z')

def validate(root):
    root = Path(root).resolve()
    errors = []
    def check(ok, message):
        if not ok: errors.append(message)
    def load(path):
        try: return json.loads(path.read_text(encoding='utf-8'))
        except (OSError, ValueError) as exc:
            errors.append(f'{path.relative_to(root)}: {exc}')
            return {}
    def web_url(value):
        try:
            p = urlsplit(value)
            return p.scheme in ('http','https') and bool(p.netloc) and not any(c.isspace() for c in value)
        except (TypeError, ValueError): return False
    def image_url(value, directory, context):
        if not isinstance(value, str) or not value:
            check(False, f'{context}: image reference required'); return
        if urlsplit(value).scheme:
            check(web_url(value), f'{context}: invalid image URL'); return
        target = (directory / unquote(urlsplit(value).path)).resolve()
        check(target.is_relative_to(root) and target.is_file(), f'{context}: local image missing: {value}')
    collections_by_language = {}
    for language, directory in [('zh',root),('en',root/'en')]:
        language_sets = {}
        for stem, key in [('games','games')]:
            path = directory/'data'/f'{stem}.json'
            document = load(path)
            records = document.get(key, [])
            check(isinstance(records,list) and bool(records), f'{language}/{stem}: entries required')
            if not isinstance(records,list): continue
            ids = [g.get('id') for g in records if isinstance(g,dict)]
            check(len(ids)==len(records), f'{language}/{stem}: each record must be an object')
            check(len(ids)==len(set(ids)), f'{language}/{stem}: duplicate ID')
            titles=[g.get('title','').strip().casefold() for g in records if isinstance(g,dict) and isinstance(g.get('title'),str)]
            check(len(titles)==len(set(titles)), f'{language}/{stem}: duplicate title; identify editions in the title')
            check(all(isinstance(i,str) and re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',i) for i in ids), f'{language}/{stem}: invalid ID format')
            by_id = {g['id']:g for g in records if isinstance(g,dict) and isinstance(g.get('id'),str)}
            language_sets[stem] = by_id
            for i,g in by_id.items():
                context = f'{language}/{stem}/{i}'
                fields = REQUIRED if stem=='games' else ['id','title','entry_type','domain','description','interaction','sources','image_url','image_source','image_kind','image_credit','image_license','verified_at']
                for field in fields: check(bool(g.get(field)), f'{context}: missing {field}')
                check(g.get('entry_type') in TYPES, f'{context}: invalid entry_type')
                if stem=='games':
                    check(g.get('category') in (CATEGORIES if language=='en' else CATEGORIES.values()), f'{context}: invalid category')
                    check(g.get('eye_role') in ROLES, f'{context}: invalid eye_role')
                    for field in ['features','tags','design_intent']:
                        check(isinstance(g.get(field),list) and all(isinstance(x,str) and x.strip() for x in g[field]), f'{context}: {field} must be a string array')
                    year=g.get('year');check(year is None or isinstance(year,int) and 1900<=year<=2100, f'{context}: invalid year')
                sources=g.get('sources',[])
                check(isinstance(sources,list) and bool(sources), f'{context}: primary source required')
                if isinstance(sources,list):
                    for source in sources:
                        check(isinstance(source,dict) and bool(source.get('title')) and web_url(source.get('url')), f'{context}: invalid source URL or title')
                for field in ['image_url','image_source']: image_url(g.get(field),directory,context+'/'+field)
                try: datetime.date.fromisoformat(g.get('verified_at',''))
                except (TypeError,ValueError): check(False, f'{context}: verified_at must be YYYY-MM-DD')
                if language=='en': check(not re.search('[\u4e00-\u9fff]',json.dumps(g,ensure_ascii=False)), f'{context}: English content contains Chinese text')
            try:
                with (directory/'data'/f'{stem}.csv').open(encoding='utf-8-sig',newline='') as f:
                    reader=csv.DictReader(f);columns=reader.fieldnames or [];rows=list(reader)
                expected_fields=set(k for g in records for k in g)
                check(set(columns)==expected_fields, f'{language}/{stem}: CSV columns out of sync')
                check([r.get('id') for r in rows]==ids, f'{language}/{stem}: CSV rows out of sync')
                for record,row in zip(records,rows):
                    for field in columns:
                        value=record.get(field)
                        if isinstance(value,(list,dict)):
                            try: equal=json.loads(row.get(field,''))==value
                            except (TypeError,ValueError): equal=False
                        else: equal=row.get(field,'')==('' if value is None else str(value))
                        check(equal,f'{language}/{stem}/{record.get("id")}: CSV field out of sync: {field}')
            except (OSError,csv.Error) as exc: check(False,f'{language}/{stem}: CSV read failed: {exc}')
        collections_by_language[language]=language_sets
    for stem in ['games']:
        zh=collections_by_language.get('zh',{}).get(stem,{})
        en=collections_by_language.get('en',{}).get(stem,{})
        check(set(zh)==set(en), f'{stem}: bilingual IDs differ')
        for i in set(zh)&set(en):
            fields=['entry_type']+(['tags','design_intent','eye_role','genre_family','year'] if stem=='games' else ['main_collection_id'])
            for field in fields:
                a,b=zh[i].get(field),en[i].get(field)
                check((set(a)==set(b)) if isinstance(a,list) and isinstance(b,list) else a==b, f'{stem}/{i}: bilingual {field} differs')
    en=collections_by_language.get('en',{})
    main=en.get('games',{})
    counts=collections.Counter(g.get('category') for g in main.values())
    tags=collections.Counter(t for g in main.values() for t in g.get('tags',[]))
    roles=collections.Counter(g.get('eye_role') for g in main.values())
    for language,directory in [('zh',root),('en',root/'en')]:
        method=load(directory/'data/review-method.json')
        check(method.get('total_entries')==len(main),f'{language}: main total out of sync')
        for field,actual in [('primary_category_counts',counts),('overlapping_tag_counts',tags),('gaze_role_counts',roles)]:
            check(method.get(field)==dict(actual), f'{language}: {field} out of sync')
    contributors=load(root/'data/contributors.json').get('contributors',[])
    handles=[x.get('github','') for x in contributors]
    check(len(handles)==len(set(h.lower() for h in handles)), 'contributors: duplicate GitHub handle')
    for item in contributors:
        check(bool(HANDLE.fullmatch(item.get('github',''))), 'contributors: invalid GitHub handle')
        check(bool(item.get('roles')), 'contributors: roles required')
    for language_sets in collections_by_language.values():
        for by_id in language_sets.values():
            for i,g in by_id.items():
                credit=g.get('contributors',[])
                check(isinstance(credit,list) and all(isinstance(h,str) and h in handles for h in credit),f'{i}: contributor handle missing from credits')
    class Links(HTMLParser):
        def handle_starttag(self,tag,attrs):
            attrs=dict(attrs)
            for key in ['src','href']:
                value=attrs.get(key,'')
                if not value or urlsplit(value).scheme or value.startswith(('#','//')): continue
                path=unquote(urlsplit(value).path)
                if path: self.paths.append(path)
    for page in list(root.glob('*.html'))+list((root/'en').glob('*.html')):
        parser=Links();parser.paths=[];text=page.read_text();parser.feed(text)
        for path in parser.paths: check((page.parent/path).resolve().exists(),f'{page.relative_to(root)}: local link missing: {path}')
        if page.parent==root/'en':check(not re.search('[\u4e00-\u9fff]',text),f'{page.relative_to(root)}: English page contains Chinese text')
    return errors

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);args=parser.parse_args()
    issues=validate(args.root)
    if issues:
        for issue in issues: print('ERROR:',issue)
        raise SystemExit(1)
    print('Catalog validation passed: IDs, required fields, bilingual records, CSV exports, sources, images, metadata, contributors and internal links.')
