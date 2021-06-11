from django.contrib import admin

# Register your models here.
from .models import Student,Emoloyee

admin.site.register(Student)
admin.site.register(Emoloyee)