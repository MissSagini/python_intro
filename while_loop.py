# requires an initialization step. This includes declaring a var and giving it the imitial state
# num = 10
# while num > 0:
#     print(num)
#     # the increment step is brought up here
#     num = num - 1
# print('Finished looping!')

# num = 1000
# while num > 0:
#     if num == 800:
#         break
#     print(num)
#     # the increment step is brought up here
#     num = num - 1
# print('Finished looping!')

# word = 'Python'
# while True:
#     guess = str(input("Which is the most popular programming language in 2026?....\n"))
#     if guess == '':
#         print('Please enter valid guess')
#         continue 
#     if guess == word:
#         print('Congragulations! You guessesd right.')
#         break
#     print('Nice attempt. Please try again, another time')

# score = '47'
# while True:
#     answer = str(input("what is 25 + 22?....\n"))
#     if answer == '':
#         print('Please enter valid number')
#         continue 
#     if answer == score:
#         print('Congragulations! You are right.')
#         break
#     print('Nice attempt. Please try again, another time')

my_num = 7
while True:
    guess = int(input('Give me a prime number between 1 and 10...\n')) #1
    if guess < 0:
        print('Enter positive number')
        continue
    if guess == my_num:
        print("Congragulations you made it!")
        break
    print('Plese try again')