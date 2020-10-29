from rest_framework import serializers

from book.models import Book,Press

class PressModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Press
        fields = ('press_name','address')

class BookModelSerializer(serializers.ModelSerializer):

    publish = PressModelSerializer()


    class Meta:
        model = Book

        fields = ('book_name','price','author_list','publish')

        # 查询深度

class BookDeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('book_name','price','publish','authors')

        extra_kwargs = {
            'book_name':{
                'required':True,
                'min_length':2,
                'error_messages':{
                    'required':'图书名必填',
                    'min_length':'图书名错误',
                }
            },
        }

    def validate(self, attrs):
        return attrs

    def validate_book_name(self,obj):
        return obj