from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

TEMPLATES_DIRS = (
	'os.path.join(BASE_DIR,"templates")'
)

def index(request):
	return render(request, "index.html")

def calendar(request):
	return render(request, "calendar.html")

def estadisticas(request):
	return render(request, "estadisticas.html")

def ayuda(request):
	return render(request, "ayuda.html")

def login(request):
	return render(request, "login.html")
