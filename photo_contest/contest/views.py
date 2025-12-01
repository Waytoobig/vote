from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Count
from .models import Candidate, Vote
from .forms import VoteForm
import json

def index(request):
    """Home page showing contest information"""
    total_candidates = Candidate.objects.count()
    total_votes = Vote.objects.count()
    
    context = {
        'total_candidates': total_candidates,
        'total_votes': total_votes,
    }
    return render(request, 'contest/index.html', context)

def vote(request):
    """Voting page"""
    # Check if user has already voted
    if not request.session.session_key:
        request.session.create()
    
    session_key = request.session.session_key
    has_voted = Vote.objects.filter(user_session=session_key).exists()
    
    if has_voted:
        return redirect('results')
    
    candidates = Candidate.objects.all()
    
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            candidate = form.cleaned_data['candidate']
            Vote.objects.create(
                candidate=candidate,
                user_session=session_key
            )
            return redirect('contest:results')
    else:
        form = VoteForm()
    
    context = {
        'candidates': candidates,
        'form': form,
    }
    return render(request, 'contest/vote.html', context)

def results(request):
    """Results page - only accessible after voting"""
    if not request.session.session_key:
        request.session.create()
    
    session_key = request.session.session_key
    has_voted = Vote.objects.filter(user_session=session_key).exists()
    
    if not has_voted:
        return redirect('contest:vote')
    
    # Get voting results
    results = Candidate.objects.annotate(
        vote_count=Count('votes')
    ).order_by('-vote_count')
    
    total_votes = sum(candidate.vote_count for candidate in results)
    
    # Calculate percentages
    for candidate in results:
        if total_votes > 0:
            candidate.percentage = (candidate.vote_count / total_votes) * 100
        else:
            candidate.percentage = 0
    
    # Get user's vote
    user_vote = None
    try:
        user_vote = Vote.objects.get(user_session=session_key)
    except Vote.DoesNotExist:
        pass
    
    context = {
        'results': results,
        'total_votes': total_votes,
        'user_vote': user_vote,
    }
    return render(request, 'contest/results.html', context)

def get_vote_status(request):
    """API endpoint to check if user has voted"""
    if not request.session.session_key:
        request.session.create()
    
    session_key = request.session.session_key
    has_voted = Vote.objects.filter(user_session=session_key).exists()
    
    return JsonResponse({'has_voted': has_voted})