  $(function  () {
    $('#execute').click(function(){
        var num = $('#productNum').val();
        var itemName = $('#productName').val();
         var regPos = / ^\d+$/;

        if(!regPos.test(num)|| itemName==null)
        {
        alert("not allowed");
       window.location.href='/users';
        }
        $.ajax({
            url:'/producers/additem/'+num+"/"+itemName,
            method:'GET',
            success:function(response){
                    alert('add success')
                    window.location.href='/users';
            }
        });
    })
    })