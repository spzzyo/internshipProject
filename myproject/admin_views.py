from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, time
from app.models import Course,Instructor, CustomUser, Lectures

@login_required(login_url="/")
def add_course(request):
    if request.method == "POST":
        course_name = request.POST.get('course_name')
        course_level = request.POST.get('course_level')
        course_description = request.POST.get('description')
        coursePicture = request.FILES.get('coursePicture')


        course = Course(
            name=course_name,
            level=course_level,
            description = course_description,
            image = coursePicture,
        )
        course.save()
        messages.success(request, 'Successfully added')
        return redirect('add_course')
    return render(request, 'hod/add_course.html')

@login_required(login_url="/")
def view_course(request):
    course= Course.objects.all()
    context={
        'course' : course,
    }
    return render (request, 'hod/view_course.html',context)

# @login_required(login_url="/")
# def edit_course(request,id):
   
#     course = Course.objects.get(id = id)

#     context={
#         'course': course,
#     }

#     return render(request, 'hod/edit_course.html', context)

# @login_required(login_url="/")
# def update_course(request):
#     if request.method =="POST":
#         name = request.POST.get('course_name')
#         course_id = request.POST.get('course_id')

#         course =Course.objects.get(id= course_id)
#         course.name = name

#         course.save()
#         messages.success(request, 'Successfully ADDED')

#         return redirect('view_course')
    
#     return render(request, 'hod/edit_course.html')

@login_required(login_url="/")
def delete_course(request,id):
    course = Course.objects.get(id = id)
    course.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect(view_course)

@login_required(login_url="/")
def add_instructor(request):
    if request.method == "POST":
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username= request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        address = request.POST.get('address')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'User with same email exists already')
            return redirect('add_instructor')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'User with same username exists already')
            return redirect('add_instructor')
        
        else :
            user=CustomUser(first_name=first_name, last_name=last_name, email= email,  username=username, user_type=2)
            user.set_password(password)
            user.save()

            instructor = Instructor(
                admin = user,
                address = address,
                gender = gender,
            )

            instructor.save()
            messages.success(request, 'Instructor data Saved')
            return redirect ('add_instructor')


    return render(request, 'hod/add_staff.html')




def view_lecture(request):
    lecture= Lectures.objects.all()
    context={
        'lecture' : lecture,
    }
    return render (request, 'hod/view_lecture.html',context)



def add_lecture(request):
    if request.method == "POST":
        instructor_id = request.POST.get('instructor')
        course_id = request.POST.get('course')
        date = request.POST.get('date')

        instructor = Instructor.objects.get(id=instructor_id)
        course = Course.objects.get(id=course_id)

        # Check if the instructor is already assigned to a lecture on the selected date
        existing_lecture = Lectures.objects.filter(date=date, instructor=instructor).first()
        if existing_lecture:
            messages.error(request, f"This instructor is already assigned to a lecture on {date}.")
            return redirect('add_lecture')

        lecture = Lectures(date=date, instructor=instructor, course=course)
        lecture.save()

        messages.success(request, 'Lecture assigned successfully.')
        return redirect('add_lecture')

    instructors = Instructor.objects.all()
    courses = Course.objects.all()
    return render(request, 'hod/add_lecture.html', {'instructors': instructors, 'courses': courses})