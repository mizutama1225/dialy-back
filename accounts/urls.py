from django.urls import path
from accounts import views

urlpatterns = [
    path("accounts/", views.user_list),
    path("accounts/<str:pk>/", views.user_detail)

]