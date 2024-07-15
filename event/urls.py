from .views import *
from django.contrib.auth.urls import path


urlpatterns = [
    path('conference/', ConferenceViewSets.as_view({'get': 'list', 'post': 'create'}), name='conference_list'),
    path('conference/<int:pk>/', ConferenceViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': "destroy"}), name='conference_detail'),

    path('session/', SessionViewSets.as_view({'get': 'list', 'post': 'create'}), name='session_list'),
    path('session/<int:pk>/', SessionViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': "destroy"}),
         name='session_detail'),

    path('participant/', ParticipantViewSets.as_view({'get': 'list', 'post': 'create'}), name='participant_list'),
    path('participant/<int:pk>/', ParticipantViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': "destroy"}),
         name='participant_detail'),

    path('booking/', BookingViewSets.as_view({'get': 'list', 'post': 'create'}), name='booking_list'),
    path('booking/<int:pk>/', BookingViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': "destroy"}),
         name='booking_detail'),

    path('speaker/', SpeakerViewSets.as_view({'get': 'list', 'post': 'create'}), name='speaker_list'),
    path('speaker/<int:pk>/', SpeakerViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': "destroy"}),
         name='speaker_detail'),

    path('ticket/', TicketViewSets.as_view({'get': 'list', 'post': 'create'}), name='ticket_list'),
    path('ticket/<int:pk>/', TicketViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': "destroy"}),
         name='ticket_detail'),

    path('notification/', NotificationViewSets.as_view({'get': 'list', 'post': 'create'}), name='notification_list'),
    path('notification/<int:pk>/', NotificationViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': "destroy"}),
         name='notification_detail'),

    path('review/', ReviewViewSets.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('review/<int:pk>/', ReviewViewSets.as_view({'get': "retrieve", 'put': 'update', 'delete': "destroy"}),
         name='review_detail'),


]