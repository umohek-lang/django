from django.shortcuts import render, redirect
# importing user creation forms for authentication
from django.contrib.auth.forms import UserCreationForm

# importing the userupdate form
from .form import UserUpdateForm
# Create your views here.


def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={'form':form}
    return render(request, 'users/signup.html', context)


def logoutconfirm(request):
    return render(request, 'users/logoutconfirm.html')


# Create User Profile here.
def profile(request):
    form = UserUpdateForm(instance=request.user) 

    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'users/profile.html', context)