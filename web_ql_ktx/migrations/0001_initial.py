# Generated by Django 4.0.4 on 2022-06-18 06:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_feedback', models.CharField(choices=[], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FoodSelling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('student_number', models.PositiveIntegerField()),
                ('type_room', models.CharField(choices=[('8', '8 người'), ('10', '10 người')], default='10', max_length=20)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('equipment', models.CharField(choices=[('1', 'Phòng có điều hòa, nóng lạnh'), ('2', 'Phòng không điều hòa, nóng lạnh')], default='1', max_length=40)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='web_ql_ktx.roomgroup')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackRoomStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_ql_ktx.feedbackcategory')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_open', models.DateTimeField()),
                ('close', models.DateTimeField()),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web_ql_ktx.room')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_rooms', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]