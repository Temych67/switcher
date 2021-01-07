from django.contrib import admin
from django.urls import path, include
from testapp import views
# from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
	path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', views.main_translater),
    ]


# urlpatterns = i18n_patterns (
# 	path('admin/', admin.site.urls),
# 	path('', views.main_translater),
# 	prefix_default_language = False,
# )