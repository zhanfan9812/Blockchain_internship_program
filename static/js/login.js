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
                    alert('登录成功');
                    window.location.href='/users';
                }else{
                    alert('登录失败');
                }
            }
        });
    })
})