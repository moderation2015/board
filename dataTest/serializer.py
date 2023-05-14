from rest_framework import serializers
from .models import board

class boardSerializer(serializers.ModelSerializer):
    class Meta:
        model = board
        fields = ["title", "content", "comment", "like", "update_date"]
# 제목/ 게시글 내용/ 댓글 수/ 좋아요 수/ 게시글 올린 시간  // 익명은 프론트에서

class writeSerializer(serializers.ModelSerializer):
    class Meta:
        model = board
        fields = ["title", "content", "update_date"]
# 제목/ 게시글 내용/ 게시글 올린 시간 DB에 쓰기