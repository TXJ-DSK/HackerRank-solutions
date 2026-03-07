def bonAppetit(bill, k, b):
    anna = sum(bill)/2 - bill[k]/2
    refund = b - anna
    if refund == 0:
        print("Bon Appetit")
    else:
        print(int(refund))
