  $(function  () {
    $('#execute').click(function(){
        var num = $('#productNum').val();
        var itemName = $('#productName').val();
//        alert(itemName)
        var description = $('#productDescription').val();
//        alert(description)
        if(itemName==null||itemName==''){
            alert('请添加商品名称');
            return;
        }
        if(num==null||num==''){
            alert('请添加商品数量');
            return;
        }
        if(description==null||description==''){
            alert('请添加商品描述');
            return;
        }
        $.ajax({
            url:'/producers/additem/'+num+"/"+itemName+"/"+description,
            method:'POST',
            success:function(response){
//                alert(response)
                if(response=='1')
                    alert('添加商品成功');
                else if(response=='0_1')
                    alert('添加商品失败，商品名称不能为纯数字');
                else if(response=='0_2')
                    alert('添加商品失败，商品数量必须为正整数');
                else if(response=='0_3')
                alert('添加商品失败，商品名称已存在');
            }
        });
    })
    })