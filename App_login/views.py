from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import HttpResponseRedirect,reverse
from django.contrib.auth.decorators import login_required

def sign_up(request):
    form = UserCreationForm()
    registered = False
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {'form':form , 'registered':registered}
    return render(request,'App_login/sign_up.html',context=dict)

def login_user(request):
    form = AuthenticationForm()
    if request.method =="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username , password = password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
    return render(request,'App_login/login.html', context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
