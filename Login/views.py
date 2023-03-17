from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def create(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        object = User.objects.create_user(username = username, password = password, first_name = f_name, last_name = l_name)
        object.save()
    return render(request,"index.html")


def retrieve(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            print("Authentication Success")
        else:
            print("Not an authorized user")
    return render(request,"retrieve.html")

