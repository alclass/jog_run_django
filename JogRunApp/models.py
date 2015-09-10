from django.db import models
from datetime import datetime
# Create your models here.

class JogRunRecord(models.Model):
  jogrun_date       = models.DateField(default=datetime.today())
  startline_daytime = models.TimeField(default=datetime.now())
  from_stamp = models.CharField(max_length=10)
  to_stamp   = models.CharField(max_length=10)
  duration = models.IntegerField(default=0) # in seconds
  run_length = models.IntegerField(default=0) # in meters
  n_of_stops = models.IntegerField(default=0)
  body_natur_weight = models.IntegerField(default=0) # in kilograms integer
  body_extra_weight = models.IntegerField(default=0) # in kilograms integer
  weather_type = models.IntegerField(default=0) # to change this to a foreign key
  feeling_qualifiers = models.IntegerField(default=0) # to change this to a one-to-many
  additional_info = models.TextField()

  def __str__(self):
    place_str = 'JogRun at {}-{}'.format(self.from_stamp, self.to_stamp)
    date_str = ': on {}'.format(self.jogrun_date)
    took = ': took {} sec.'.format(self.duration)
    return '%s %s %s' %(place_str, date_str, took)
