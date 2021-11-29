def computepay(h, r):
    if h <= 40:
        pay = h * r
    else:
        pay=  (40 * r) + ((h-40) * (r*1.5))
    return pay

hrs = input("Enter Hours:")
rate = input("Enter hourly rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Retry - please enter numbers only")
    quit()

#p = computepay(10, 20)
p = computepay(h,r)
print("Pay", p)
