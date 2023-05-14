from rest_framework import permissions
from rest_framework.views import APIView
from .models import Contact
from django.core.mail import send_mail
from rest_framework.response import Response

class ContactCreateView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data


        print(data)
        send_mail(
            data['subject'],
            'Name: '
            + data['name']
            + '\nEmail: '
            + data['email']
            + '\n\nMessage:\n'
            + data['message'],
            'dom.biznes@internet.ru',
            ['itpythonzhanbolot@gmail.com'],
            fail_silently=False
        )
        print('finish')
        contact = Contact(name=data['name'], email=data['email'], subject=data['subject'], message=data['message'])
        contact.save()

        return Response({'success': 'Message sent successfully'})
