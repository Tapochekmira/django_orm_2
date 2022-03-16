from django.shortcuts import render

from datacenter.models import (
    Visit,
    get_duration,
    format_duration
)


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in visits:
        duration_at_second = get_duration(visit)
        ready_to_output_duration = format_duration(duration_at_second)
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': ready_to_output_duration,
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
