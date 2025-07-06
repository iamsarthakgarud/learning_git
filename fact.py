def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))
