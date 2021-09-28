import pdfkit
from django.contrib import admin
from django.template.loader import get_template
from django.utils.html import format_html

from .models import FirstReport


class FirstReportAdminSite(admin.ModelAdmin):
    actions = ['make_report']
    list_display = ['id', 'merchant']
    list_display_links = ['id', 'merchant']

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
            options = {'page-size': 'A4', 'dpi': 500}
            pdfkit.from_string(html, obj.merchant + '-out.pdf', options)


admin.site.register(FirstReport, FirstReportAdminSite)
