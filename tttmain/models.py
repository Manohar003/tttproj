from django.db import models
from datetime import  datetime
# Create your models here.
class Submitnum(models.Model):
    #ttt_ques = models.CharField(max_length=500)
    ttt_text = models.TextField()
    ttt_datime = models.DateTimeField("date published",default=datetime.now())

    def __str__(self):
        return self.ttt_text
