from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
	# return HttpResponse("Hello World")
	return render(request, 'index.html')

# db.schema_view.insert_one({"notebook": "testnb", "view": "testview", "fields":["fieldone"]})
def addField(request):
	# field_name = request.POST["name"]
	pass
