$(function  () {
    var url = decodeURI(window.location.href);
    var update_id = url.split('=')[1]
    var B = ['0','生产厂商','物流人员','仓库管理人员','管理员'];
    if(url.search(/role_update.html/)!=-1)
    {
        $.ajax({
            url:'/getinfo',
            method:'POST',
            async : false,
            data:{id:update_id},
            success:function(response){
                $('#username_input').val(response.username);
                $('#password_input').val("");
                $('#email_input').val(response.email);
                $('#gender_input').val(response.gender);
                $("#role_input").val(response.role);
            }
        });
    }
    if(url.search(/personal_info.html/)!=-1)
    {
        $.ajax({
            url:'/getinfo',
            method:'POST',
            async : false,
            data:{id:update_id},
            success:function(response){
                $('#username_input').val(response.username);
                $('#email_input').val(response.email);
                $('#gender_input').val(response.gender);
                $("#role_input").val(B[response.role]);
            }
        });
    }

})