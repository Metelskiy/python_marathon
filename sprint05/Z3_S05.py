def solve_quadric_equation(a, b, c):
    try:
        a=float(a)
        b=float(b)
        c=float(c)
        d = b ** 2 - 4 * a * c
        #if d > 0:
        x1 = (-b - d**(0.5)) / (2 * a)
        x2 = (-b + d**(0.5)) / (2 * a)
        return f"The solution are x1={complex(x1)} and x2={complex(x2)}"
    except(ZeroDivisionError):
        return "Zero Division Error"
    except:
        return "Could not convert string to float"
print(solve_quadric_equation(1,4,5))
