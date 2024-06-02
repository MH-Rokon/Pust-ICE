from django.shortcuts import render
from notice.models import event,notice,AdmissionNotice,Research



def home(request):
    # Fetching the first five notices, events, and research entries
    first_five_notices = notice.objects.all()[:5]
    first_five_events = event.objects.all()[:5]
    first_five_research = Research.objects.all()[:5]
    
    return render(request, 'home.html', {
        'first_five_notices': first_five_notices,
        'first_five_events': first_five_events,
        'first_five_research': first_five_research,
    })
