def palindrome():
    user_input = input("Please Enter The Words: ")
    right = len(user_input) - 1
    left = 0

    while left < right:
        if user_input[left] != user_input[right]:
            print("Not a Palindrome")
            return
        left += 1
        right -= 1

    print("It is a Palindrome")


palindrome()