from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import FormView
from django.views.generic.base import ContextMixin
from django.views.generic import *
from django.shortcuts import *
from .models import *
from .forms import *


class ApplicationContext(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(ApplicationContext, self).get_context_data(**kwargs)
        context['tables'] = DashTable.objects.all()
        return context


class TableContext(ApplicationContext, ContextMixin):
    def get_table(self):
        if not hasattr(self, "_table"):
            self._table = DashTable.objects.get(id=self.kwargs['table_id'])
        return self._table

    def get_context_data(self, **kwargs):
        context = super(TableContext, self).get_context_data(**kwargs)
        context["table"] = self.get_table()
        return context

class TableForm(FormView):

    def get_success_url(self):
        return self.get_table().get_absolute_url()

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.table = self.get_table()
        obj.save()
        return HttpResponseRedirect(self.get_success_url())


# Create your views here.
def hello(request):
    return redirect('/create')


class DashTableView(TableContext, DetailView):
    model = DashTable
    pk_url_kwarg = 'table_id'


class CreateTableView(ApplicationContext, CreateView):
    model = DashTable
    fields = ["name"]

class CreateFieldView(TableContext, TableForm, CreateView):
    model = DashField
    fields = ["name", "datatype"]

class DataViewAdd(TableContext, FormView):
    template_name = 'dashformapp/dataviews_form.html'

    def get_fields(self):
        # return list(self.get_dataview().fields_set.all().values_list("name", flat=True))
        return list(self.get_table().dashfield_set.all())

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
        table = self.get_table()
        newrow = DashEntry(table=table, json=json_form)
        newrow.save()
        return redirect("/")