from stock.models import Income, Expense,TempExpense
from django.utils import timezone
from django.contrib.auth.models import User


def create(request):
    name = request.POST['name']
    value = request.POST['value']
    record_type = request.POST['type']
    result = {}
    if value == '' or name == '':
        result['message'] = 'name and amount cannot be empty!!'
        return result
    elif int(value) <= 0:
        return {'message': 'amount format is wrong!!'}
    if record_type == '1':
        Income(name=name, value=value, date_log=timezone.now()).save()
        return 'success-income'
    elif record_type == '2':
        Expense(name=name, value=value, date_log=timezone.now()).save()
        return 'success-expense'
    elif record_type == '3':
        TempExpense(name=name, value=value, date_log=timezone.now()).save()
        return 'success-temp'
    else:
        result['message'] = 'select type'
    return result


def edit(request):
    item = None
    id = request.POST['statement_id']
    value = request.POST['value']
    if value == '':
        return 'Amount is not valid'
    if request.POST.get('form') == '1':
        item = Income.objects.get(id=id)
    if request.POST.get('form') == '2':
        item = Expense.objects.get(id=id)
    if request.POST.get('form') == '3':
        item = TempExpense.objects.get(id=id)

    if int(value) < 0:
        return 'Amount is not valid'
    if 'DELETE' in request.POST:
        if check_password(request):
            item.delete()
            return 'deleted'
        return 'password is not correct'
    else:
        item.value = int(value)
        item.save()
        return 'updated'


def check_password(request):
    if User.objects.get(username=request.user). \
            check_password(request.POST.get('form_verifypwd')):
        return True
    return False
