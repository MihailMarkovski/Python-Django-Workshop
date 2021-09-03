from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import RegisterForm, UserProfileForm
from accounts.models import UserProfile


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'user': user,
            'profile': user.userprofile,
            'pets': user.userprofile.pet_set.all(),
            'form': UserProfileForm
        }

        return render(request, 'accounts/user_profile.html', context)
    else:
        form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()

            return redirect('current profile user')

        return redirect('current profile user')




def register(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm
        }

        return render(request, 'accounts/register.html', context)
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(user=user)

            profile.save()
            login(request, user)

            return redirect('pets list')

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)



def logout_user(request):
    logout(request)
    return redirect('index')