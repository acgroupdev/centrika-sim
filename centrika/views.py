from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer


class TransactionDetail(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    lookup_field = "transaction_id"
