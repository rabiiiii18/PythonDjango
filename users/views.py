from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def landing(request):
    if request.method == "POST":
        name = request.POST.get("name")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        Email = request.POST.get("email")
        Password = request.POST.get("password")
        ConfirmPassword = request.POST.get("ConfirmPassword")

        if Password==ConfirmPassword:
            user=User.objects.create_user(
                username=name,
                first_name=firstname,
                last_name=lastname,
                email=Email,
                password=Password,
            )
            user.save()
            return redirect("crud:home")
        else:
            print("user validation failed")
        
    return render(request,"user/register.html")

def loginUser(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            username=request.POST.get("name")
            password=request.POST.get("password")
            user=authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect("crud:home")
            else:
                return redirect("users:sigin")
        return render(request,"user/login.html")
    else:
        return redirect("crud:home")



@login_required 
def logoutUser(request):
    logout(request)
    return redirect("crud:home")