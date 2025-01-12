tasks = []

while True:
    a = input("\n1:Add Task, 2: View Task, 3: Exit\nchoose: ")
    if a == "1":
        tasks.append(input("Enter tasks: "))
    elif a == "2":
        print("\nTasks:", *tasks, sep="\n ")
    elif a == "3":
        break
    else:
        print("Incorrect option")
