from django.conf import settings
from rest_framework import serializers

from user.models import Teacher

class TeacherSerializer(serializers.Serializer):

    username = serializers.CharField()
    course = serializers.CharField()
    phone = serializers.CharField()

    gender = serializers.SerializerMethodField()


    def get_gender(self,obj):
        return obj.get_gender_display()


    head_pic = serializers.SerializerMethodField()

    def get_head_pic(self,obj):
        return '%s%s%s'%('http://127.0.0.1:8000/',settings.MEDIA_URL,str(obj.head_pic))

class TeacherDeSerializer(serializers.Serializer):

    username = serializers.CharField(
        max_length=10,
        min_length=2,
        error_messages={
            'max_length':'名字太长',
            'min_length':'名字太短',
        }
    )
    gender = serializers.IntegerField()
    course = serializers.CharField()
    password = serializers.CharField()
    phone = serializers.CharField(
        max_length=11,
        min_length=11,
        error_messages={
            'max_length': '位数错误',
            'min_length': '位数错误',
        }
    )

    def create(self, validated_data):
        return Teacher.objects.create(**validated_data)

