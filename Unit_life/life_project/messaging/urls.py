from django.urls import path
from .views import (
    MessageListView,
    MessageDetailView,
    MessageCreateView,
    # MessageUpdateView,
    MessageDeleteView,
    InboxView,
)

from . import views


urlpatterns = [
    path('', MessageListView.as_view(), name='messaging-home'),
    path('message/<int:pk>', MessageDetailView.as_view(), name='message-detail'),
    path('message/new/', MessageCreateView.as_view(), name='message-create'),
    # path('message/<int:pk>/update/', MessageUpdateView.as_view(), name='message-update'),
    path('message/<int:pk>/delete/', MessageDeleteView.as_view(), name='message-delete'),
    path('about/', views.about, name='messaging-about'),
    # Add URLs for sending, archiving, and other message actions.
    path('inbox/', InboxView.as_view(), name='inbox'),
    # path('inbox/compose/', InboxView.as_view(), name='compose-message'),
    path('inbox/sent-items/', InboxView.as_view(), name='sent-items'),
    path('inbox/archive/', InboxView.as_view(), name='archived-messages'),
    path('inbox/delete/', InboxView.as_view(), name='delete'),
    path('inbox/restore/', InboxView.as_view(), name='restore-messages'),
    path('inbox/empty/', InboxView.as_view(), name='empty'),
    path('inbox/search/', InboxView.as_view(), name='search'),
    path('inbox/settings/', InboxView.as_view(), name='settings'),
    path('inbox/help/', InboxView.as_view(), name='help'),
    path('inbox/about/', InboxView.as_view(), name='about'),
    path('inbox/contact/', InboxView.as_view(), name='contact'),
    path('inbox/privacy/', InboxView.as_view(), name='privacy'),
    path('inbox/terms/', InboxView.as_view(), name='terms'),
    path('inbox/cookies/', InboxView.as_view(), name='cookies'),
    path('inbox/security/', InboxView.as_view(), name='security'),
    path('inbox/notifications/', InboxView.as_view(), name='notifications'),
    path('inbox/feedback/', InboxView.as_view(), name='feedback'),
    path('inbox/updates/', InboxView.as_view(), name='updates'),
    path('inbox/upgrade/', InboxView.as_view(), name='upgrade'),
    path('inbox/subscribe/', InboxView.as_view(), name='subscribe'),
    path('inbox/unsubscribe/', InboxView.as_view(), name='unsubscribe'),
    path('inbox/confirm/', InboxView.as_view(), name='confirm'),
    path('inbox/verify/', InboxView.as_view(), name='verify'),
    path('inbox/activate/', InboxView.as_view(), name='activate'),
    path('inbox/deactivate/', InboxView.as_view(), name='deactivate'),
    path('inbox/enable/', InboxView.as_view(), name='enable'),
    path('inbox/disable/', InboxView.as_view(), name='disable'),
    path('inbox/accept/', InboxView.as_view(), name='accept'),
    path('inbox/reject/', InboxView.as_view(), name='reject'),
    

    # Add URLs for viewing, editing, and deleting messages.
    path('inbox/view/', InboxView.as_view(), name='view'),
    path('inbox/edit/', InboxView.as_view(), name='edit'),
    path('inbox/delete/', InboxView.as_view(), name='delete'),
    path('inbox/forward/', InboxView.as_view(), name='forward'),
    path('inbox/reply/', InboxView.as_view(), name='reply'),
    path('inbox/reply-all/', InboxView.as_view(), name='reply-all'),
    path('inbox/edit-draft/', InboxView.as_view(), name='edit-draft'),
    path('inbox/delete-draft/', InboxView.as_view(), name='delete-draft'),
    path('inbox/forward-draft/', InboxView.as_view(), name='forward-draft'),
    path('inbox/reply-draft/', InboxView.as_view(), name='reply-draft'),
    path('inbox/reply-all-draft/', InboxView.as_view(), name='reply-all-draft'),
    path('inbox/move/', InboxView.as_view(), name='move'),
    path('inbox/copy/', InboxView.as_view(), name='copy'),
    path('inbox/print/', InboxView.as_view(), name='print'),
    path('inbox/download/', InboxView.as_view(), name='download'),
    path('inbox/save/', InboxView.as_view(), name='save'),

]
