from django.shortcuts import render

from .models import RegisterData

from .forms import RegisterForm,LoginForm
from django.http import HttpResponse
from django.contrib import messages

def Register_View(request):
    if request.method=='POST':
        rform=RegisterForm(request.POST)
        if rform.is_valid():
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            username=request.POST.get('username')
            password=request.POST.get('password')
            mobile=request.POST.get('mobile')

            data=RegisterData(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                mobile=mobile
                
                )
            data.save()
            rform=RegisterForm()
            context={'form':rform}
            return render(request,'Reg_App/index.html',context)

    else:
        rform=RegisterForm()
        context={'form':rform}
        return render(request,'Reg_App/index.html',context)

def login_view(request):
    if request.method=='POST':
        lform=LoginForm(request.POST)
        if lform.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=RegisterData.objects.filter(username=username,password=password)

            if not user:
                messages.warning(request,'Incorrect Username or Password')

                lform=LoginForm()
                context={'form':lform}
                return render(request,'Reg_App/login.html',context)
            else:
                return HttpResponse('Login Sucess')

    lform=LoginForm()
    context={'form':lform}
    return render(request,'Reg_App/login.html',context)

