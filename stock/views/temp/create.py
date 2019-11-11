from stock.models import TempExpense
from django.utils import timezone
from django.contrib.auth.models import User


def create(request):
    name = request.POST['name']
    value = request.POST['value']
    if value == '' or name == '':
        return 'name and amount cannot be empty!!'
    elif int(value) <= 0:
        return 'amount format is wrong!!'
    TempExpense(name=name, value=value, date_log=timezone.now()).save()
    return 'success'


def edit(request):
    id = request.POST['temp_id']
    value = request.POST['value']
    if value == '':
        return 'Amount is not valid'
    if int(value) < 0:
        return 'Amount is not valid'
    if 'DELETE' in request.POST:
        if check_password(request):
            TempExpense.objects.get(id=id).delete()
            return 'deleted'
        return 'password is not correct'
    else:
        update = TempExpense.objects.get(id=id)
        update.value = int(value)
        update.save()
        return 'updated'


def check_password(request):

    if User.objects.get(username=request.user). \
            check_password(request.POST.get('form_verifypwd')):
        return True
    return False
