function getCount(url,data){//返回总条数，需自己调用得到总条数，然后传给变量count
    //url:查询总数据条数的url
    //data:状态，status
    var count = 50;
    $.ajax({
        url:url+"/"+data,
        async: false,
        success:function (data) {
            count = data;
        }
    });
    return count
}
function getData(url,status,curr,limit){//获取后台根据分页查询的数据

    var data = "";
    $.ajax({
        url:url+"/"+status+"/"+curr+"/"+limit,
        async: false,
        success:function (response) {
            data = response;
        }
    })
    return data;
}
function showPage(pageId,count,limit,getDataByPageURL,status){
      layui.use('laypage', function(){
        var laypage = layui.laypage;
        //执行一个laypage实例
        laypage.render({
            elem: pageId //注意，这里的 test1 是 ID，不用加 # 号
            ,count: count //数据总数，从服务端得到
        });
        /*切换*/
        laypage.render({
            elem: pageId
            ,count: count //数据总数，从服务端得到
			,limit:limit
            ,jump: function(obj, first){
                //obj包含了当前分页的所有参数，比如：
               // alert("当前页："+obj.curr); //得到当前页，以便向服务端请求对应页的数据。
                //alert("每页条数："+obj.limit); //得到每页显示的条数
                var data = getData(getDataByPageURL,status,obj.curr,obj.limit)
                var html = makeHtml(data,status);
                $("tbody").empty()
                 $("tbody").append(html);
                //首次执行
                if(!first){

                }
            }
        });
    });//分页结束
}
/*function makeHtml(data){
    var html = "";
          for (var i = 0;i<data.data.length;i++){
              var j = i+1;
              html += "<tr>\n" +
                  "\t\t\t\t\t\t\t\t\t<td>"+j+"</td>\n" +
                  "\t\t\t\t\t\t\t\t\t<td>"+data.data[i].id+"</td>\n" +
                  "\t\t\t\t\t\t\t\t\t<td>"+data.data[i].product_name+"</td>\n" +
                  "\t\t\t\t\t\t\t\t\t<td>"+data.data[i].number+"</td>\n" +
                  "\t\t\t\t\t\t\t\t\t<td>已入库</td>\n" +
                  "\t\t\t\t\t\t\t\t\t<td>"+data.data[i].date_of_pro+"</td>\n" +
                  "\t\t\t\t\t\t\t\t\t<td>"+data.data[i].description+"</td>\n" +
                  "\t\t\t\t\t\t\t\t</tr>"
          }
          return html;
}*/

/*自己定义变量，重写makeHtml方法*/