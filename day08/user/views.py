from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from user.models import Teacher
from user.serializers import TeacherSerializer, TeacherDeSerializer


class TeacherAPIView(APIView):

    def get(self,request,*args,**kwargs):
        teacher_id = kwargs.get('id')
        if teacher_id:
            teacher_obj = Teacher.objects.filter(pk=teacher_id )
            if teacher_obj:
                teacher_serializer = TeacherSerializer(teacher_obj,many=True).data
                return Response({
                    'status':200,
                    'message':'查询单个教师成功',
                    'results':teacher_serializer
                })
            else:
                return Response({
                    'status':400,
                    'message':'该用户不存在'
                })
        else:
            teacher_objects_all = Teacher.objects.all()
            if teacher_objects_all:

                teachers_data = TeacherSerializer(teacher_objects_all,many=True).data
                return Response({
                    'status':200,
                    'message':'查询所有教师成功',
                    'results':teachers_data
                })
            else:
                return Response({
                    'status':400,
                    'message':'查询所有教师失败'
                })


    def post(self,request,*args,**kwargs):
        request_data = request.data
        print(request_data,22)
        if not isinstance(request_data,dict) or request_data == {}:
            return Response({
                'status':400,
                'message':'参数有误',
            })

        serializer = TeacherDeSerializer(data=request_data)

        if serializer.is_valid():
            teacher_ser = serializer.save()
            print(111111111)
            return Response({
                'status':200,
                'message':'教师添加成功',
                'results':TeacherSerializer(teacher_ser).data
            })
        else:
            return Response({
                'status':400,
                'message':'教师添加失败',
                'result':serializer.errors
            })



    def delete(self,request,*args,**kwargs):
        teacher_id = kwargs.get('id')
        if teacher_id:
            teacher_obj = Teacher.objects.get(pk=teacher_id)
            teacher_serializer = TeacherSerializer(teacher_obj).data
            try:
                teacher_obj.delete()
                return Response({
                    'status': 200,
                    "message": '删除成功',
                    'results':teacher_serializer
                })
            except:
                return Response({
                    'status': 400,
                    "message": '未找到该教师，删除失败'
                })
        else:
            return Response({
                'status': 404,
                "message": '页面未找到'
            })





