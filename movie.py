import random
class Person:
    def __init__(self,name,phone,age,gender,mailid,wallet):
        self.name = name
        self.phone = phone
        self.age = age
        self.gender = gender
        self.mailid = mailid
        self.wallet = wallet

        self.ticket = []


    def details(self):
        print(f'name : {self.name} \nage : {self.age} \ngender : {self.gender} \nemail : {self.mailid} \nphone : {self.phone} \nwallet bal : {self.wallet} \n')


    def add_amt(self):
        amt = int(input('enter the amount : '))
        self.wallet += amt
        print(f'{amt} added to wallet')


class Theatre:
    def __init__(self,name,capacity,movie,b_price,s_price):
        self.name = name
        self.capacity = capacity
        self.movie = movie
        self.b_price = b_price
        self.s_price = s_price
        self.boxoffice = 0
        self.balcony = list(range(1,capacity//2+1))
        self.second = list(range(capacity//2+1,capacity+1))


    def details(self):
        print(f'name : {self.name} \nmovie : {self.movie} \ncapacity : {self.capacity}\nbalcony price : {self.b_price}\nsecond class : {self.s_price}\nBox office coll : {self.boxoffice}')

    def display_seats(self):
        ind = 0
        print(f'-----------------------------Balcony Rs.{self.b_price}--------------------------')
        for i in range(len(self.balcony)//10 + 1):
            for j in range(10):
                if ind == len(self.balcony):
                    break
                print(self.balcony[ind],end='\t')
                
                ind += 1
            print()

        ind = 0
        print(f'------------------------------Second Rs.{self.s_price}------------------------------')
        for i in range(len(self.second)//10 + 1):
            for j in range(10):
                if ind == len(self.second):
                    break
                print(self.second[ind],end='\t')
                
                ind += 1
                    
            print()

        print('######################### SCREEN ##############################')
        print('         #########################################')


class Book_ticket:

    def __init__(self):
        self.seats = []
        self.total = 0
        self.status = ''
        self.tno = random.randint(100000,999999)

    def select_seat(self,theatre,person):
        seat_no = eval(input('enter the seat number : '))
        if type(seat_no) == int:
        
            seat_no = (seat_no,)
    
        for i in range(len(theatre.balcony)):
            if theatre.balcony[i] in seat_no:
                if person.wallet >= theatre.b_price:
                    self.seats.append(theatre.balcony[i])
                    person.wallet -= theatre.b_price
                    theatre.balcony[i] = '@'
                    self.total += theatre.b_price
                else:
                    self.cancel_booking(theatre,person)
                    print('insufficient fund')


        for i in range(len(theatre.second)):
            if theatre.second[i] in seat_no:
                if person.wallet >= theatre.s_price:
                    self.seats.append(theatre.second[i])
                    person.wallet -= theatre.s_price
                    theatre.second[i] = '@'
                    self.total += theatre.s_price
                else:
                    self.cancel_booking(theatre,person)
                    print('insufficient fund')

            
        person.ticket.append(self)
        self.status = 'booking Successfull'

    def cancel_booking(self,theatre,person):
        for i in range(len(theatre.balcony)):
            if i+1  in self.seats:
                theatre.balcony[i] = i+1


        second_class = list(range(theatre.capacity//2+1,theatre.capacity+1))
        for i,j in zip(second_class,range(len(theatre.second))):
            if i in self.seats:
                theatre.second[j] = i
        
        person.wallet += self.total
        
        self.status = 'Booking cancelled'
        print('tickects has been cancelled')
        

    def display_ticket(self,theatre,person):
        print('Tickect No : ',self.tno)
        print('user name : ',person.name)
        print('theatre name : ',theatre.name)
        print('seat no : ',self.seats)
        print('Total : Rs.',self.total)
        print('Status : ',self.status)


Gt_mall = Theatre('Pvr',50,'Thor',300,200)
Prasanna = Theatre('prasana',100,'Mad max',200,150)
while True :
    print('                      Welcome to Theatre                         ')
    print('enter list to display movie list')
    print('enter create to create user profile')
    print('enter ticket to display ticket')
    print('enter user to display User details')
    print('enter stop to terminate program')
    print('enter book to book ticket')
    print('enter cancel to cancel the booking')
    action = input(' : ')
    if action == 'stop':
        break
    elif action == 'create':
        name = input('enter the name : ')
        phone = int(input('enter the phone nummber : '))
        age = int(input('enter the age : '))
        email = input('enter the email id : ')
        gender = input('enter the gender : ')
        wallet = int(input('enter the amount : '))
        
        person = Person(name,phone,age,gender,email,wallet)
    elif action == 'ticket':
        for ticket in person.ticket:
            ticket.display_ticket(Gt_mall,person)
    elif action == 'list':
        Gt_mall.details()
    elif action == 'user':
        person.details()
    elif action == 'book':
        b_t = Book_ticket()
        b_t.select_seat(Gt_mall,person)
    elif action == 'cancel':
        for ticket in person.ticket:
            ticket.display_ticket(Gt_mall,person)
        print('enter the ticket no to cancel booking : ')
        no = int(input(' : '))
        person.ticket[no-1].cancel_booking(Gt_mall,person)
    else:
        print('invalid choice')

