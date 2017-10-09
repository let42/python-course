# Write a function that print something n times
# including relatives spaces


def pprint(wyp, ntimes):
    wyp = str(wyp) + " "
    print wyp * ntimes

def main():
    
    pprint(555, 24)
    
    exit(0)

main()