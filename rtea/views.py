from django.shortcuts import render
from django.http import HttpResponse

def tea(request):
   return render(request, 'tea.html')
