from django.shortcuts import render

from django.views.generic.base import TemplateView

from django.http import HttpResponse 
import datetime

def index(request):
	return HttpResponse("Hello Humans")


def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('index.html')

class HomeView(TemplateView):
	template_name = 'index.html'