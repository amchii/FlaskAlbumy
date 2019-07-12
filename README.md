来自于李辉的Flask书上的示例程序：[Albumy](https://github.com/greyli/albumy) , 个人意见向地改进了少许代码，修复了一些已知bug :

1. [新评论未进行`photo.can_comment`验证的bug](https://github.com/greyli/albumy/issues/24)

   [`if not photo.can_comment`](https://github.com/amchii/FlaskAlbumy/blob/5aae074617bf96a7ab7c7febc9b07e057530bfda/albumy/blueprints/main.py#L283)

   

2. [收藏关注时登陆后的跳转问题](https://github.com/greyli/albumy/issues/22)

   [`if request.method.lower() == 'get':`](https://github.com/amchii/FlaskAlbumy/blob/5aae074617bf96a7ab7c7febc9b07e057530bfda/albumy/blueprints/main.py#L335)

   

3. [鼠标在头像上悬浮的时候出现的用户信息不能即时更新](https://github.com/greyli/albumy/issues/16)

   [`$el.popover('dispose');`](https://github.com/amchii/FlaskAlbumy/blob/5aae074617bf96a7ab7c7febc9b07e057530bfda/albumy/static/js/script.js#L75)

   

4. [关注页分页的bug](https://github.com/greyli/albumy/issues/25)

   [`pagination = user.following.filter(Follow.followed_id != user.id).paginate(page=page, per_page=per_page)`](https://github.com/amchii/FlaskAlbumy/blob/4fe090fc04b1e40120d85105f919a910f4fd386b/albumy/blueprints/user.py#L96)

   

5. 评论区评论时间的tooltip显示当前时间的bug

   

   ​		给`tooltip`的title传递函数可以正常显示，和Bluelog相同。

 6. 更换头像时若上传图片后不更新头像，则`user.avatar_raw`会被取代

    ​	这个通过给User新建一个`avatar_raw_temp`字段，用于保存上传头像原图时的文件名。在	   `change_avatar.html` 和更换头像的视图函数中通过`has_temp`参数进行判断

    

    

    