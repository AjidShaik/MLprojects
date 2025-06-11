# def is_prime(n):
#     if n <= 1:
#         return False

#     is_prime_flag = True
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime_flag = False
#             break

#     return is_prime_flag

# # Example:
# print(is_prime(7))   # True
# print(is_prime(12))  # False

# factorial number
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

#     #Example 
# print(factorial(5))

#fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for i in range (n):
        print(a, end=" ")
        a,b =b, a + b
#example
print(fibonacci(7))
