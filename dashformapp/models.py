from django.db import models
from django.contrib.postgres.fields import JSONField


class DashTable(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/%d" % (self.id)


class DashField(models.Model):
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
    table = models.ForeignKey("DashTable")

    def __unicode__(self):
        return self.name


class DashEntry(models.Model):
    table = models.ForeignKey("DashTable")
    json = JSONField()

    def get_absolute_url(self):
        return "/%d/%d" % (self.table.id, self.id)