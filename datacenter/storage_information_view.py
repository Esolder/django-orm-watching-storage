from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datetime import datetime
from django.utils.timezone import localtime
from datacenter.duration import get_duration, format_duration


def storage_information_view(request):
    non_closed_visits = []
    visitors_not_leaved = Visit.objects.filter(leaved_at__isnull=True)
    for visit in visitors_not_leaved:
        visitor_dict = {
            'who_entered': visit.passcard,
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(get_duration(visit)),
        }
        non_closed_visits.append(visitor_dict)
    
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)



