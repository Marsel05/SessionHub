from .models import *
from rest_framework import serializers


class ConferenceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = '__all__'


class SessionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'


class ParticipantSerializers(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class SpeakerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'


class TicketSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class NotificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'