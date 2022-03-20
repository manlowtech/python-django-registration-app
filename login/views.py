from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request,'logins/index.html')

def register(request):
    #form = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Account created you can now login')
            return redirect('/admin')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request,'logins/register.html',context)
