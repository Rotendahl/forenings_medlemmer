from django.utils import timezone
from django.views.generic.detail import DetailView
from members.models import Department


class DepartmentDetailView(DetailView):
    model = Department

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
