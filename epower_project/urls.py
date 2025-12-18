from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views  # Core uygulamasındaki views dosyasını çağırıyoruz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),             # İşte sihirli satır: Boş sayfaya gelince home çalışsın
    path('hakkimizda/', views.about, name='about'),
    path('iletisim/', views.contact, name='contact'),
    path('kariyer/', views.career, name='career'),
    path('kvkk/', views.kvkk, name='kvkk'),
    path('sartlar-ve-kosullar/', views.terms, name='terms'),
    path('gizlilik-politikasi/', views.privacy, name='privacy'),
    path('urunler/', views.products, name='products'),
    path('haberler/', views.news, name='news'),
    path('haberler/<slug:slug>/', views.news_detail, name='news_detail'),
    path('hizmetler/', views.services, name='services'),
    path('urunler/disli-kutusu/', views.gearbox_detail, name='gearbox_detail'),
    path('urunler/diferansiyel/', views.differential_detail, name='differential_detail'),
    ]

# Resimlerin çalışması için:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)