def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

moveTower(3,"A","B","C")

def get_fib(position):
    if(position >= 0 and position < 2): return position
    return get_fib(position - 1) + get_fib(position - 2)

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
