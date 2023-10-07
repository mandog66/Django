from django.shortcuts import render, redirect
from mysite import models

def index(request):
    pols = models.Poll.objects.all()
    return render(request, 'index.html', locals())

def poll(requset, pollid):
    try:
        poll = models.Poll.objects.get(id=pollid)
    except:
        poll = None
    if poll is not None:
        pollitems = models.PollItem.objects.filter(poll=poll).order_by('-vote')
    return render(requset, 'poll.html', locals())

def vote(requset, pollid, pollitemid):
    try:
        pollitem = models.PollItem.objects.get(id=pollitemid)
    except:
        pollitem = None
    if pollitem is not None:
        pollitem.vote = pollitem.vote + 1
        pollitem.save()
    target_url = '/poll/{}'.format(pollid)
    return redirect(target_url)
