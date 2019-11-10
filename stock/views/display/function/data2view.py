from django.db.models import Sum
from django.utils import timezone
from stock.models import Item, TopUp, LogSheet
from . import calculater, statement as statementfile
from account_control.scripts.script import user_superior


def getdisplay(log_sheets_start, log_sheets_end, date_statement_end):
    ListFirst = []
    ListEnd = []
    ListVolume = []
    ListMoney = []
    ListSum = []
    Sum_temp = 0
    top_ups = TopUp.objects.filter(date_log__gt=log_sheets_start[0].date_log, date_log__lt=date_statement_end)
    items = Item.objects.all()
    for item in items:
        sheet_start = 0
        sheet_end = 0
        if log_sheets_start.filter(item=item).count() == 1:
            if item.type == 1:
                sheet_start = log_sheets_start.get(item=item).value
            if item.type == 2:
                sheet_start = 0
            if item.type == 3:
                sheet_start = log_sheets_start.get(item=item).value
        if item.type == 3:
            item_top_ups = top_ups.filter(item=item).aggregate(Sum('value'))
            sum_top_up = item_top_ups['value__sum']
            if sum_top_up:
                sheet_start += int(sum_top_up)
            else:
                sheet_start += 0
        ListFirst.append(sheet_start)

        if log_sheets_end.filter(item=item).count() == 1:
            if item.type == 2:
                if log_sheets_start.filter(item=item):
                    if log_sheets_end.get(item=item):
                        sheet_end = log_sheets_end.get(item=item).value - log_sheets_start.get(item=item).value
                else:
                    if log_sheets_end.filter(item=item):
                        sheet_end = log_sheets_end.get(item=item).value
            else:
                sheet_end = log_sheets_end.get(item=item).value
        ListEnd.append(sheet_end)

        # call function from other file
        ListVolume.append(calculater.volume_sale(item, sheet_start, sheet_end))
        ListMoney.append(calculater.item_money(item, sheet_start, sheet_end))
        Sum_temp += calculater.item_money(item, sheet_start, sheet_end)
        ListSum.append(Sum_temp)
    statement = statementfile.getstatement(log_sheets_start[0].date_log, date_statement_end)
    get_top_up = gettopup(top_ups=top_ups, logsheet=log_sheets_start)
    is_display_reset = '0'

    content = {'items': zip(items, ListFirst, ListEnd, ListVolume, ListMoney, ListSum),
               'top_ups': get_top_up,
               'incomes': statement['incomes'],
               'expenses': statement['expenses'],
               'temps': statement['temps'],
               'is_Display_reset': is_display_reset,
               }
    Sum_temp = statement['sum_income'] + Sum_temp
    content['sum_income'] = Sum_temp
    Sum_temp = -statement['sum_expense'] + Sum_temp
    content['sum_expense'] = Sum_temp
    Sum_temp = -statement['sum_temp'] + Sum_temp
    content['sum_temp'] = Sum_temp

    return content
#  End get display


# get topup
def gettopup(top_ups, logsheet):
    ListTop = []
    items = Item.objects.filter(type=3)
    list_row = ['name']
    for name in items:
        list_row.append(name.name)
    ListTop.append(list_row)
    list_sheet = ['date']
    for getvalue in items:
        sheet = 0
        if logsheet.filter(item=getvalue).count() == 1:
            sheet = logsheet.get(item=getvalue).value
        list_sheet.append(sheet)
    ListTop.append(list_sheet)
    if not top_ups.last():  # check if top_up is exist ?
        return ListTop
    top_last = top_ups.last().version
    for loop in range(top_last + 1):
        if top_ups.filter(version=loop).count() > 0:
            row_top = top_ups.filter(version=loop)
            top_data = ['']
            for item in items:
                data_item = ''
                if row_top.filter(item=item).count() == 1:
                    data_item = row_top.get(item=item).value
                    top_data[0] = row_top.get(item=item).date_log  #
                top_data.append(data_item)
            ListTop.append(top_data)
    return ListTop


# start set display
def setdisplay(request):
    items = Item.objects.all()
    log_sheet_last = LogSheet.objects.last()
    current_time = timezone.now()
    for item in items:
        new_log_sheet = LogSheet(item=item,
                                 version=log_sheet_last.version + 1,
                                 value=request.POST.get(item.name),
                                 date_log=current_time)
        new_log_sheet.save()

    user_superior(request)  # update account_manager start
    return calculater.normal_get_log(request)
