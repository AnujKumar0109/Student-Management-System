from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # ==========================================
    # ADMIN
    # ==========================================

    path(
        'admin/',
        admin.site.urls
    ),


    # ==========================================
    # ACCOUNTS
    # ==========================================

    path(
        'accounts/',
        include('accounts.urls')
    ),


    # ==========================================
    # STUDENTS
    # ==========================================

    path(
        'students/',
        include('students.urls')
    ),


    # ==========================================
    # HOME
    # ==========================================

    path(
        '',
        lambda request:
            redirect('/accounts/signup/')
    ),

]


# ==========================================
# MEDIA FILES
# ==========================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    
    
    path("admin/", admin.site.urls),