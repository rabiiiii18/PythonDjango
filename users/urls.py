from django.urls import path
from .views import landing,loginUser,logoutUser

app_name="users"
urlpatterns = [
    path('register/',landing,name="landing"),
    path('login/',loginUser,name="loginUser"),
    path('logout/',logoutUser,name="logoutUser"),
    
   
]
