from Course import *
from Room import *
from MeetingTime import *
from Instructor import *
from Department import *

class Data:
    ROOMS = [["R1", 25], ["R2", 45], ["R3", 35]]
    MEETING_TIMES = [["MT1", "MWF 09:00 - 10:00"],
                     ["MT2", "MWF 10:00 - 11:00"],
                     ["MT3", "TTH 09:00 - 10:30"],
                     ["MT4", "TTH 10:30 - 12:00"]]
    INSTRUCTORS = [["I1", "Dr James Web"],
                   ["I2", "Mr. Mike Brown"],
                   ["I3", "Dr Steve Day"],
                   ["I4", "Mrs Jane Doe"]]
    def __init__(self):
        self._rooms =  []; self._meetingTimes = []; self._instructors = []
        for i in range(0, len(self.ROOMS)):
            self._rooms.append(Room(self.ROOMS[i][0], self.ROOMS[i][1]))
        for i in range(0, len(self.MEETING_TIMES)):
            self._meetingTimes.append(MeetingTime(self.MEETING_TIMES[i][0], self.MEETING_TIMES[i][1]))
        for i in range(0, len(self.INSTRUCTORS)):
            self._instructors.append(Instructor(self.INSTRUCTORS[i][0], self.INSTRUCTORS[i][1]))
        
        course1 = Course("C1", "325k", [self._instructors[0], self._instructors[1]], 25)
        course2 = Course("C2", "319k", [self._instructors[0], self._instructors[1], self._instructors[2]], 35)
        course3 = Course("C3", "462k", [self._instructors[0], self._instructors[1]], 25)
        course4 = Course("C4", "464k", [self._instructors[2], self._instructors[3]], 30)
        course5 = Course("C5", "360C", [self._instructors[3]], 35)
        course6 = Course("C6", "303k", [self._instructors[0], self._instructors[2]], 45)
        course7 = Course("C7", "303L", [self._instructors[1], self._instructors[3]], 45)
        
        self._courses = [course1, course2, course3, course4, course5, course6, course7]
        dept1 = Department("MATH", [course1, course3])
        dept2 = Department("EE", [course2, course4, course5])
        dept3 = Department("PHY", [course6, course7])
        
        self._depts = [dept1, dept2, dept3]
        self._numberOfClasses = 0
        for i in range(0, len(self._depts)):
            self._numberOfClasses += len(self._depts[i].get_courses())
            
    def get_rooms(self): return self._rooms
    def get_instructors(self): return self._instructors
    def get_courses(self): return self._courses
    def get_depts(self): return self._depts
    def get_meetingTimes(self): return self._meetingTimes
    def get_numberOfClasses(self): return self._numberOfClasses