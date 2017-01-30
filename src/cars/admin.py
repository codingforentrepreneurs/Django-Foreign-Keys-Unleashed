from django.contrib import admin

# Register your models here.

from .models import Car

class CarAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__email', 'name', 'user__id']
    raw_id_fields = ['user']
    readonly_fields = ['updated_by']
    class Meta:
        model = Car

    def save_model(self, request, obj, form, change):
        # if not change:
        #     '''
        #     New obj
        #     '''
        #     obj.user = request.user
        # else:
        if change:
            obj.updated_by = request.user
        obj.save()


admin.site.register(Car, CarAdmin)