from django.shortcuts import render

from datacenter.models import (
    Visit,
    is_visit_long,
    Passcard,
    get_duration,
    format_duration
)


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        duration_at_second = get_duration(visit)
        ready_to_output_duration = format_duration(duration_at_second)

        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': ready_to_output_duration,
                'is_strange': is_visit_long(visit)
            }
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
