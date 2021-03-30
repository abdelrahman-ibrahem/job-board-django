from django.urls import path 
from . import views
app_name = "logins"
urlpatterns = [
    path('' , views.signIn , name="signin"),
    path('signup/' , views.signUp , name="signup"),
    path('logout/' , views.Logout_view , name="logout")
    #  path('profile/edit',views.profile_edit , name='profile_edit'),
]
