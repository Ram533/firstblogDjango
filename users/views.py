from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, UserUpdateForm, UserUpdateProfile
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been Created! You are now able to Sign In')
            return redirect('loginpage')
    else :
        form = RegisterForm()
    return render(request,'users/register.html',{'form' : form, 'title' : 'Register' })

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = UserUpdateProfile(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            messages.success(request, f'Your Profile has been updated!')
            return redirect('profilepage')
        
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = UserUpdateProfile(instance=request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form,
        'title' : 'Profile'
    }
    return render(request,'users/profile.html',context)