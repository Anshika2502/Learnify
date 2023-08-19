from typing import Any, Dict
from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Course , Video
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import CoursePermissionMixin

# Create your views here.
class CourseListView(ListView):
    model = Course
    template_name = "content/course_list.html"
    # queryset = Course.objects.all()
    

class CourseDetailView(DetailView):
    model = Course
    template_name = "content/course_detail.html"

class VideoDetailView(LoginRequiredMixin, CoursePermissionMixin, DetailView):
    model = Video
    template_name = "content/video_detail.html"

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        course = get_object_or_404(Course , slug=self.kwargs["course_slug"])
        context['course'] = course

        #subscription = self.request.user.student.subscription
        #pricing_tier = subscription.pricing

        #pricing_tier in course.pricing_tiers.all()

        return context