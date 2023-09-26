#------POPULAR ERRORS---------

##1 File not found
try:
    file = open("file.txt")
    a_dictionary = {"key": "value"}
    value = a_dictionary["key"]
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"Wrong with {error_message}")

else:
    content = file.read()
    print(content)

finally: 
    file.close()
    print("File closed.")


# #Key Error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non-existent_key"]

# #IndexError
# fruit = ["Apple", "Banana"]
# fruit_item = fruit[3]

# #TypeError
# text = "abc"
# print(text + 5)