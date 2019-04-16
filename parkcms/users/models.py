from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user = models.CharField(max_length = 32,verbose_name='用户名')
    pwd = models.CharField(max_length = 32,verbose_name='密码')
    
    class Meta:
        ordering = ('id',)
        verbose_name = u'用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user