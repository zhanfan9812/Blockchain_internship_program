$(function  () {
    var url = decodeURI(window.location.href);
    var update_id = url.split('=')[1]
    $('#change_psw').click(function(){
        $(".layui-col-md12").empty();
        var html_append ="<div class=\"layui-form-item\">\n" +
           "\t\t\t\t\t\t<label class=\"layui-form-label\">原密码</label>\n" +
           "\t\t\t\t\t\t<div class=\"layui-input-inline layer-inputs\">\n" +
           "\t\t\t\t\t\t\t<input type=\"text\" value=\"\" id=\"psw_input\"  placeholder=\"请输入密码\" class=\"layui-input\">\n" +
           "\t\t\t\t\t\t</div>\n" +
           "\t\t\t\t\t</div>\n" +
           "\t\t\t\t\t<div class=\"layui-form-item\">\n" +
           "\t\t\t\t\t\t<label class=\"layui-form-label\">新密码</label>\n" +
           "\t\t\t\t\t\t<div class=\"layui-input-inline layer-inputs\">\n" +
           "\t\t\t\t\t\t\t<input type=\"text\" value=\"\" id=\"npsw_input\"  placeholder=\"请输入新密码\" class=\"layui-input\">\n" +
           "\t\t\t\t\t\t</div>\n" +
           "\t\t\t\t\t</div>"+
           "<div class=\"layui-form2-item\"  style=\"margin-left: 50px;\">\n" +
        "\t\t\t\t\t\t<a  href=\"javascript:;\" class=\"layui-btn\" onclick='change_psw("+update_id+")' id=\"new_psw\" ><i class=\"layui-icon layui-icon-form\"></i>修改</a>\n" +
        "\t\t\t\t\t</div>"
        $('.layui-col-md12').append(html_append);
    })
})