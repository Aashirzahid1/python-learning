fruits=["apple","banana","cherry","peach","mango"]
print(fruits[0])
print(fruits[len(fruits)-1])
print(fruits[2])

#Question 2

numbers=[10,20,30]

numbers.append(40)

numbers.insert(0,5)

print(numbers)


# Q3 
a=[1,2]
b=[3,4]

a.append(b)
print(a)
a.pop()
print(a)

a.extend(b)
print(a)

#Q4
colors=["red","green","blue"]
for x in range(len(colors)-1):
    if colors[x]=="green":
        colors[x]="yellow"
print(colors)


# Q5 

animals=["cat","dog","bird","fish"]
animals.pop()
print(animals)

#Q6

sentence = "python is fun to learn"
sentence_list=sentence.split(" ")
sentence_list.append("today")
print(sentence_list)
again_sentence=",".join(sentence_list)
print(again_sentence)

print(again_sentence.replace(","," "))


# Q7

numbers=[4,2,7,2,9,2]
print(numbers.count(2))
print(numbers.index(7))


#Q8
lists=[]
for x in range(5):
    num=input("Enter a num:")
    lists.append(num)
print(lists)
print(max(lists))
print(min(lists))
total=0
for x in range(5):
   total+=int(lists[x])
print(total)
print(f"Average: {total/5}")


#Q9 
numbers=[7,2,9,4,5]
maximum=0
for i in range(len(numbers)-1):
    if numbers[i]>maximum:
        maximum=numbers[i]
print(maximum)


#Final Task

task=[]
x=True
while x:
    print("1. Add a task")
    print("2. veiw all tasks")
    print("3. Remove a task")
    print("4. Exit")

    num=int(input("Enter a task"))

    if num == 1:
        new=input("enter the task")
        task.append(new)

    if num == 2:
        print(task)

    if num == 3:
        for i,j in enumerate(task):
         print(i,j)
        new=int(input("Enter the task index you wnat to remove"))
        task.pop(new)
        print(task)

    if num == 4:
        x=False