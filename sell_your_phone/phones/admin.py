from django.contrib import admin

from sell_your_phone.phones.models import Phone


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('brand', 'phone_model', 'year', 'likes_count')

    def likes_count(self, obj):
        return obj.like_set.count()


admin.site.register(Phone, PhoneAdmin)
