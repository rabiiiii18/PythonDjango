"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import homepage,create,particularData,contact,deleteData,updateData,aboutus


app_name="crud"
urlpatterns = [
    path("",homepage,name="home"),
    path("about/",aboutus,name="about"),
    path("create/",create,name="create"),
    path("<int:id>",particularData,name="particular"),
    path("delete/<int:id>",deleteData,name="delete"),
    path("update/<int:id>",updateData,name="update"),

    path("contacts/",contact,name="contacts"),
]
