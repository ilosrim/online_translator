from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  word = request.GET.get('q', '')
  return render(request, 'index.html', {'q': word})