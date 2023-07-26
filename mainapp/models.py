from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited", editable=False)
    is_deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()


class News(BaseModel):
    title = models.CharField(max_length=256, verbose_name="Title")
    description = models.CharField(max_length=1024, verbose_name="Description")
    body = models.TextField(blank=True, null=True, verbose_name="Body")
    body_as_markdown = models.BooleanField(default=False, verbose_name="As markdown")

    def __str__(self) -> str:
        return f"{self.pk} {self.title}"

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
        ordering = ("-created",)


class Course(models.Model):
    name = models.CharField(max_length=256, verbose_name="Name")
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    description_as_markdown = models.BooleanField(verbose_name="As markdown", default=False)
    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Cost", default=0)
    cover = models.CharField(max_length=25, default="no_image.svg", verbose_name="Cover")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Created", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited", editable=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.pk} {self.name}"


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson_number = models.PositiveIntegerField(verbose_name="Lesson number")
    title = models.CharField(max_length=256, verbose_name="Name")
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    description_as_markdown = models.BooleanField(verbose_name="As markdown", default=False)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Created", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited", editable=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.course.name} | {self.lesson_number} | {self.title}"


class CourseTeachers(models.Model):
    course = models.ManyToManyField(Course)
    first_name = models.CharField(max_length=128, verbose_name="Name")
    last_name = models.CharField(max_length=128, verbose_name="Surname")
    day_birth = models.DateField(verbose_name="Birth date")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Created", editable=False)
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited", editable=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "{0:0>3} {1} {2}".format(self.pk, self.last_name, self.first_name)
