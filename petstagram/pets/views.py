from django.shortcuts import render, redirect

# Create your views here.
from functions.clean_up import clean_up_files
from pets.forms.comment_form import CommentForm

from pets.forms.pet_form import PetForm
from pets.models import Pet, Like, Comment


def pets_list(request):
    content = {
        'pets': Pet.objects.all()
    }
    return render(request, 'pet_list.html', content)


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


def details_or_comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':

        content = {
            'pet': Pet.objects.get(pk=pk),
            'form': CommentForm,

        }
        return render(request, 'pet_detail.html', content)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                text=form.cleaned_data['text'],

            )
            comment.pet = pet

            comment.save()
            return redirect('pet details or comment', pk)

        context = {
            'pet': pet,
            'form': form
        }

        return render(request, 'pet_detail.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like()
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
            'pet': pet
        }
        return render(request, 'pet_delete.html', context)

    else:
        pet.delete()
        return redirect('pets list')
