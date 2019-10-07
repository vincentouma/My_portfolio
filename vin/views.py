from django.shortcuts import render
from django.http  import HttpResponse
from django.shortcuts import get_object_or_404
from tinymce.models import HTMLField
from django.core.exceptions import ObjectDoesNotExist
from .models import *

# Create your views here.
def home(request):

    return render(request,'home.html')

def all_project(request):

    all_project = Project.fetch_all_images()


    return render(request,"all_project.html",{"all_project":all_project})


def about(request):

    return render(request,"about.html")


def skill(request):

    all_skill = Skill.fetch_all_images()
    
    return render(request,"skill.html",{"all_skill":all_skill})


def contact(request):

    return render(request,"contact.html")