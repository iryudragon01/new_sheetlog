popupinput = document.getElementById('popup_input')
const log = document.getElementById('main_tab');
const last_value = document.getElementsByClassName("last_value");
var totalitem=document.getElementsByClassName('lastvalue').length

function nextid(id){
  if(id==totalitem){return 1
  }else{ return eval(id+1)}
}

function getdate(){
        get_date=document.getElementById('date_block')
        display_date=document.getElementById('date_display')
        if (get_date.style.display=="block"){
          get_date.style.display = "none"
          display_date.style.display = "block"
        }else{
          get_date.style.display = "block"
          display_date.style.display="none"
        }

     }

function opentab(pagename,linkbutton,colorbg){
    tabcontent=document.getElementsByClassName("tabcontent")
     // hide all tabcontent
     for(i=0;i<tabcontent.length;i++){
        tabcontent[i].style.display="none";
     }

     // clear button bg
     tablink = document.getElementsByClassName("tablink")
     for(i=0;i<tablink.length;i++){
     tablink[i].style.backgroundColor="";
     }
     document.getElementById(pagename).style.display="block";
     linkbutton.style.backgroundColor="#ccc";
     }






function input(item,position){
pos = item.getBoundingClientRect();
popupinput.style.display ="none"
popupinput.for=item
popupinput.type="number"
popupinput.value=eval(item.innerHTML)
popupinput.style.top=pos.top+'px'
popupinput.style.left=pos.left+'px'
popupinput.style.display = 'block'
popupinput.focus()
popupinput.select()

}
function inputkeydown(event){
  if(event.keyCode ==13){

    sub=popupinput.for.id.split('_')
    oldvalue=eval(popupinput.for.innerHTML)
    newvalue=eval(popupinput.value)
    diff=eval(newvalue-oldvalue)
    lasttd=document.getElementById("last_"+sub[1])
    lasttd.innerHTML=eval(eval(lasttd.innerHTML)+diff)
    saletd=document.getElementById("sale_"+sub[1])
    saletd.innerHTML=eval(eval(saletd.innerHTML)+diff)
    popupinput.style.display = "none"
    document.getElementById(sub[0]+"_"+nextid(eval(sub[1]))).click()
    updatetable()

  }
}
function inputblur(){
  popup_input.style.display = "none"
}
function updatetable(){
  summoney=0
  for(i=1;i<=totalitem;i++){
    price=eval(document.getElementById('price_'+i).innerHTML)
    sale=eval(document.getElementById('sale_'+i).innerHTML)
    money=price*sale
    summoney +=money
    document.getElementById("money_"+i).innerHTML=money
  }
  document.getElementById('sum_'+totalitem).innerHTML=summoney
}

opentab("main_tab",document.getElementById('main_button'),'#4caf50')
