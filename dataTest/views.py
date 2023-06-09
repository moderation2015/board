from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import board
from .serializer import boardSerializer, writeSerializer


def board_list(request):
    if request.method == 'GET': # GET 방식일 때
        query_set = board.objects.all() # ORM으로 board의 모든 객체 받아옴
        serializer = boardSerializer(query_set, many=True) # JSON으로 변환
        return JsonResponse(serializer.data, safe=False) # JSON타입의 데이터로 응답

    elif request.method == 'POST': # POST방식일 때
        data = JSONParser().parse(request) # 요청들어온 데이터를 JSON 타입으로 파싱
        serializer = writeSerializer(data=data) # Serializer를 사용해 전송받은 데이터를 변환하기 위함
        if serializer.is_valid(): # 생성한 모델과 일치하면
            serializer.save() # 데이터 저장
            return JsonResponse(serializer.data, status=201) # 정상 응답 201
        return JsonResponse(serializer.errors, status=400) # 모델에 일치하지 않는 데이터일 경우