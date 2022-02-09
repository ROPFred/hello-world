from django.shortcuts import render
from .models import Project # Project is the database name

# Create your views here.
def home(request):
    projects = Project.objects.all()   # this grab all objects
    return render(request, 'portfolio/home.html', {'projects':projects})