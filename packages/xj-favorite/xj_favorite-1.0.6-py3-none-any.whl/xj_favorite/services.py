"""
Created on 2022-05-03
@author:刘飞
@description:收藏表逻辑处理
"""
import logging
from django.db.models import F
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import status
from rest_framework import serializers
from xj_thread.models import Thread, ThreadStatistic
from xj_comment.models import CommentAbstract
from .models import Favorite, FavoriteSource
from .serializers import FavoriteSerializers, FavoriteSourceSerializers
from .utils.custom_response import util_response

log = logging.getLogger()


class FavoriteServices:
    def __init__(self):
        pass

    @staticmethod
    def favorite_source_list(request):
        """
        收藏来源表列表
        """
        obj = FavoriteSource.objects.all()
        res = FavoriteSourceSerializers(obj, many=True)
        return res.data, None

    @staticmethod
    def favorite_list(request):
        """
        收藏列表
        """
        size = request.query_params.get('size', 10)
        page = request.query_params.get('page', 1)
        source_id = request.query_params.get('source_id')
        favorite_type = request.query_params.get('favorite_type')
        # print("> source_id, favorite_type:", source_id, favorite_type)
        if not all([source_id, favorite_type]):
            raise serializers.ValidationError('必传参数未传。')
        keys = 'source_id_id type user_id'.split()
        values = [source_id, favorite_type, request.user.get('user_id', None)]  # 当前返回的user是字典类型，这样就形成了边界检查，不至于报500。
        conditions = {k: v for k, v in zip(keys, values) if v}
        obj = Favorite.objects.filter(**conditions)
        paginator = Paginator(obj, size)
        try:
            obj = paginator.page(page)
        except PageNotAnInteger:
            obj = paginator.page(1)
        except EmptyPage:
            obj = paginator.page(paginator.num_pages)
        except Exception as e:
            log.error(f'收藏列表分页:{str(e)}')
            raise serializers.ValidationError(f'{str(e)}')
        res = FavoriteSerializers(obj, many=True)
        data = {'total': paginator.count, 'list': res.data}
        return data, None

    @staticmethod
    def favorite_add(request):
        """
        收藏新增
        """
        source_id = request.data.get('source_id')
        favorite_type = request.data.get('favorite_type')
        source_item_id = request.data.get('source_item_id')
        thread_id = request.data.get('thread_id')
        # 数据校验
        if not all([source_id, favorite_type, source_item_id]):
            raise serializers.ValidationError('必传参数未传。')
        if favorite_type not in ['likes', 'favorite', 'shares']:  # 这里类型现在只有有三个【likes，favorite，shares】
            raise serializers.ValidationError('没有这个收藏类型。')
        # 找到来源表对象，根据value值判断
        source_obj = FavoriteSource.objects.filter(id=source_id).first()
        if not source_obj:
            raise serializers.ValidationError('信息来源对象不存在。')

        # 构造数据
        conditions = {'source_id_id': source_id, 'type': favorite_type, 'source_item_id': source_item_id,
                      'user_id': request.user.get('user_id', None), 'thread_id': thread_id}
        # 判断有无收藏过
        old_obj = Favorite.objects.filter(**conditions)
        if old_obj:
            raise serializers.ValidationError('您已经收藏过这条信息了。')

        # 根据操作的表的不同来更新数据
        if source_obj.value == 'thread':  # 信息表
            # 信息统计表更新数据
            if favorite_type == 'likes':
                ThreadStatistic.objects.filter(thread_id=source_item_id).update(likes=F('likes') + 1)
            elif favorite_type == 'favorite':
                ThreadStatistic.objects.filter(thread_id=source_item_id).update(favorite=F('favorite') + 1)
            elif favorite_type == 'shares':
                ThreadStatistic.objects.filter(thread_id=source_item_id).update(shares=F('shares') + 1)
        elif source_obj.value == 'comment':  # 评论表
            if not thread_id:
                raise serializers.ValidationError('对应信息表id为必传。')
            # 找到对应评论表
            comment = CommentAbstract.get_student_db_model(thread_id=thread_id)
            # 评论信息更新
            if favorite_type == 'likes':
                comment.objects.filter(id=source_item_id).update(likes=F('likes') + 1)
            elif favorite_type == 'favorite':
                comment.objects.filter(id=source_item_id).update(favorite=F('favorite') + 1)
            elif favorite_type == 'shares':
                comment.objects.filter(id=source_item_id).update(shares=F('shares') + 1)
        elif source_obj.value == 'user':  # 用户相关【暂时没有】
            pass

        # 新增一条收藏表数据
        obj = Favorite.objects.create(**conditions)
        data = {"id": obj.id}
        return data, None

    @staticmethod
    def favorite_delete(request):
        """
        取消收藏
        """
        _id = request.data.get('id')
        fav_obj = Favorite.objects.filter(id=_id).first()
        if fav_obj:
            source_obj = fav_obj.source_id
            if source_obj:
                favorite_type = fav_obj.type
                source_item_id = fav_obj.source_item_id
                thread_id = fav_obj.thread_id
                # 根据操作的表的不同来更新数据
                if source_obj.value == 'thread':  # 信息表
                    # 信息统计表更新数据
                    if favorite_type == 'likes':
                        ThreadStatistic.objects.filter(thread_id=source_item_id).update(likes=F('likes') - 1)
                    elif favorite_type == 'favorite':
                        ThreadStatistic.objects.filter(thread_id=source_item_id).update(favorite=F('favorite') - 1)
                    elif favorite_type == 'shares':
                        ThreadStatistic.objects.filter(thread_id=source_item_id).update(shares=F('shares') - 1)
                elif source_obj.value == 'comment':  # 评论表
                    if thread_id:
                        # 找到对应评论表
                        comment = CommentAbstract.get_student_db_model(thread_id=thread_id)
                        # 评论信息更新
                        if favorite_type == 'likes':
                            comment.objects.filter(id=source_item_id).update(likes=F('likes') - 1)
                        elif favorite_type == 'favorite':
                            comment.objects.filter(id=source_item_id).update(favorite=F('favorite') - 1)
                        elif favorite_type == 'shares':
                            comment.objects.filter(id=source_item_id).update(shares=F('shares') - 1)
                elif source_obj.value == 'user':  # 用户相关【暂时没有】
                    pass
            fav_obj.delete()
        else:
            raise serializers.ValidationError('消息记录不存在。')
        return None, None
