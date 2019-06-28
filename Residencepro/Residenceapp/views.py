from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Register
from.forms import ResidenceForm,Loginform
from django.contrib.auth import authenticate
def home(request):
    if request.method=='POST':
         rform = ResidenceForm(request.POST)
         if rform.is_valid():
             username = request.POST.get('username','')
             email = request.POST.get('email','')
             password = request.POST.get('password','')
             confirm_password = request.POST.get('confirm_password','')
             data = Register(
                 username=username,
                 email=email,
                 password=password,
                 confirm_password=confirm_password
             )
             data.save()
             rform = ResidenceForm()
             return render(request,'Register.html',{'rform':rform})
    else:
        rform = ResidenceForm()
        return render(request,'Register.html',{'rform':rform})

def login(request):
    if request.method == 'POST':
        lform=Loginform(request.POST)
        if lform.is_valid():
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = Register.objects.filter(username=username , password=password)
            if not user:
                return HttpResponse('Invalid user')
            else:
                return HttpResponse('Login successfully')
        lform = Loginform()
        return render(request, 'login.html', {'lform': lform})
    else:
        lform = Loginform()
        return render(request, 'login.html', {'lform': lform})


        '''if user is not None:
            n='<h1> login successfully'
            return HttpResponse(n)
        else:
                c='<h1> username and password wrong'
                return HttpResponse(c)
'''

