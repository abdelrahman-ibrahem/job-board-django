from django.urls import path 
from . import views
app_name = "jobs"
urlpatterns = [
    path('',views.jobs , name="jobs"),
    path('add_job/',views.add_job , name='add_job'),
    path('<int:id_number>' , views.job_details , name="job_detail")
]
