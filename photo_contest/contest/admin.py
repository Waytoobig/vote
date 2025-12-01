from django.contrib import admin
from .models import Candidate, Vote

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'photographer', 'category', 'total_votes', 'is_active', 'created_at']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['name', 'photographer', 'description']
    readonly_fields = ['total_votes']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'image', 'description')
        }),
        ('Photographer Details', {
            'fields': ('photographer', 'category')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['candidate', 'user_session', 'created_at']
    list_filter = ['candidate', 'created_at']
    search_fields = ['candidate__name', 'user_session']