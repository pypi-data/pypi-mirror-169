import Path
from Word4Univer import Lab, LabInfo, StudentInfo, TitlePages

from .Subjects import TestSubject


class TstuTitlePageLab(Lab):

    info = LabInfo(
        name="Test lab",
        index=8,
        theme="Test Lab theme",
        subject=TestSubject
    )

    def __init__(self, student: StudentInfo):
        super().__init__(self.info, student, style=Path.get_src("styles/tstu.xml"))

    def run(self):
        TitlePages.tstu(self.document)
        pass
