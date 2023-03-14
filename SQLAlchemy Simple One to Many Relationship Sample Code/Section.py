from sqlalchemy import Column, Integer, String, Time, ForeignKeyConstraint, UniqueConstraint
from sqlalchemy.orm import Mapped, relationship

from orm_base import Base


class Section(Base):
    __tablename__ = 'sections'

    departmentAbbreviation = Column(String(10), primary_key=True)
    courseNumber = Column(Integer, primary_key=True)
    sectionNumber = Column(Integer, primary_key=True)
    semester = Column(String(10), primary_key=True)
    sectionYear = Column(Integer, primary_key=True)
    building = Column(String(6), nullable=False)
    room = Column(Integer, nullable=False)
    schedule = Column(String(6), nullable=False)
    startTime = Column(Time, nullable=False)
    instructor = Column(String(80), nullable=False)

    course: Mapped["Course"] = relationship("Course", back_populates="sections")

    __table_args__ = (
        ForeignKeyConstraint(
            ['departmentAbbreviation', 'courseNumber'], ['courses.departmentAbbreviation', 'courses.courseNumber']
        ),
        UniqueConstraint('building', 'room', 'schedule', 'startTime', name='sections_uk_01'),
        UniqueConstraint('building', 'room', 'semester', 'sectionYear', 'schedule', 'startTime', 'instructor', name='sections_uk_02')
    )

    def __init__(self, course, sectionNumber, semester, sectionYear, building, room, schedule, startTime, instructor):
        self.course = course
        self.departmentAbbreviation = course.departmentAbbreviation
        self.courseNumber = course.courseNumber
        self.sectionNumber = sectionNumber
        self.semester = semester
        self.sectionYear = sectionYear
        self.building = building
        self.room = room
        self.schedule = schedule
        self.startTime = startTime
        self.instructor = instructor



    def __str__(self):
        return f"{self.departmentAbbreviation} {self.courseNumber}-{self.sectionNumber} ({self.semester} {self.sectionYear}) with {self.instructor} at {self.building} {self.room}, {self.schedule} {self.startTime}"
