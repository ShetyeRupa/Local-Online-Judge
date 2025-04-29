import sys

def solve_problem_1():  # Sum of Two Numbers
    a, b = map(int, input().split())
    print(a + b)

def solve_problem_2():  # Maximum of Three Numbers
    a, b, c = map(int, input().split())
    print(max(a, b, c))

def solve_problem_3():  # Even or Odd
    n = int(input())
    print("Even" if n % 2 == 0 else "Odd")

def solve_problem_4():  # Factorial
    n = int(input())
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

def solve_problem_5():  # Reverse String
    s = input().strip()
    print(s[::-1])

def solve_problem_6():  # Fibonacci
    n = int(input())
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    print(a)

if __name__ == "__main__":
    problem_id = sys.argv[1] if len(sys.argv) > 1 else "1"
    
    if problem_id == "1":
        solve_problem_1()
    elif problem_id == "2":
        solve_problem_2()
    elif problem_id == "3":
        solve_problem_3()
    elif problem_id == "4":
        solve_problem_4()
    elif problem_id == "5":
        solve_problem_5()
    elif problem_id == "6":
        solve_problem_6()
    else:
        print("Invalid problem ID")