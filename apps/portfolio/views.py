import logging
from django.shortcuts import render
from django.views.generic import ListView

from apps.portfolio.models import ProjectModel

logger = logging.getLogger(__name__)


class HomeView(ListView):
    model = ProjectModel
    template_name = "home.html"
