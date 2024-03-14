from django.dispatch import receiver

from django.db.models.signals import post_save

from .models import Post

from django.core.mail import send_mail

from django.contrib.auth.models import User

from django.conf import settings

from django.utils.html import strip_tags
from django.template.loader import render_to_string

# this is one to send simple plain message:------
# @receiver(post_save, sender=Post)
# def post_created_send_email(sender, instance, created, **kwargs):
#     obj = Post.objects.latest('id')
#     # print(obj)

#     recipient_list = []

#     for user in User.objects.all():
#         recipient_list.append(user.email)

#     print(recipient_list)

#     subject = 'New Article is Posted'
#     message = f"Hello, Hope you doing great. We have Posted New article on '{obj.title}'"
#     email_from = settings.EMAIL_HOST_USER
#     send_mail(subject=subject, message=message, from_email=email_from, recipient_list=recipient_list)




# Second way to send email with dynamic content:----
@receiver(post_save, sender=Post)
def post_created_send_email(sender, instance, created, **kwargs):
    obj = Post.objects.latest('id')
    # print(obj)

    recipient_list = []

    for user in User.objects.all():
        recipient_list.append(user.email)

    # print(recipient_list)

    subject = 'New Article is Posted'
    html_message = render_to_string('mail_template.html', context={'obj':obj})
    message = strip_tags(html_message)
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject=subject, message=message, from_email=email_from, recipient_list=recipient_list,html_message=html_message)