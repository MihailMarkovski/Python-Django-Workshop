from django.shortcuts import render, redirect

from app.forms.profiles import ProfileForm, DeleteProfile
from app.models import Profile, Expense


def profile_index(request):
    profile = Profile.objects.all()[0]
    expenses = Expense.objects.all()
    expenses_total_cost = sum(exp.price for exp in expenses)
    profile.budget_left = profile.budget - expenses_total_cost
    context = {
        'profile': profile,
        'expenses': expenses
    }

    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'GET':
        context = {
            'form': ProfileForm(),

        }

        return render(request, 'home_no_profile.html', context)

    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'form': form

        }

        return render(request, 'home_no_profile.html', context)


def edit_profile(request):
    profile = Profile.objects.get()
    if request.method == 'GET':
        context = {

            'form': ProfileForm(instance=profile),

        }
        return render(request, 'profile_edit.html', context)
    else:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile index')

        context = {

            'form': form,

        }
        return render(request, 'profile_edit.html', context)


def delete_profile(request):
    profile = Profile.objects.get()
    expenses = Expense.objects.all()
    if request.method == 'GET':
        context = {
            'profile': profile,
            'form': DeleteProfile(instance=profile)
        }
        return render(request, 'profile_delete.html', context)
    else:
        profile.delete()

        expenses.delete()
        return redirect('index')
