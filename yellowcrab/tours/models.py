from django.db import models
from stdimage.models import StdImageField


class Zone(models.Model):
    code = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.code}"


class Report(models.Model):
    description = models.CharField(max_length=255)
    report_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.description} ({self.report_date})"


class ReportLine(models.Model):
    description = models.CharField(max_length=10240)
    image = StdImageField(blank=True, variations={"large": (600, 400)})
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, blank=True, null=True)

    def short_description(self):
        if self.description is None:
            return None
        elif len(self.description) > 10:
            return f"{str(self.description)[:7]}..."
        else:
            return str(self.description)

    def __str__(self):
        return f"{self.short_description()} on {self.report.description}"
