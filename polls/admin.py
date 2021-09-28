import os

from django.contrib import admin

from django.template.loader import get_template

from .models import FirstReport
import pdfkit


class FirstReportAdminSite(admin.ModelAdmin):
    actions = ['make_report']

    def make_report(self, req, query):
        for obj in query:
            context = {
                "invoice_id": 123,
                "customer_name": "John Cooper",
                "amount": 1399.99,
                "today": "Today",
                'merchant': obj.merchant
            }
            template = get_template('first-report.html')
            html = template.render(context)
            pdfkit.from_string(html, obj.merchant + '-out.pdf')



admin.site.register(FirstReport, FirstReportAdminSite)
