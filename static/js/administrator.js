$(function  () {
    var url = decodeURI(window.location.href);
    /* 得到id*/
    alert(url)
    var id = url.split('=')[1]
    alert(id)
    $('#select').click(function(){
        var username = $('#username').val();
        $.ajax({
            url:'/select_username',
            method:'POST',
            async : false,
            data:{username:username},
            success:function(response){
                    alert(response.data[0].username);
                    var html= "<tr>" +
									"<td>1</td>"+
                                        "<td>"+response.data[0].age+"</td>"+
                                        "<td>"+response.data[0].username+"</td>"+
                                        "<td>10</td>"+
                                        "<td><input type='checkbox' name='switch' lay-skin='switch' data-url='' value='1' data-id='1' title='状态' lay-text='启用|禁用' checked='checked'></td>"+
									"<td>"+
									"<a class='layui-btn layui-btn-sm layui-btn-normal' title='编辑' onclick='execute_open('编辑角色', 'role_operation.html?id=1', 1000, 500)' href='javascript:;'><i class='layui-icon layui-icon-edit'></i>编辑</a>"	+
									"<a class='layui-btn layui-btn-sm layui-btn-danger' title='删除' onclick='execute_del(this, 1, '')' href='javascript:;'><i class='layui-icon layui-icon-delete'></i>删除</a>"	+
									"</td>"+
								"</tr>";
//                    var html = "sada";
                    $('tbody').append(html);
                    alert('查询成功');
            }
        });
    })
})