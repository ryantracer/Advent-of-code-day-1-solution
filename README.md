# Advent-of-code-day-1-solution
This is my solution for the first challenge of advent of code, i decided to save all of the codes that i write while solving it for funsies.

# The challenge
With a little storytelling about elves needing a password for the entrance of the north pole, it is supposedly a safe-like entrance that rotates in a cycle, the numbers go from 0 to 99 and the starting position is 50, the password is the amount of times we reach 0, it can rotate to the left or the right.

L8 for example means "eight to the left" while R20 means "twenty to the right".

the code uses modular arithmetic to maintain a cycle and adds for right (R), then subtracts for left (L).

the website will give you your input for the problem, with my script i got the number 1129.
