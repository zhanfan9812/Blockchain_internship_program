function makeHtml(data,status){
    var A=["0","生产中","待运输","运输中","已到达","已入库"];
    var html = "";
          for (var i = 0;i<data.data.length;i++){
             var j = i+1;
              html += "<tr>\n" +
                  "\t\t\t\t\t\t\t\t\t<td>"+j+"</td>\n" +
                  "\t\t\t\t\t\t\t\t\t<td>"+data.data[i].id+"</td>\n" +
                  "\t\t\t\t\t\t\t\t\t<td>"+data.data[i].product_name+"</td>\n" +
                  "\t\t\t\t\t\t\t\t\t<td>"+data.data[i].number+"</td>\n" +
                  "\t\t\t\t\t\t\t\t\t<td>"+A[status]+"</td>\n" +
                  "\t\t\t\t\t\t\t\t\t<td>"+data.data[i].date_of_pro+"</td>\n" +
                  "\t\t\t\t\t\t\t\t\t<td>"+data.data[i].description+"</td>\n" +
                  "\t\t\t\t\t\t\t\t\t<td>\n" +
                  "\t\t\t\t\t\t\t\t\t\t<a class=\"layui-btn layui-btn-sm layui-btn-normal\" title=\"编辑\" onclick=\"execute_open('更新商品状态', 'commodities_UpdateStatus.html?id="+data.data[i].id+"', 1000, 500)\" href=\"javascript:;\"><i class=\"layui-icon layui-icon-edit\"></i>编辑</a>\n" +
                  "\t\t\t\t\t\t\t\t\t\t<a class=\"layui-btn layui-btn-sm layui-btn-normal\" title=\"编辑\" onclick=\"execute_open('更新商品状态', 'commodities_UpdateStatus.html?id="+data.data[i].id+"', 1000, 500)\" href=\"javascript:;\"><i class=\"layui-icon layui-icon-edit\"></i>物流二维码</a>\n" +
                  "\t\t\t\t\t\t\t\t\t</td>\n" +
                  "\t\t\t\t\t\t\t\t</tr>";
          }
          return html;
}
$(function () {
      var url = decodeURI(window.location.href);
    /* 得到id*/
    var status = url.split("=")[1];
    var limit = 5;
    var count = getCount("/warehouse/getCount",status);//数据总条数
    /*分页注册*/
    showPage("layuipage",count,limit,"/warehouse/getProductsByPage",status)
    $("#searchCommodityInwareHouse").click(function () {
        var productId = $("#productId").val();
        if (productId == null || productId ==""){
            alert("请输入商品名称或Id")
            return
        }
        $.ajax({
            url:"/warehouse/searchByCondition/"+status+"/"+productId,
            method:"get",
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
                    "\t\t\t\t\t\t\t\t\t<td>"+A[status]+"</td>\n" +
                    "\t\t\t\t\t\t\t\t\t<td>"+data.product.date_of_pro+"</td>\n" +
                    "\t\t\t\t\t\t\t\t\t<td>"+data.product.description+"</td>\n" +
                    "\t\t\t\t\t\t\t\t\t<td>\n" +
                    "\t\t\t\t\t\t\t\t\t\t<a class=\"layui-btn layui-btn-sm layui-btn-normal\" title=\"编辑\" onclick=\"execute_open('更新商品状态', 'commodities_UpdateStatus.html?id="+data.product.id+"', 1000, 500)\" href=\"javascript:;\"><i class=\"layui-icon layui-icon-edit\"></i>编辑</a>\n" +
                    "\t\t\t\t\t\t\t\t\t\t<a class=\"layui-btn layui-btn-sm layui-btn-normal\" title=\"编辑\" onclick=\"execute_open('更新商品状态', 'commodities_UpdateStatus.html?id="+data.product.id+"', 1000, 500)\" href=\"javascript:;\"><i class=\"layui-icon layui-icon-edit\"></i>物流二维码</a>\n" +
                    "\t\t\t\t\t\t\t\t\t</td>\n" +
                    "\t\t\t\t\t\t\t\t</tr>"
                    $("tbody").append(html);
                }
            }
        })
    });
});