from django.db import models
class board(models.Model):
    board_id = models.AutoField(primary_key =True) #게시글 id
    title = models.CharField(max_length=50, null=True) # 제목
    content = models.TextField(null=True) #  게시글 내용
    update_date = models.DateTimeField(auto_now_add= True, null=True) #게시글 올린 시간
    views = models.PositiveIntegerField() # 조회수
    like = models.BooleanField(default=False) # 좋아요
    comment = models.PositiveIntegerField() # 댓글 수
    #comment_id 댓글 id
    #user_id 고객 id

# board 와 좋아요 모델을 서로 매핑시켜줘야하고 foriegn키로 서로 연결시켜줘야한다.