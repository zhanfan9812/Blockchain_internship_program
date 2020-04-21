$(function  () {
    var id = $("#my_userid").text()
    var personal_html = "<dd>"+
                              "<a onclick='execute_open(\"基本资料\", \"personal_info.html?id="+id+"\", 1000, 500)' href=\"javascript:;\">基本资料</a>"+
                        "</dd>";
    $('#html_append').before(personal_html);
})
