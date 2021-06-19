from django.db import models
from django.conf import settings


class Person(models.Model):
    name = models.CharField(max_length=255, null=False)
    secondName = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=12, null=False)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name + " " + self.secondName

    def get_id(self):
        return str(self.id)


class Meeting(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=512)
    start_time = models.DateTimeField(null=True)
    is_free = models.BooleanField(null=False, default=True)


class PersonMeeting(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)


class UserMeeting(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)


class JobOffer(models.Model):
    title = models.CharField(max_length=255, unique=True, null=False)
    isActive = models.BooleanField(null=False)
    creation_date = models.DateField(null=False)
    dueDate = models.DateField()
    description = models.CharField(max_length=5000)
    bottomSalaryRange = models.IntegerField(null=False)
    upperSalaryRange = models.IntegerField(null=False)
    additionalBenefits = models.CharField(max_length=5000)
    requirements = models.CharField(max_length=1000, null=False, default='brak')
    niceToHave = models.CharField(max_length=5000)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def requirements_split(self):
        return self.requirements.split(',')

    def benefits_split(self):
        return self.additionalBenefits.split(',')

    def nicetohave_split(self):
        return self.niceToHave.split(',')


class Application(models.Model):
    date = models.DateField(null=False)
    file = models.BinaryField(null=False)
    skills = models.CharField(max_length=5000)
    jobOffer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Education(models.Model):
    uni_name = models.CharField(max_length=255, null=False, default='brak')
    languages = models.CharField(max_length=1000, null=False, default='brak')
    application = models.ForeignKey(Application, on_delete=models.CASCADE)


class PromisingCandidate(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, null=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=False)


class OpinionAboutCandidate(models.Model):
    Content = models.CharField(max_length=5000, null=False)
    candidate = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
