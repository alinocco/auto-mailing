import uuid
from datetime import datetime, timedelta
import pytz

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Operator(models.Model):
    name = models.CharField(max_length=32)
    index = models.IntegerField(unique=True)

    created_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=32)

    created_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Mailing(models.Model):
    start_date = models.DateTimeField(
        default=datetime.now(),
        validators=[MinValueValidator(datetime.now())])
    stop_date = models.DateTimeField(blank=True, null=True)
    message_text = models.TextField()
    operator = models.ForeignKey(Operator, on_delete=models.SET_NULL, blank=True, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    def __str__(self):
        return f'{self.start_date}-{self.stop_date} {self.message_text[:20]}...'

    def save(self, *args, **kwargs):
        if not self.stop_date:
            self.stop_date = self.start_date + timedelta(days=30) 

        super(Mailing, self).save(*args, **kwargs)

    class Meta:
        ordering = ['start_date']


class Customer(models.Model):
    phone = models.IntegerField(validators=[MinValueValidator(70000000000), MaxValueValidator(79999999999)])
    operator = models.ForeignKey(Operator, on_delete=models.SET_NULL, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, blank=True, null=True)

    TIMEZONES = tuple(zip(pytz.common_timezones, pytz.common_timezones))
    timezone = models.CharField(max_length=32, choices=TIMEZONES,  default='UTC')

    created_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    def __str__(self):
        return self.phone

    class Meta:
        ordering = ['phone']


class Message(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField()

    created_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    def __str__(self):
        return f'{self.created_date} {self.mailing} to {self.customer}'

    class Meta:
        ordering = ['is_sent']
