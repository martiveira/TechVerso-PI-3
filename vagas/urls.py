from django.urls import path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.index, name="vagas"),
    path('create/', views.create_job_post, name='create'),
    path('list/', views.list_job_posts, name='list'),

]
urlpatterns += [
    path('example/', TemplateView.as_view(template_name='example_template.html'), name='example'),
]