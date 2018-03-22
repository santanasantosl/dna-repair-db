# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from forms import ContactFrom

# Create your views here.
# Create your views here.
def contact(request):
    title = "Contact"
    form = ContactFrom(request.POST or None)
    context = {

        'title': title,
        'form': form,
        'confirm_message': None
    }
    if form.is_valid():
        comment = form.cleaned_data['comment']
        name = form.cleaned_data['name']
        sbj = 'Message from DNA Repair DB'
        msg = '%s %s' % (comment, name)
        frm = form.cleaned_data['email']
        to_us = [settings.EMAIL_HOST_USER, 'lss19@pitt.edu']
        send_mail(sbj, msg, frm, to_us, fail_silently=False)
        title = 'Thank you'
        confirm_message = """
        Thank you for your message.We have received it and will be in contact as soon as possible.
        """
        context = {
            'title': title,
            'form': None,
            'confirm_message': confirm_message
        }

    template = 'contact.html'
    return render(request, template, context)