from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255, null=False)
    secondName = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, unique=True, null=False)
    phone = models.CharField(max_length=12, unique=True, null=False)


class Role(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)


class PersonRole(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


class Meeting(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=512)
    date = models.DateField(null= False)


class PersonMeeting(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
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
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Requirement(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=512, null=False)
    jobOffer = models.ForeignKey(JobOffer, on_delete=models.CASCADE)


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
    description = models.CharField(max_length = 512)
    degree = models.CharField(max_length=255, null=False)
    graduationDateOrExpectedDate = models.DateField(null=False)
    inProgress = models.BooleanField(null=False)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)


class PromisingCandidate(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, null=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=False)


class OpinionAboutCandidate(models.Model):
    Content = models.CharField(max_length=5000, null=False)
    candidate = models.ForeignKey(Person, related_name = 'candidate',on_delete=models.CASCADE, null=False)
    hrManager = models.ForeignKey(Person, related_name = 'hr', on_delete=models.CASCADE, null=False)
