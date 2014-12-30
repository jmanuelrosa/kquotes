from django.contrib import admin

from .models import Quote
from .models import Score


class ScoreInline(admin.TabularInline):
    model = Score
    fields = ("user", "quote", "score")
    extra = 0


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    inlines = [ScoreInline]
