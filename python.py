import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from numpy import random

global iddd

def terms1():
    print("TERMS AND CONDITIONS the use of this Application, AND, AND other related Agreement OR legal relationship WITH the Owner IN a legally binding way. Capitalized words are defined IN the relevant dedicated section of this document. The User must read this document carefully.")
    print("In particular, certain provisions may only apply to Consumers or to those Users that do not qualify as Consumers. Such limitations are always explicitly mentioned within each affected clause. In the absence of any such mention, clauses apply to all Users.")
    print("Single OR additional conditions of use OR access may apply IN specific scenarios AND IN such cases are additionally indicated within this document. By using this Application, Users confirm to meet the following requirements: There are no restrictions FOR Users IN terms of being Consumers OR Business Users;")
    print("Users are required to immediately AND unambiguously inform the Owner via the contact details indicated IN this document, IF they think their personal information, including but not limited to User accounts, access credentials or personal data, have been violated, unduly disclosed or stolen.")
    print("The disclaimers and exclusions under this agreement shall not apply to the extent prohibited by applicable law.")
    while True:
        xx = input("")
        if xx.lower() == "x":
            mainfunc()
            break

def spec1():
    db = mysql.connector.connect(user='root', password='tiger', host='localhost', database='sqltables')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM special_gift_offers")
    df = pd.DataFrame(cursor.fetchall(), columns=["Special Offers!", "Click"])
    print(df)
    
    ordspe = input("")
    while True:
        if ordspe.lower() == "x":
            mainfunc()
            break
        elif ordspe in ["1", "2", "3"]:
            tables = { "1": "christmas", "2": "NewYear", "3": "MakarS" }
            cursor.execute(f"SELECT * FROM {tables[ordspe]}")
            df = pd.DataFrame(cursor.fetchall(), columns=["S.no", "Product", "Price", "Savings!", "Click"])
            print(df)
            
            while True:
                try:
                    orddd = int(input("Click the corresponding number to select a product or 0 to go back "))
                    if orddd == 0:
                        spec1()
                        break
                    cursor.execute(f"SELECT COUNT(*) FROM {tables[ordspe]}")
                    max_items = cursor.fetchone()[0]
                    if 1 <= orddd <= max_items:
                        cursor.execute(f"INSERT INTO cart(Product_Name,Price,CLick) SELECT Product_Name,Price,Click FROM {tables[ordspe]} WHERE click = {orddd}")
                        cursor.execute(f"SELECT Product_name FROM {tables[ordspe]} WHERE sno = {orddd}")
                        product = cursor.fetchone()[0]
                        print(f"{product} has been added to cart. Click the corresponding number to select another product or 0 to go back")
                        db.commit()
                    else:
                        print("Invalid selection")
                except ValueError:
                    print("Please enter a valid number")
        else:
            ordspe = input("")

def abt1():
    db = mysql.connector.connect(user='root', password='tiger', host='localhost', database='sqltables')
    cursor = db.cursor()
    print("Rambola shopping ltd. (estb.2023) is a multinational online shopping brand")
    print("The foundation was laid by three young enterpreneurs in their class XIIth IP project")
    
    cursor.execute("SELECT review FROM review")
    reviews = [i[0] for i in cursor.fetchall()]
    
    fig, ax = plt.subplots()
    ax.plot(reviews, marker='o', color="black", linestyle="dashdot")
    ax.set_yticks([0,1,2,3,4,5,6])
    plt.xticks([])
    plt.xlabel("Reviews")
    plt.show()
    
    while input("Click X to go back ").lower() != "x":
        pass
    mainfunc()

def cart1():
    db = mysql.connector.connect(user='root', password='tiger', host='localhost', database='sqltables')
    cursor = db.cursor()
    
    cursor.execute("SELECT Product_Name, Price, Quantity, Sno FROM cart")
    df = pd.DataFrame(cursor.fetchall(), columns=["Product Name", "Price", "Quantity", "cart code"])
    print(df)
    
    if not df.empty:
        subtotal = sum(df["Price"] * df["Quantity"])
        print(f"subtotal= {subtotal}")
    
    print("Press M to edit the cart\nPress Q to clear the cart\nPress P to proceed to checkout\nPress X to go back")
    aw = input().lower()
    
    if aw == "x":
        mainfunc()
    elif aw == "m":
        try:
            editsno = int(input("Enter the cart code of product you would want to edit "))
            editsco = int(input("Enter the required quantity or click 0 to remove "))
            
            if editsco == 0:
                cursor.execute(f"DELETE FROM cart WHERE sno = {editsno}")
                print("The product has been removed")
            elif 1 <= editsco <= 12:
                cursor.execute(f"UPDATE cart SET quantity = {editsco} WHERE sno = {editsno}")
                print("Update done successfully")
            else:
                print("We do not have the required amount of this product")
            db.commit()
            cart1()
        except ValueError:
            print("Invalid input")
            cart1()
    elif aw == "q":
        cursor.execute("DELETE FROM cart")
        db.commit()
        print("The cart has been cleared")
        mainfunc()
    elif aw == "p":
        if df.empty:
            print("Your cart is empty")
            mainfunc()
            return
            
        print("Enter delivery details")
        a1 = input("Enter address ")
        a2 = input("Enter City ")
        a3 = input("Enter pincode ")
        
        print("Enter Payment details\n1. UPI\n2. Cash on Delivery\n3. Credit/Debit Card")
        a4 = input()
        
        x = random.choice([3, 5, 7, 9])
        print(f"Your order will arrive in {x} days")
        
        try:
            msgmsg = int(input("Rate your shopping experience (out of 5)! "))
            cursor.execute(f"INSERT INTO review(review) VALUES({msgmsg})")
            cursor.execute("DELETE FROM cart")
            db.commit()
        except ValueError:
            print("Invalid rating")
        print("Hope you had a good shopping experience, Goodbye!")
    else:
        cart1()

def acc1():
    db = mysql.connector.connect(user='root', password='tiger', host='localhost', database='sqltables')
    cursor = db.cursor()
    
    cursor.execute(f"SELECT login1.uname, login1.password, infologin.accname, infologin.accnum, infologin.accage, infologin.accg FROM login1,infologin WHERE infologin.uid = {iddd} AND login1.uid=infologin.uid")
    df = pd.DataFrame(cursor.fetchall(), columns=["Username", "Password", "Name", "Phone number", "Age", "Gender"])
    print(df)
    
    print("Click A to alter the credentials or X to go back")
    while True:
        xx = input().lower()
        if xx == "x":
            mainfunc()
            break
        elif xx == "a":
            print("N: Name\nP: Phone number\nA: Age\nG: Gender\nAny other key to go back")
            xxx = input().lower()
            
            if xxx == "n":
                xname = input("Enter the new name ")
                cursor.execute(f"UPDATE infologin SET accname = '{xname}' WHERE uid = {iddd}")
            elif xxx == "p":
                xphone = input("Enter the new Mobile Number ")
                cursor.execute(f"UPDATE infologin SET accnum = '{xphone}' WHERE uid = {iddd}")
            elif xxx == "a":
                xage = input("Enter your age ")
                cursor.execute(f"UPDATE infologin SET accage = '{xage}' WHERE uid = {iddd}")
            elif xxx == "g":
                xgen = input("Enter your gender ")
                cursor.execute(f"UPDATE infologin SET accg = '{xgen}' WHERE uid = {iddd}")
            else:
                acc1()
                break
            
            db.commit()
            print("Update successful")
            acc1()
            break

def category_menu(table_name, columns):
    db = mysql.connector.connect(user='root', password='tiger', host='localhost', database='sqltables')
    cursor = db.cursor()
    
    cursor.execute(f"SELECT * FROM {table_name}")
    df = pd.DataFrame(cursor.fetchall(), columns=columns)
    print(df)
    
    while True:
        try:
            orddd = int(input("Click the corresponding number to select a product or 0 to go back "))
            if orddd == 0:
                menu1()
                break
            
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            max_items = cursor.fetchone()[0]
            
            if 1 <= orddd <= max_items:
                cursor.execute(f"INSERT INTO cart(Product_Name,Price,CLick) SELECT Product_Name,Price,CLick FROM {table_name} WHERE click = {orddd}")
                cursor.execute(f"SELECT Product_name FROM {table_name} WHERE sno = {orddd}")
                product = cursor.fetchone()[0]
                print(f"{product} has been added to cart. Click the corresponding number to select another product or 0 to go back")
                db.commit()
            else:
                print("Invalid selection")
        except ValueError:
            print("Please enter a valid number")

def Mobiles_Computers_Accessories():
    category_menu("Mobiles_Computers_Accessories", ["", "", "", ""])

def Beauty_Health():
    category_menu("Beauty_Health", ["", "", "", ""])

def Groceries():
    category_menu("Groceries", ["", "", "", ""])

def Sports_Bags_Luggage():
    category_menu("Sports_Baggage_Luggage", ["", "", "", ""])

def Kids_Toys_Games():
    category_menu("Kids_Toys_Games", ["", "", "", ""])

def Entertainment():
    category_menu("Entertainment", ["", "", "", ""])

def menu1():
    db = mysql.connector.connect(user='root', password='tiger', host='localhost', database='sqltables')
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM menu")
    df = pd.DataFrame(cursor.fetchall(), columns=["", ""])
    print(df)
    
    while True:
        choice = input().lower()
        if choice == "p":
            Mobiles_Computers_Accessories()
            break
        elif choice == "q":
            Beauty_Health()
            break
        elif choice == "r":
            Groceries()
            break
        elif choice == "s":
            Sports_Bags_Luggage()
            break
        elif choice == "t":
            Kids_Toys_Games()
            break
        elif choice == "u":
            Entertainment()
            break
        elif choice == "x":
            mainfunc()
            break

def sgn():
    db = mysql.connector.connect(user='root', password='tiger', host='localhost', database='sqltables')
    cursor = db.cursor()
    
    global urnm
    urnm = input("Enter a Username ")
    cursor.execute(f"SELECT * FROM login1 WHERE uname = '{urnm}'")
    
    if cursor.fetchone():
        print("Username is taken, try again")
        sgn()
    else:
        pwr = input("Enter a unique password ")
        cursor.execute(f"INSERT INTO login1(uname, password) VALUES('{urnm}','{pwr}')")
        db.commit()
        print("Credentials acquired, Welcome!")
        accinfo()

def accinfo():
    db = mysql.connector.connect(user='root', password='tiger', host='localhost', database='sqltables')
    cursor = db.cursor()
    
    print("Please enter the following details")
    accname = input("Enter your Full Name ")
    accnum = input("Enter your mobile number ")
    accage = int(input("Enter your Age "))
    accg = input("Enter your Gender ")
    
    cursor.execute(f"INSERT INTO infologin(accname,accnum,accage,accg) VALUES('{accname}','{accnum}',{accage},'{accg}')")
    db.commit()
    
    cursor.execute(f"SELECT uid FROM login1 WHERE uname = '{urnm}'")
    global iddd
    iddd = cursor.fetchone()[0]
    mainfunc()

def mainfunc():
    print("Press M to access the menu")
    print("Press C to check your cart")
    print("Press S to see special gift offers")
    print("Press A to view account details")
    print("Press V to know more about us")
    print("Press T to read the terms and conditions")
    print("Press X to Exit")
    
    while True:
        choice = input().lower()
        if choice == "m":
            menu1()
            break
        elif choice == "t":
            terms1()
            break
        elif choice == "c":
            cart1()
            break
        elif choice == "s":
            spec1()
            break
        elif choice == "a":
            acc1()
            break
        elif choice == "v":
            abt1()
            break
        elif choice == "x":
            try:
                msgmsg = int(input("Rate your shopping experience (out of 5)! "))
                db = mysql.connector.connect(user='root', password='tiger', host='localhost', database='sqltables')
                cursor = db.cursor()
                cursor.execute(f"INSERT INTO review(review) VALUES({msgmsg})")
                cursor.execute("DELETE FROM cart")
                db.commit()
            except ValueError:
                pass
            print("Hope you had a good shopping experience, Goodbye!")
            break

def lgn():
    db = mysql.connector.connect(user='root', password='tiger', host='localhost', database='sqltables')
    cursor = db.cursor()
    
    print("Welcome!")
    global urnm
    urnm = input("Enter your username ")
    cursor.execute(f"SELECT * FROM login1 WHERE uname = '{urnm}'")
    
    if cursor.fetchone():
        for _ in range(4):
            pwr = input("Enter your password ")
            cursor.execute(f"SELECT * FROM login1 WHERE password = '{pwr}'")
            
            if cursor.fetchone():
                cursor.execute(f"SELECT uid FROM login1 WHERE uname = '{urnm}'")
                global iddd
                iddd = cursor.fetchone()[0]
                print("Welcome to Rambola Shopping!")
                mainfunc()
                return
            else:
                print("Invalid Password, try again")
        print("Access denied")
    else:
        print('Invalid User Name')
        print("0: Try again\n9: Exit")
        if input() == "0":
            lgn()

def intr():
    print("1: Login\n2: Sign up")
    in1 = input()
    if in1 == "1":
        lgn()
    elif in1 == "2":
        sgn()

db = mysql.connector.connect(user='root', password='tiger', host='localhost', database='sqltables')
cursor = db.cursor()
cursor.execute("SELECT * FROM login1")

if not cursor.fetchall():
    print("Welcome")
    sgn()
else:
    intr()