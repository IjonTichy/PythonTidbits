

def quadratic(a, b, c):
    s1 = ( (b**2) - (4*a*c) ) ** 0.5
    s2 = 2*a

    ret = [(-b - s1) / s2, (-b + s1) / s2]
    return ret
