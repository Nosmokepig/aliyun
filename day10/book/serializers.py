from rest_framework import serializers
from book.models import Book, Press, User


class BookListSerializer(serializers.ListSerializer):

    def update(self, instance, validated_data):
        for index,obj in enumerate(instance):
            self.child.update(obj,validated_data[index])
        return instance
class PressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Press
        fields = ('press_name','address')
class BookModelSerializer(serializers.ModelSerializer):
    publish = PressModelSerializer()
    class Meta:
        model = Book
        fields = ('book_name','price','publish','authors','pic',)
        list_serializer_class = BookListSerializer

        extra_kwargs = {
            "book_name":{
                'required':True,
                'min_length':2,
                'error_messages':{
                    'required':'请输入书名',
                    'min_length':'书名太短',
                }
            },
            'pic':{
                'write_only':True
            },
            'authors':{
                'write_only':True
            },
        }
    def validate(self, attrs):
        pass

    def validate_book_name(self, obj):
        pass
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','gender')
        extra_kwargs = {
            "username":{
                'required':True,
                'min_length':2,
                'error_messages': {
                    'required': '请输入书名',
                    'min_length': '书名太短',
                }
            },
            "password":{
                'required':True,
                'min_length':6,
                'error_messages': {
                    'required': '请输入密码',
                    'min_length': '密码太短',
                }
            },
        }