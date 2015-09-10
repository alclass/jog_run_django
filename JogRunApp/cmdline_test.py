#!/usr/bin/env python
import  os, sys
abspath = os.path.abspath('.')
path_current_pieces = abspath.split('/')
if len(path_current_pieces)>1:
  path_one_above = '/'.join(path_current_pieces[:-1])
else:
  path_one_above = '/'.join(path_current_pieces)

django_sett_package = os.path.join(path_one_above, 'jog_run_django')
sys.path.insert(0, django_sett_package)

os.environ['DJANGO_SETTINGS_MODULE']=os.path.join(django_sett_package, 'settings.py')
print('set DJANGO_SETTINGS_MODULE to', os.environ['DJANGO_SETTINGS_MODULE'])

from models import JogRunRecord

def test_from_cmdline():
  jr = JogRunRecord()
  print('jr ==>>', jr)

if __name__ == '__main__':
  pass
  #test_from_cmdline()
