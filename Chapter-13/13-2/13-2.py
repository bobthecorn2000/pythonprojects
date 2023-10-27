#!/usr/bin/env python3

from ctypes.wintypes import DOUBLE


def move_disk(n, src, dest, temp):
    print("    move_disk(n={:d}, src={:s}, dest={:s}, temp={:s})".format(n, src, dest, temp))

    if n == 0:
        return
    else:
        move_disk(n-1, src, temp, dest)
        print("Move disk", n, "from", src, "to", dest)
        move_disk(n-1, temp, dest, src)
        
def main():
    print("**** TOWERS OF HANOI ****")
    print()
    num_disks = int(input("Enter number of disks: "))
    print(f"it would take a minimum of {2**num_disks - 1} moves to complete")
    input("press enter to start")
    print()
    
    move_disk(num_disks, "A", "C", "B")

    print()
    print("All disks have been moved.")

if __name__ == "__main__":
    #ignore this i wanted to see how high i could get the number on an overclocked gaming pc so i set it to the max int, turns out very high. let it run overnight. was still going in the morning
    import sys
    sys. setrecursionlimit(2147483647)
    print(sys.getrecursionlimit())
    
    main()