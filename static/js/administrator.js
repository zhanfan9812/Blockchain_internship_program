function delete_id(obj, id) {
    layer.confirm('确认要删除吗？', function(index) {
		layer.load();
        $.ajax({
            url:'/delete_id',
            type:'Post',
            data:{'id':id},
            dataType:'json',
            success:function(data) {
                alert(data);
				layer.closeAll('loading');
                if (data == '1') {
                    $(obj).parents("tr").remove();
                    layer.msg(data.message,{icon:1,time:1000});return false;
                } else {
                    layer.msg(data.message,{icon:2,time:1000});return false;
                }
            },
			error : function(e){
				layer.closeAll('loading');
				layer.msg(e.responseText, {icon: 2, time: 1000});
			}
        });
    });
}

$(function  () {

    var url = decodeURI(window.location.href);
    /* 得到id*/
//    alert(url)
    if(url.search(/role_list.html/)!=-1)
    {
        var role = url.split('=')[1]
//        alert(role);
    }
    if(url.search(/role_operation.html/)!=-1)
    {
        var update_id = url.split('=')[1]

        $('#save').click(function(){
            var username = $('#username_input').val();
            var password = $('#password_input').val();
            var email = $('#email_input').val();
            var gender = $('#gender_input').val();
            var role_input =  $("#role_input").val();
            $.ajax({
                url:'/update_id',
                method:'POST',
                data:{username:username,password:password,email:email,gender:gender,role:role_input,id:update_id},
                success:function(response){
                    if(response=='1'){
                        alert('修改成功');

                    }else{
                        alert('修改失败');
                    }
                }
            });
        })
    }


    /* select by role*/
    $.ajax({
        url:'/select_role',
        method:'POST',
        async : false,
        data:{role:role},
        success:function(response){
            var html = "";
            for (var i = 0 ;i<response.data.length;i++){
                var j=i+1
                html+= "<tr>" +
                            "<td>"+j+"</td>"+
                            "<td>"+response.data[i].id+"</td>"+
                            "<td>"+response.data[i].username+"</td>"+
                            "<td>"+response.data[i].email+"</td>"+
                            "<td>"+response.data[i].gender+"</td>"+
                            "<td>"+
                                "<a class='layui-btn layui-btn-sm layui-btn-normal' title='编辑' onclick='execute_open(\"编辑角色\", \"role_operation.html?id="+response.data[i].id+"\", 1000, 500)' href=\"javascript:;\"><i class='layui-icon layui-icon-edit'></i>编辑</a>"	+
							    "<a class='layui-btn layui-btn-sm layui-btn-danger' title='删除' onclick='delete_id(this, "+response.data[i].id+")' href='javascript:;'><i class='layui-icon layui-icon-delete'></i>删除</a>"	+
                            "</td>"+
                        "</tr>";
            }
            $('tbody').append(html);
        }
    });

    /* select by username*/
    $('#select').click(function(){
        var username = $('#username_select').val();
        $.ajax({
            url:'/select_username',
            method:'POST',
            async : false,
            data:{username:username,role:role},
            success:function(response){
                if(response == '0'){
                    alert('查无此人')
                }
                else{
                    $("tbody").empty();
                    alert(response.username);
                    var html= "<tr>" +
                                    "<td>"+1+"</td>"+
                                    "<td>"+response.id+"</td>"+
                                    "<td>"+response.username+"</td>"+
                                    "<td>"+response.email+"</td>"+
                                    "<td>"+response.gender+"</td>"+
                                    "<td>"+
									    "<a class='layui-btn layui-btn-sm layui-btn-normal' title='编辑' onclick='execute_open('编辑角色', 'role_operation.html?id=1', 1000, 800)' href='javascript:;'><i class='layui-icon layui-icon-edit'></i>编辑</a>"	+
									    "<a class='layui-btn layui-btn-sm layui-btn-danger' title='删除' onclick='delete_id(this, "+response.id+")' href='javascript:;'><i class='layui-icon layui-icon-delete'></i>删除</a>"	+
									"</td>"+
								"</tr>";
//                    var html = "sada";
                    $('tbody').append(html);
                    alert('查询成功');
                }
            }
        });
    })


    $('#save').click(function(){
        var username = $('#username_input').val();
        var password = $('#password_input').val();
        var email = $('#email_input').val();
        var gender = $('#gender_input').val();
        var role_input =  $("#role_input").val();
        $.ajax({
            url:'/add',
            method:'POST',
            data:{username:username,password:password,email:email,gender:gender,role:role_input},
            success:function(response){
                if(response=='1'){
                    alert('保存成功');

                }else{
                    alert('保存失败');
                }
            }
        });
    })
})