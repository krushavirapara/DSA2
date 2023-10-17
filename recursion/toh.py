def toh(s,d,h,n):
    if n==1:
        print(f"movr disk {n} from {s} ro {d}")
        return 
    else:
        toh(s,h,d,n-1)
        print(f"move disk {n} from {s} to {d}")
        toh(h,d,s,n-1)

print(toh('s','d','h',3))
    