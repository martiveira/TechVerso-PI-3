from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'vagas'

urlpatterns = [
    path("", views.index, name="index"),
    path('create/', views.create_job_post, name='create'),
    path('list/', views.list_job_posts, name='lista'),
    path('example/', TemplateView.as_view(template_name='example_template.html'), name='example'),
]