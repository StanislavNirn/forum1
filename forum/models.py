from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
import os


class User(AbstractUser):
    def imagepath(instance,filename):
        ext = filename.split('.')[-1]
        filename = 'avatar.{}'.format(ext)
        val="avatars/" + str(instance.username) + "/" + str(filename)

        if os.path.exists(val):
            os.remove(val)
        return val
            
    avatar = models.ImageField(upload_to=imagepath, height_field='', width_field='', blank=True)
    posts = models.IntegerField(default=0)
    replies = models.IntegerField(default=0)

    def __str__(self):
        return 'ID: {}, Пользователь: {}'.format(self.id, self.username)

class Discussao(models.Model):
    class Meta:
        verbose_name = "тема"
        verbose_name_plural = "темы"
    
    titulo = (models.CharField(max_length=200))

    def __str__(self):
        return 'Тема: {}'.format(self.titulo)

class Topico(models.Model):
    class Meta:
        verbose_name = "вопрос"
        verbose_name_plural = "вопросы"

    discussao_fk = models.ForeignKey(Discussao, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = RichTextField()
    data_postagem = models.DateField(default=timezone.now)

    def __str__(self):
        return 'Название: {}, Автор: {}, ID: {}'.format(self.titulo, self.autor, self.id)

class Resposta(models.Model):
    topico_fk = models.ForeignKey(Topico, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = RichTextField()
    data_postagem = models.DateField(default=timezone.now)
    class Meta:
        verbose_name = "ответ"
        verbose_name_plural = "ответы"

    def __str__(self):
        return 'Название: {}, Автор: {}, ID: {}'.format(self.topico_fk.id, self.autor, self.id)

