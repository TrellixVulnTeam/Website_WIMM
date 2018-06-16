from django.db import models
from django.db.models.fields import exceptions
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
<<<<<<< HEAD
from django.utils import timezone
=======
>>>>>>> c20bd6b7ac120328896a0ffab65bd760c25e2c51

class ReadNum(models.Model):
    read_num = models.IntegerField(default=0, verbose_name='阅读量')

    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class ReadNumExpandMethod():
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)
            readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk)
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:
<<<<<<< HEAD
            return 0

class ReadDetail(models.Model):
    date = models.DateField(default=timezone.now)
    read_num = models.IntegerField(default=0, verbose_name='阅读量')

    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
=======
            return 0
>>>>>>> c20bd6b7ac120328896a0ffab65bd760c25e2c51