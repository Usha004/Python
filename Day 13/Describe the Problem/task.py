def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
#loop starting from 1 to repeating until 19 times as the second number excludes..(20-1)
# 2. When is the function meant to print "You got it"?
# as the function inside the if statement it will print whenever the condition true
# 3. What are your assumptions about the value of i?
#in for loop value of i valid from 1 to 19 as 20 excludes so we have to change the range then only for loop inside of if statements goes, otherwise it will come out of for loop and nothing will go print.
