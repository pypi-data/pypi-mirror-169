"""
Created on 2022-05-03
@author:刘飞
@description:收藏表逻辑分发
"""
from rest_framework.views import APIView
from .services import FavoriteServices
from utils.custom_authorization import Authentication
from xj_user.utils.custom_authorization import CustomAuthentication
from utils.custom_response import util_response

f = FavoriteServices()


class FavoriteSourceListView(APIView):
    """
    get:收藏来源表列表
    """
    authentication_classes = (CustomAuthentication,)

    def get(self, request):
        data, error_text = f.favorite_source_list(request)
        return util_response(data=data)


class FavoriteListView(APIView):
    """
    get:收藏列表
    post:添加收藏
    delete:取消收藏
    """
    authentication_classes = (CustomAuthentication,)

    def get(self, request):
        data, error_text = f.favorite_list(request)
        return util_response(data=data)

    def post(self, request):
        data, error_text = f.favorite_add(request)
        return util_response(data=data)

    def delete(self, request):
        data, error_text = f.favorite_delete(request)
        return util_response(data=data)
