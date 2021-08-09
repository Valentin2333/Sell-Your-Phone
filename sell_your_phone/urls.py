from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from sell_your_phone import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('sell_your_phone.common.urls')),
                  path('phones/', include('sell_your_phone.phones.urls')),
                  path('accounts/', include('sell_your_phone.accounts.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
