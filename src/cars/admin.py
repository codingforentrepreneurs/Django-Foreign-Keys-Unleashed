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

    # def get_queryset(self, request):
    #     qs = super(CarAdmin, self).get_queryset(request)
    #     if request.user.is_superuser: #request.user.is_staff
    #         return qs
    #     return qs.filter(user=request.user)

    # def has_change_permission(self, request, obj=None):
    #     """
    #     means is staff (request.user.is_staff)
    #     """
    #     if not obj:
    #         return True 
    #     return obj.user == request.user or request.user.is_superuser

    # def get_readonly_fields(self, request, *args, **kwargs):
    #     if request.user.is_superuser:
    #         return []
    #     return ['user']


admin.site.register(Car, CarAdmin)