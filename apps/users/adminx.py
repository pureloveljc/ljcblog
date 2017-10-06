# _*_ encoding:utf-8 _*_
_auther_ = "root"
_date_ = "2017-09-08 下午 9:34"
import xadmin
from .models import Tag,Cateory,Article,Ad,Comment,Links



class TagAdmin(object):
    list_display =['name']
    search_fields=['name']
    list_filter=['name']


class CateoryAdmin(object):
    list_display = ['name','index']
    search_fields =  ['name','index']
    list_filter =  ['name','index']


class ArticleAdmin(object):

    list_display = ['title', 'desc','content','click_count','is_recommend','date_published','user','category','tag']
    search_fields =  ['title', 'desc','content','click_count','is_recommend','date_published','user','category','tag']
    list_filter =  ['title', 'desc','content','click_count','is_recommend','date_published','user','category','tag']


class AdAdmin(object):
    pass

class CommentAdmin(object):
    pass

class LinksAdmin(object):
    pass



xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Cateory,CateoryAdmin)
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Ad,AdAdmin)
xadmin.site.register(Comment,CommentAdmin)
xadmin.site.register(Links,LinksAdmin)