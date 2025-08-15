from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Review

def leave_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        review_text = request.POST.get('review_text')
        
        if name and review_text:
            Review.objects.create(name=name, review_text=review_text)
            messages.success(request, 'Ваш отзыв успешно отправлен!')
            return redirect('leave_review')
        else:
            messages.error(request, 'Пожалуйста, заполните все поля')
    
    
    return render(request, 'pages/forms/leave_review.html', locals())