from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    STATUS =(('new','new'),('used','used'),('very_old','very_old'))
    title = models.CharField(max_length=50)
    isbn =models.IntegerField(max_length=13,unique=True)
    author_name = models.CharField(max_length=20)
    edition_number = models.IntegerField(max_length=13)
    publication_date = models.DateField()
    status = models.CharField(max_length=10,choices=STATUS)
    fees=models.DecimalField(max_digits=6, decimal_places=2)
    link = models.URLField()
    renter = models.ForeignKey(User)

    def __unicode__(self):
        return self.title  