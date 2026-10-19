from django.contrib import admin

from users.models import User

admin.site.site_title = "后台管理系统"
admin.site.site_header = "后台管理"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_per_page = 20  # 每页显示条数

    fieldsets = (
        (
            "基本信息",
            {
                "fields": (
                    "openid",
                    "username",
                    "password",
                )
            },
        ),
        (
            "联系方式",
            {
                "fields": ("phone", "email"),
            },
        ),
        (
            "权限",
            {
                "fields": ("is_active", "is_superuser", "is_staff")
            }
        )
    )

    list_display = ["id", "username"]
    list_display_links = ["id", "username"]
