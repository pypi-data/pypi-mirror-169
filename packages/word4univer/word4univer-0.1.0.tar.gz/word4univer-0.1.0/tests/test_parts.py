import Labs
from Word4Univer import StudentInfo


def main():
    lab = Labs.PartsLab(StudentInfo())
    lab.run()
    lab.save_to_file()


if __name__ == "__main__":
    main()
