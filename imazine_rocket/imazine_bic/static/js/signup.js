function clearText(thefield){
        if (thefield.defaultValue==thefield.value)
                thefield.value = ""
            }

var check = function(el) {
    var password = document.getElementById('pw');
        var passwordCheck = el;
        
        //F12 누르고 개발자 도구 Console에서 확인.
        console.log('password=' + password.value + ', passwordCheck=' + passwordCheck.value);
        console.log('isValid=' + password.value === passwordCheck.value);
        
        if (password.value !== passwordCheck.value) {

            passwordCheck.value = '';
            document.get
            passwordCheck.placeholder = '비밀번호를 다시 확인해주세요.';
                
        alert('비밀번호가 일치하지 않습니다!');
        return;
         }
    }

          

var echeck = function(ech) {
    var email = document.getElementById('email');
    email=ech;
    var regExp = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;
              
              if (email.value !== null && email.match(regExp) != null) {
                  alert('회원가입 성공!');         
              }
              //alert('이메일 주소를 확인해주세요.');
              email.placeholder = '비밀번호를 다시 확인해주세요.';
              ech.placeholder='이메일을 다시 확인해주세요.';
    }
