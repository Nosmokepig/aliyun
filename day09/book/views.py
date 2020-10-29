from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response

# Create your views here.
from book.models import Book
from book.serializers import BookModelSerializer, BookDeModelSerializer


class BookAPIView(APIView):
    def get(self,request,*args,**kwargs):

        book_id = kwargs.get('id')

        if book_id:
            book = Book.objects.filter(pk=book_id)
            if book:
                data = BookModelSerializer(book,many=True).data

                return Response({
                    'status':200,
                    'message':'查询单本书成功',
                    'results':data
                })
            else:
                return Response({
                    'status':400,
                    'message':'该书不存在',
                })
        else:
            books = Book.objects.all()
            data = BookModelSerializer(books,many=True).data

            return Response({
                'status':200,
                'message':'查询所有书成功',
                'results':data,
            })


    def post(self,request,*args,**kwargs):
        request_data = request.data
        print(request.data)
        if isinstance(request_data,dict):
            many = False
        elif isinstance(request_data,list):
            many = True

        else:
            return Response({
                'status':400,
                'message':'参数有误',
            })
        serializer = BookDeModelSerializer(data=request_data,many=many)
        serializer.is_valid(raise_exception=True)
        book_obj = serializer.save()

        return Response({
            'status':200,
            'message':'添加图书成功',
            'results':BookModelSerializer(book_obj,many=many).data
        })
    def delete(self,request,*args,**kwargs):

        book_id = kwargs.get('id')
        if book_id:
            ids = [book_id]
        else:
            ids = request.data.get('ids')

        response = Book.objects.filter(pk__in=ids,is_delete=False).update(is_delete=True)
        if response:

            return Response({
                'status':200,
                'message':'删除成功',
            })

        return Response({
            "status": 400,
            "message": '删除失败'
        })
    def put(self, request, *args, **kwargs):
        request_data = request.data
        book_id = kwargs.get("id")
        if book_id:
            try:
                book_obj = Book.objects.get(pk=book_id)
            except Book.DoesNotExist:
                return Response({
                    "status": 400,
                    "message": '图书不存在'
                })
            serializer = BookDeModelSerializer(data=request_data, instance=book_obj)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "status": 200,
                "message": '修改成功',
                "results": BookModelSerializer(book_obj).data
            })
        else:
            return Response({
                "status": 400,
                "message": '修改错误',
            })
    def patch(self, request, *args, **kwargs):

        request_data = request.data
        book_id = kwargs.get("id")

        try:
            book_obj = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({
                "status": 400,
                "message": '图书不存在'
            })
        serializer = BookDeModelSerializer(data=request_data, instance=book_obj, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "status": 200,
            "message": '修改成功',
            "results": BookModelSerializer(book_obj).data
        })



