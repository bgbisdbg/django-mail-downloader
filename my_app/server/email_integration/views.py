from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets

from .models import EmailAccount, EmailMessage
from .serializers import EmailAccountSerializer
from .tasks import import_emails


class EmailAccountViewSet(viewsets.ModelViewSet):
    queryset = EmailAccount.objects.all()
    serializer_class = EmailAccountSerializer


@csrf_protect
def message_list(request):
    if request.method == 'POST':
        import_emails()
        return redirect('message_list')

    messages = EmailMessage.objects.all()
    return render(request, 'email_integration/message_list.html', {'messages': messages})

