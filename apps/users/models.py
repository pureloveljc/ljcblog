# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

# 用户模型
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/defaut.png')
    qq = models.CharField(max_length=20, blank=True, null=True, unique=True, verbose_name='QQ号')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号')
    nick_name=models.CharField(max_length=50,verbose_name=u"昵称",default="")
    birday=models.DateField(verbose_name=u"生日",null=True,blank=True)#null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空。blank 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填，比如 admin 界面下增加 model 一条记录的时候。直观的看到就是该字段不是粗体
    gender=models.CharField(max_length=10,choices=(("male",u"男"),("female","女")),default="female")
    adderss=models.CharField(max_length=100,default=u"")
    image=models.ImageField(upload_to="image/%y/%m",default=u"image/default.png",max_length=100)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标签名称')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Cateory(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')
    index = models.IntegerField(default=999, verbose_name='分类的排序')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=500, verbose_name='文章描述')
    content = models.TextField(verbose_name='文章内容')
    click_count = models.IntegerField(default=0, verbose_name='点击量')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(User, verbose_name='用户')
    category = models.ForeignKey(Cateory, blank=True, null=True, verbose_name='分类')
    tag = models.ManyToManyField(Tag, blank=True, null=True,verbose_name='标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_published']

    def __unicode__(self):
        return self.title


        # 评论模型


class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='用户')
    article = models.ForeignKey(Article, blank=True, null=True, verbose_name='文章')
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-date_published']

    def __unicode__(self):
        return self.content


        # 友情链接


class Links(models.Model):
    title = models.CharField(max_length=50, verbose_name='链接标题')
    desc = models.CharField(max_length=200, verbose_name='链接描述')
    callback_url = models.URLField(verbose_name='url地址')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    index = models.IntegerField(default=999, verbose_name='排序')

    class Meta:
        verbose_name = '链接'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.title


        # 广告


class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name='广告标题')
    desc = models.CharField(max_length=200, verbose_name='广告描述')
    image_url = models.ImageField(upload_to='ad/%Y/%m', verbose_name='图片路径')
    callback_url = models.URLField(null=True, blank=True, verbose_name='url地址')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    index = models.IntegerField(default=999, verbose_name='排序')

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.title
