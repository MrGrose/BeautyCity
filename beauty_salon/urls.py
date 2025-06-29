from beauty_salon.api import (api_dates, api_masters, api_salons, api_services,
                              api_timeslots)
from beauty_salon.views import (index, notes, privacy_policy, service,
                                service_finally, view_call_me, view_feedback,
                                view_login, view_manager, view_register,
                                view_tips)
from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "beauty_salon"

urlpatterns = [
    path("", index, name="index"),
    path("service/", service),
    path("service-finally/", service_finally, name="service_finally"),
    path("notes/", notes, name="notes"),

    path("register/", view_register, name="register"),
    path("login/", view_login, name="login"),
    path("logout/", LogoutView.as_view(next_page="beauty_salon:index"), name="logout"),
    path("call/", view_call_me, name="call_me"),
    path("feedback/", view_feedback, name="feedback"),
    path("manager/", view_manager, name="manager"),
    path("privacy-policy/", privacy_policy, name="privacy_policy"),
    path("tips/", view_tips, name="view_tips"),

    path('api/salons/', api_salons, name='api_salons'),
    path('api/masters/', api_masters, name='api_masters'),
    path('api/services/', api_services, name='api_services'),
    path('api/timeslots/', api_timeslots, name='api_timeslots'),
    path('api/dates/', api_dates, name='api_dates'),

    path('payment/create/<int:appointment_id>/', views.create_payment, name='create_payment'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/fail/', views.payment_fail, name='payment_fail'),
    path('yookassa-webhook/', views.yookassa_webhook, name='yookassa_webhook'),
    path("tips/pay/<int:appointment_id>/", views.create_tips_payment, name="create_tips_payment"),
]
