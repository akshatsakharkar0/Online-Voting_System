from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('electionlist/', views.election_list, name='election_list'),
    path('vote/<int:election_id>/', views.vote, name='vote'),
    path('results/<int:election_id>/', views.results_view, name='results'),

]
