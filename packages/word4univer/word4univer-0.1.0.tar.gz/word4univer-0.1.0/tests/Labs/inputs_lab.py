from Word4Univer import Lab, LabInfo, StudentInfo, Inputs

from .Subjects import TestSubject


class InputsLab(Lab):

    inputs = Inputs(
        text=str,
        order=int,
    )

    info = LabInfo(
        name="Test inputs lab",
        index=11,
        theme="Test Lab theme",
        subject=TestSubject
    )

    def __init__(self, student: StudentInfo):
        super().__init__(self.info, student, __file__, "docparts", self.inputs)

    def run(self):
        self.document.add_step("inputs")
