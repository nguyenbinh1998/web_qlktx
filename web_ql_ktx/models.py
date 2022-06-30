from django.db import models
from django.contrib.auth.models import User


class RoomGroup(models.Model):
    name = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(max_length=200, unique=True)


class Room(models.Model):
    STATUS_CHOICES = (('8', '8 người'), ('10', '10 người'))
    EQUIPMENT_CHOICES = (('1', 'Phòng có điều hòa, nóng lạnh'), ('2', 'Phòng không điều hòa, nóng lạnh'))
    name = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    position = models.ForeignKey(RoomGroup, on_delete=models.CASCADE, related_name="rooms")
    student_number = models.PositiveIntegerField()
    type_room = models.CharField(max_length=20, choices=STATUS_CHOICES, default="10")
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    equipment = models.CharField(max_length=40, choices=EQUIPMENT_CHOICES, default="1")


class BookRoom(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="book_rooms")
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    start_open = models.DateTimeField()
    close = models.DateTimeField()

class FeedbackCategory(models.Model):
    FEEDBACK_CHOICES = ()
    type_feedback = models.CharField(max_length=50, choices=FEEDBACK_CHOICES)

class FeedbackRoomStatus(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedbacks")
    feedback_id = models.ForeignKey(FeedbackCategory, on_delete=models.CASCADE)

class FoodSelling(models.Model):
    name = models.CharField(max_length=50)

class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Notification(models.Model):
    title = models.CharField(max_length=50)
    content= models.TextField()

