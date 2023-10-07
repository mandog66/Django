from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from allauth.account.decorators import verified_email_required
from mysite import models

def index(request):
    polls = models.Poll.objects.all()
    return render(request, 'index.html', locals())

@login_required
# @verified_email_required
def poll(requset, pollid):
    try:
        poll = models.Poll.objects.get(id=pollid)
    except:
        poll = None
    if poll is not None:
        pollitems = models.PollItem.objects.filter(poll=poll).order_by('-vote')
    return render(requset, 'poll.html', locals())

@login_required
# @verified_email_required
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
