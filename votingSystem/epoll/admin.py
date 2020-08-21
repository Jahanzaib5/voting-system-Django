from django.contrib import admin
from .models import Position, Candidate, VoteStatus

# Register your models here.
admin.site.register(Position)
admin.site.register(Candidate)
#admin.site.register(VoteStatus)