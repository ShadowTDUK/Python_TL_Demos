from practice_functions import say_hello_to_someone

message = say_hello_to_someone("Maggie")
print(message)

print("hello", "bye", "cat", "dog")
print("hello", "bye", "cat", "dog", "tuesday", "wednesday")

message_b = say_hello_to_someone("Homer")
print(message_b)

print("Print is a VARIADIC function")
print("It has been designed to accept a variable number of arguments")

print("Rod", "Jane", "Freddy", sep="-")
print("Rod", "Jane", "Freddy", end="!\u00A9\n")
print("Game Over")
print("Game Over")