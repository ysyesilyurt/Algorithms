# Check digit controller
Simple check-digit controller for Student Id's


A check digit is a form of redundancy check used for error detection on identification numbers, such as bank account numbers, which are used in an application where they will at least sometimes be input manually. It consists of one or more digits computed by an algorithm from the other digits (or letters) in the sequence input. With a check digit, one can detect simple errors in the input of a series of characters (usually digits) such as a single mistyped digit or some permutations of two successive digits. My university implements also a check digit algorithm for student numbers. A student number has exactly six digits. The Algorithm works as follows: 

1. sum = 0
2. For each digit in the student number that has an odd position (first, third, fifth) take the digit and add it to the sum.
3. For each digit in the student number that has an even position (second, forth, sixth) take twice the digit. If this result of doubling is a two digit number then add each of these digits to the sum, otherwise add the result of the doubling (which is a single digit number itself) to the sum.
4. The one digit number, which when added to the sum results in a multiple of 10, is the check digit

This program determines the digit that is missing from a student-id or if no digit is missing to determine whether it is valid or not. 
A student-id will be read from the standard input as '######-#', where each # is a decimal digit or a ‘?’ (question mark). 
There must be at most one question mark. It is also possible that no question mark appears in the input (then the program checks the validity of the Id).


I/O Example:

Please enter the student Id in form '######-#', to exit type 'quit' 

232456-6

	INVALID

248965-6

	VALID

2?8965-6

	248965-6

248965-?

	248965-6