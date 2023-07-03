from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from bookmark.views import BookmarkLV, BookmarkDV
from mysite.views import HomeView, UserCreateView, UserCreateDoneTV

urlpatterns = [
    path("admin/", admin.site.urls),
    #인증
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),

    path('', HomeView.as_view(), name='home'),
    path('blog/', include('blog.urls')),
    path('photo/', include('photo.urls')),

    path('bookmark/', include('bookmark.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)