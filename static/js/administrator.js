function delete_id(obj, id) {
    layer.confirm('确认要删除吗？', function(index) {
		layer.load();
        $.ajax({
            url:'/delete_id',
            type:'Post',
            data:{'id':id},
            dataType:'json',
            success:function(data) {
//                alert(data);
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
function makeHtml(response,status){
      var sex=["0","男","女"];
    var html = "";
          for (var i = 0;i<response.data.length;i++){
              var j=i+1;
                html+= "<tr>" +
                            "<td>"+j+"</td>"+
                            "<td>"+response.data[i].id+"</td>"+
                            "<td>"+response.data[i].username+"</td>"+
                            "<td>"+response.data[i].email+"</td>"+
                            "<td>"+sex[response.data[i].gender]+"</td>"+
                            "<td>"+
                                "<a class='layui-btn layui-btn-sm layui-btn-normal' title='编辑' onclick='execute_open(\"编辑角色\", \"role_update.html?id="+response.data[i].id+"\", 1000, 500)' href=\"javascript:;\"><i class='layui-icon layui-icon-edit'></i>编辑</a>"	+
							    "<a class='layui-btn layui-btn-sm layui-btn-danger' title='删除' onclick='delete_id(this, "+response.data[i].id+")' href='javascript:;'><i class='layui-icon layui-icon-delete'></i>删除</a>"	+
                            "</td>"+
                        "</tr>";
          }
          return html;
}
$(function  () {
    var url = decodeURI(window.location.href);
    /* 得到导航栏role*/
    if(url.search(/role_list.html/)!=-1)
    {
        var role = url.split('=')[1]
    }
    /* 得到要修改的角色id*/
    if(url.search(/role_update.html/)!=-1)
    {
        var update_id = url.split('=')[1]
    }
    if(url.search(/personal_info.html/)!=-1)
    {
        var update_id = url.split('=')[1]
    }
    if(role != null && role !=""){
    var limit = 5;
    var count = getCount("/role/getCountByRole",role);//数据总条数
    /*分页注册*/
    showPage("layuipage",count,limit,"/role/getRoleByRolePage",role)
    }

    var sex=["0","男","女"];

    /* update by id*/
    $('#update_id').click(function(){
        var username = $('#username_input').val();
        var password = $('#password_input').val();
        var email = $('#email_input').val();
        var gender = $('#gender_input').val();
        var role_input = $("#role_input").val();

        $.ajax({
            url:'/update_id',
            method:'POST',
            async : false,
            data:{username:username,password:password,email:email,gender:gender,role:role_input,id:update_id},
            success:function(response){
                if(response=='1'){
                    alert('修改成功');
                }
                else if(response=='0_1'){
                    alert('输入不能为空');
                }
                else if(response=='0_2'){
                    alert('用户名已被注册');
                }
                else if(response=='0_3'){
                    alert('邮箱已被注册');
                }
            }
        });
    })

     /* 修改个人信息*/
    $('#update_personal').click(function(){
        var email = $('#email_input').val();
        var gender = $('#gender_input').val();
        $.ajax({
            url:'/update_personal',
            method:'POST',
            async : false,
            data:{email:email,gender:gender,id:update_id},
            success:function(response){
                if(response=='1'){
                    alert('修改成功');
                }
                else if(response=='0_1'){
                    alert('输入不能为空');
                }
                else if(response=='0_3'){
                    alert('邮箱已被注册');
                }
            }
        });
    })

    /* select by role*/


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
//                   alert(response.username);
                    var html= "<tr>" +
                                    "<td>"+1+"</td>"+
                                    "<td>"+response.id+"</td>"+
                                    "<td>"+response.username+"</td>"+
                                    "<td>"+response.email+"</td>"+
                                    "<td>"+sex[response.gender]+"</td>"+
                                    "<td>"+
									    "<a class='layui-btn layui-btn-sm layui-btn-normal' title='编辑' onclick='execute_open(\"编辑角色\", \"role_update.html?id="+response.id+"\", 1000, 500)' href=\"javascript:;\"><i class='layui-icon layui-icon-edit'></i>编辑</a>"	+
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

    /* add user*/
    $('#save').click(function(){
        var username = $('#username_input').val();
        var password = $('#password_input').val();
        var email = $('#email_input').val();
        var gender = $('#gender_input').val();
        var role_input =  $("#role_input").val();
        $.ajax({
            url:'/add',
            method:'POST',
            async : false,
            data:{username:username,password:password,email:email,gender:gender,role:role_input},
            success:function(response){
                if(response=='1'){
                    alert('添加成功');
                }
                else if(response=='0_1'){
                    alert('输入不能为空');
                }
                else if(response=='0_2'){
                    alert('用户名已被注册');
                }
                else if(response=='0_3'){
                    alert('邮箱已被注册');
                }
            }
        });
    })
})