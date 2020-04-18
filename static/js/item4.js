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
    var id = url.split('=')[1]

      $.ajax({
            url:'/producers/list',
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
                                        "<td>"+response.data[i].date+"</td>";


                                        }
                    $('tbody').append(html);

            }
        });

$('#search').click(function(){
        var name = $('#test').val();
      $.ajax({
            url:'/producers/searchbyid',
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
                                        "<td>"+response.data[i].date+"</td>";
                                        }
                    $('tbody').append(html);

            }
        });



          })

    })

