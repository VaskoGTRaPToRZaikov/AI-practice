def is_prime(num):
    if num < 2:
        return False
    return all(num % i != 0 for i in range(2,int(num ** 0.5) + 1))

numbers = [int(number.strip()) for number in input().split(", ")]

prime_numbers = [number for number in numbers if is_prime(number)]
composite_numbers = [number for number in numbers if not is_prime(number) and number > 1]
even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 !=0]


print(f"Primes: {prime_numbers}")
print(f"Composites: {composite_numbers}")
print(f"Evens: {even_numbers}")
print(f"Odds: {odd_numbers}")





