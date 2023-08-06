"""
Created on 2022-05-04
@author:刘飞
@description:收藏模块序列化器
"""
from django.utils.translation import gettext as tr
from rest_framework import serializers
from xj_thread.models import Thread
from xj_comment.models import CommentAbstract
from .models import Favorite, FavoriteSource


class FavoriteSourceSerializers(serializers.ModelSerializer):
    """收藏来源表序列化器"""
    value = serializers.SerializerMethodField()

    class Meta:
        model = FavoriteSource
        fields = '__all__'

    def get_value(self, instance):
        return tr(instance.value)


class FavoriteSerializers(serializers.ModelSerializer):
    """收藏列表序列化器"""
    label_name = serializers.SerializerMethodField()

    class Meta:
        model = Favorite
        fields = '__all__'

    def get_label_name(self, instance):
        label_name = None
        # 根据收藏来源表和具体内容展示标签名称
        source_obj = instance.source_id
        if source_obj:
            if source_obj.value == 'thread':  # 信息表
                # 信息统计表更新数据
                thread_obj = Thread.objects.filter(id=instance.source_item_id).first()
                if thread_obj:
                    label_name = thread_obj.title
            elif source_obj.value == 'comment':  # 评论表
                thread_id = instance.thread_id
                if thread_id:
                    # 找到对应评论表
                    comment = CommentAbstract.get_student_db_model(thread_id=thread_id)
                    comment_obj = comment.objects.filter(id=instance.source_item_id).first()
                    if comment_obj:
                        label_name = comment_obj.message
            elif source_obj.value == 'user':  # 用户相关【暂时没有】
                pass
        return label_name
