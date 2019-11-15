from django.urls import path
from stock.views.Item import views as item_views
from stock.views.Top_up import views as top_up_views
from stock.views.display import views as display_views
from stock.views.statement import views as statement_views
app_name = 'stock'
urlpatterns = [
    # Display
    path('',display_views.IndexView,name='index'),


    # Item
    path('item/create/',item_views.CreateView,name='create_item'),
    path('item/list/',item_views.ListView,name='list_item'),
    path('item/edit/<int:pk>/',item_views.EditView,name='edit_item'),

    # topup
    path('topup/',top_up_views.Top_up_View,name='create_top_up'),
    path('topup/list/',top_up_views.Top_up_List_View,name='list_top_up'),
    path('topup/edit/<int:pk>',top_up_views.Top_up_Edit_View,name='edit_top_up'),

    # statement
    path('create_statement/<int:pk>',statement_views.CreateView,name='create_statement'),
    path('list_statement/<int:form>/',statement_views.ListView,name='list_statement'),
    path('edit_statement/<int:form>/<int:pk>/',statement_views.EditView,name='edit_statement'),


    #test
    path('test/',display_views.testformView)

]