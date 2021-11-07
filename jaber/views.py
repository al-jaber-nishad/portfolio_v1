from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):

  title = Title.objects.latest('updated')
  about = About.objects.latest('updated')
  category = Category.objects.all()
  skills = Skills.objects.all()
  projects = Projects.objects.all()
  social = Social.objects.latest('updated')
  
  context = {
    'title' : title,
    'about' : about,
    'category' : category,
    'skills' : skills,
    'projects' : projects,
    'social' : social,


  }

  return render(request, 'index.html', context)