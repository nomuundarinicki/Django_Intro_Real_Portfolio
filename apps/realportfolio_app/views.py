from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
def index(request):

    return render (request,'realportfolio_app/index.html')

def about(request):

    return render (request,'realportfolio_app/about.html')

def projects(request):

    return render (request,'realportfolio_app/project.html')

def testimonials(request):

    return render (request,'realportfolio_app/testimonial.html')
