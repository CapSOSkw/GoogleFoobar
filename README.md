# GoogleFoobar

## Minion Task Scheduling

Time to solve: 24 hours.

#### Description

Commander Lambda's minions are upset! They're given the worst jobs on the whole space station, and some of them are starting to complain that even those worst jobs are being allocated unfairly. If you can fix this problem, it'll prove your chops to Commander Lambda so you can get promoted!

Minion's tasks are assigned by putting their ID numbers into a list, one time for each day they'll work on that task. As shifts are planned well in advance, the lists for each task will contain up to 99 integers. When a minion is scheduled for the same task too many times, they'll complain about it until they're taken off the task completely. Some tasks are worse than others, so the number of scheduled assignments before a minion will refuse to do a task varies depending on the task. You figure you can speed things up by automating the removal of the minions who have been assigned a task too many times before they even get a chance to start complaining.

Write a function called answer(data, n) that takes in a list of less than 100 integers and a number n, and returns that same list but with all of the numbers that occur more than n times removed entirely. The returned list should retain the same ordering as the original list - you don't want to mix up those carefully planned shift rotations! For instance, if data was [5, 10, 15, 10, 7] and n was 1, answer(data, n ) would return the list [5, 15, 7] because 10 occurs twice, and was thus removed from the list entirely.

#### Languages

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

#### Test Cases

#### Test Case 1

Inputs:

    (int list) data = [1, 2, 3]

    (int) n = 0

Output:

    (int list) []

#### Test Case 2

Inputs:

    (int list) data = [1, 2, 2, 3, 3, 3, 4, 5, 5]

    (int) n = 1

Output:

    (int list) [1, 4]
    
    


## En Route Salute

Time to solve: 72 hours.

#### Description

Commander Lambda loves efficiency and hates anything that wastes time. She's a busy lamb, after all! She generously rewards henchmen who identify sources of inefficiency and come up with ways to remove them. You've spotted one such source, and you think solving it will help you build the reputation you need to get promoted.

Every time the Commander's employees pass each other in the hall, each of them must stop and salute each other - one at a time - before resuming their path. A salute is five seconds long, so each exchange of salutes takes a full ten seconds (Commander Lambda's salute is a bit, er, involved). You think that by removing the salute requirement, you could save several collective hours of employee time per day. But first, you need to show her how bad the problem really is.

Write a program that counts how many salutes are exchanged during a typical walk along a hallway. The hall is represented by a string. For example:
"--->-><-><-->-"

Each hallway string will contain three different types of characters: '>', an employee walking to the right; '<', an employee walking to the left; and '-', an empty space. Every employee walks at the same speed either to right or to the left, according to their direction. Whenever two employees cross, each of them salutes the other. They then continue walking until they reach the end, finally leaving the hallway. In the above example, they salute 10 times.

Write a function answer(s) which takes a string representing employees walking along a hallway and returns the number of times the employees will salute. s will contain at least 1 and at most 100 characters, each one of -, >, or <.

#### Languages

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

#### Test Cases

#### Test Case 1

Inputs:

    (string) s = ">----<"

Output:

    (int) 2

#### Test Case 2

Inputs:
 
   (string) s = "<<>><"

Output:

    (int) 4


