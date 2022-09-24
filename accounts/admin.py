from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CUCHANGEFORM, CUCREATIONFORM
from .models import CustomUser

class CUADMIN(UserAdmin):
    model = CustomUser
    form = CUCHANGEFORM
    add_form = CUCREATIONFORM
    list_display = (
        'username',
        'age',
        'email',
        'is_staff',
    )
    fieldsets = UserAdmin.fieldsets + ((None, {'fields' : ('age',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields' : ('age',)}),)

admin.site.register(CustomUser, CUADMIN)