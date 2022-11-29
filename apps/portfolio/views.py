import logging
from django.views.generic import ListView, DetailView

from apps.portfolio.models import ProjectModel

logger = logging.getLogger(__name__)


class HomeView(ListView):
    model = ProjectModel
    template_name = "home.html"
    queryset = ProjectModel.objects.filter(is_active=True)


# class ProjectDetailView(DetailView):
#     model = ProjectModel
#     template_name = 'projectDetail.html'
#     slug_field = 'slug'
