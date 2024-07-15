from .serializers import *
from .models import *
from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class ReviewViewSets(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [DjangoFilterBackend, SearchFilter]


class ConferenceViewSets(viewsets.ModelViewSet):
    queryset = Conference.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    filterset_fields = ['title']
    search_fields = ['title']

class SessionViewSets(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


class ParticipantViewSets(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


class BookingViewSets(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


class SpeakerViewSets(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


class TicketViewSets(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


class NotificationViewSets(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]