$(function(){
    var url = decodeURI(window.location.href);
    /* 得到id*/
    var id = url.split("=")[1];
    var A=["0","生产中状态","待运输状态","运输中状态","已到达状态","已入库状态"];
    $.ajax({
        url:"/warehouse/getInfo/"+id,
        method:"POST",
        async:false,
        success:function (data) {
            var nextStatus = 1 + data.product.status;
            $("#updateInfo").empty();
                  var html = "<div class=\"layui-form-item\">\n" +
                    "\t\t\t\t\t\t<label class=\"layui-form-label\">订单号</label>\n" +
                    "\t\t\t\t\t\t<div class=\"layui-input-inline layer-inputs\">\n" +
                    "\t\t\t\t\t\t\t<input name=\"order_code\" id=\"order_code\" style=\"width: 180px;height: 30px\" value=\"\">\n" +
                    "\t\t\t\t\t\t</div>\n" +
                    "\t\t\t\t\t\t<div class=\"layui-form-mid layui-word-aux\">请输入订单号</div>\n" +
                    "\t\t\t\t\t</div>\n" +
                    "\t\t\t\t\t<div class=\"layui-form-item\">\n" +
                    "\t\t\t\t\t\t<label class=\"layui-form-label\">出发地</label>\n" +
                    "\t\t\t\t\t\t<div class=\"layui-input-inline layer-inputs\">\n" +
                    "\t\t\t\t\t\t\t<input name=\"start_place\" id=\"start_place\" style=\"width: 180px;height: 30px\" value=\"\">\n" +
                    "\t\t\t\t\t\t</div>\n" +
                    "\t\t\t\t\t\t<div class=\"layui-form-mid layui-word-aux\">请输入商品出发地</div>\n" +
                    "\t\t\t\t\t</div>\n" +
                    "\t\t\t\t\t<div class=\"layui-form-item\">\n" +
                    "\t\t\t\t\t\t<label class=\"layui-form-label\">目的地</label>\n" +
                    "\t\t\t\t\t\t<div class=\"layui-input-inline layer-inputs\">\n" +
                    "\t\t\t\t\t\t\t<input name=\"end_place\" id=\"end_place\" style=\"width: 180px;height: 30px\" value=\"\">\n" +
                    "\t\t\t\t\t\t</div>\n" +
                    "\t\t\t\t\t\t<div class=\"layui-form-mid layui-word-aux\">请输入商品目的地</div>\n" +
                    "\t\t\t\t\t</div>\n" +
                    "\t\t\t\t\t<div class=\"layui-form-item\">\n" +
                    "\t\t\t\t\t\t<label class=\"layui-form-label\">商品状态</label>\n" +
                    "\t\t\t\t\t\t<div class=\"layui-input-inline layer-inputs\">\n" +
                    "\t\t\t\t\t\t\t<select name=\"pid\" id=\"pid\" lay-filter=\"pid\" style=\"width: 180px;height: 50px\">\n" +
                    "\t\t\t\t\t\t\t\t<option value=\""+data.product.status+"\" selected=\"selected\">"+A[data.product.status]+"</option>\n" +
                    "\t\t\t\t\t\t\t\t<option value=\""+nextStatus+"\">"+A[nextStatus]+"</option>\n" +
                    "\t\t\t\t\t\t\t</select>\n" +
                    "\t\t\t\t\t\t</div>\n" +
                    "\t\t\t\t\t\t<div class=\"layui-form-mid layui-word-aux\">请选择商品状态</div>\n" +
                    "\t\t\t\t\t</div>\n" +
                    "\t\t\t\t\t<div class=\"layui-form-item\">\n" +
                    "\t\t\t\t\t\t<label class=\"layui-form-label\"></label>\n" +
                    "\t\t\t\t\t\t<div class=\"layui-input-inline layer-inputs\">\n" +
                    "\t\t\t\t\t\t\t<input type=\"hidden\">\n" +
                    "\t\t\t\t\t\t</div>\n" +
                    "\t\t\t\t\t\t<div class=\"layui-form-mid layui-word-aux\"></div>\n" +
                    "\t\t\t\t\t</div>\n" +
                    "\t\t\t\t\t<div class=\"layui-form-item\" style=\"margin-left: 50px;\">\n" +
                    "\t\t\t\t\t\t<button class=\"layui-btn\" id=\"saveStatus\"><i class=\"layui-icon layui-icon-form\"></i>保存</button>\n" +
                    "\t\t\t\t\t</div>";
            $("#updateInfo").append(html);
//            $('#product_name').val(data.product.product_name);
//            $('#product_num').val(data.product.number);
//            $('#product_description').val(data.product.description);
        }
    })
    $("#saveStatus").click(function () {
        var order_code=$('#order_code').val();
        var start_place=$('#start_place').val();
        var end_place=$('#end_place').val();
        var product_status=$('#pid option:selected').val();
        $.ajax({
            url:"/warehouse/updateInfo/"+id,
            method:"POST",
            data:{id:id,
            order_code:order_code,
            start_place:start_place,
            end_place:end_place,
            product_status:product_status},
            success:function (response) {
                if(response=='1'){
                    alert('修改成功');
                }
                else if(response=='0_1'){
                    alert('输入不能为空');
                }
            }
        })
    });
});