from django.db import models

# Create your models here.
class Category(models.Model):
    '''分类
    '''
    name = models.CharField(max_length = 50,verbose_name = '名称')
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    '''
    标签
    '''
    name = models.CharField(max_length = 20, verbose_name = '名称')

    def __str__(self):
        return self.name

class Blog(models.Model):
    '''
    博客
    '''
    title = models.CharField(max_length = 50, verbose_name = '标题')
    author = models.CharField(max_length = 50, verbose_name = '作者')
    content = models.TextField(verbose_name = '正文')
    createdTime = models.DateTimeField(verbose_name = '发布时间', auto_now_add = True)
    category = models.ForeignKey(Category, verbose_name = '分类')
    tags = models.ManyToManyField(Tag, blank = True, null = True, verbose_name ='标签')

    def __str__(self):
        return self.title

class Comment(models.Model):
    '''
    评论
    '''
    blog = models.ForeignKey(Blog, verbose_name = '博客')
    name = models.CharField(max_length = 50, verbose_name = '评论者')
    email = models.EmailField(verbose_name = '邮箱')
    content = models.CharField(max_length = 100, verbose_name = '评论内容')
    createdTime = models.DateTimeField(verbose_name = '发布时间', auto_now_add = True)
