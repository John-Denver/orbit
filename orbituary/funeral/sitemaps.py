from django.contrib.sitemaps import Sitemap
from .models import Obituary
from django.urls import reverse

class ObituarySitemap(Sitemap):
    def items(self):
        return Obituary.objects.all()

    def location(self, obituary):
        return reverse('view_obituary_detail', args=[obituary.slug])

    def lastmod(self, obituary):
        return obituary.submission_date
