from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Presentation)
admin.site.register(Stage)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(UserSetting)


