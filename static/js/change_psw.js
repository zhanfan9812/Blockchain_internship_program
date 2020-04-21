function  change_psw(id) {
//    var url = decodeURI(window.location.href);
//    var update_id = url.split('=')[1]
        var psw = $('#psw_input').val();
        var npsw = $('#npsw_input').val();
        $.ajax({
            url:'/new_psw',
            method:'POST',
            async : false,
            data:{id:id,psw:psw,npsw:npsw},
            success:function(response){
                if(response=='1'){
                    alert('修改成功');
                }
                else if(response=='0_1'){
                    alert('输入不能为空');
                }
                else if(response=='0_2'){
                    alert('原密码错误');
                }
            }
        });
}