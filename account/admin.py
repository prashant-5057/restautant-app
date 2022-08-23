from django.contrib import admin
from account.models import  User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.


class UserModelAdmin(BaseUserAdmin):
    
    
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','email', 'name', 'is_admin')
    # list_filter = ('is_admin',)
    # fieldsets = (
    #     ('UserCredentials', {'fields': ('email', 'password')}),
    #     ('Personal info', {'fields': ('name','tc','like','save_post')}),
    #     ('Permissions', {'fields': ('is_admin',)}),
    # )
    # # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # # overrides get_fieldsets to use this attribute when creating a user.
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'name','tc', 'password1', 'password2'),
    #     }),
    # )
    # search_fields = ('email',)
    # ordering = ('email','id')
    ordering = ('email',)
    # filter_horizontal = ()


admin.site.register(User,UserModelAdmin)