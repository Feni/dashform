from django.forms import *

from dashformapp.models import DashField


class DataEntryForm(Form):
    def __init__(self, *args, **kwargs):
        json_fields = kwargs.pop('json_fields')
        super(DataEntryForm, self).__init__(*args, **kwargs)

        for i, field in enumerate(json_fields):
            if field.datatype == DashField.TYPE_BOOLEAN:
                dj_field = BooleanField(label=field.name)
            elif field.datatype == DashField.TYPE_NUMBER:
                dj_field = IntegerField(label=field.name) # TODO: int vs float
            else:
                dj_field = CharField(label=field.name)
            self.fields['json_%s' % field.id] = dj_field
        print(self.fields)
