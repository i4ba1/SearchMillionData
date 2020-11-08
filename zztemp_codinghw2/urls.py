from django.conf.urls import url
from zztemp_codinghw2 import views
from django.urls import path

urlpatterns = [
    # url(r'^api/zztemp_codinghw2$', views.search_query),
    path('search_query/<str:text>', views.search_query, name="search_query"),
    # url(r'^api/zztemp_codinghw2/published$', views.tutorial_list_published)
]
