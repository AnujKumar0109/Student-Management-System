from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    # ==============================
    # SIGN UP
    # ==============================

    path(
        "signup/",
        views.signup,
        name="signup"
    ),


    # ==============================
    # LOGIN
    # ==============================

    path(
        "login/",
        views.user_login,
        name="login"
    ),


    # ==============================
    # LOGOUT
    # ==============================

    path(
        "logout/",
        views.user_logout,
        name="logout"
    ),


    # ==============================
    # PASSWORD RESET
    # ==============================

    # 1. Enter Email
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="registration/password_reset_form.html",
            success_url="/accounts/password-reset/done/",
        ),
        name="password_reset"
    ),


    # 2. Email Sent
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="registration/password_reset_done.html"
        ),
        name="password_reset_done"
    ),


    # 3. Set New Password
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="registration/password_reset_confirm.html",
            success_url="/accounts/password-reset-complete/",
        ),
        name="password_reset_confirm"
    ),


    # 4. Password Reset Complete
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registration/password_reset_complete.html"
        ),
        name="password_reset_complete"
    ),

]