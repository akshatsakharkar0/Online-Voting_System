from django.shortcuts import render, redirect
from .models import Election, Candidate, Vote, Voter
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def base(request):
    return render(request, 'voting/base.html',{})



def vote(request, election_id):
    election = Election.objects.get(id=election_id)
    candidates = Candidate.objects.filter(election=election)
    voter, created = Voter.objects.get_or_create(user=request.user)

    if voter.has_voted:
        return render(request, 'voting/error.html',{'message': "You have already voted in this election."})

    if request.method == 'POST':
        candidate_id = request.POST.get('candidate')
        candidate = Candidate.objects.get(id=candidate_id)
        Vote.objects.create(user=request.user, election=election, voted=True, candidate=candidate)
        voter.has_voted = True
        voter.save()
        messages.success(request, "Your vote has been successfully submitted.")
        return redirect('results', election_id=election.id)

    return render(request, 'voting/vote.html', {'election': election, 'candidates': candidates})


@login_required
def election_list(request):
    elections = Election.objects.filter(is_active=True)  # Filter active elections # Get the user's votes
    user_votes = set(Vote.objects.filter(user=request.user).values_list('election_id', flat=True))
    for election in elections:
        election.can_vote = election.id not in user_votes

    # Add a flag to each election to check if the user can vote
    for election in elections:
        election.can_vote =election.id not in user_votes
    return render(request, 'voting/election_list.html', {'elections': elections})

from django.shortcuts import render, get_object_or_404

def results_view(request, election_id):
    election = get_object_or_404(Election, id=election_id)
    candidates = Candidate.objects.filter(election=election)  # Get all candidates for the election
    context = {
        'election': election,
        'candidates': candidates,
    }
    return render(request, 'voting/results.html', context)