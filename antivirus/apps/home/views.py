from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
	template_name = 'home/index.html'

class TestView(TemplateView):
	template_name = 'home/test.html'
