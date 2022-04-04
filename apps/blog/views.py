from typing import Dict, Any
from django.views.generic import TemplateView
from apps.insurance.forms import InsuranceReminderForm

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['insurance_reminder_form'] = InsuranceReminderForm()
        return context