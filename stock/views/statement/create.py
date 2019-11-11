from stock.models import Income, Expense
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
    else:
        result['message'] = 'select type'
    return result


def edit(request):
    id = request.POST['income_id']
    value = request.POST['value']
    if value == '':
        return 'Amount is not valid'
    if int(value) < 0:
        return 'Amount is not valid'
    if 'DELETE' in request.POST:
        if check_password(request):
            Income.objects.get(id=id).delete()
            return 'deleted'
        return 'password is not correct'
    else:
        update = Income.objects.get(id=id)
        update.value = int(value)
        update.save()
        return 'updated'


def editexpense(request):
    id = request.POST['expense_id']
    value = request.POST['value']
    if value == '':
        return 'Amount is not valid'
    if int(value) < 0:
        return 'Amount is not valid'
    if 'DELETE' in request.POST:
        if check_password(request):
            Expense.objects.get(id=id).delete()
            return 'deleted'
        return 'password is not correct'
    else:
        update = Expense.objects.get(id=id)
        update.value = int(value)
        update.save()
        return 'updated'


def check_password(request):
    if User.objects.get(username=request.user). \
            check_password(request.POST.get('form_verifypwd')):
        return True
    return False
