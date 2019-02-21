#!/usr/bin/env python

def main():
	# Input is in form "######-#"
	while(True):
		student_id = raw_input("Please enter the student Id in form '######-#', to exit type 'quit' \n")

		if student_id == "quit":
			print "Quitting..."
			exit(1)

		else:

			index = student_id.find('?')

			if student_id[6] != '-':
				print "Student Id has not been entered in correct form, please try again."
				continue

			if index == -1:
				# There is no '?' in student_id, check for validity of the student id
				sum = compute(student_id,index)
				if sum % 10 == 0:
					print "VALID"
				else:
					print "INVALID"

			elif index == 0:
				sum = compute(student_id,index)
				closest_multiple = ((sum / 10) + 1) * 10
				digit = (closest_multiple - sum) % 10
				id = merge(student_id,digit,index)
				print id

			elif index == 1:
				sum = compute(student_id,index)
				closest_multiple = ((sum / 10) + 1) * 10
				if ((closest_multiple - sum) % 10) % 2 != 1:
					# Digit was multiplied by 2 and multiplication wasn't greater than 10 in this case
					digit = ((closest_multiple - sum) % 10) / 2
					id = merge(student_id,digit,index)
					print id
				else:
					# Digit was multiplied by 2 and multiplication was greater than 10 in this case
					digit = int('1' + str(((closest_multiple - sum) % 10) - 1)) / 2
					id = merge(student_id, digit, index)
					print id

			elif index == 2:
				sum = compute(student_id, index)
				closest_multiple = ((sum / 10) + 1) * 10
				digit = (closest_multiple - sum) % 10
				id = merge(student_id, digit, index)
				print id

			elif index == 3:
				sum = compute(student_id, index)
				closest_multiple = ((sum / 10) + 1) * 10
				if ((closest_multiple - sum) % 10) % 2 != 1:
					# Digit was multiplied by 2 and multiplication wasn't greater than 10 in this case
					digit = ((closest_multiple - sum) % 10) / 2
					id = merge(student_id, digit, index)
					print id
				else:
					# Digit was multiplied by 2 and multiplication was greater than 10 in this case
					digit = int('1' + str(((closest_multiple - sum) % 10) - 1)) / 2
					id = merge(student_id, digit, index)
					print id

			elif index == 4:
				sum = compute(student_id, index)
				closest_multiple = ((sum / 10) + 1) * 10
				digit = (closest_multiple - sum) % 10
				id = merge(student_id, digit, index)
				print id

			elif index == 5:
				sum = compute(student_id, index)
				closest_multiple = ((sum / 10) + 1) * 10
				if ((closest_multiple - sum) % 10) % 2 != 1:
					# Digit was multiplied by 2 and multiplication wasn't greater than 10 in this case
					digit = ((closest_multiple - sum) % 10) / 2
					id = merge(student_id, digit, index)
					print id
				else:
					# Digit was multiplied by 2 and multiplication was greater than 10 in this case
					digit = int('1' + str(((closest_multiple - sum) % 10) - 1)) / 2
					id = merge(student_id, digit, index)
					print id

			elif index == 7:
				sum = compute(student_id, index)
				closest_multiple = ((sum / 10) + 1) * 10
				digit = (closest_multiple - sum) % 10
				id = merge(student_id, digit, index)
				print id

def even_pos(num):
	value = 2 * int(num)
	if value < 10:
		return value
	else:
		return int(str(value)[0]) + int(str(value)[1])

def compute(stud_id,index):
	if index == -1:
		result = int(stud_id[0]) + even_pos(stud_id[1]) + int(stud_id[2]) + even_pos(stud_id[3]) + int(stud_id[4]) + even_pos(stud_id[5]) + int(stud_id[7])
	elif index == 0:
		result = even_pos(stud_id[1]) + int(stud_id[2]) + even_pos(stud_id[3]) + int(stud_id[4]) + even_pos(stud_id[5]) + int(stud_id[7])
	elif index == 1:
		result = int(stud_id[0]) + int(stud_id[2]) + even_pos(stud_id[3]) + int(stud_id[4]) + even_pos(stud_id[5]) + int(stud_id[7])
	elif index == 2:
		result = int(stud_id[0]) + even_pos(stud_id[1]) + even_pos(stud_id[3]) + int(stud_id[4]) + even_pos(stud_id[5]) + int(stud_id[7])
	elif index == 3:
		result = int(stud_id[0]) + even_pos(stud_id[1]) + int(stud_id[2]) + int(stud_id[4]) + even_pos(stud_id[5]) + int(stud_id[7])
	elif index == 4:
		result = int(stud_id[0]) + even_pos(stud_id[1]) + int(stud_id[2]) + even_pos(stud_id[3]) + even_pos(stud_id[5]) + int(stud_id[7])
	elif index == 5:
		result = int(stud_id[0]) + even_pos(stud_id[1]) + int(stud_id[2]) + even_pos(stud_id[3]) + int(stud_id[4]) + int(stud_id[7])
	elif index == 7:
		result = int(stud_id[0]) + even_pos(stud_id[1]) + int(stud_id[2]) + even_pos(stud_id[3]) + int(stud_id[4]) + even_pos(stud_id[5])
	return result

def merge(stud_id,digit,index):
	if index == 0:
		id = str(digit) + stud_id[1] + stud_id[2] + stud_id[3] + stud_id[4] + stud_id[5] + stud_id[6] + stud_id[7]
	elif index == 1:
		id = stud_id[0] + str(digit) + stud_id[2] + stud_id[3] + stud_id[4] + stud_id[5] + stud_id[6] + stud_id[7]
	elif index == 2:
		id = stud_id[0] + stud_id[1] + str(digit) + stud_id[3] + stud_id[4] + stud_id[5] + stud_id[6] + stud_id[7]
	elif index == 3:
		id = stud_id[0] + stud_id[1] + stud_id[2] + str(digit) + stud_id[4] + stud_id[5] + stud_id[6] + stud_id[7]
	elif index == 4:
		id = stud_id[0] + stud_id[1] + stud_id[2] + stud_id[3] + str(digit) + stud_id[5] + stud_id[6] + stud_id[7]
	elif index == 5:
		id = stud_id[0] + stud_id[1] + stud_id[2] + stud_id[3] + stud_id[4] + str(digit) + stud_id[6] + stud_id[7]
	elif index == 7:
		id = stud_id[0] + stud_id[1] + stud_id[2] + stud_id[3] + stud_id[4] + stud_id[5] + stud_id[6] + str(digit)
	return id


if __name__ == "__main__":
	main()