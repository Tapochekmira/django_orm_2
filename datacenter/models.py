from datetime import datetime

from django.db import models
from django.utils.timezone import make_aware


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def get_duration(visit):
    entry_time = visit.entered_at
    if visit.leaved_at:
        duration = visit.leaved_at - entry_time
        delta_in_seconds = duration.total_seconds()
    else:
        now_time = make_aware(datetime.now())
        delta_in_seconds = int((now_time - entry_time).total_seconds())
    return delta_in_seconds


def format_duration(duration):
    ready_to_output = f'{duration // 3600}:{duration % 3600 // 60}:{duration % 60}'
    return ready_to_output


def is_visit_long(visit, minutes=60):
    duration_in_second = get_duration(visit)
    second = minutes * 60
    return duration_in_second > second
