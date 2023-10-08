class Star_cinema:
    __hall_list = []

    def entry_hall(self, hall):
        Star_cinema.__hall_list.append(self)


class hall(Star_cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)
        super().__init__()

    def entry_show(self, id, movie_name, time):
        movieinfo = (id, movie_name, time)
        self.show_list.append(movieinfo)
        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        # self.seats[id] = sit

    def book_seats(self, id, seatlist):
        if id not in [show[0] for show in self.show_list]:
            print("Invalid ID")
            return False
        mainseat = self.seats[id]
        booked = []
        for seat in seatlist:
            (r, c) = seat
            # print(r, c)
            if 0 <= r <= self.rows and 0 <= c <= self.cols:
                if mainseat[r - 1][c - 1] == 0:
                    mainseat[r - 1][c - 1] = 1
                    booked.append(seat)
                # print(f"({r,c}) seat is booked for you")
                else:
                    print(f"Seat ({r}, {c}) is already booked.")
            else:
                print("invaild row coloum")
        for book in booked:
            print(f"seat {book} is booked for you")

    def view_show_list(self):
        for show in self.show_list:
            print(f"Show id: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}")

    def view_avaiable_seats(self, sid):
        seats = self.seats[sid]
        print("1 is shows booked seats ")
        print("0 is shows available seats ")
        for row in seats:
            for seat in row:
                print(seat, end=" ")
            print()

    # print(len(self.hall_list))


hal1 = hall(5, 5, 1)
# hal1.entry_hall()
hal1.entry_show(12, "loss", "4 pm")


while True:
    print("1.BUY tickets")
    print("2.view which show is running")
    print("3.view available seats")
    print("4.exit")
    print("Enter your option :- ")
    op = int(input())
    if op == 1:
        num = int(input("enter number of tickets"))
        id = int(input("enter show id:- "))
        seatlist = []
        for i in range(1, num + 1):
            r = int(input("enter the seat row:- "))
            c = int(input("enter the seat colum:- "))
            seatlist.append((r, c))
        hal1.book_seats(id, seatlist)
    elif op == 2:
        hal1.view_show_list()
    elif op == 3:
        id = int(input("Enter the show id:- "))
        hal1.view_avaiable_seats(id)
    elif op == 4:
        print("thank you ")
        break
