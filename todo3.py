tasks = []

while True :
    print("===To Do List---")
    print("1: Add new tasks")
    print("2: show tasks")
    print("3: exit")

    choice = input("please choose")



    if choice == "1" :
        task = input('enter your new task')
        tasks.append(task)
        print("task added")
    elif choice == "2" :
        if not  tasks:
            print("this is empty...!")
        else :
            for i , t in enumerate(tasks,1):
                print(f"{i}, {t}")
    elif choice == "3":
        print("bye")
        break
    else:
        prakint("not found")      

print("oops")