from django.contrib import admin

from FINAL_EXAM.drawings.models import Drawing


@admin.register(Drawing)
class DrawingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'kid_owner_drawing_display', 'date_of_publication', 'user')
    ordering = ('pk',)
    list_filter = ('kid_owner_drawing', 'user')

    # date-based drilldown navigation by that field
    date_hierarchy = 'date_of_publication'

    list_per_page = 20

    def kid_owner_drawing_display(self, obj):
        return obj.kid_owner_drawing

    kid_owner_drawing_display.short_description = 'Kid owner of drawing'

    fieldsets = (
        ('Drawing Info', {
            'fields': ('drawing', 'description'),
        }),
        ('Additional Info', {
            'fields': ('kid_owner_drawing', 'user',),
        }),
    )
