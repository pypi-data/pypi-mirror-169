from Labs import TstuTitlePageLab, TimpTitlePageLab
from Word4Univer import StudentInfo


def main():
    student = StudentInfo()

    lab = TstuTitlePageLab(student)
    lab.run()
    lab.save_to_file()

    lab = TimpTitlePageLab(student)
    lab.run()
    lab.save_to_file()


if __name__ == "__main__":
    main()
