from django.db import models

# Create your models here.
class JobSearch(models.Model):
    date_started = models.DateField()
    date_ended = models.DateField()
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['date_started']

class JobApplication(models.Model):
    company_name = models.CharField(max_length=255)
    date_applied = models.DateField()
    job_title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    notes = models.TextField()
    submission_source = models.CharField(max_length=255, choices=[('LinkedIn', 'LinkedIn'),
                                                                ('Glassdoor', 'Glassdoor'),
                                                                ('Monster', 'Monster'),
                                                                ('Indeed', 'Indeed'),
                                                                ('Company Website', 'Company Website'),
                                                                ('Other', 'Other')])

    stage = models.CharField(max_length=255, choices=[('Recruiter Phone Screen', 'Recruiter Phone Screen'),
                                    ('Behavioral Interview', 'Behavioral Interview'),
                                    ('First Technical Interview', 'First Technical Interview'),
                                    ('Second Technical Interview', 'Second Technical Interview'),
                                    ('Third Technical Interview', 'Third Technical Interview'),
                                    ('Other', 'Other')])

    final_decision = models.CharField(max_length=255, choices=[('No Offer', 'No Offer'),
                                                                ('Offer Accepted', 'Offer Accepted'),
                                                                ('Offer Rejected', 'Offer Rejected'),
                                                                ('Company Ghosted Me', 'Company Ghosted Me'),
                                                                ('I Ghosted Company', 'I Ghosted Company'),
                                                                ('Counter Offer Pending', 'Counter Offer Pending')])
    contact_info = models.TextField()
    salary_range_low = models.DecimalField(null = True, blank = True, max_digits= 10, decimal_places = 2)
    salary_range_high = models.DecimalField(null = True, blank = True, max_digits = 10, decimal_places = 2)
    salary = models.DecimalField(null = True, blank = True, max_digits = 10, decimal_places = 2)
    job_search = models.ForeignKey(JobSearch, related_name='my_job_apps', on_delete=models.CASCADE)

    class Meta:
        ordering = ['job_search__date_started']

