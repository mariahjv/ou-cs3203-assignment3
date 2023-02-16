def sums(nums):
    sum = 0

    for i in nums:
        sum = sum + i

    return (sum)

def multiply(nums):
    product = 1

    for i in nums:
        product = product * i

    return (product)

def reverse(nums):
    reversed = nums[:: -1]

    return (reversed)

def main():
    nums = []
    user = input("Enter a number or 'done' to finish): ")
    while user != "done":
        nums.append(int(user))
        user = input("Enter a number or 'done' to finish: ")

    if len(nums) == None:
        print("No numbers were entered.")
    else:
        operation = input("Enter 'sum', or 'multiply': ")
        if operation == "sum":
            result = sums(nums)
            print(f"The sum of {nums} is {result}")
        elif operation == "multiply":
            result = multiply(nums)
            print(f"The product of {nums} is {result}")
        else:
            print("Invalid operation. Please enter 'sum' or 'multiply'.")