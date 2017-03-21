from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def hello(request):
	dataview = DataViews.objects.first()
	return render(request, 'index.html', {'dataview': dataview})

# db.schema_view.insert_one({"notebook": "testnb", "view": "testview", "fields":["fieldone"]})
def addField(request):
	# field_name = request.POST["name"]
	pass
