from django.shortcuts import render, redirect
from stock.models import Income, Expense, TempExpense
from account_control.models import UserStart
from .create import create, edit
from account_control.scripts.script import is_superior


def CreateView(request, pk):
    content = {
        'popup': 'popup_statement',
        'form': pk
    }
    if request.POST:
        result = create(request)
        if result == 'success-income':
            return redirect('stock:list_statement',1)
        elif result == 'success-expense':
            return redirect('stock:list_statement',2)
        elif result == 'success-temp':
            return redirect('stock:list_statement',3)
        else:
            content['message'] = result
    return render(request, 'stock/statement/create.html', content)


def EditView(request, form, pk):
    content = {
        'form': form
    }
    if not is_superior(request):
        return redirect('account_control:permit_denied')
    if form == 1:
        if Income.objects.filter(id=pk).count() == 0:
            return redirect('stock:list_statement',form=1)
        else:
            content["statement"] = Income.objects.get(id=pk)
    if form == 2:
        if Expense.objects.filter(id=pk).count() == 0:
            return redirect('stock:list_statement',form=2)
        else:
            content["statement"] = Expense.objects.get(id=pk)
    if form == 3:
        if TempExpense.objects.filter(id=pk).count() == 0:
            return redirect('stock:list_statement',form=3)
        else:
            content["statement"] = TempExpense.objects.get(id=pk)
    if request.POST:
        result = edit(request)
        if result == 'updated' or result == 'deleted':
            return redirect('stock:list_statement',form=form)
        else:
            content['message'] = result
    return render(request, 'stock/statement/edit.html', content)


def ListView(request, form):
    content = {
        'form': form,
        'title': 'hello'
               }
    worker = UserStart.objects.get(username=request.user)
    if form == 1:
        data = Income.objects.filter(date_log__gt=worker.date_log)
        content['lists'] = data
    elif form == 2:
        data = Expense.objects.filter(date_log__gt=worker.date_log)
        content['lists'] = data
    elif form == 3:
        data = TempExpense.objects.filter(date_log__gt=worker.date_log)
        content['lists'] = data
    return render(request, 'stock/statement/list.html', content)

