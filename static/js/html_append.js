$(function  () {
    var id = $("#my_userid").text()
    var personal_html = "<dd>"+
                              "<a onclick='execute_open(\"编辑角色\", \"personal_info.html?id="+id+"\", 1000, 500)' href=\"javascript:;\">基本资料</a>"+
                        "</dd>";
    $('#html_append').append(personal_html);
})
