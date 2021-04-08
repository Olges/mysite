# соединение всех частей проекта через ссылки на приложения

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
# добавление соотношение статических файлов
# только на период разработки
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    # перенаправляет на приложение accounts если в url ничего не указывать кроме основного сайта
    # path('', RedirectView.as_view(url='/accounts/', permanent=True)),
]

# добавление статичных файлов
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)