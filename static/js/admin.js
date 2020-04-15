layui.use(['element', 'form', 'layedit', 'laydate', 'upload', 'colorpicker'], function(){
    var form = layui.form,
        layer = layui.layer,
		element = layui.element,
        layedit = layui.layedit,
        laydate = layui.laydate,
        upload = layui.upload,
		colorpicker = layui.colorpicker;
    
	/**日期选择**/
		/**开始日期**/
	laydate.render({elem: '#start_time', type: 'datetime'});
		/**结束日期**/
    laydate.render({elem: '#end_time', type: 'datetime'});
	
	/**颜色选择**/
	colorpicker.render({
		elem: '#font-color',
		color: '#1c97f5',
		done: function(color){
			$('#font-color-input').val(color);
		}
	});
	
	/**
	 * 操作管理--数据操作
	 * @param String url 请求路径
	 * @param json data.field 提交的json数据
	 * @return json code 0:操作成功；1:value 返回操作后的状态
	 */
    form.on('submit(execute)', function(data) {
        layer.confirm('确认要保存吗？',function(index) {
			layer.load();
            var url = data.field.request_url;
			console.log(url);
            $.ajax({
                url:'' + url + '',
                type:'Post',
                data:data.field,
                dataType: "json",
                success: function (data) {
					layer.closeAll('loading');
                    if (data.code == 0) {
                        layer.msg(data.message, {icon: 1, time: 1000});
                        setTimeout(function () {
                            window.parent.location.reload();
                            var index = parent.layer.getFrameIndex(window.name);
                            parent.layer.close(index);
                        }, 1000);
                    } else {
                        layer.msg(data.message, {icon: 2, time: 1000});
                        return false;
                    }
                },
				error : function(e){
					layer.closeAll('loading');
					layer.msg(e.responseText, {icon: 2, time: 1000});
				}
            });
            return false;
        });
        return false;
    });
	
	/**
	 * 操作管理--数据状态
	 * @param object switch 当前
	 * @param int id 当前操作对象ID
	 * @param int status 当前操作对象状态
	 * @return json code 0:操作成功；1:value 返回操作后的状态
	 */
    form.on('switch', function(switchs) {
		layer.confirm('确认要修改吗？', function(index) {
			layer.load();
			var id = $(switchs.elem).data('id');
			var url = $(this).data('url');
			var status = switchs.value;
			$.ajax({
				url:''+ url +'',
				type:'Post',
				data:{'id':id, 'status':status},
				dataType:'json',
				success:function(data) {
					layer.closeAll('loading');
					if(data.code == 0){
						$(switchs.elem).attr('value', data.data);
						layer.msg(data.message,{icon:1,time:1000});
						return false;
					}else{
						layer.msg(data.message,{icon:2,time:1000});
						return false;
					}
				},
				error : function(e){
					layer.closeAll('loading');
					layer.msg(e.responseText, {icon: 2, time: 1000});
				}
			});
			return false;
		});
    });
	
	/**
	 * 操作管理--文件上传
	 * @param upload_pictures 需要上传事件ID
	 * @param place 文件存放位置
	 * @param layui_progress 进度条事件
	 * @param images_url 返回路径赋值图片ID
	 * @return json code 0:操作成功；1:操作失败；route 返回的图片路径
	 */
    upload.render({
        elem: '#upload_pictures', 
		url: '', 
		data:{
			file_place: function (){
				return $(this).data('place');
			}
        }, 
		multiple: true, 
		progress: function(n){
            var percent = n + '%';
            element.progress('layui_progress', percent);
        }, 
		before: function(obj){
            layer.load();
        }, 
		done: function (data) {
            layer.closeAll('loading');
            if (data.code == 0) {
                layer.msg(data.message, {icon: 1, time: 1000});
                $('#images_url').attr('src', data.route);
                var id_name = $(this)[0]['elem'][0]['attributes'][2]['value'];
                $('#' + id_name).val(data.route);
				return false;
            } else {
                layer.msg(data.message, {icon: 2, time: 1000});
                return false;
            }
        }, 
		error: function(e){
            layer.closeAll('loading');
            layer.msg(e.responseText, {icon: 2, time: 1000});
        }
    });
	
});

/**
 * 操作管理--打开界面
 * @param String title 界面标题
 * @param String url 访问路径
 * @param int width 打开宽度
 * @param int height 打开高度
 */
function execute_open(title, url, width, height) {
    layer.open({
        type: 2,
        title: ''+ title +'',
        shadeClose: true,
        shade: 0.8,
        area: [''+ width +'px', ''+ height +'px'],
        content: ''+ url +'',
    });
}

/**
 * 操作管理--数据删除
 * @param object obj 当前操作对象
 * @param int id 操作ID
 * @param String url 访问路径
 * @return json code 0:操作成功；1:操作失败
 */
function execute_del(obj, id, url) {
    layer.confirm('确认要删除吗？', function(index) {
		layer.load();
        $.ajax({
            url:''+ url +'',
            type:'Post',
            data:{'id':id},
            dataType:'json',
            success:function(data) {
				layer.closeAll('loading');
                if (data.code == 0) {
                    $(obj).parents("tr").remove();
                    layer.msg(data.message,{icon:1,time:1000});return false;
                } else {
                    layer.msg(data.message,{icon:2,time:1000});return false;
                }
            },
			error : function(e){
				layer.closeAll('loading');
				layer.msg(e.responseText, {icon: 2, time: 1000});
			}
        });
    });
}

/**选项卡切换**/
var nav_id = $('.layui-this').data('nav');
$('#layui_nav_left_' + nav_id).show();

$('.layui-layout-left').find('.layui-nav-item').click(function () {
	var nav_id = $(this).data('nav');
	$('#layui_nav_left_' + nav_id).show().siblings().hide();
});

$('.layui-nav-child').find('dd').find('a').click(function () {
	var url = $(this).data('url');
	$('.layui-iframe').attr('src', url);
});