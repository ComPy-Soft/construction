from itertools import chain

app_name = 'HR'

from .hr_views.employee_attendance_views import employee_attendance_templates
from .hr_views.employee_notes_views import employee_notes_templates
from .hr_views.employee_views import employee_templates
from .hr_views.loan_disbursement_views import loan_disbursement_templates
from .hr_views.loan_receipts_views import loan_receipts_templates
from .hr_views.salary_head_views import salary_head_templates
from .hr_views.salary_slip_views import salary_slip_templates
from .hr_views.salary_structure_views import salary_structure_templates
from .hr_views.generate_payroll_views import generate_payroll_templates

urlpatterns = list(chain(employee_attendance_templates,
                        employee_notes_templates,
                        employee_templates,
                        loan_disbursement_templates,
                        loan_receipts_templates,
                        salary_head_templates,
                        salary_slip_templates,
                        salary_structure_templates,
                        generate_payroll_templates
                        ))