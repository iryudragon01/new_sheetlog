var popup
current_popup=''
function viewpage(){
  mytype=document.getElementById('type').value
  select = document.getElementById(popup).childNodes
  choice=eval(mytype*2-1)
  set_type(select[choice])
}

function popup_type(e){
    current_popup=''
    cancel_popup()
    position= document.getElementById(popup)
    position.style.top=eval(e.pageY-50)+'px'
    position.style.left=eval(e.pageX-50)+'px'
    position.style.display="block";
    current_popup=popup
  }


function select_type(type){
  document.getElementById(popup).style.display="none"
  current_popup=''
  set_type(type)
  }

function blur_type(){
    document.getElementById('popup').style.display="none";
}

function set_type(type){
  type_hidden = document.getElementById('type')
  type_show = document.getElementById('type_selectd')
  type_show.innerHTML=type.innerHTML
  type_hidden.value = type.value
}

function submitform(method1){
  document.getElementById(method1).click()
}


function verify(arg,position){
    vrfElement = document.getElementById('verifypwd')
    if(arg=='DELETE'){
     vrfElement.style.top = position.pageY+'px'
     vrfElement.style.left = position.pageX+'px'
     vrfElement.style.display = "block";
  }else if(arg == 'submit'){
      vrfElement.style.display ='none'
      document.getElementById('form_verifypwd').value=vrfElement.querySelector('input').value
      submitform('DELETE')
    }else{
      vrfElement.style.display = "none"
    }
}
