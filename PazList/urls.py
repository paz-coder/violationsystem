
from django.contrib import admin
from django.urls import path
from mypage import views
from django.contrib.auth.views import LoginView,LogoutView


#-------------FOR ADMIN RELATED URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),


    path('aboutus', views.aboutus_view),
   


    path('adminclick', views.adminclick_view),
    path('teacherclick', views.teacherclick_view),
    path('studentclick', views.studentclick_view),

    path('adminsignup', views.admin_signup_view),
 
    path('adminlogin', LoginView.as_view(template_name='mypage/adminlogin.html')),
    path('teacherlogin', LoginView.as_view(template_name='mypage/teacherlogin.html')),



    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='mypage/index.html'),name='logout'),


    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-teacher', views.admin_teacher_view,name='admin-teacher'),
    path('admin-view-teacher', views.admin_view_teacher_view,name='admin-view-teacher'),
    path('delete-teacher-from-school/<int:pk>', views.delete_teacher_from_school_view,name='delete-teacher-from-school'),
    path('update-teacher/<int:pk>', views.update_teacher_view,name='update-teacher'),
    path('admin-add-teacher', views.admin_add_teacher_view,name='admin-add-teacher'),
    path('admin-approve-teacher', views.admin_approve_teacher_view,name='admin-approve-teacher'),
    path('approve-teacher/<int:pk>', views.approve_teacher_view,name='approve-teacher'),
    path('reject-teacher/<int:pk>', views.reject_teacher_view,name='reject-teacher'),
    
    path('admin-student', views.admin_student_view,name='admin-student'),
    path('admin-view-student', views.admin_view_student_view,name='admin-view-student'),
    path('delete-student-from-school/<int:pk>', views.delete_student_from_school_view,name='delete-student-from-school'),
    path('update-student/<int:pk>', views.update_student_view,name='update-student'),
    path('admin-add-student', views.admin_add_student_view,name='admin-add-student'),

    path('admin-appointment', views.admin_appointment_view,name='admin-appointment'),
    path('admin-view-appointment', views.admin_view_appointment_view,name='admin-view-appointment'),
    path('admin-add-appointment', views.admin_add_appointment_view,name='admin-add-appointment'),
    path('admin-approve-appointment', views.admin_approve_appointment_view,name='admin-approve-appointment'),
    path('approve-appointment/<int:pk>', views.approve_appointment_view,name='approve-appointment'),
    path('reject-appointment/<int:pk>', views.reject_appointment_view,name='reject-appointment'),
]





