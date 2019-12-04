from django.db import models

class MonitorInfo(models.Model):
    userId = models.CharField(max_length=50,verbose_name='用户ID')
    alertName = models.CharField(max_length=200,verbose_name='报警名称')
    timestamp = models.DateTimeField()
    alertState = models.CharField(max_length=50,verbose_name='报警状态')
    dimensions = models.CharField(max_length=200,verbose_name='发生报警的对象')
    expression = models.CharField(max_length=200,verbose_name='报警条件')
    curValue = models.CharField(max_length=50,verbose_name='报警发生或恢复时监控项的当前值')
    metricName = models.CharField(max_length=100,verbose_name='监控项名称')
    metricProject = models.CharField(max_length=100,verbose_name='产品名称')

    # class Meta:
    #     verbose_name = '监控'
    #     verbose_name_plural = verbose_name
