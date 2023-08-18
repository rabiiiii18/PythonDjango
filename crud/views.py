from django.shortcuts import redirect, render
from .models import Blog, Contact
from .forms import BlogForm
from django.http import HttpResponse
from django.core.paginator import Paginator
from myproject.settings import EMAIL_HOST_USER 
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):

    blog = Blog.objects.all()
    paginator = Paginator(blog, 2) 

    page_number = request.GET.get("blog")
    page_obj = paginator.get_page(page_number)
    data = request.GET.get("search") 
    if data != "" and data is not None:
        searchData = Blog.objects.filter(title__contains=data)
        print(searchData)
        return render(request,"crud/index.html",{"blog":searchData})
    return render(request,"crud/index.html",{"Blogs":page_obj})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        subject="Important Message about collobration!!"
        recipient="ravi@yopmail.com",
        html_content=render_to_string('crud/email.html',{'name':name,'description':message,'mail':email})
        email=EmailMessage(
               subject,
               html_content,
               EMAIL_HOST_USER,
               recipient
           )
        email.fail_silently=False
        if email!=None:
               email.send()

        crud = Contact(
            name = name,
            email= email,
            message = message
        )
        crud.save()
        print(name)
        return redirect("crud:home")


    return render(request,"crud/contact.html")

def particularData(request,id):
    blog = Blog.objects.get(id=id)
    return render(request,"crud/post.html",{"blog":blog})

@login_required
def create(request):
    forms = BlogForm(request.POST or None)
    print(forms)
    if(forms.is_valid()):
        forms.save()
        return redirect("crud:home")
    return render(request, "crud/create.html")

def deleteData(request,id):
    deldata = Blog.objects.get(id=id)   
    deldata.delete()
    return redirect('crud:home')


def updateData(request,id):
    blog = Blog.objects.get(id=id)
    forms = BlogForm(request.POST or None,instance=blog)
    context = {
        "forms":forms,
        "title":blog.title,
        "subtitle":blog.subtitle,
        "description":blog.description
    }
    if forms.is_valid():
        forms.save()
        return redirect("crud:home")
    return render(request, "crud/create.html",context)

def aboutus(request):
    return render(request,"crud/about.html")
