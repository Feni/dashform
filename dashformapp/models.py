from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Collections(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

# Essentially a table - a view into a slice of data
class DataViews(models.Model):
    name = models.CharField(max_length=60)    
    collection = models.ForeignKey("Collections")

    def __unicode__(self):
        return self.name

class Fields(models.Model):
    TYPE_BOOLEAN = "BOOL"
    TYPE_NUMBER = "NUM"
    TYPE_TEXT = "TXT"

    CHOICES_TYPE = (
        (TYPE_BOOLEAN, 'Boolean'),
        (TYPE_NUMBER, 'Number'),
        (TYPE_TEXT, 'Text')
    )

    name = models.CharField(max_length=60)
    datatype = models.CharField(choices=CHOICES_TYPE, max_length=10)
    view = models.ForeignKey("DataViews")
    hidden = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class Data(models.Model):
    collection = models.ForeignKey("Collections")
    json = JSONField()
