"""Regression tests for the checks that protect community contributions."""
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from validate_catalog import validate
from sync_catalog import sync

class CatalogValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)/'catalog'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('__pycache__','*.pyc','.git'))
    def tearDown(self): self.temp.cleanup()
    def change(self,path,operation):
        p=self.root/path;d=json.loads(p.read_text());operation(d);p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
    def assert_error(self,text): self.assertTrue(any(text in error for error in validate(self.root)),text)
    def test_current_catalog_passes(self): self.assertEqual(validate(self.root),[])
    def test_duplicate_id_is_rejected(self):
        self.change('en/data/games.json',lambda d:d['games'].append(dict(d['games'][0])))
        self.assert_error('duplicate ID')
    def test_source_scheme_is_checked(self):
        self.change('en/data/games.json',lambda d:d['games'][0]['sources'][0].update(url='javascript:alert(1)'))
        self.assert_error('invalid source URL')
    def test_required_description_is_checked(self):
        self.change('en/data/games.json',lambda d:d['games'][0].update(description=''))
        self.assert_error('missing description')
    def test_stale_csv_is_rejected(self):
        self.change('en/data/games.json',lambda d:d['games'][0].update(description='Updated description'))
        self.assert_error('CSV field out of sync: description')
    def test_bilingual_ids_are_checked(self):
        self.change('en/data/games.json',lambda d:d['games'].pop())
        self.assert_error('bilingual IDs differ')
    def test_statistics_are_checked(self):
        self.change('en/data/review-method.json',lambda d:d.update(total_entries=999))
        self.assert_error('main total out of sync')
    def test_credit_handles_are_checked(self):
        self.change('data/contributors.json',lambda d:d['contributors'][0].update(github='invalid/name'))
        self.assert_error('invalid GitHub handle')
    def test_sync_handles_a_new_bilingual_record(self):
        for language in ['','en/']:
            def add(doc):
                row=dict(doc['games'][0]);row.update(id='community-fixture',title='Community fixture');doc['games'].append(row)
            self.change(language+'data/games.json',add)
        sync(self.root)
        self.assertEqual(validate(self.root),[])
        method=json.loads((self.root/'data/review-method.json').read_text())
        self.assertEqual(method['total_entries'],123)

if __name__=='__main__': unittest.main()
