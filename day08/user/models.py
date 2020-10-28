from django.db import models

# Create your models here.
class Teacher(models.Model):
    gender_choices = (
        (0,'male'),
        (1,'female'),
        (2,'other'),
    )

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=60)
    gender = models.SmallIntegerField(choices=gender_choices,default=0)
    course = models.CharField(max_length=100)
    phone = models.CharField(max_length=11,null=True,blank=True)
    head_pic = models.ImageField(upload_to='pic/',default='pic/1.jpg')


    class Meta:
        db_table = 'teacher'
        verbose_name = '教师'
        verbose_name_plural = verbose_name



    def __str__(self):
        return self.username