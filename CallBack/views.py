from django.http import JsonResponse ,HttpResponse
from CallBack import models
from django.views import View
import requests
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import time ,datetime

class Alarm(View):

    def get(self,request):
        rest

    def post(self,request):

        userId = request.POST.get('userId')
        alertName = request.POST.get('alertName')
        timestamp = request.POST.get('timestamp')
        alertState = request.POST.get('alertState')
        dimensions = request.POST.get('dimensions')
        expression = request.POST.get('expression')
        curValue  = request.POST.get('curValue')
        metricName = request.POST.get('metricName')
        metricProject = request.POST.get('metricProject')
        timestamp = int(timestamp)
        timestamp = time.localtime(timestamp)
        timestamp = time.strftime("%Y-%m-%d",timestamp)

        warring = models.MonitorInfo.objects.update_or_create(userId=userId,alertName=alertName,timestamp=timestamp,alertState=alertState,dimensions=dimensions,expression=expression,curValue=curValue,metricName=metricName,metricProject=metricProject)
        url = "https://oapi.dingtalk.com/robot/send?access_token=0fbf617e24a2eaea1ad8fcd5e08823cd0a39cf54dd5e79b334c4bbe6c66a3044"
        HEADERS = {
            "Content-Type": "application/json ;charset=utf-8 "
        }
        # message = {
        #     'monitor': 'xbay',
        #     '用户ID': userId,
        #     '告警名称': alertName,
        #     '告警时间': timestamp,
        #     '告警状态': alertState,
        #     '发生报警的对象': dimensions,
        #     '告警条件': expression,
        #     '告警值': curValue,
        #     '监控项名称': metricName,
        #     '产品名称': metricProject,
        # }
        js = json.loads(dimensions)
       # res = [item[key] for item in list for key in item]
        data = {
            "msgtype": "markdown",
            "monitor": "xbay",
            "markdown": {
              "title":"项目单测情况",
              "text": "#### 啊啊啊我要报警啦 @所有人\n" +
              "#### __介个东西报警啦__:{}\n".format(metricName) +
              "#### __发生报警的对象__:{}\n".format(js[0]['instanceId']) +
              "#### __告警时间__:{}\n".format(timestamp) +
              "#### __告警状态__:{}\n".format(alertState) +
              "#### __告警值__:{}\n".format(curValue) +
              "#### __主机名称__:{}\n".format(metricProject) +
              "> ###### monitor \n"
         },
            "at": {
                "isAtAll": 0  # @全体成员（在此可设置@特定某人）
            }
        }

        data = json.dumps(data,sort_keys=True,indent=2)
        request = requests.post(url, data=data, headers=HEADERS)
        return HttpResponse(request.text)
