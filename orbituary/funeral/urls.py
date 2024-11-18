from django.urls import path
from . import views
from funeral.sitemaps import ObituarySitemap
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    path('submit_obituary/', views.submit_obituary, name='submit_obituary'),
    path('view_obituaries/', views.view_obituaries, name='view_obituaries'),
    path('obituary/<slug:slug>/', views.view_obituary_detail, name='view_obituary_detail'),
    path('sitemap.xml', sitemap, {'sitemaps': {'obituaries': ObituarySitemap}}),
]
