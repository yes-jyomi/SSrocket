

$("#email").keyup(function(){
    var email=$(this).val();
    // 이메일 검증할 정규 표현식
    var reg=/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if(reg.test(email)){//정규표현식을 통과 한다면
                $("#emailErr").hide();
                successState("#email");
    }else{//정규표현식을 통과하지 못하면
                $("#emailErr").show();
                errorState("#email");
    }
});

$("#pwd").keyup(function(){
    var pwd=$(this).val();
    // 비밀번호 검증할 정규 표현식
    var reg=/^.{8,}$/;
    if(reg.test(pwd)){//정규표현식을 통과 한다면
                $("#pwdRegErr").hide();
                successState("#pwd");
    }else{//정규표현식을 통과하지 못하면
                $("#pwdRegErr").show();
                errorState("#pwd");
    }
});
$("#rePwd").keyup(function(){
    var rePwd=$(this).val();
    var pwd=$("#pwd").val();
    // 비밀번호 같은지 확인
    if(rePwd==pwd){//비밀번호 같다면
        $("#rePwdErr").hide();
        successState("#rePwd");
    }else{//비밀번호 다르다면
        $("#rePwdErr").show();
        errorState("#rePwd");
    }
});

// 성공 상태로 바꾸는 함수
function successState(sel){
    $(sel)
    .parent()
    .removeClass("has-error")
    .addClass("has-success")
    .find(".glyphicon")
    .removeClass("glyphicon-remove")
    .addClass("glyphicon-ok")
    .show();

    $("#myForm button[type=submit]")
                .removeAttr("disabled");
};
// 에러 상태로 바꾸는 함수
function errorState(sel){
    $(sel)
    .parent()
    .removeClass("has-success")
    .addClass("has-error")
    .find(".glyphicon")
    .removeClass("glyphicon-ok")
    .addClass("glyphicon-remove")
    .show();

    $("#myForm button[type=submit]")
                .attr("disabled","disabled");
};   