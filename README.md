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
    
    

# ====================================
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

# ======================================
## Find the Access Codes

Time to solve: 96 hours.

### Description

In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. But the only door leading to the LAMBCHOP chamber is secured with a unique lock system whose number of passcodes changes daily. Commander Lambda gets a report every day that includes the locks' access codes, but only she knows how to figure out which of several lists contains the access codes. You need to find a way to determine which list contains the access codes once you're ready to go in. 

Fortunately, now that you're Commander Lambda's personal assistant, she's confided to you that she made all the access codes "lucky triples" in order to help her better find them in the lists. A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z, such as (1, 2, 4). With that information, you can figure out which list contains the number of access codes that matches the number of locks on the door when you're ready to go in (for example, if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).

Write a function answer(l) that takes a list of positive integers l and counts the number of "lucky triples" of (lst[i], lst[j], lst[k]) where i < j < k.  The length of l is between 2 and 2000 inclusive.  The elements of l are between 1 and 999999 inclusive.  The answer fits within a signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0. 

For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the answer 3 total.

### Languages

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

### Test Cases

#### Test Case 1

Inputs:
    (int list) l = [1, 1, 1]
Output:
    (int) 1

#### Test Case 2

Inputs:
    (int list) l = [1, 2, 3, 4, 5, 6]
Output:
    (int) 3
    
# ==============================   
## Fuel Injection Perfection

#### Description
Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for her LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit of sabotage while you're at it - so you took the job gladly.

Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time.

The fuel control mechanisms have three operations:

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

Write a function called answer(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

For example:
answer(4) returns 2: 4 -> 2 -> 1
answer(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

#### Test cases


Inputs:
    (string) n = "4"
Output:
    (int) 2

Inputs:
    (string) n = "15"
Output:
    (int) 5

# ============================
## Baby Bomb

#### The challenge specification
You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in order to do so, you need to deploy special self-replicating bombs designed for you by the brightest scientists on Bunny Planet. There are two types: Mach bombs (M) and Facula bombs (F). The bombs, once released into the LAMBCHOP's inner workings, will automatically deploy to all the strategic points you've identified and destroy them at the same time.

But there's a few catches. First, the bombs self-replicate via one of two distinct processes:
Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
Every Facula bomb spontaneously creates a Mach bomb.

For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle.

Second, you need to ensure that you have exactly the right number of Mach and Facula bombs to destroy the LAMBCHOP device. Too few, and the device might survive. Too many, and you might overload the mass capacitors and create a singularity at the heart of the space station - not good!

And finally, you were only able to smuggle one of each type of bomb - one Mach, one Facula - aboard the ship when you arrived, so that's all you have to start with. (Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP, but that's not going to stop you from trying!)

You need to know how many replication cycles (generations) it will take to generate the correct amount of bombs to destroy the LAMBCHOP. Write a function answer(M, F) where M and F are the number of Mach and Facula bombs needed. Return the fewest number of generations (as a string) that need to pass before you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M and F will be string representations of positive integers no larger than 10^50. For example, if M = "2" and F = "1", one generation would need to pass, so the answer would be "1". However, if M = "2" and F = "4", it would not be possible.


#### Test cases
Inputs:
`(string) M = "2" (string) F = "1"`

Output:
`(string) "1"`


Inputs:
`(string) M = "4" (string) F = "7"`

Output:
`(string) "4"`

Inputs:
`(string) M = "2" (string) F = "4"`

Output:
`(string) "impossible"`

### Understanding

I guess the best way to describe the problem is to imagine yourself starting with two numbers `F` and `M`, both of which have the value of `1`. At the start you are currently in `step 0`, to progress a step you must either;

* Add the value of `F` onto `M` to calculate a new `M`, _or_,
* Add the value of `M` onto `F` to calculate a new `F`.

Because of the rules of the specification we can create some facts:

* Because of the steps, `F` can never equal `M` if `step n` > `0`.
* If `F` > `M` we know that the last step to take place involved adding `M` to `F`.
* If `M` > `F` we know that the last step to take place involved adding `F` to `M`.

### A Solution

One sure way to solve this challenge is to reverse engineer the two numbers they provide. From the rules to get from `step n` to `step n-1` we just do `F` = `F` - `M` or `M` = `M` - `F` depending if `F` or `M` is larger than the other.

For example:
```
F = 7   M = 4
    F > M ∴ F = 7 - 4
F = 3   M = 4
    M > F ∴ M = 4 - 3
F = 3   M = 1
    F > M ∴ F = 3 - 1
F = 2   M = 1
    F > M ∴ F = 2 - 1
F = 1   M = 1
```

Well.. that is fairly easy, we have a solution already - we know that if we do not end up with `1` and `1` there is no solution.

But... It is pretty slow. The specification mentions that the inputs can be up to 10^50 in size. Now imagine if we had the inputs `F = 1` and `M = 10^50` we would have to do our calculation 10^50 - 1 times, and who knows how long you will be waiting for that to compute.

This problem occurs when `F | M` is larger by several multiples than its counterpart. So how about we see how many times `F | M` fits into `M | F`, then we increase the counter for how many times it can be divided into the other one.

For example:
```
F = 31   M = 4
    F > M ∴ F = 31 - 4 * (31 / 4) //Rounded down of course
F = 3    M = 4
...
```

This solution avoids the problem with massive differences in the numbers and greatly optimizes the solution.

I think this challenge is pretty straight forward but the real challenge is making it optimized, I think there is enough in this file for you to go and take a good shot at this problem.

### Summary

In summary the steps for this solution are:

* Find out if the current `step` you are on is _solvable_.

* If it is, find out if `F` or `M` is bigger.

* Divide the smaller one into the bigger one, round down, to find out the multiplier to increase the counter and to subtract the larger one to find the answer faster.

* Repeat steps until you have `1` and `1`, frequently check if _solvable_ using a custom function and finally print out the counter of how many steps it took.

Some tips:

* Write a custom method to check if you can actually solve the problem, i.e. check if > 0, check `F` != `M` ect.

* Expect numbers larger than 10^32! So use `BigInteger` for example.

* If you are testing your solution and the tests are not running and instead you get a generic `error` it is most likely because the solution you have provided is unoptimized and is too slow. Test out your solution with big numbers.

* If you want some good numbers to test edge case, provide a number N and N + 1 as long as they are greater than 1.
Good luck!

