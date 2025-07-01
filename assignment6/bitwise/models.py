from djongo import models

class Submission(models.Model):
    input_a = models.IntegerField()
    input_b = models.IntegerField()
    input_c = models.IntegerField()
    input_d = models.IntegerField()
    input_e = models.IntegerField()
    average = models.FloatField()
    is_above_50 = models.BooleanField()
    positives = models.IntegerField()
    even_odd = models.JSONField()
    greater_than_10 = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Submission"
        verbose_name_plural = "Submissions"