# Generated by Django 5.0.7 on 2024-07-15 08:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('topics', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('organizers', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.conference')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('send_at', models.DateTimeField()),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.participant')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('room', models.CharField(max_length=100)),
                ('session_type', models.CharField(max_length=100)),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.conference')),
                ('speaker', models.ManyToManyField(related_name='speaker', to='event.speaker')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='Оценка')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.session')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.session'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Подтверждено', 'Подтверждено'), ('В ожидании', 'В ожидании')], max_length=100)),
                ('participant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='event.participant')),
                ('session', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='event.session')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(choices=[('ранняя регистрация', 'ранняя регистрация'), ('стандартный билет', 'стандартный билет'), ('VIP-билет)', 'VIP-билет)')], max_length=100)),
                ('price', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('Не Оплачено', 'Не Оплачено'), ('Оплачено', 'Оплачено')], max_length=100)),
                ('conference', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='event.conference')),
                ('participant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='event.participant')),
            ],
        ),
    ]
