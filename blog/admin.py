from django.contrib import admin
from .models import post
from .forms import loginform , Signupform

# Register your models here.
@admin.register(post)
class postmodeladmin(admin.ModelAdmin):
    list_display = ['id','title','desc']
    
# @admin.register(loginform)
# class loginmodeladmin(admin.ModelAdmin):
#     list_display = ['id','username','password']    
    
# @admin.register(Signupform)
# class signupmodeladmin(admin.ModelAdmin):
#     list_display = ['id','first_name','email', 'password1']