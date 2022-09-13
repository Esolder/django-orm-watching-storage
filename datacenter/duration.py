from datetime import datetime
from django.utils.timezone import localtime, now

def get_duration(visit):
    if not visit.leaved_at:
        return (now() - localtime(visit.entered_at)).total_seconds()
    return (localtime(visit.leaved_at) - localtime(visit.entered_at)).total_seconds()

def format_duration(duration):
    return datetime.fromtimestamp(duration).strftime('%H:%M:%S')