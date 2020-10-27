import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from user_app.models import User

@method_decorator(csrf_exempt,name='dispatch')
class UserView(View):

    # get 请求

    def get(self,request,*args,**kwargs):
        user_id = kwargs.get('id')

        if user_id:
            user_res = list(User.objects.filter(pk=user_id))
            if user_res:
                return JsonResponse({
                    'status':200,
                    'message':'查询单个用户成功',
                    'results':user_res
                },safe=False,json_dumps_params={'default': self.json_str})
        else:
            user_all = list(User.objects.all())
            if user_all:
                return JsonResponse({
                    'status':200,
                    'message':'查询所有用户成功',
                    'results':user_all
                },safe=False,json_dumps_params={'default':self.json_str})
        return JsonResponse({
            'status':400,
            'message':'查询失败'
        })

    # 转json字符串方法
    def json_str(self,u):
        if isinstance(u,User):
            return {'id':u.id,'name':u.username,'gender':u.gender}
        else:
            print(type(u))

    # post请求

    def post(self,request,*args,**kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user_add = User.objects.create(username=username,password=password)
            return JsonResponse({
                'status':200,
                'message':'新增单个用户成功',
                'results':{'username':user_add.username,'gender':user_add.gender}
            })

        except:
            return JsonResponse({
                'status':400,
                'message':'新增失败'
            })

    def delete(self,request,*args,**kwargs):
        id = kwargs.get('id')
        if id:
            try:
                user_obj = User.objects.get(pk=id)
                user_obj.delete()
                return JsonResponse({
                    'status':200,
                    "message":'删除成功'
                })
            except:
                return JsonResponse({
                    'status':400,
                    'message':'未找到用户,删除失败'
                })
        else:
            return JsonResponse({
                'status':400,
                'message':'删除失败'
            })

