function imgch01(){
    var img=document.getElementById("main-bt01");
            img.src = "../img/main-btgr01.png";
<<<<<<< HEAD:imazine_rocket/imazine_bic/templates/imazine_bic/static/js/main.js
            location.href="reservation_1.html";
=======
            location.href="{% url 'reservation_1'%}";
>>>>>>> 0fa3fd3244a22594ad9eeae6c480da787cbe899e:imazine_rocket/imazine_bic/static/js/main.js
        }

function imgch02(){
     var img=document.getElementById("main-bt02");
              img.src = "../img/main-btgr02.png";
              location.href="reservation_2.html";
        }

function imgch03(){
    var img=document.getElementById("main-bt03");
               img.src = "../img/main-btgr03.png";
               location.href="reservation_3.html";
        }
function imgch04(){
     var img=document.getElementById("main-bt04");
                img.src = "../img/main-btgr04.png";
                location.href="reservation_end.html";
        }
       
       

//function href 안에 url 처리