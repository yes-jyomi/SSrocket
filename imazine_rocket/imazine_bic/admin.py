from django.contrib import admin
from .models import History
from .models import User
from .models import Course
from .models import Company
# Register your models here.

admin.site.register(History)
admin.site.register(User)
admin.site.register(Course)
admin.site.register(Company)