from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from functions.clean_up import clean_up_files
from pets.forms.comment_form import CommentForm

from pets.forms.pet_form import PetForm
from pets.models import Pet, Like, Comment


def pets_list(request):
    context = {
        'pets': Pet.objects.all(),
    }
    return render(request, 'pet_list.html', context)


@login_required
def create_pet(request):
    pet = Pet()
    if request.method == 'GET':
        form = PetForm(instance=pet)
        context = {
            'form': form,
            'pet': pet,

        }

        return render(request, 'pet_create.html', context)
    else:
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pets list')

    context = {
        'form': form,
        'pet': pet,

    }

    return render(request, 'pet_create.html', context)


@login_required
def details_or_comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':

        context = {
            'pet': pet,
            'form': CommentForm,
            'can_delete': request.user == pet.user.user,
            'can_edit': request.user == pet.user.user,
            'has_liked': pet.like_set.filter(user_id=request.user.userprofile.id).exists(),
            'can_like': request.user == pet.user.user,

        }
        return render(request, 'pet_detail.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.pet = pet
            comment.user = request.user.username
            comment.save()
            return redirect('pet details or comment', pk)

        context = {
            'pet': pet,
            'form': form
        }

        return render(request, 'pet_detail.html', context)


def like_pet(request, pk):
    like = Like.objects.filter(user_id=request.user.userprofile.id, pet_id=pk).first()
    if like:
        like.delete()
    else:
        pet = Pet.objects.get(pk=pk, )
        like = Like(str(pk), user=request.user.userprofile)
        like.pet = pet
        like.save()
        return redirect('pet details or comment', pk)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        form = PetForm(instance=pet)
        context = {
            'form': form,
            'pet': pet,

        }

        return render(request, 'pet_edit.html', context)

    else:
        old_img = pet.image_url
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            clean_up_files(old_img.path)
            form.save()

            return redirect('pet details or comment', pet.pk)

    context = {
        'form': form,
        'pet': pet,

    }

    return render(request, 'pet_edit.html', context)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':

        context = {
            'pet': pet,

        }
        return render(request, 'pet_delete.html', context)

    else:
        pet.delete()
        return redirect('pets list')
