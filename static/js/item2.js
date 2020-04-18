
function delete_id(obj, id) {
    layer.confirm('确认要删除吗？', function(index) {
		layer.load();
        $.ajax({
            url:'/producers/deleteitem',
            type:'Post',
            data:{productId:id},
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
    var id = url.split('=')[1]

      $.ajax({
            url:'/producers/list3',
            method:'POST',
            async : false,
            success:function(response){

                    var html = "";
                    for (var i = 0 ;i<response.data.length;i++){
                    var j=i+1;
                             html+="<tr>" +
									"<td>"+j+"</td>"+
                                        "<td>"+response.data[i].id+"</td>"+
                                        "<td>"+response.data[i].product_name+"</td>"+
                                        "<td>"+response.data[i].number+"</td>"+
                                        "<td>"+response.data[i].status+"</td>"+
                                        "<td>"+response.data[i].date+"</td>"+

									"<td>"+
									          "\t\t\t\t\t\t\t\t\t\t<a class=\"layui-btn layui-btn-sm layui-btn-normal\" title=\"编辑\" onclick=\"execute_open('更新商品状态', 'producerUpdateStatus.html?id="+response.data[i].id+"', 1000, 300)\" href=\"javascript:;\"><i class=\"layui-icon layui-icon-edit\"></i>编辑</a>\n" +
									"<a class='layui-btn layui-btn-sm layui-btn-danger' title='删除' onclick='delete_id(this,"+response.data[i].id+")' href='javascript:;'><i class='layui-icon layui-icon-delete'></i>删除</a>"	+
									"</td>"+
								"</tr>";
                                        }
                    $('tbody').append(html);

            }
        });

$('#search').click(function(){
        var name = $('#test').val();

      $.ajax({
            url:'/producers/searchbyid3',
            method:'POST',
            async : false,
            data:{product_name:name},
            success:function(response){
                    if(response.data==null)
                        {
                        alert("nothing found");
                        }
                    $('tbody').empty();
                    var html = "";
                    for (var i = 0 ;i<response.data.length;i++){
                             var j=i+1;
                             html+="<tr>" +
									"<td>"+j+"</td>"+
                                        "<td>"+response.data[i].id+"</td>"+
                                        "<td>"+response.data[i].product_name+"</td>"+
                                        "<td>"+response.data[i].number+"</td>"+
                                        "<td>"+response.data[i].status+"</td>"+
                                        "<td>"+response.data[i].date+"</td>"+

									"<td>"+
									          "\t\t\t\t\t\t\t\t\t\t<a class=\"layui-btn layui-btn-sm layui-btn-normal\" title=\"编辑\" onclick=\"execute_open('更新商品状态', 'producerUpdateStatus.html?id="+response.data[i].id+"', 1000, 300)\" href=\"javascript:;\"><i class=\"layui-icon layui-icon-edit\"></i>编辑</a>\n" +
									"<a class='layui-btn layui-btn-sm layui-btn-danger' title='删除' onclick='delete_id(this,"+response.data[i].id+")' href='javascript:;'><i class='layui-icon layui-icon-delete'></i>删除</a>"	+
									"</td>"+
								"</tr>"+"<script src="+"../static/js/edititem.js"+"></script>";
                                        }
                    $('tbody').append(html);

            }
        });



          })

    })





