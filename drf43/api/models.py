from django.db import models

class Singer(models.Model):
    name=models.CharField(max_length=90)
    gender=models.CharField(max_length=90)

    def __str__(self):
        return self.name
    


class Song(models.Model):
    title=models.CharField(max_length=90)
    singer=models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='song1')
    duration=models.IntegerField()


    def __str__(self):
        return self.title
    
