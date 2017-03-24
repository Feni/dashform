from django.forms import *

class DataEntryForm(Form):
    def __init__(self, *args, **kwargs):
        json_fields = kwargs.pop('json_fields')
        super(DataEntryForm, self).__init__(*args, **kwargs)

        for i, field in enumerate(json_fields):
            self.fields['json_%s' % field.id] = CharField(label=field.name)
        print(self.fields)
