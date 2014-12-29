from django.db import models
from django.utils.translation import ugettext_lazy as _

from kquotes.base.utils.slug import slugify_uniquely


class Organization(models.Model):
    name = models.CharField(null=False, blank=True, max_length=256, verbose_name=_("name"))
    slug = models.SlugField(null=False, blank=True, max_length=256, unique=True, verbose_name=_("slug"))

    created_date = models.DateTimeField(null=False, blank=False, auto_now_add=True, verbose_name=_("created date"))
    modified_date = models.DateTimeField(null=False, blank=False, auto_now=True, verbose_name=_("modified date"))

    class Meta:
        verbose_name = "organization"
        verbose_name_plural = "organizations"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_uniquely(self.name, self, max_length=256)
        super().save(*args, **kwargs)
