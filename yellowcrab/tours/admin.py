from django.contrib import admin
from django.http import HttpResponse
from .models import Report, ReportLine, Zone
from .render import PdfRender
import datetime


def generate_reports(modeladmin, request, queryset):
    if len(queryset) is 1:
        for data in queryset:
            params = {
                "description": data.description,
                "lines": data.reportline_set.all(),
                "generation_date": datetime.datetime.now(),
            }
            pdf = PdfRender.render("tours/report.html", params)
            return HttpResponse(pdf, content_type="application/pdf")

    else:
        # TODO: generate a zip file containing a collection of reports.
        pass


generate_reports.short_description = "Generate reports"


class ReportAdmin(admin.ModelAdmin):
    list_display = ["description", "report_date"]
    actions = [generate_reports]


class ReportLineAdmin(admin.ModelAdmin):
    list_display = ["description", "report"]


admin.site.register(Report, ReportAdmin)
admin.site.register(ReportLine, ReportLineAdmin)
admin.site.register(Zone)
