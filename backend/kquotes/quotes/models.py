from django.db import models
from django.conf import settings
from django.core import validators
from django.utils.translation import ugettext_lazy as _


class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="quote_scores",
                             verbose_name=_("user"))
    quote = models.ForeignKey("quotes.Quote", related_name="scores", verbose_name=_("quote"))
    score = models.IntegerField(default=0, verbose_name=_("score"),
                                validators=[validators.MinValueValidator(0),
                                validators.MaxValueValidator(5)])
    created_date = models.DateTimeField(null=False, blank=False, auto_now_add=True,
                                        verbose_name=_("created date"))

    class Meta:
        verbose_name = _("Score")
        verbose_name_plural = _("Scores")
        unique_together = ("user", "quote")


class Quote(models.Model):
    quote = models.TextField(null=False, blank=False, verbose_name=_("quote"))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                               related_name="quotes", verbose_name=_("author"))
    external_author = models.TextField(null=False, blank=True, verbose_name=_("external author"))
    explanation = models.TextField(null=False, blank=True, verbose_name=_("explanation"))

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                                related_name="quotes_created",
                                verbose_name=_("creator"))
    created_date = models.DateTimeField(null=False, blank=False, auto_now_add=True,
                                        verbose_name=_("created date"))

    users_rates = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='quotes_rated',
                                         blank=True, through="quotes.Score")

    class Meta:
        verbose_name = _("quote")
        verbose_name_plural = _("quotes")
        ordering = ["-created_date"]

    def __str__(self):
        return self.quote
