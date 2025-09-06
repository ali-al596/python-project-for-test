
works = []

print("---To Do List---")
print('1: add new work')
print("2: show works ")
print("3: exit")

selected_number = input("choose")

if selected_number == 1 :
    work = input("Add your new work")
    works.append(work)
    print('work added')

elif selected_number == 2 :
    if not works:
        print("no work added")
    else :
        print(works)

elif selected_number == 3 :
    print("goodbye")
    