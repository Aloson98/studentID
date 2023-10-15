from .student import Student


def student(request):
    return {'student': Student(request)}