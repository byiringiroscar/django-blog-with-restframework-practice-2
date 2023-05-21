from django.db import models
import datetime


# Create your models here.

class Statistic(models.Model):
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    goals = models.IntegerField()
    assists = models.IntegerField()
    player_image = models.ImageField(blank=True, null=True, upload_to='images/')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Statistic"
        ordering = ['id']


class Comment(models.Model):
    post = models.ForeignKey(Statistic, related_name="comments", on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=250)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post, self.name)


