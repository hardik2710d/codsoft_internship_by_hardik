to_do_list = []

while True:
    print("To Do List")
    print("1.view tasks")
    print("2.add task")
    print("3.mark task as done")
    print("4.end")

    user= input("enter what opperation to perform(1/2/3/4): ")


    if user=="1":
        a=len(to_do_list)
        if a==0:
            print("tasks are empty\n")
        else:
            for i in range (a):
                task=to_do_list[i]
                if task['done']:
                    b="DONE"
                else:
                    b="PENDING"

                print(str(i+1)+"."+task['title']+"["+b+"]\n")


    elif user=="2":
        task=input("enter task: ")
        
        new_task = {"title": task, "done": False}
        to_do_list.append(new_task)

        print("task added.\n")
        

    elif user=="3":
        a=len(to_do_list)
        if a==0:
            print("no tasks to mark done\n")
        else:
            i=1
            for task in to_do_list:
                print(i,".",task['title'],'\n')
                i=i+1


            try:
                num = int(input("enter task number to mark done: "))
                to_do_list[num-1]["done"]=True
                print("task marked as done\n")
            except:
                print("invalid number\n")


    elif user=="4":
        print("exiting to do list\n")
        break


    else:
        print("invalid input\n")
