from django.urls import path
from . import views


urlpatterns = [

    # ==========================================
    # STUDENT LIST
    # ==========================================

    path(
        "",
        views.student_list,
        name="student_list"
    ),


    # ==========================================
    # DASHBOARD
    # ==========================================

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),
    
    # ==========================================
    # HOST / ADMIN DASHBOARD
    # ==========================================

    path(
    "host-dashboard/",
    views.host_dashboard,
    name="host_dashboard"
    ),


    # ==========================================
    # ADD STUDENT
    # ==========================================

    path(
        "add/",
        views.student_add,
        name="student_add"
    ),


    # ==========================================
    # EXPORT EXCEL
    # ==========================================

    path(
        "export-excel/",
        views.export_students_excel,
        name="export_students_excel"
    ),


    # ==========================================
    # STUDENT ID CARD
    # ==========================================

    path(
        "<int:pk>/id-card/",
        views.student_id_card,
        name="student_id_card"
    ),
    
    path(
        "<int:pk>/id-card/pdf/",
        views.student_id_card_pdf,
        name="student_id_card_pdf"
        ),


    # ==========================================
    # EDIT STUDENT
    # ==========================================

    path(
        "<int:pk>/edit/",
        views.student_edit,
        name="student_edit"
    ),


    # ==========================================
    # DELETE STUDENT
    # ==========================================

    path(
        "<int:pk>/delete/",
        views.student_delete,
        name="student_delete"
    ),


    # ==========================================
    # STUDENT DETAIL
    # Keep this LAST because <int:pk>/ is generic
    # ==========================================
    path(
    "profile/",
    views.profile,
    name="profile"),
    

    path(
        "<int:pk>/",
        views.student_detail,
        name="student_detail"
    ),

]