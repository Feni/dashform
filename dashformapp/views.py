from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import FormView
from django.views.generic.base import ContextMixin
from django.views.generic import *
from django.shortcuts import *
from .models import *
from .forms import *

class CollectionContext(ContextMixin):
    def get_collection(self):
        if not hasattr(self, "_collection"):
            # self._collection = Collections.objects.get(id=self.kwargs["collection_id"])
            self._collection = Collections.objects.first()
        return self._collection

    def get_context_data(self, **kwargs):
        context = super(CollectionContext, self).get_context_data(**kwargs)
        context["collection"] = self.get_collection()
        return context


class DataViewContext(ContextMixin):
    def get_dataview(self):
        if not hasattr(self, "_dataview"):
            self._dataview = DataViews.objects.first()
        return self._dataview

    def get_context_data(self, **kwargs):
        context = super(DataViewContext, self).get_context_data(**kwargs)
        context["dataview"] = self.get_dataview()
        return context



# Create your views here.
def hello(request):
    dataview = DataViews.objects.first()
    return render(request, 'index.html', {'dataview': dataview})

class DataViewDetail(CollectionContext, DataViewContext, DetailView):
    model = DataViews
    pk_url_kwarg = 'dataview_id'

class DataViewAdd(CollectionContext, DataViewContext, FormView):
    template_name = 'dashformapp/dataviews_form.html'

    def get_fields(self):
        # return list(self.get_dataview().fields_set.all().values_list("name", flat=True))
        return list(self.get_dataview().fields_set.all())

    def get_form(self, form_class=None):
        print "get form "
        kwargs = self.get_form_kwargs()
        json_fields=self.get_fields()
        kwargs["json_fields"] = json_fields
        print self.request.POST
        return DataEntryForm(self.request.POST or None, json_fields=json_fields)

    def form_to_json(self, form):
        print "form to json "
        fields = self.get_fields()
        values = {}
        for field in form.fields:
            if field.startswith("json_"):
                field_id = str(field.replace("json_", ""))
                # field_name = fields[field_id]
                # values[field_name] = form.cleaned_data[field]
                values[field_id] = form.cleaned_data[field]
        return values

    def form_valid(self, form):
        print "Form valid " + str(form)
        json_form = self.form_to_json(form)
        collection = self.get_collection()
        newrow = Data(collection=collection, json=json_form)
        newrow.save()
        return redirect("/")