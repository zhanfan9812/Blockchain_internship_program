function delete_id(obj, id) {
    $.ajax({
            url:'/producers/deleteitem',
            type:'Post',
            data:{productId:id},
            success:function(data) {
                if (data == '0') {
                    $(obj).parents("tr").remove();
                    alert("删除成功");
                    return;
                }
            }
    });
}
function makeHtml(response,status){
    var html = "";
          for (var i = 0;i<response.data.length;i++){
              var j = i+1;
              html+="<tr>" +
									"<td>"+j+"</td>"+
                                        "<td>"+response.data[i].id+"</td>"+
                                        "<td>"+response.data[i].product_name+"</td>"+
                                        "<td>"+response.data[i].number+"</td>"+
                                        "<td>生产中</td>"+
                                        "<td>"+response.data[i].date+"</td>"+
                                        "<td>"+response.data[i].description+"</td>"+

									"<td>"+
									          "\t\t\t\t\t\t\t\t\t\t<a class=\"layui-btn layui-btn-sm layui-btn-normal\" title=\"编辑\" onclick=\"execute_open('更新商品状态', 'commodities_UpdateStatus.html?id="+response.data[i].id+"', 1000, 500)\" href=\"javascript:;\"><i class=\"layui-icon layui-icon-edit\"></i>编辑</a>\n" +
									"<a class='layui-btn layui-btn-sm layui-btn-danger' title='删除' onclick='delete_id(this,"+response.data[i].id+")' href='javascript:;'><i class='layui-icon layui-icon-delete'></i>删除</a>"	+
									"</td>"+
								"</tr>";
          }
          return html;
}

$(function  () {
    var url = decodeURI(window.location.href);
    var id = url.split('=')[1]
    var status = 1;
    var limit = 5;
    var count = getCount("/warehouse/getCount",status);//数据总条数
    alert(count)
    /*分页注册*/
    showPage("layuipage",count,limit,"/warehouse/getProductsByPage",status)
//console.log(A);


$('#search').click(function(){
        var name = $('#test').val();

//console.log(A);
      $.ajax({
            url:'/producers/searchbyid3',
            method:'POST',
            async : false,
            data:{product_name:name},
            success:function (data) {
                if (data == null ||data == ""){
                   alert("未搜索到相应商品！")
                    return}
                else {
                    $("tbody").empty();
                     html = "<tr>\n" +
                    "\t\t\t\t\t\t\t\t\t<td>"+1+"</td>\n" +
                    "\t\t\t\t\t\t\t\t\t<td>"+data.product.id+"</td>\n" +
                    "\t\t\t\t\t\t\t\t\t<td>"+data.product.product_name+"</td>\n" +
                    "\t\t\t\t\t\t\t\t\t<td>"+data.product.number+"</td>\n" +
                    "\t\t\t\t\t\t\t\t\t<td>生产中</td>\n" +
                    "\t\t\t\t\t\t\t\t\t<td>"+data.product.date_of_pro+"</td>\n" +
                    "\t\t\t\t\t\t\t\t\t<td>"+data.product.description+"</td>\n" +
                    "\t\t\t\t\t\t\t\t\t<td>\n" +
                    "\t\t\t\t\t\t\t\t\t\t<a class=\"layui-btn layui-btn-sm layui-btn-normal\" title=\"编辑\" onclick=\"execute_open('更新商品状态', 'commodities_UpdateStatus.html?id="+data.product.id+"', 1000, 500)\" href=\"javascript:;\"><i class=\"layui-icon layui-icon-edit\"></i>编辑</a>\n" +
                    "\t\t\t\t\t\t\t\t\t\t<a class='layui-btn layui-btn-sm layui-btn-danger' title='删除' onclick='delete_id(this,"+data.product.id+")' href='javascript:;'><i class='layui-icon layui-icon-delete'></i>删除</a>\n" +
                    "\t\t\t\t\t\t\t\t\t</td>\n" +
                    "\t\t\t\t\t\t\t\t</tr>"
                    $("tbody").append(html);
                }
            }
        });



          })

    })
//"<a class='layui-btn layui-btn-sm layui-btn-danger' title='删除' onclick='delete_id(this,"+response.data.id+")' href='javascript:;'><i class='layui-icon layui-icon-delete'></i>删除</a>"




