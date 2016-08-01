from django.db import models


class Market(models.Model):
    # Trading name of the marketplace
    name = models.CharField(max_length=200, null=True, blank=True)
    # Description of the marketplace suitable for a seller.
    description = models.CharField(max_length=200, null=True, blank=True)
    # URL of the market
    web_address = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
