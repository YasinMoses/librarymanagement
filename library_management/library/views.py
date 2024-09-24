from datetime import timezone
from rest_framework import viewsets
from .models import Book, Member, Transaction
from .serializers import BookSerializer, MemberSerializer, TransactionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        transaction = self.get_object()
        # Assume rent fee calculation logic here
        transaction.date_returned = timezone.now()
        rent_fee = 100  # Example rent fee calculation
        transaction.rent_fee = rent_fee
        transaction.member.outstanding_debt += rent_fee
        if transaction.member.outstanding_debt > 500:
            return Response({"error": "Outstanding debt exceeds KES 500."}, status=400)
        transaction.save()
        transaction.member.save()
        return Response({'status': 'book returned'})
