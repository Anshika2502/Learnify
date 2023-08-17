from typing import Any, Dict
from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Course , Video

# Create your views here.
class CourseListView(ListView):
    model = Course
    template_name = "content/course_list.html"
    # queryset = Course.objects.all()
    

class CourseDetailView(DetailView):
    model = Course
    template_name = "content/course_detail.html"

class VideoDetailView(DetailView):
    model = Video
    template_name = "content/video_detail.html"

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        course = get_object_or_404(Course , slug=self.kwargs["course_slug"])
        context['course'] = course
        return context