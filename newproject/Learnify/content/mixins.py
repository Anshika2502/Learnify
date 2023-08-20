from django.shortcuts import redirect, get_object_or_404
from .models import Course

class CoursePermissionMixin:
    def dispatch(self, request, *args, **kwargs):
        course = get_object_or_404(Course, slug=self.kwargs['course_slug'])
        subscription = request.user.student.subscription
        pricing_tier = subscription.pricing
        if not pricing_tier in course.pricing_tiers.all():
            return redirect('course-detail', slug = course.slug)
        return super().dispatch(request, *args, **kwargs)