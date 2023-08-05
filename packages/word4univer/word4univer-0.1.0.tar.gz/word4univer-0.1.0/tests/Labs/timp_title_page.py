import Path
from Word4Univer import Lab, LabInfo, StudentInfo, TitlePages

from .Subjects import TestSubject


class TimpTitlePageLab(Lab):

    info = LabInfo(
        name="Test timp lab",
        index=9,
        theme="Test Lab theme",
        subject=TestSubject
    )

    def __init__(self, student: StudentInfo):
        super().__init__(self.info, student)

    def run(self):
        TitlePages.timp(self.document)
        pass
