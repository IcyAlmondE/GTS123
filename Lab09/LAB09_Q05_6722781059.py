def SeatType():
    s = input("Select the seat type (P or D or H): ")
    l = "PDH"
    while s not in l:
        print("Wrong seat type! Please select again.")
        s = input("Select the seat type (P or D or H): ")
    return l.index(s)

def MovieType():
    m = input("Select the movie type (1 or 2): ")
    l = "12"
    while m not in l:
        print("Wrong movie type! Please select again.")
        m = input("Select the movie type (1 or 2): ")
    return l.index(m)

def TicketPrice(s, m):
    price = [[100, 120],
             [140, 200],
             [400, 500]]
    print("\nThe tichket price is", price[s][m])

TicketPrice(SeatType(), MovieType())