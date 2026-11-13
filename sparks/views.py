from django.shortcuts import render
from .models import Spark

def sparks(request):
    sparks = Spark.objects.all()
    context = {'sparks': sparks}
    return render(request, 'sparks/sparks.xhtml', context) 
