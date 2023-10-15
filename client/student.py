class Student():
    def __init__(self, request):
        self.session = request.session
        student = self.session.get('skey', set())
        self.student = student
        
    def create(self):
        pass