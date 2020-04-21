$(function () {
  var url = decodeURI(window.location.href);
  var A=["0","生产中","待运输","运输中","已到达","已入库"];
    /* 得到id*/
    var id = url.split("=")[1];
       $.ajax({
        url:"/product/getProductInfo/"+id,
        method:"post",
        success:function (data) {
             $("#qr_code").attr("src",data.data.qr_code)
            $("#productName").text(data.data.product_name)
            $("#productNum").text(data.data.number)
            $("#productStatus").text(A[data.data.status])
            $("#productScri").text(data.data.description)
            $("#productCreaTime").text(data.data.date_of_pro)
            var block_info = data.data.block_info;
            var block = block_info.split("\n\n");
            var html = "";
            for (var i = 0;i<block.length;i++){
                block_data = block[i].split("\n");
                 html  = html + "<tr>\n" ;
                for (var j = 0 ;j<block_data.length;j++){
                    if(j == 7){
                       createTime = block_data[j].split(":");
                       TimeData = "" +createTime[1]+":"+createTime[2]+":"+createTime[3];
                       html = html + "<td>"+TimeData+"</td>\n" ;
                       continue;
                    }
                    html = html + "<td>"+block_data[j].split(':')[1]+"</td>\n" ;
                }

                html = html +"</tr>";
            }
             $("tbody").append(html);
        }

    });

})