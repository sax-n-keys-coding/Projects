def grow(n):
    if n >= 10:
        grow(n // 10)
    print(n)
    
def shrink(n):
    print(n)
    if n >= 10:
        shrink(n // 10)

def cascade(n):
    grow(n)
    if n >= 10:
        shrink(n // 10)
        
cascade(123)