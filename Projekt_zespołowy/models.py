from django.db import models
from django.conf import settings


class Person(models.Model):
    name = models.CharField(max_length=255, null=False)
    secondName = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, unique=True, null=False)
    phone = models.CharField(max_length=12, unique=True, null=False)

    def __str__(self):
        return self.name


class Meeting(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=512)
    date = models.DateField(null=False)


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
    niceToHave = models.CharField(max_length=5000)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def benefits_split(self):
        return self.additionalBenefits.split(',')

    def nicetohave_split(self):
        return self.niceToHave.split(',')

    # def __init__(self,a,b,c,d,e,f,g,h,j):
    #     self.title = a
    #     self.isActive =b
    #     self.creation_date = c
    #     self.dueDate = d
    #     self.description = e
    #     self.bottomSalaryRange=f
    #     self.upperSalaryRange = g
    #     self.additionalBenefits = h
    #     self.niceToHave = j


class Requirement(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=512, null=False)
    jobOffer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Application(models.Model):
    date = models.DateField(null=False)
    file = models.BinaryField(null=False)
    skills = models.CharField(max_length=5000)
    jobOffer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Experience(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=512)
    startDate = models.DateField(null=False)
    endDate = models.DateField()
    stillWorking = models.BooleanField(null=False)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)


class Education(models.Model):
    name = models.CharField(max_length=255, null=False)

    description = models.CharField(max_length=5000)

    degree = models.CharField(max_length=255, null=False)
    graduationDateOrExpectedDate = models.DateField(null=False)
    inProgress = models.BooleanField(null=False)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)


class PromisingCandidate(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, null=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=False)


class OpinionAboutCandidate(models.Model):
    Content = models.CharField(max_length=5000, null=False)
    candidateId = models.IntegerField(null=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
