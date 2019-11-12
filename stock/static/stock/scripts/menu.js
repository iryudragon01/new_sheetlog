function menu_statement(position){
  menu_list = document.getElementById('popup_menu_statement')
  menu_list.style.top = position.pageY+'px'
  menu_list.style.left = position.pageX+'px'
  menu_list.style.display="block"
 current_popup = 'activate'
}
function cancel_popup(){
  if(current_popup == 'activate'){
    document.getElementById('popup_menu_statement').style.display='none'
    current_popup='deactivate'
  }

}
