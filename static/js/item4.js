$(function  () {
    var url = decodeURI(window.location.href);
    var id = url.split('=')[1]
 var A=["0","生产中","待运输","运输中","已到达","已入库"];

//console.log(A);
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
                                        "<td>"+A[response.data[i].status]+"</td>"+
                                        "<td>"+response.data[i].date+"</td>"+
                                        "<td>"+response.data[i].description+"</td>"+
                                    "</tr>";
                                        }
                    $('tbody').append(html);

            }
        });

$('#search').click(function(){
        var name = $('#test').val();
         var A=["0","生产中","待运输","运输中","已到达","已入库"];

//console.log(A);
      $.ajax({
            url:'/producers/searchbyid',
            method:'POST',
            async : false,
            data:{product_name:name},
            success:function(response){
                     if(response.data==null||response.data == "")
                        {
                        alert("未搜索到相应商品！");
                        }
//                    alert(response.data.description)
                    $('tbody').empty();
                    var html = "";
                    html+="<tr>" +
                                "<td>"+1+"</td>"+
                                    "<td>"+response.data.id+"</td>"+
                                    "<td>"+response.data.product_name+"</td>"+
                                    "<td>"+response.data.number+"</td>"+
                                    "<td>"+A[response.data.status]+"</td>"+
                                    "<td>"+response.data.date+"</td>"+
                                    "<td>"+response.data.description+"</td>"+
                             "</tr>";
                    $('tbody').append(html);

            }
        });
          })

    })

