from django.contrib import admin
from . import models


# admin paneli uchun registratsiyadan otish 
admin.site.register(models.Quiz)
admin.site.register(models.Question)
admin.site.register(models.Option)
admin.site.register(models.QuizTaker)
admin.site.register(models.Answer)
admin.site.register(models.Result)

# Register your models here.