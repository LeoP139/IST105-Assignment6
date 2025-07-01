from djongo import models

class CalculationResult(models.Model):
    original_values = models.JSONField()
    sorted_values = models.JSONField()
    average = models.FloatField()
    average_check = models.BooleanField()
    positive_count = models.IntegerField()
    positive_parity = models.CharField(max_length=5)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']