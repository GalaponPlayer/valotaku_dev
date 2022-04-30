from django.db import models

# Create your models here.

# チーム募集に関する各データ
class CreateTeam(models.Model):
    team_name = models.CharField(max_length = 50, verbose_name='チーム名')
    rank = models.CharField(max_length = 50, verbose_name='ランク帯')

    def __str__(self):
        return self.team_name
    
    class Meta:
        verbose_name_plural = 'チーム募集（仮）'

class TeamDetail(models.Model):
    team_name = models.CharField(max_length = 50, verbose_name='チーム名')
    rank = models.CharField(max_length = 50, verbose_name='ランク帯')

    def __str__(self):
        return self.team_name
    
    class Meta:
        verbose_name_plural = '募集チーム'