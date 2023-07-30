from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tmsg
import sqlite3 as sql

root = Tk()  # main window


def create_table():
    con = sql.connect("users.db")
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS user(id integer PRIMARY KEY AUTOINCREMENT, firstname text NOT NULL, lastname text NOT NULL, username text NOT NULL, password text NOT NULL )""")
    cur.execute(
        """CREATE TABLE IF NOT EXISTS booking(id INTEGER PRIMARY KEY AUTOINCREMENT, username text NOT NULL, location text NOT NULL,hotel text NOT NULL,date text NOT NULL,days integer NOT NULL,rent INTEGER NOT NULL)""")
    con.commit()
    con.close()


def add_hotel(new_ho, new_re):
    con = sql.connect("users.db")
    cur = con.cursor()
    cur.execute(f"""INSERT INTO rent(hotel,rent) VALUES('{new_ho}','{new_re}')""")
    con.commit()
    con.close()


def remove_hotel(ho):
    con = sql.connect("users.db")
    cur = con.cursor()
    cur.execute(f"""DELETE FROM rent WHERE hotel='{ho}'""")
    con.commit()
    con.close()


def change_rent(hotel_name, newrent):
    con = sql.connect("users.db")
    cur = con.cursor()
    cur.execute(f"""UPDATE rent SET rent='{newrent}' WHERE hotel='{hotel_name}'""")
    con.commit()
    con.close()


create_table()
new_ho = StringVar()
new_re = StringVar()
ho = StringVar()
hotel_name = StringVar()
changed_rent = StringVar()


# user code begins here
def user():
    # User mode
    new_user_window = Toplevel()
    new_user_window.geometry("1200x800")
    new_user_window.title("USER MODE")
    bg = PhotoImage(file="E:\\23ce0208-dd0c-4ccd-9da1-61e65dad4129.png")
    Label(new_user_window, image=bg).place(x=0, y=0)

    username_var = StringVar()

    def new_user_input():
        # if both passwords do not match then error message
        if p.get() != cn.get():
            msg = Label(new_user_window, text="Password Doesnot Match!Type again.", fg='red')
            msg.place(x=1000, y=500)
        else:
            con = sql.connect("users.db")
            cur = con.cursor()
            cur.execute(
                f"""INSERT INTO user(firstname,lastname,username,password) VALUES('{fn.get()}','{ln.get()}','{un.get()}','{p.get()}')""")
            con.commit()
            con.close()

    def new_user():
        con = sql.connect("users.db")
        cur = con.cursor()
        cur.execute(
            f"""INSERT INTO user(firstname,lastname,username,password) VALUES('{fn.get()}','{ln.get()}','{un.get()}','{p.get()}')""")
        con.commit()
        con.close()

    def checking():
        con = sql.connect("users.db")
        cur = con.cursor()
        cur.execute(
            f"SELECT username FROM user WHERE username='{username.get()}' AND password='{password.get()}';")
        counter = cur.fetchone()
        if counter is None:
            return False
        else:
            return True

    def submit():
        check = checking()

        def loc():
            pass

        def cindate():
            pass

        def newbook():
            # User can make a new booking here
            us = Toplevel()
            us.geometry("720x480")
            us.configure(bg="Lightblue")

            list1 = ['Lahore', 'Rawalpindi', 'Islamabad', 'Faisalabad', 'Multan']

            location = StringVar()
            hotel = StringVar()
            day = StringVar()
            month = StringVar()
            year = StringVar()
            days = StringVar()

            def add_booking():
                def pp():  # if postpaid selected then this happens
                    tmsg.showinfo("Confirmation", "Your booking is confirmed ")
                    us.destroy()
                    payment.destroy()
                    us.destroy()

                def credit():  # if prepaid selected then this menu appears
                    def mesg():
                        tmsg.showinfo("Booking Confirmed", "Your booking has been confirmed")

                    Label(payment, text="Card Number", bg="LightBlue", font="Helvetica 14").place(x=100, y=100)
                    Label(payment, text="Name", bg="LightBlue", font="Helvetica 14").place(x=100, y=150)
                    Label(payment, text="Expiry Date", bg="LightBlue", font="Helvetica 14").place(x=100, y=200)
                    Label(payment, text="Card Pin", bg="LightBlue", font="Helvetica 14").place(x=100, y=250)
                    Entry(payment, font="Helvetica 14").place(x=250, y=200)
                    Entry(payment, font="Helvetica 14").place(x=250, y=250)
                    Entry(payment, font="Helvetica 14").place(x=250, y=100)
                    Entry(payment, font="Helvetica 14").place(x=250, y=150)
                    Button(payment, text="Submit", width=10, bg="Seagreen", command=mesg).place(x=200, y=300)

                # When booking is made user can select the payment method
                payment = Tk()
                payment.configure(bg="LightBlue")
                payment.geometry("650x600")
                Label(text="Add payment type:")
                b1 = Button(payment, font="Lucida 15", width=15, text="Credit Card", bg="Seagreen",
                            command=credit).pack(side=LEFT, anchor="nw")
                b2 = Button(payment, font="Lucida 15", width=15, text="Debit Card", bg="Seagreen", command=credit).pack(
                    side=LEFT, anchor="nw")
                b3 = Button(payment, font="Lucida 15", width=15, text="Easy Paisa", bg="Seagreen", command=credit).pack(
                    side=LEFT, anchor="nw")
                b4 = Button(payment, font="Lucida 15", width=15, text="Post Paid", bg="Seagreen", command=pp).pack(
                    side=LEFT, anchor="nw")
                rent = 0

                # here rents are specified
                if hotel.get() == 'Crown':
                    rent = 15000
                elif hotel.get() == 'Monal':
                    rent = 11000
                elif hotel.get() == 'United':
                    rent = 12000
                elif hotel.get() == 'Pearl':
                    rent = 13000

                con = sql.connect("users.db")
                cur = con.cursor()
                cur.execute(f"""SELECT count('hotel') FROM booking WHERE hotel='{hotel.get()}' """)
                count = cur.fetchall()[0][0]

                if count > 10:
                    Error = Label(us, text="Sorry! This Hotel is Full.Kindly choose another one", fg='red')
                    Error.place(x=350, y=120)
                    con.commit()
                else:
                    cur.execute(
                        f"""INSERT INTO booking('username','location','hotel','date','days','rent') VALUES('{username_var.get()}','{location.get()}','{hotel.get()}','{day.get() + '/' + month.get() + '/' + year.get()}','{days.get()}','{rent}')""")
                    con.commit()
                    con.close()

            # user can select the location here
            combo = ttk.Combobox(
                us, values=list1, textvariable=location, height=20, font="Arial 15 italic")
            combo.set("Pick a location")
            combo['state'] = 'readonly'
            combo.place(x=10, y=50)
            list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
                     17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
            list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
            list4 = [2023, 2024]
            list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

            con = sql.connect("users.db")
            cur = con.cursor()
            cur.execute("""SELECT hotel FROM rent""")
            list6 = cur.fetchall()
            con.commit()
            con.close()

            # User can select the Hotel of his choice
            combo6 = ttk.Combobox(us, value=list6, textvariable=hotel, height=20, font="Arial 15 italic")
            combo6.set("Pick a Hotel")
            combo6['state'] = 'readonly'
            combo6.place(x=10, y=100)

            # User can choose the checkin date
            label1 = Label(us, text="Check-in date", bg="Lightblue", font="Arial 15 italic").place(x=0, y=160)
            combo2 = ttk.Combobox(us, values=list2, textvariable=day, height=20, width=10, font="Arial 15 italic")
            combo2.set("dd")
            combo2['state'] = 'readonly'
            combo2.place(x=10, y=200)

            # User can select the month
            combo3 = ttk.Combobox(us, values=list3, textvariable=month, height=20, width=10, font="Arial 15 italic")
            combo3.set("mm")
            combo3['state'] = 'readonly'
            combo3.place(x=160, y=200)

            # User can select teh year
            combo4 = ttk.Combobox(us, values=list4, textvariable=year, height=20, width=10, font="Arial 15 italic")
            combo4.set("yyyy")
            combo4['state'] = 'readonly'
            combo4.place(x=310, y=200)

            # User can select the number of days to be booked
            combo5 = ttk.Combobox(us, values=list5, textvariable=days, height=20, width=10, font="Arial 15 italic")
            combo5.set("Select days")
            combo5['state'] = 'readonly'
            combo5.place(x=10, y=300)

            Button(us, text="Submit", command=add_booking, height=2, bg="Seagreen", font="Arial 10 italic").place(x=25,
                                                                                                                  y=400)

        def oldbook():  # User can checkhi old bookings
            info = Toplevel()
            info.geometry('700x400')
            info.title("Your Bookings")
            info.configure(bg="LightBlue")

            con = sql.connect("users.db")
            cur = con.cursor()
            cur.execute(f"""SELECT * FROM booking WHERE username='{username_var.get()}' """)
            rows = cur.fetchall()
            con.commit()
            con.close()
            # Bookings table shows up in old bookings
            table = ttk.Treeview(info, columns=('id', 'username', 'hotel', 'location', 'date', 'days', 'rent'),
                                 show='headings')

            for x in rows:
                table.insert('', 'end', values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6]))

            table.heading('id', text='ID')
            table.heading('username', text='Username')
            table.heading('location', text='Location')
            table.heading('hotel', text='Hotel')
            table.heading('date', text='Date')
            table.heading('days', text='Days')
            table.heading('rent', text='Rent')

            table.column('id', width=40)
            table.column('username', width=100)
            table.column('location', width=100)
            table.column('hotel', width=100)
            table.column('date', width=100)
            table.column('days', width=100)
            table.column('rent', width=100)

            table.pack(padx=20, pady=50)

        # if password or username are not the same then error
        if check is False:
            tmsg.showerror("Error", "Incorrect username or password")

        else:
            username_var.set(username.get())
            new_user_window.destroy()
            us = Toplevel()
            us.geometry("420x300")
            us.title("Us")
            us.configure(bg="Lightblue")
            Button(us, text="Book a New Room", bg="Seagreen", font="Lucida 18 bold", width=25, height=2,
                   command=newbook).place(x=20, y=40)
            Button(us, text="Old Bookings", bg="Seagreen", font="Lucida 18 bold", width=25, height=2,
                   command=oldbook).place(x=20, y=150)

    # user can log in to his account
    Label(new_user_window, text="Login to your account", font="Arial 28 bold").place(x=150, y=150)
    Label(new_user_window, text="Username:", font="Arial 14").place(x=150, y=300)
    Label(new_user_window, text="Password:", font="Arial 14").place(x=150, y=350)
    username = Entry(new_user_window, font="Arial 14")
    username.place(x=270, y=300)
    password = Entry(new_user_window, font="Arial 14")
    password.place(x=270, y=350)
    Button(new_user_window, text="LOGIN", height=3, width=10, command=submit).place(x=310, y=400)

    # If user id new he can make a new account
    Label(new_user_window, text="New here?", font="Arial 28 bold").place(x=800, y=150)
    un = StringVar()
    p = StringVar()
    fn = StringVar()
    ln = StringVar()
    cn = StringVar()
    Label(new_user_window, text="First Name:", font="Arial 14").place(x=760, y=240)
    Label(new_user_window, text="Last Name:", font="Arial 14").place(x=760, y=280)
    Label(new_user_window, text="Username:", font="Arial 14").place(x=760, y=320)
    Label(new_user_window, text="Create Password:", font="Arial 14").place(x=760, y=360)
    Label(new_user_window, text="Confirm Password:", font="Arial 14").place(x=760, y=400)
    Entry(new_user_window, textvariable=fn, font="Arial 14").place(x=930, y=240)
    Entry(new_user_window, textvariable=ln, font="Arial 14").place(x=930, y=280)
    Entry(new_user_window, textvariable=un, font="Arial 14").place(x=930, y=320)
    Entry(new_user_window, textvariable=p, font="Arial 14").place(x=930, y=360)
    Entry(new_user_window, textvariable=cn, font="Arial 14").place(x=930, y=400)
    Button(new_user_window, text="SUBMIT", height=3, width=10, command=new_user_input).place(x=1000, y=440)
    new_user_window.mainloop()


# Admin code begins here
# Admin window appears
def admin():
    root.destroy()
    admin = Tk()  # a new window made
    admin.configure(bg="LightBlue")

    def submit():  # Admin logged in

        def add():  # This function is to add another hotel in the list
            add = Tk()
            add.geometry("433x244")
            add.configure(bg="LightBlue")

            Label(add, bg="Lightblue", text="Enter hotel").place(x=100, y=30)
            new_hotel = Entry(add, textvariable=new_ho)
            new_hotel.place(x=200, y=30)

            Label(add, bg="LightBlue", text="Specify rent").place(x=100, y=90)
            new_rent = Entry(add, textvariable=new_re)
            new_rent.place(x=200, y=90)

            Button(add, bg="Seagreen", text="Submit", command=lambda: add_hotel(new_hotel.get(), new_rent.get()),
                   width=9,
                   height=2, font="Arial 10 italic").place(x=200, y=120)

        def remove():  # This function is to remove a hotel from the list
            remove = Tk()
            remove.title("Remove Hotel")
            remove.geometry("433x400")
            remove.configure(bg="Lightblue")
            con = sql.connect("users.db")
            cur = con.cursor()
            cur.execute("""SELECT hotel FROM rent """)
            hotels = cur.fetchall()
            con.commit()
            con.close()

            combo = ttk.Combobox(
                remove, values=[hotel for hotel, in hotels], textvariable=ho, height=20, font="Arial 15 italic")
            combo.set("Pick a hotel")
            combo['state'] = 'readonly'
            combo.place(x=100, y=150)
            Button(remove, bg="Seagreen", text="Submit", command=lambda: remove_hotel(combo.get()), height=2,
                   font="Arial 10 italic").place(x=180, y=250)

        def specify():  # This function is used to specify the rent of a hotel
            specify = Tk()
            specify.title("Specify Rent")
            specify.geometry("433x400")
            specify.configure(bg="Lightblue")

            con = sql.connect("users.db")
            cur = con.cursor()
            cur.execute("""SELECT hotel FROM rent""")
            hotels = cur.fetchall()
            cur.execute("""SELECT rent FROM rent""")
            rent = cur.fetchall()
            con.commit()
            con.close()

            l = Label(specify, bg="Lightblue", text="Enter hotel.", font="Arial 18 italic").place(x=160, y=40)

            box1 = ttk.Combobox(specify, values=hotels, textvariable=hotel_name, height=20, font="Arial 15 italic")
            box1.set('Select hotel')
            box1['state'] = 'readonly'
            box1.place(x=110, y=90)
            text = Label(specify, bg="Lightblue", font="Arial 10", text="Enter new rent")
            text.place(x=90, y=210)
            enter = Entry(specify, font="Arial 10", textvariable=changed_rent)
            enter.place(x=200, y=210)
            btn1 = Button(specify, bg="Seagreen", text="submit", command=lambda: change_rent(box1.get(), enter.get()))
            btn1.place(x=190, y=250)

        # if password and username are same admin logs in
        if un.get() == uname and p.get() == pword:
            admin.destroy()
            new = Tk()  # new window made

            # new window configuration
            new.geometry("1200x700")
            new.configure(bg="Lightblue")
            b1 = Button(new, bg="Seagreen", text="Add\nHotel", height=4, width=8,
                        font="Arial 16 bold", command=add)
            b1.pack(side=TOP, anchor='nw')
            b4 = Button(new, bg="Seagreen", text="Remove\nHotel", height=4,
                        width=8, font="Arial 16 bold", command=remove)
            b4.pack(side=TOP, anchor='nw')
            b5 = Button(new, bg="Seagreen", text="Specify\nRent", height=4,
                        width=8, font="Arial 16 bold", command=specify)
            b5.pack(side=TOP, anchor='nw')
            tree = ttk.Treeview(new, columns=('id', 'username', 'location', 'hotel', 'date', 'days', 'rent'),
                                show='headings')

            # The table appears
            tree.heading('id', text='ID')
            tree.heading('username', text='Username')
            tree.heading('location', text='Location')
            tree.heading('hotel', text='Hotel')
            tree.heading('date', text='Date')
            tree.heading('days', text='Days')
            tree.heading('rent', text='Rent')

            tree.column('id', width=40)
            tree.column('username', width=100)
            tree.column('location', width=100)
            tree.column('hotel', width=100)
            tree.column('date', width=100)
            tree.column('days', width=50)
            tree.column('rent', width=100)

            tree.place(x=620, y=10)

            con = sql.connect("users.db")
            cur = con.cursor()
            cur.execute("""SELECT * FROM booking""")
            data = cur.fetchall()
            for value in data:
                tree.insert('', 'end', values=(
                    value[0], value[1], value[2], value[3], value[4], value[5], value[6]))

            location = StringVar()
            name = StringVar()
            rent = IntVar()


        else:  # if password is not the same error occurs
            tmsg.showerror("Error", "Your credentials are incorrect.Try again")

    # password and username of admin
    uname = "Admin1234"
    pword = "00"

    # admin window configuration
    admin.geometry("484x455")
    admin.title("Admin interface")
    un = StringVar()
    p = StringVar()
    Label(admin, text="Username:", font="Arial 14").place(x=100, y=120)
    Label(admin, text="Password:", font="Arial 14").place(x=100, y=160)
    Entry(admin, textvariable=un, font="Arial 14").place(x=230, y=120)
    Entry(admin, textvariable=p, font="Arial 14").place(x=230, y=160)
    Button(admin, bg="SeaGreen", text="LOGIN", height=3, width=10,
           command=submit).place(x=240, y=200)


# Main window code begins here
root.title("Hotel Booking System")
root.geometry("1200x800")
bg = PhotoImage(file="E:\\Main-Hotel1.png")
Label(root, image=bg).place(x=0, y=0)
Label(root, text="Welcome to 'AMAB'", font="Arial 22 bold").pack(
    pady=20)
Label(root, text="We provide...\nAmazing hotels \n At Unbelievable prices ", font="Arial 19 roman", fg='GOLD').place(
    x=500, y=200)
b1 = Button(root, text="USER", width=10, height=2, bg='GREY',
            command=user, font="Arial 19 roman").place(x=400, y=330)
b2 = Button(root, text="ADMIN", width=10, height=2, bg='GREY',
            command=admin, font="Arial 19 roman").place(x=700, y=330)
Label(root,
      text="Contact us:\nPhone no:051-3724065\nEmail:Amab95@gmail.com\nOffice:Plaza#67,Commercial area,H-12\nIslamabad",
      fg='GREEN', font="Arial 12 roman").place(x=10, y=530)
Label(root, text="Terms of Use\tPrivacy Policy",
      font="Arial 12 underline", fg="GREEN").place(x=900, y=600)

root.mainloop()