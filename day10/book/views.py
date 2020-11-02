from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import viewsets
from book.models import Book, Press, User
from book.serializers import BookModelSerializer, UserModelSerializer


class BookGenericAPIView(GenericAPIView,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.CreateModelMixin,
                         mixins.UpdateModelMixin
                         ):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    lookup_field = 'id'
    def get(self,request,*args,**kwargs):
        if 'id' in kwargs:
            return self.retrieve(request,*args,**kwargs)
        else:
            return self.list(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args, **kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)
    def put(self,request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class UserViewSetView(viewsets.GenericViewSet,
                      mixins.CreateModelMixin
                      ):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def user_login(self,request,*args,**kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            is_exist = User.objects.get(username=username)
        except:
            return Response('用户名不存在')
        if is_exist:
            database_pwd = is_exist.password
            if database_pwd == password:
                return Response('登录成功，欢迎您：%s'%username)
            else:
                return Response('用户名或密码不正确')
    def register(self,request,*args,**kwargs):
        print(request.data)
        username = request.data.get('username')
        password = request.data.get('password')
        is_exist = User.objects.filter(username=username)
        if is_exist:
            return Response('用户名已存在，请重新注册')
        else:
            res = self.create(request,*args,**kwargs)
            return Response('创建成功用户名为：'+username)



