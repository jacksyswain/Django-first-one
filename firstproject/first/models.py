from django.db import models
from django.utils import timezone  

# Create your models here.
class products(models.Model):
  product_choice=[
    ('hd','hair-drier'),
    ('bm','bat-minton'),
    ('cl','cat-lead'),
    ('hm','hand-malt'),
    ('bc','base-candle'),
    ('lm','left-mount'),
  ]

  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='first/')
  date = models.DateTimeField(default= timezone.now)
  type = models.CharField(max_length=2,choices=product_choice)

  def __str__(self):
    return self.name