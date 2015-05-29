from django.conf.urls import include, url
from django.contrib import admin
from .views import IndexView, TestView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^test/$', TestView.as_view(), name='test'),
	# url(r'^preguntar/$', QuestionCreateView.as_view(), name='create_question'),
]