from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.contrib.auth.models import User
# Create your views here.
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    # UpdateView,
    DeleteView
)
from django.contrib import messages
from .models import Message
from .forms import ComposeMessageForm




# class InboxView(ListView):
#     model = Message
#     template_name = 'messaging/inbox.html'
#     context_object_name = 'messages'
#     queryset = Message.objects.filter(is_archived=False)


def home(request):
    return render(request, 'messaging/home.html', {'Messages':InboxView.objects.all()})

class MessageListView(ListView):
    model = Message
    template_name = 'messaging/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'messages'
    ordering = ['-timestamp']



class MessageListView(ListView):
    model = Message
    template_name = 'messaging/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'messages'
    ordering = ['-timestamp']

class MessageDetailView(DetailView):
    model = Message

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['subject', 'body', 'recipient']

    def form_valid(self, form):
        form.instance.sender = self.request.user # Set the sender on the form
        return super().form_valid(form) # Validate form by running form_valid method from parent class.

class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Message
    success_url = "/"

    def test_func(self):
        message = self.get_object()
        # return self.request.user == message.sender
        if self.request.user == message.sender:
            return True
        return False

def about(request):
    return render(request, 'messaging/about.html', {'subject': 'About'})





class InboxView(ListView):
    model = Message
    template_name = 'messaging/inbox.html'
    context_object_name = 'messages'

    def get_queryset(self):
        # Filter messages based on recipient and not archived
        return Message.objects.filter(recipient=self.request.user, is_archived=False)


@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user, is_archived=False)
    return render(request, 'messaging/inbox.html', {'messages': messages})

@login_required
def sent_items(request):
    messages = Message.objects.filter(sender=request.user)
    return render(request, 'messaging/sent_items.html', {'messages': messages})

@login_required
def archived_messages(request):
    messages = Message.objects.filter(recipient=request.user, is_archived=True)
    return render(request, 'messaging/archived_messages.html', {'messages': messages})

@login_required
def message_detail(request, message_id):
    message = Message.objects.get(id=message_id)
    return render(request, 'messaging/message_detail.html', {'message': message})

# @login_required
# def compose_message(request):
#     if request.method == 'Message':
#         # Handle message composition and sending here
#         # ...
#         print("Compose Message View: Message request received")
#         return redirect('inbox')
#     print("Compose Message View: GET request received")
#     return render(request, 'messaging/compose_message.html')


@login_required
def compose_message(request):
    if request.method == 'Message':
        form = ComposeMessageForm(request.Message)
        if form.is_valid():
            # Create a new message object
            recipient_username = form.cleaned_data['recipient']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']

            recipient = User.objects.get(username=recipient_username)

            message = Message(sender=request.user, recipient=recipient, subject=subject, body=body)
            message.save()

            # Implement logic to send the message (e.g., via email)
            # You can use Django's EmailMessage class for sending emails.

            messages.success(request, 'Message sent successfully.')
            return redirect('inbox')
    else:
        form = ComposeMessageForm()

    return render(request, 'messaging/compose_message.html', {'form': form})
