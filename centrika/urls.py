from django.urls import path
from .views import TransactionDetail

urlpatterns = [
    path(
        "transaction/<str:transaction_id>/",
        TransactionDetail.as_view(),
        name="transaction-detail",
    ),
]
