from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from allauth.account.decorators import verified_email_required
from mysite import models, forms
from datetime import datetime

def index(request):
    all_polls = models.Poll.objects.all().order_by('-created_at')
    paginator = Paginator(all_polls, 5)
    p = request.GET.get('p')

    try:
        polls = paginator.page(p)
    except PageNotAnInteger:
        polls = paginator.page(1)
    except EmptyPage:
        polls = paginator.page(paginator.num_pages)
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
def vote(request, pollid, pollitemid):
    target_url = '/poll/{}'.format( pollid)
    if models.VoteCheck.objects.filter(userid=request.user.id, pollid=pollid,
                                    vote_date = datetime.today()):
        return redirect(target_url)
    else:
        vote_rec = models.VoteCheck(userid=request.user.id, pollid=pollid,
                                    vote_date = datetime.today())
        vote_rec.save()
    try:
        pollitem = models.PollItem.objects.get(id = pollitemid)
    except:
        pollitem = None
    if pollitem is not None:
        pollitem.vote = pollitem.vote + 1
        pollitem.save()
    return redirect(target_url)

@login_required
def govote(request):
    try:
        is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

        votes = 0

        if (request.method != "GET") or (not is_ajax):
            return HttpResponse(votes)

        pollid = request.GET.get('pollid')
        is_voted = models.VoteCheck.objects.filter(userid=request.user.id, pollid=pollid, vote_date = datetime.today())

        if (not is_voted):
            pollitemid = request.GET.get('pollitemid')
            pollitem = models.PollItem.objects.get(id=pollitemid)
            pollitem.vote = pollitem.vote + 1
            pollitem.save()
            votes = pollitem.vote

            vote_rec = models.VoteCheck(userid=request.user.id, pollid=pollid, vote_date = datetime.today())
            vote_rec.save()

        return HttpResponse(votes)
    except:
        votes = 0
        return HttpResponse(votes)
    
@login_required
def addpollitem(request, pollid=''):
    if request.method == 'POST':
        pollid = request.POST['pollid']
        poll = models.Poll.objects.get(id=pollid)
        new_pollitem = models.PollItem(poll=poll)
        form = forms.PollItemForm(request.POST, instance=new_pollitem)
        if form.is_valid():

            form.save()
            return redirect('/addpollitem/'+pollid)
    else:
        form = forms.PollItemForm()

    poll = models.Poll.objects.get(id=pollid)
    pollitems = models.PollItem.objects.filter(poll=poll)
    return render(request, 'addpollitem.html', locals())

@login_required
def addpoll(request):
    if request.method == 'POST':
        username = request.user.username
        user = User.objects.get(username=username)
        new_poll = models.Poll(user=user)
        form = forms.PollForm(request.POST, instance=new_poll)
        if form.is_valid():
            form.save()
            return redirect('/addpoll')
    else:
        form = forms.PollForm()

    username = request.user.username
    user = User.objects.get(username=username)
    polls = models.Poll.objects.filter(user=user)
    return render(request, "addpoll.html", locals())

@login_required
def delpoll(request, pollid):
    try:
        poll = models.Poll.objects.get(id = pollid)
    except:
        pass
    if poll is not None:
        poll.delete()
    return redirect('/addpoll/')

@login_required
def delpollitem(request, pollid, pollitemid):
    try:
        pollitem = models.PollItem.objects.get(id = pollitemid)
    except:
        pass
    if pollitem is not None:
        pollitem.delete()
    return redirect('/addpollitem/{}/'.format(pollid))
