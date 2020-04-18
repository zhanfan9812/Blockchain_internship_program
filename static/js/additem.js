  $(function  () {
    $('#execute').click(function(){
    alert("ddddd");
        var num = $('#productNum').val();
        var itemName = $('#productName').val();
        var description=$('#productDescription').val();
         var regPos = / ^\d+$/;

        if(!regPos.test(num)|| itemName==null)
        {
        alert("not allowed");
       window.location.href='/users';
        }
        $.ajax({
            url:'/producers/additem/'+num+"/"+itemName+"/"+description,
            method:'GET',
            success:function(response){
                    alert('add success')
                    window.location.href='/users';
            }
        });
    })
    })