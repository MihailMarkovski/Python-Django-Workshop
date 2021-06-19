from django.shortcuts import render, redirect

from app.forms.expenses import ExpensesForm, DisForm
from app.models import Expense


def create_expense(request):
    if request.method == 'GET':
        context = {
            'form': ExpensesForm
        }
        return render(request, 'expense_create.html', context)
    else:
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('index')

        context = {
            'form': form
        }
        return render(request, 'expense_create.html', context)


def edit_expense(request, pk):
    expenses = Expense.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'expense': expenses,
            'form': ExpensesForm(instance=expenses),
        }

        return render(request, 'expense_edit.html', context)
    else:
        form = ExpensesForm(request.POST, instance=expenses)
        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'expense': expenses,
            'form': form,
        }

        return render(request, 'expense_edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'expense': expense,
            'form': DisForm(instance=expense)
        }

        return render(request, 'expense_delete.html', context)
    else:
        expense.delete()
        return redirect('index')

#
