from django.db import models
from django.contrib.auth.models import User
from extensions.utils import datetime_to_jalali_str
from django.urls import reverse

# Create your models here.


class URL(models.Model):
    STATUS_CHOICES = (
        ('E', 'فعال'),
        ('D', 'غیر فعال'),
    )
    address = models.URLField(max_length=256, verbose_name="آدرس لینک")
    visits = models.PositiveIntegerField(default=0, verbose_name="تعداد بازدیدها")
    created = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='urls', verbose_name='ایجادکننده')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت', 
                              default=STATUS_CHOICES[0][0])

    def __str__(self):
        return self.address

    def jcreated(self):
        return datetime_to_jalali_str(self.created)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_images', verbose_name='تصویر نمایه')
    birthdate = models.DateField(blank=True, verbose_name="تاریخ تولد")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Code(models.Model):
    slug = models.SlugField(max_length=6, verbose_name="کلید", unique=True)
    target = models.OneToOneField(URL, on_delete=models.CASCADE, 
                                  related_name='code', verbose_name='مقصد')

    def __str__(self):
        return reverse('url_shortener') + self.code
