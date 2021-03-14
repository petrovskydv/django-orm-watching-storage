from django.shortcuts import render

from datacenter.models import Visit


def storage_information_view(request):
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at__isnull=True)
    for visit in visits:
        seconds = visit.get_duration()
        non_closed_visits.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': visit.entered_at,
                'duration': visit.format_duration(seconds),
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
