from django.conf.urls import url
from .apis import FavoriteListView, FavoriteSourceListView

urlpatterns = [
    url(r'^source_list/?$', FavoriteSourceListView.as_view(), name='source_lists'),
    url(r'^list/?$', FavoriteListView.as_view(), name='lists'),
]
