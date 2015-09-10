from datetime import datetime
# Create your models here.

class JogRunRecord():
  jogrun_date       = datetime.today()
  startline_daytime = datetime.now()
  from_stamp = 'USIN'
  to_stamp   = 'MARQ'
  duration = 60*30
  run_length = 6000
  n_of_stops = 0
  body_natur_weight = 75
  body_extra_weight = 0
  weather_type = 1
  feeling_qualifiers = [1,2,3]

  def __str__(self):
    place_str = 'JogRun at {}-{}'.format(self.from_stamp, self.to_stamp)
    date_str = ': on {}'.format(self.jogrun_date)
    took = ': took {} sec.'.format(self.duration)
    return '%s %s %s' %(place_str, date_str, took)

def test_from_cmdline():
  jr = JogRunRecord()
  print('jr ==>>', jr)

if __name__ == '__main__':
  test_from_cmdline()