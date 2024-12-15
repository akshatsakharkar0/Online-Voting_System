from django.contrib import admin
from .models import Election, Candidate, Voter, Vote


class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'election',  'get_vote_count')  # Display name and election in the list view
    search_fields = ('name', 'election__name')  # Allow searching by candidate name and election name
    list_filter = ('election',)  # Filter by election in the admin panel
    ordering = ('election', 'name')  # Ordering candidates by election and name

    def get_vote_count(self, obj):
        # Count the number of votes for this candidate in the election
        return Vote.objects.filter(candidate=obj).count()  # Corrected query to use `candidate` field
    get_vote_count.short_description = 'Votes'

# Register the Candidate model with custom admin
admin.site.register(Candidate, CandidateAdmin)

# Optionally, if you want to add a filter for election in the Candidate model
admin.site.register(Election)

class VoterAdmin(admin.ModelAdmin):
    list_display = ('user', 'election', 'has_voted')  # Display voter name, election, and voting status
    search_fields = ('user__username', 'election__name')  # Search by voter username or email
    list_filter = ('has_voted',)  # Filter by voting status
    ordering = ('user',)

    def get_election(self, obj):
        # Get the election that the voter has voted in by checking the Vote model
        vote = Vote.objects.filter(user=obj.user).first()  # Get the first vote (assuming only one vote per user)
        if vote:
            return vote.election.name  # Return the election's name
        return None
    get_election.short_description = 'Election Voted In'  # Label for the column in the admin

# Register the Voter model with custom admin
admin.site.register(Voter, VoterAdmin)

admin.site.register(Vote)
