from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'




'''

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email','phone')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

# Re-register UserAdmin
admin.site.register(User, UserAdmin)




# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = models.Profile
    can_delete = False
    verbose_name_plural = 'Profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)



'''