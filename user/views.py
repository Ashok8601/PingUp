from django.shortcuts import render,HttpResponse
from user.models import Chat,ChatMember,Message,MessageStatus,Reaction,Pinguser
from django.contrib.auth.hashers import make_password,check_password
def signup(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        mobile=request.POST.get("mobile")
        password=request.POST.get("password")
        pin= request.POST.get("pin")
        if not mobile or not password or not pin:
            return HttpResponse("please enter mobile password pin ")
        hashed_pass=make_password(password)
        user=Pinguser.objects.create(name=name,mobile=mobile,email=email,password=hashed_pass,pin=pin)
        user.save() 
        return HttpResponse("signup successful")    
    return render(request,"signup.html")    