from django.db import models


# from apps.user.models import User


class FavoriteSource(models.Model):
    class Meta:
        db_table = 'eh_favorite_source'
        verbose_name_plural = '收藏来源表'

    id = models.AutoField(verbose_name='ID', primary_key=True)
    value = models.CharField(verbose_name='值', max_length=255)

    def __str__(self):
        return self.value


class Favorite(models.Model):
    class Meta:
        db_table = 'eh_favorite'
        verbose_name_plural = '收藏表'

    id = models.AutoField(verbose_name='ID', primary_key=True)
    source_id = models.ForeignKey(verbose_name='收藏来源表ID', to=FavoriteSource, db_column='source_id', related_name='+',
                                  on_delete=models.DO_NOTHING)
    type = models.CharField(verbose_name='收藏类型', max_length=20)
    # user_id = models.ForeignKey(verbose_name='用户ID', to=User, db_column='user_id', related_name='+', on_delete=models.DO_NOTHING)
    user_id = models.BigIntegerField(verbose_name='用户ID', db_index=True)
    source_item_id = models.BigIntegerField(verbose_name='来源表数据id', db_index=True, null=True, blank=True)
    thread_id = models.BigIntegerField(verbose_name='信息表id', null=True, blank=True)  # [非必填]信息表id，否则分表后评论相关无法明确位置

    def __str__(self):
        return self.id
