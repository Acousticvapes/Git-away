class Teachers:

    def __init__(self, first, last, subject, grade):
        self.first = first
        self.last = last
        self.subject = subject
        self.grade = grade

    def class_desc(self):
        return '{}, {}'.format(self.first, self.subject)

    def all(self):
        return '{} {}, {} | {}'.format(self.first, self.last, self.subject, self.grade)

teach_1 = Teachers('Calvin', 'Greenway', 'IT Instructor', 'N/A')
teach_2 = Teachers('Diamond', 'Staley', 'Assistant Instructor', 'N/A')
teach_3 = Teachers("Jor'Danna", "Davis", "Social Support", "N/A")
teach_4 = Teachers('Christian', 'Reeves', 'Professional Development', 'N/A')
teach_5 = Teachers('Kyle', 'Wise', 'Recruitment', 'N/A')


Teachers_first = (teach_1.first, teach_2.first, teach_3.first, teach_4.first, teach_5.first)
print(Teachers_first)
print(teach_1.all(), teach_2.all(), teach_3.all(), teach_4.all(), teach_5.all())
