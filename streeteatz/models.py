from django.db import models

# Create your models here.
class Vendor(models.Model):
  name = models.CharField(max_length = 20)
  phone_number = models.CharField(max_length = 11)
  location = models.CharField(max_length = 200)
  address = models.CharField(max_length = 200)
  status = models.BooleanField(default = False)
  hours = models.CharField(max_length = 200)
  description = models.CharField(max_length = 200)
  tags = models.CharField(max_length = 200)
  website = models.CharField(max_length = 200)
  img = models.CharField(max_length = 200)
  wait_time = models.IntegerField()
  upvote = models.BooleanField(default = False)
  downvote = models.BooleanField(default = False)
  favorited = models.BooleanField(default = False)
  up_rating = models.IntegerField(default=0)
  down_rating = models.IntegerField(default=0)

  def __str__(self):
    return self.name
  