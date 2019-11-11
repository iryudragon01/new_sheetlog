from stock.models import Item
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
def create(request):
    empty = check_emtpy([request.POST.get('name'),
                                request.POST.get('price'),
                                request.POST.get('type')])

    if empty:
        return 'Invalid form ,Form cannot be empty'
    itemexist = Item.objects.filter(name=request.POST.get('name')).count()
    if itemexist == 0:
        newitem = Item(name=request.POST.get('name'),
                       price=int(request.POST.get('price')),
                       type=int(request.POST.get('type')),
                       )
        newitem.save()
        return 'success'
    return 'Item is exist'


def edit(request, pk):
    if 'DELETE' in request.POST:
        if request.POST.get('form_verifypwd') == '46503888':
            del_item = Item.objects.get(id=pk)
            del_item.delete()
            return 'success'
        return 'password is not correct'
    else:
        update_item = Item.objects.get(id=pk)
        update_item.price = request.POST.get('price')
        update_item.type = request.POST.get('type')
        update_item.save()
        return 'success'

def check_emtpy(strings):
    for string in strings:
        print(string,'forloop.counter')
        if string == '' or string == None :
            return True

    return False
