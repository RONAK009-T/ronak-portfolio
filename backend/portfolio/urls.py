from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('project/<slug:slug>/', views.project_detail_view, name='project_detail'),
    path('api/launch/<slug:slug>/', views.start_project_api, name='start_project'),
    path('api/stop/<slug:slug>/', views.stop_project_api, name='stop_project'),
    path('api/generate/excel/', views.generate_excel_api, name='generate_excel'),
    path('api/generate/ppt/', views.generate_ppt_api, name='generate_ppt'),
]
