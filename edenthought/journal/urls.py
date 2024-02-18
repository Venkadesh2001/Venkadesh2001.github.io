from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.homepage,name=''),
    path('register',views.register,name='register'),
    path('my-login',views.my_login,name='my-login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('create-thought',views.create_thought,name='create-thought'),
    path('view-thought',views.view_thoughts,name='view-thought'),
    path('update-thought/<str:pk>',views.update_thought,name='update-thought'),
    path('delete-thought/<str:pk>',views.delete_thought,name='delete-thought'),
    path('profile-management',views.profile_management,name='profile-management'),
    path('delete-account',views.delete_account,name='delete-account'),
    path('logout',views.logout,name='logout'),


    #Password management

    #step 1 : Allow us to enter our email in order to receive a password

    path('reset_password',auth_views.PasswordResetView.as_view(template_name = 'journal/password-reset.html'),name = 'reset_password'),

    # step 2 : show a success messagge stating that an email was sent to reset our password

    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name = 'journal/password-reset-sent.html'),name = 'password_reset_done'),

    # step 3 : send a link to our email, so that we can reset our password

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'journal/password-reset-form.html'),name = 'password_reset_confirm'),

    # step 4: show a success message that our password was changed

    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name = 'journal/password-reset-complete.html'),name = 'password_reset_complete'),
    
]