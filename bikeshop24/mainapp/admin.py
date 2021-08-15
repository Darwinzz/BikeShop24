from django import forms
from django.contrib import admin

from .models import *


class BicycleCategoryChoiceField(forms.ModelChoiceField):

    pass


class HelmetCategoryChoiceField(forms.ModelChoiceField):

    pass


class BicycleAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return BicycleCategoryChoiceField(Category.objects.filter(slug='Bicycle'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class HelmetAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return BicycleCategoryChoiceField(Category.objects.filter(slug='Helmet'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Bicycle, BicycleAdmin)
admin.site.register(Helmet, HelmetAdmin)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Customer)