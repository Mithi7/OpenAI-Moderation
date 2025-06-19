from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import ModerationAttempt

def moderation_view(request):
    return render(request, 'moderation.html')

@csrf_exempt
def moderation_api(request):
    if request.method == 'POST':
        message = request.POST.get('content', '').strip()
        if not message:
            return JsonResponse({'success': False, 'error': 'No content provided.'}, status=400)

        try:
            moderation_attempt = ModerationAttempt(settings.OPENAI_API_KEY)
            moderation = moderation_attempt.get_results(message=message)

            response_data = {
                'success': True,
                'categories': moderation.get('categories', {}),
                'scores': moderation.get('category_scores', {}),
                'flagged': moderation.get('flagged', False),
                'id': moderation.get('id'),
            }
            return JsonResponse(response_data)

        except Exception as e:
            error_message = str(e)
            if 'rate limit exceeded after retries' in error_message.lower():
                return JsonResponse({'success': False, 'error': error_message}, status=429)
            else:
                return JsonResponse({'success': False, 'error': error_message}, status=500)

    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method.'}, status=405)
