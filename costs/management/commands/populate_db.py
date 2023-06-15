from django.core.management.base import BaseCommand
from costs.models import Job, Salary

class Command(BaseCommand):
    help = 'Populate the database with predefined data'

    def handle(self, *args, **options):
        # Define the jobs and their corresponding salaries
        jobs_and_salaries = {
            'Software Engineer': 90000,
            'Data Scientist': 95000,
            'Marketing Manager': 80000,
            'Sales Manager': 85000,
            'Mechanical Engineer': 90000,
            'Civil Engineer': 85000,
            'Financial Analyst': 80000,
            'Project Manager': 95000,
            'Graphic Designer': 70000,
            'Human Resources Manager': 80000,
        }

        # Create the jobs and salaries in the database
        for job_title, salary_amount in jobs_and_salaries.items():
            salary, created = Salary.objects.get_or_create(salary=salary_amount)
            Job.objects.get_or_create(job_title=job_title, salary=salary)

        # Print a success message
        self.stdout.write(self.style.SUCCESS('Database has been populated with job and salary data.'))
