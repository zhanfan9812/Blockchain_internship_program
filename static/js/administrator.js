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
                if (data == '0') {
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
    var id = url.split('=')[1]
//    alert(id)

    /* select by role*/
    $.ajax({
        url:'/select_role',
        method:'POST',
        async : false,
        data:{role:id},
        success:function(response){
            var html = "";
            for (var i = 0 ;i<response.data.length;i++){
                var j=i+1
                html+= "<tr>" +
                            "<td>"+j+"</td>"+
                            "<td>"+response.data[i].id+"</td>"+
                            "<td id = 'user'>"+response.data[i].username+"</td>"+
                            "<td>"+response.data[i].email+"</td>"+
                            "<td>"+response.data[i].gender+"</td>"+
                            "<td>"+
                                "<a class='layui-btn layui-btn-sm layui-btn-normal' title='编辑' onclick='execute_open('编辑角色', 'role_operation.html?id=1', 1000, 500)' href='javascript:;'><i class='layui-icon layui-icon-edit'></i>编辑</a>"	+
							    "<a class='layui-btn layui-btn-sm layui-btn-danger' title='删除' onclick='delete_id(this, "+response.data[i].id+")' href='javascript:;'><i class='layui-icon layui-icon-delete'></i>删除</a>"	+
                            "</td>"+
                        "</tr>";
            }
            $('tbody').append(html);
        }
    });

    /* select by username*/
    $('#select').click(function(){
        var username = $('#username').val();
        $.ajax({
            url:'/select_username',
            method:'POST',
            async : false,
            data:{username:username,role:id},
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
                                    "<td id = 'user'>"+response.username+"</td>"+
                                    "<td>"+response.email+"</td>"+
                                    "<td>"+response.gender+"</td>"+
                                    "<td>"+
									    "<a class='layui-btn layui-btn-sm layui-btn-normal' title='编辑' onclick='execute_open('编辑角色', 'role_operation.html?id=1', 1000, 500)' href='javascript:;'><i class='layui-icon layui-icon-edit'></i>编辑</a>"	+
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
})