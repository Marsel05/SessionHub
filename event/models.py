from django.db import models
from django.contrib.auth.models import User


class Conference(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    organizers = models.OneToOneField(User, on_delete=models.CASCADE)


class Speaker(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='image/', null=True, blank=True)
    topics = models.CharField(max_length=100)


class Session(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    room = models.CharField(max_length=100)
    session_type = models.CharField(max_length=100)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    speaker = models.ManyToManyField(Speaker, related_name="speaker")


class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)


class Ticket(models.Model):
    participant = models.OneToOneField(Participant, on_delete=models.CASCADE)
    conference = models.OneToOneField(Conference, on_delete=models.CASCADE)
    CHOICES_TICKET = (
        ('ранняя регистрация', 'ранняя регистрация'),('стандартный билет', 'стандартный билет'), ('VIP-билет)', 'VIP-билет)')
    )
    ticket_type = models.CharField(choices=CHOICES_TICKET, max_length=100)
    price = models.PositiveIntegerField(default=0)
    CHOICES_TICKET = (
        ('Не Оплачено', 'Не Оплачено'),
        ('Оплачено', 'Оплачено'),
    )
    status = models.CharField(choices=CHOICES_TICKET, max_length=100)


class Notification(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    message = models.TextField()
    send_at = models.DateTimeField()


class Review(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=1, verbose_name='Оценка')
    comment = models.TextField()
    created_at = models.DateTimeField()


class Booking(models.Model):
    participant = models.OneToOneField(Participant, on_delete=models.CASCADE)
    session = models.OneToOneField(Session, on_delete=models.CASCADE)
    CHOICES_STATUS = (
        ('Подтверждено', 'Подтверждено'),('В ожидании', 'В ожидании')
    )
    status = models.CharField(choices=CHOICES_STATUS, max_length=100)






