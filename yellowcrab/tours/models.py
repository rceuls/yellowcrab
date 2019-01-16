from django.db import models
from stdimage.models import StdImageField


class Report(models.Model):
    description = models.CharField(max_length=255)
    report_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.description} ({self.report_date})"


class ReportLine(models.Model):
    description = models.CharField(max_length=10240)
    image = StdImageField(blank=True, variations={"large": (600, 400)})
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
