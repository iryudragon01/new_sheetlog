from django.shortcuts import render, redirect
from stock.models import Item, TopUp
from stock.views.Top_up.Data2View import list, top_up, edit
from account_control.scripts.script import is_superior


def Top_up_View(request):
    content = {'items': Item.objects.filter(type=3)}
    if request.POST:
        top_up(request)
        return redirect('stock:list_top_up')
    return render(request, 'stock/top_up/create.html', content)


def Top_up_List_View(request):
    content = list(request)
    return render(request, 'stock/top_up/list.html', content)


def Top_up_Edit_View(request, pk):
    if not is_superior(request):
        return redirect('account_control:permit_denied')
    if TopUp.objects.filter(id=pk).count() == 1:
        content = {'top_up': TopUp.objects.get(id=pk)}
        if request.POST:
            result = edit(request, pk)
            if result == 'success':
                return redirect('stock:list_top_up')
            else:
                content['message'] = result
        return render(request, 'stock/top_up/edit.html', content)
    return redirect('stock:list_top_up')
