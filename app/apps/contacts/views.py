from apps.contacts import models as contacts_models
from django.shortcuts import render, redirect
from django.contrib import messages
from apps.telegram_bot.views import (
    send_contact_request_notification,
    send_review_notification,
)


def contact_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')

        if name and contact:
            contacts_models.ContactRequest.objects.create(name=name, contact=contact)
            messages.success(request, 'Спасибо! Мы свяжемся с вами в ближайшее время.')
            # Telegram notification (safe if bot not configured)
            try:
                send_contact_request_notification(name=name, contact=contact)
            except Exception:
                # Do not interrupt user flow if Telegram sending fails
                pass
        else:
            messages.error(request, 'Пожалуйста, заполните все поля.')

        return redirect('/#contact')

    # На POST рассчитано, но на всякий случай вернём на главную
    return redirect('/#contact')


def review_submit(request):
    """Create a new Review from POST and redirect to the reviews page."""
    if request.method == 'POST':
        name = request.POST.get('name')
        review_text = request.POST.get('review_text')

        if name and review_text:
            contacts_models.Review.objects.create(name=name, review_text=review_text)
            messages.success(request, 'Спасибо за ваш отзыв!')
            # Telegram notification (safe if bot not configured)
            try:
                send_review_notification(name=name, review_text=review_text)
            except Exception:
                pass
        else:
            messages.error(request, 'Пожалуйста, заполните все поля.')

        return redirect('reviews')

    # Fallback
    return redirect('reviews')