$(function(){
    var url = decodeURI(window.location.href);
    /* 得到id*/
    var id = url.split("=")[1];
    alert(id)
    $("#saveStatus").click(function () {
        $.ajax({
            url:"/warehouse/updateStatus/"+$('#pid option:selected').val()+"/"+id,
            method:"get",
            success:function (data) {
                alert("更新成功")
            }
        })
    });
});
