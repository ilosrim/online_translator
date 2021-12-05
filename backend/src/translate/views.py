from django.shortcuts import render
from django.http import HttpResponse
from .models import Dictionaries

def index(request):
  word = request.GET.get('q', '')
  if word and word!= '':
    result = Dictionaries.objects.filter(inglizcha__contains=word).all()[:3]
  else:
    result = None
  
  return render(request, 'index.html', {'q': word, 'result': result})