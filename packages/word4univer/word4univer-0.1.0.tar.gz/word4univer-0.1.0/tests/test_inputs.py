import Labs
from Word4Univer import StudentInfo


def main():
    lab = Labs.InputsLab(StudentInfo())

    for key, t in lab.inputs:
        print(key, t)

    lab.inputs.set("text", "Hello, World!")

    try:
        lab.inputs.set("order", "Hello, World")
    except ValueError as e:
        print(e)

    lab.inputs.set("order", 4)

    lab.run()
    lab.save_to_file()


if __name__ == "__main__":
    main()
