from django.contrib import admin

from FINAL_EXAM.kids.models import Kid


@admin.register(Kid)
class KidAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'user', 'slug')
    list_per_page = 20
    list_filter = ('name', 'user')
    fieldsets = (
            ('Personal Info', {
                'fields': ('name', 'personal_photo', 'date_of_birth'),
            }),
            ('Parent info', {
                'fields': ('user',),
            }),
        )





