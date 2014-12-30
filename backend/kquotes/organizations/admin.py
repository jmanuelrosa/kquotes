from django.contrib import admin
from .models import Organization
from .models import Member


class MemberInline(admin.TabularInline):
    model = Member
    fields = ("organization", "user", "is_owner", "is_admin")
    extra = 0


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    inlines = [MemberInline]
