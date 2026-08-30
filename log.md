## Day 1:

## Learnt
- functions, variables, parameters, def, round etc.
- how code works, top to bottom
- format strings

## Error
- multiple syntax errors, fixed them myself — mostly strings written wrong

## One line i didn't understand and now i do

- N/A

# Day 2

## Learnt
- convert strings to numbers BEFORE doing maths on them
- parentheses decide what a function acts on: float(p) / 100, not float(p / 100)
- functions take values through their parameter, not by re-fetching input inside

## Error
- repeated "str / int" TypeError - kept converting after dividing instead of before

## Done
- CS50P Pset 0 complete: indoor, playback, faces, einstein, tip - all submitted, full marks, no help from ai
- pset 0 complete, Bandit 0–8 done

## Day 3 

## Learnt
- conditionals in py: if, elif, else, match, or
- boolean expression, along with >, <, == etc.
- learnt more about being comfortable with the basics from before, indentation, def functions, etc.

## Error
- multiple syntax errors structuring expressions worked through and corrected

## Done
- thoroughly completed lecture 1: conditionals

## Day 4

## Learnt
- utilise .split() to assign multiple values, also methods like .startswith(), .endswith()
- utilising conditionals such as if, elif, match
- utilising comparison and arithmetic operators to match output to input
- general fluency and understanding of more complex code

## Error
- lots of minor syntax errors with comparison operators 
- def functions not functioning due to syntax errors within, not just syntax errors but not knowing what to assign to what, to make the code function - e.g: got the return value of a function as intended, not sure how to print that return value with print(), turns out you can just include the function inside of print to return the end value. - print(function())

## Done
- CS50 Problem set 1 - start to finish, full marks, minimal ai with no answers given by it, as always.

## Day 5

## Learnt
- Not following usual format today, small session - Finished 45 minutes into lecture 2. Understanding everything fine so far, just short on time today so i will finish lecture 2 + problem set 2 tomorrow.

## Day 6 

## Learnt 
- Learnt nested loops, and how to structure the logic to let the inner loop run before moving onto the outer loop, e.g using end="" to carry on the inner loop on the same line, and then manually print() after its done to move onto the next.

## Done 
- Finished lecture 2 - Loops

- Been busy the past couple of days, which threw the schedule off track. Was meant to also complete problem set 2 today, but atleast i finished the lecture with the given time i had. Going to move onto the problem set tomorrow and work on better consistency and bigger session times.

## Day 7

## Learnt 
- from the 2 tasks i completed i have learnt how to take more personalised input, and structure my code combining multiple things i have learnt so far to handle more complex tasks. Today has been especially 'for in' 'if in' 'char', combining strings, using end="" and mainly using loops - while True:

## Error
- using wrong logic multiple times trying to create lists, use 'for in' instead of 'if in' etc. I can differenciate them now, and use them accordingly.

## Done 
- completed tasks 1 and 2 on problem set 2, took me more time than expected, much longer than other problem sets so i wasnt able to complete it in one sitting, i'll complete it tomorrow and hopefully still work towards those bigger session times.

## Day 8

## Learnt
- Learnt significantly more about how methods, and functions actually take inputs, and how to structure them - as mentioned below
- Learnt the rule of counting ranges, indexing contrary to counting say len(string), len starts at 1 and counts content normally however when counting ranges etc. starts from 0 counting upwards for a different purpose

## Error 
- lead myself in circles with AI, not using it for answers but minimal guidance, instead it sent me in circles, using the wrong methods and structure. In the future when using AI for minimal guidance i will prioritise my own intuition, and resources such as py docs to avoid wasted time and AI misleading. 
*although - i am very serious about my own research and learning, i do not cut any corners with AI.*
- Misunderstanding several methods/functions, causing syntax errors and wrong tools — e.g. .replace() to delete instead of pass, range for length forgetting len(), .isdigit("0") passing an argument it doesn't take.
- Confused i as a value instead of a position in range(len(s)) loops — kept mixing char with i, breaking slices like s[i:].
- Misusing and misunderstanding return True within loops, not realising this will ultimately return True and break the loop instead of validating as true and moving on.

## Done
- Finished 2 more tasks in problem set 2, dedicated 4-5 hours today to this non-stop, however due to constant circling, and lost progression due to wrong structuring i lost a lot of time, lesson learnt. 1 more task remaining for problem set 2 - cs50 is having some problems with github, and i cannot check nor submit work so i will complete this aswell as hopefully lecture 3 in tomorrows session.


## Day 9:

## Learnt 
- dict, learnt the function, structure, and how to index in and find the matching key:value
- jog knowledge on basic shell commands - grep, cat

## Error
- not knowing how to index into dict, just trying to print(dictvariable) which printed the whole thing literally.

## Done
- finished problem set 2, although i cannot submit nor check due to error with github and cs50 persisting.
- very lightly skimmed lecture 1 of missing semester 

## Day 10

## Learnt
- learnt to focus more on structuring code so the logic flows, to avoid things such as the exception error below
- learnt try/except statements, how to catch errors such as ValueErrors or ZeroDivisionErrors and either pass them or print the error back to the user more succinctly + learnt what ValueErrors cover.
- how to utilise while loops to cover more code and contain more functionality, covered more on break, pass however i'd learnt them in past independent research

## Error
- trying to use multiple elses in a try:exception statement, instead should have just used multiple ' if * or if * or if * in a single else - yeah i still suck at explaining any code but lets work on it 
- structured the exception wrong - code structure ran lines of code outside of the try statement so they tried to run before they were actually filtered by the exception.

## Done
- finished lecture 3 - exceptions
- completed and submitted task 1 of problem set 3 

## Day 11

## Learnt
- Better understanding how keywords and statements function logically - continue, return, except, if, etc.
- More complex structuring of while loops incorporating: try:except statement and if:else conditional inside of loop, etc.
- how to create dicts from user input, used formatted string to print keys:values, utilised sorted() function to print the dict alphabetically etc., How to index into dict and manipulate keys / values per user input
- Assign variables to a value e.g 0, and then utilise a while loop so user can dynamically change the value with every input, then print/return a final value when the loop breaks.
- Exception handling different errors, ValueError and KeyError mainly for user input mistakes, But also EOFError to print / run a function after user quits (most commonly control+d).
- Better understanding of general code structure / logic, mainly indentation.

## Error
- spent 90 minutes on a problem set 3 task mainly fighting an overlapping pass statement and a exception handling KeyError, both fighting the same Error of input not matching what is inside of dict, eventually i realised i didnt need to handle KeyError at all, the exception was only meant to handle EOFError, when the user control+d to exit the program, i only realised this after fighting it for 90 minutes. After realisation it made the code 10x simpler, i should've noticed the logic not making sense earlier and checked if the error i was using inside of the exception was actually correct. Ultimately the 90 minutes was worth the lesson.
- When structuring my while loop, I used keywords like return and continue to attempt to return a validated value from an expression and then continue with the loop, not knowing return actually breaks out of the loop and returns said value as the final value. Instead for conditionals that need a body, I incorporated the rest of the loop inside of the body so the value is validated and then the loop continues to flow logically as intended.
- Mixed up keys and values in dict, I thought they were the opposite - value = word / item in dict, key = number of instances etc. but they are the other way around, resulted in wasted time but now i know.

## Done
- spent 5 hours on 2 tasks from problem set 3, a lot of trial and error, 1 task remaining until pset3 is finished. Will finish it tomorrow session and then catch up on either missing semester, or the CLI deliverable from Week 1.

## Day 12

## Learnt
- How to index into a list and assign the position of item in list to a variable using .index 
- Taking an input which has a possibility of being either digits or a string, and validating accordingly
- Padding in f strings to make sure digits are formatted correctly (x:02) so single digit characters lead with a 0
- Better understanding in general from restructuring code completely numerous times and fixing my errors. 
- While building my CLI, I learnt I could implement more complex features from things i have already learnt, such as instructing the user to type certain words which would register and function accordingly. In this case the words were 'list' and 'end'. When inputted, list would give a list of everything purchased so far today, aswell as give a running total so far before continuing to input again. When 'end' is inputted, the end of the spending day is signalled and a finalised total is printed.
- Customised the CLI to be user friendly and print a brief explanation of how the program functions when started.

## Error
- Same error as yesterday with return statement, realised yesterday that it breaks out of while loops and returns a final value, however today I learnt it also breaks out of whole function definitions and does the same.
- Misunderstanding of keywords 'pass' and 'continue'. I thought pass takes invalid input, disregards it, and re-runs the loop from the top — but it does not. pass does nothing with an invalid input and continues through to the code below, so invalid input still gets processed by everything beneath it as if the input was valid. The proper keyword here is continue, which does what I actually intended: on invalid input, skip the rest of the loop and jump back to the top, re-prompting the user.
- ^^ pattern accross days showing my main problem is understanding how to structure code, how logic flows, and the behavior of keywords and statements.
- On the last task of pset 3, structured the whole thing to work, but unconventionally. In the end i had the code which worked for every input except one error which accepted wrong input format, because of this one error, I had to restructure the whole code from the beginning: another brutal lesson which I need to work on avoiding.
- While building my CLI, I built the code perfectly, and then when testing, it was outputting the total as only one of the costs instead of tallying the cost up and building the value of the hardcoded total = 0 variable. I spent a hour restructuring code to try and fix it, and in the end it was simply a case of the += operator being backwards, and the program failing silently. Insane.

## Done
- Finished CS50 Problem set 3
- Successfully built my own expense tracker CLI incorporating multiple things I have learnt so far: Very proud of that one. (attached to repo)

## Day 13

## Learnt
- Took a step back to the fundamentals, learnt about how basic hardware functions and how it comes into play with everything. Learnt how cpu, gpu, ram and ssd actually function and what they handle which helped my understanding of how they come into play when running things like python and ubuntu (software in general)
- Gained a clearer understanding of what Linux actually is (just the kernel), what a kernel does, and how it differs from a full distribution like Ubuntu. (also clarified grey areas on understanding software like python and c/c++: mainly how things are interpreted and the logic flow top to bottom + differences between languages.)

## Error
- No specific bugs, but a huge grey area at the start regarding the fundamentals, I simply didnt know how everything functioned literally, what a kernel actually is vs a distro like ubuntu, what the hardware in my pc actually does etc. (Mostly clarified now)

## Done
- No concrete work completion today, which is fine. Today I wanted to step away from the guided work and focus on things I genuinely didnt understand, which happened to be the fundamentals listed above. Mostly back and fourth with AI, asking about said things and then making AI elaborate on grey areas until a clear understanding was reached.