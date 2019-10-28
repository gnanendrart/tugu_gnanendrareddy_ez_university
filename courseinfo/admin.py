from django.contrib import admin
from .models import Section, Student, Instructor, Course, Registration, Semester, Period, Year

admin.site.register(Semester)
admin.site.register(Period)
admin.site.register(Year)
admin.site.register(Section)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Registration)
