from django.shortcuts import render
from app.models import Instructor, Lectures

def lecture_schedule(request, instructor_id):
    instructor = Instructor.objects.get(admin=instructor_id)
    lectures = Lectures.objects.filter(instructor=instructor)

    context = {
        'instructor' : instructor,
        'lectures' : lectures,
    }

    return render(request, 'staff/schedule.html', context)
