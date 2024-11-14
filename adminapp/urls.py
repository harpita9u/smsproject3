from django.urls import path , include
from . import views

urlpatterns=[
    path('',views.projecthomepage,name='projecthomepage'),
    path('printpagecall/', views.printpagecall, name='printpagecall'),
    path('printpageLogic/', views.printpageLogic, name='printpagelogic'),
    path('exceptionpagecall/',views.exceptionpagecall,name='exceptionpagecall'),
    path('exceptionpagelogic/',views.exceptionpagelogic,name='exceptionpagelogic'),
    path('randomcall/',views.randomcall,name='randomcall'),
    path('randomlogic/',views.randomlogic,name='randomlogic'),
    path('calculatorlogic/',views.calculatorlogic,name='calculatorlogic'),
    path('calculatorpagecall/',views.calculatorpagecall,name='calculatorpagecall'),
    path('add_task/',views.add_task,name='add_task'),
    path('<int:pk>/delete/',views.delete_task,name='delete_task'),
    path('UserRegisterlogic/',views.UserRegisterlogic,name='UserRegisterlogic'),
    path('UserRegisterPagecall/',views.UserRegisterPagecall,name='UserRegisterPagecall'),
    path('datetimepagelogic/',views.datetimepagelogic,name='datetimepagelogic'),
    path('datetimepagecall/',views.datetimepagecall,name='datetimepagecall'),
    path('add_student/',views.add_student,name='add_student'),
    path('student_list/',views.student_list,name='student_list'),
    path('UserLoginLogic/',views.UserLoginLogic,name='UserLoginLogic'),
    path('UserLoginPageCall/',views.UserLoginPageCall,name='UserLoginPageCall'),
    path('logout/', views.logout, name='logout'),
    path('upload_file/',views.upload_file,name='upload_file'),
    path('feedback_form/',views.feedback_form,name='feedback_form'),
]