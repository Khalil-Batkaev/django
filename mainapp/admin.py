from django.contrib import admin
from mainapp import models as mainapp_models
from django.utils.translation import gettext_lazy as _


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "is_deleted"]
    search_fields = ["title", "description", "body"]
    actions = ["mark_deleted"]

    def mark_deleted(self, request, queryset):
        queryset.update(is_deleted=True)

    mark_deleted.short_description = _("Пометить удаленными")


@admin.register(mainapp_models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "get_course_name", "lesson_number", "title", "is_deleted"]
    ordering = ["-course__name", "-lesson_number"]
    list_per_page = 5
    list_filter = ["course", "created", "is_deleted"]
    actions = ["mark_deleted"]

    def get_course_name(self, obj):
        return obj.course.name

    get_course_name.short_description = _("Course")

    def mark_deleted(self, request, queryset):
        queryset.update(is_deleted=True)

    mark_deleted.short_description = _("Пометить удаленными")


@admin.register(mainapp_models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_deleted"]
