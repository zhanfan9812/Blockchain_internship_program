$(function  () {
    $('#submit').click(function(){
        var username = $('#username').val();
        var password = $('#password').val();
        $.ajax({
            url:'/login',
            method:'POST',
            data:{username:username,password:password},
            success:function(response){
                if(response=='1'){
                    window.location.href='/users';
                }else{
                    alert('登录失败,用户名或密码错误!');
                }
            }
        });
    })
    $(document).keydown(function (event) {
        if (event.keyCode == 13) {
            $('#submit').triggerHandler('click');
        }
     });
})