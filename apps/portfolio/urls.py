from django.urls import path
from apps.portfolio.views import HomeView  # , ProjectDetailView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    #path('project/<slug:slug>', ProjectDetailView.as_view(), name='project_detail')
]
