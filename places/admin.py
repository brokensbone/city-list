from django.contrib import admin
from .models import Business, BusinessGroup, Location

class BusinessInline(admin.TabularInline):
    model = Business
    extra = 1  # Show one extra blank form for a new Business

class LocationAdmin(admin.ModelAdmin):
    inlines = [BusinessInline]
    list_display = ('__str__', 'address')

class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'business_group', 'location', 'category', 'date_opened', 'date_closed')
    list_filter = ('category', 'business_group')
    search_fields = ('name', 'notes')

admin.site.register(Location, LocationAdmin)
admin.site.register(Business, BusinessAdmin)
admin.site.register(BusinessGroup)
