
def check_pelindrome(input_value):
    if input_value == input_value[::-1]:
        print("yes")
    else:
        print("no")


while True:
    input_value = input()
    
    if input_value == '0':
        break
    else:
        check_pelindrome(input_value)

    
    