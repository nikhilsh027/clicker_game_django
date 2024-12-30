from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import GameScore
import json

def game_view(request):
    return render(request, 'g1.html')

@csrf_exempt
def save_score(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        score = data.get('score')
        GameScore.objects.create(score=score)
        return JsonResponse({'message': 'Score saved successfully'})

