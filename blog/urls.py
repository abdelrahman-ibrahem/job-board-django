from django.urls import path 
from . import views
app_name = "blogs"
urlpatterns = [
    path('', views.blog_post , name="blog"),
    path('single_blog/', views.single_blog_post , name="single_blog")
]
