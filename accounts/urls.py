from django.urls import path
from . import views
from django.contrib.auth import views as djangoViews


urlpatterns = [
    path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),

    path('login/', djangoViews.LoginView.as_view(), name='login'),
    path('logout/', djangoViews.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),

    path('password_change/', djangoViews.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', djangoViews.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', djangoViews.PasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', djangoViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('rest/done/', djangoViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_reset/done/', djangoViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
]



