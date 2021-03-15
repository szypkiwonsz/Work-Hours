from django.apps import AppConfig


class SalaryCalculatorConfig(AppConfig):
    name = 'salary_calculator'

    def ready(self):
        import salary_calculator.signals
