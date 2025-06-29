from tkinter import *
from tkinter import messagebox
import random, os, tempfile, smtplib

#functionality part
def clear():
    bathsoapEntry.delete(0, END)
    facecreamEntry.delete(0, END)
    facewashEntry.delete(0, END)
    hairsprayEntry.delete(0, END)
    hairgelEntry.delete(0, END)
    bodylotionEntry.delete(0, END)

    bathsoapEntry.insert(0, 0)
    facecreamEntry.insert(0, 0)
    facewashEntry.insert(0, 0)
    hairsprayEntry.insert(0, 0)
    hairgelEntry.insert(0, 0)
    bodylotionEntry.insert(0, 0)

    riceEntry.delete(0, END)
    oilEntry.delete(0, END)
    ungaEntry.delete(0, END)
    wheatEntry.delete(0, END)
    sugarEntry.delete(0, END)
    TeaEntry.delete(0, END)

    riceEntry.insert(0, 0)
    oilEntry.insert(0, 0)
    ungaEntry.insert(0, 0)
    wheatEntry.insert(0, 0)
    sugarEntry.insert(0, 0)
    TeaEntry.insert(0, 0)

    afiaEntry.delete(0, END)
    pepsiEntry.delete(0, END)
    spriteEntry.delete(0, END)
    quencherEntry.delete(0, END)
    cocacolaEntry.delete(0, END)
    delmonteEntry.delete(0, END)

    afiaEntry.insert(0, 0)
    pepsiEntry.insert(0, 0)
    spriteEntry.insert(0, 0)
    quencherEntry.insert(0, 0)
    cocacolaEntry.insert(0, 0)
    delmonteEntry.insert(0, 0)

    cosmetictaxEntry.delete(0, END)
    grocerytaxEntry.delete(0, END)
    drinkstaxEntry.delete(0, END)

    cosmeticpriceEntry.delete(0, END)
    grocerypriceEntry.delete(0, END)
    drinkspriceEntry.delete(0, END)

    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    #billnumberEntry.delete(0, END)

    textarea.delete(1.0, END)






def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP("smtp.gmail.com", 587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = email_textarea.get(1.0, END)
            ob.sendmail(senderEntry.get(), receiverEntry.get(), message)
            ob.quit()
            messagebox.showinfo("Success", "bill is successfully sent", parent=root1)
            root1.destroy()
        except:
            messagebox.showerror("Error", "Something went wrong, please try again", parent=root1)
    if textarea.get(1.0, END) == "\n":
        messagebox.showerror("Error", "Bill is empty")
    else:
        root1 = Toplevel()
        root1.grab_set()
        root1.title("Send Email")
        root1.config(bg="gray20")
        root1.resizable(0,0)

        senderFrame = LabelFrame(root1, text="SENDER", font=("arial", 16, "bold"), bd=6, bg="gray20", fg="white")
        senderFrame.grid(row=0, column=0, padx=40, pady=20)

        senderLabel = Label(senderFrame, text="Sender's Email", font=("ariel", 14, "bold"), bg="gray20", fg="white")
        senderLabel.grid(row=0, column=0, padx=10, pady=8)

        senderEntry = Entry(senderFrame, font=("ariel", 14, "bold"), bd=2, width=23, relief=RIDGE)
        senderEntry.grid(row=0, column=1)

        passwordLabel = Label(senderFrame, text="Password", font=("ariel", 14, "bold"), bg="gray20", fg="white")
        passwordLabel.grid(row=1, column=0, padx=10, pady=8)

        passwordEntry = Entry(senderFrame, font=("ariel", 14, "bold"), bd=2, width=23, relief=RIDGE, show="*")
        passwordEntry.grid(row=1, column=1)

        recipientFrame = LabelFrame(root1, text="RECIPIENT", font=("arial", 16, "bold"), bd=6, bg="gray20", fg="white")
        recipientFrame.grid(row=1, column=0, padx=40, pady=20)

        receiverLabel = Label(recipientFrame, text="receiver's Email", font=("ariel", 14, "bold"), bg="gray20", fg="white")
        receiverLabel.grid(row=0, column=0, padx=10, pady=8)
    
        receiverEntry = Entry(recipientFrame, font=("ariel", 14, "bold"), bd=2, width=23, relief=RIDGE)
        receiverEntry.grid(row=0, column=1, padx=10, pady=8)

        messageLabel = Label(recipientFrame, text="message", font=("ariel", 14, "bold"), bg="gray20", fg="white")
        messageLabel.grid(row=1, column=0, padx=10, pady=8)

        email_textarea = Text(recipientFrame, font=("ariel", 14, "bold"), bd=2, relief=SUNKEN, width=42, height=11)
        email_textarea.grid(row=2, column=0, columnspan=2)
        email_textarea.delete(1.0, END)
        email_textarea.insert(END, textarea.get(1.0, END).replace("*", "").replace("-", "").replace("\t\t\t", "\t\t"))
        sendButton = Button(root1, text="SEND", font=("arial", 16, "bold"), width=15, command=send_gmail)
        sendButton.grid(row=2, column=0, pady=20)



    root1.mainloop()




def print_bill():
    if textarea.get(1.0, END) == "\n":
        messagebox.showerror("Error", "Bill is empty")
    else:
        file = tempfile.mktemp(".txt")
        open(file, "w").write(textarea.get(1.0, END))
        os.startfile(file, "print")



def search_bill():
    for i in os.listdir("bills/"):
        if i.split(".")[0]==billnumberEntry.get():
            f = open(f"bills/{i}", "r")
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror("Error", "Invalid Bill Number")


if not os.path.exists("bills"):
    os.mkdir("bills")

def save_bill():
    global billnumber
    result = messagebox.askyesno("Confirm", "Do you want to save the bill?")
    if result:
        bill_content = textarea.get(1.0, END)
        file = open(f"bills/ {billnumber}.txt", "w")
        file.write(bill_content)
        file.close()
        messagebox.showinfo("Success", f"bill number: {billnumber} is saved successfully")
        billnumber = random.randint(500, 1000)


billnumber=random.randint(500, 1000)
def bill_area():
    if nameEntry.get()=="" and phoneEntry.get()=="":
        messagebox.showerror("Error", "Customer Details Required")
    elif cosmeticpriceEntry.get()=="" and grocerypriceEntry.get()=="" and drinkspriceEntry.get()=="":
        messagebox.showerror("Error", "No Product Selected")
    elif cosmeticpriceEntry.get()=="0 Kes" and grocerypriceEntry.get()=="0 Kes" and drinkspriceEntry.get()=="0 Kes":
        messagebox.showerror("Error", "No products Selected")
    else:
            
        textarea.delete(1.0, END)
        textarea.insert(END, "\t\t**Welcome Customer**")
        textarea.insert(END, f"\n\n Bill Number: {billnumber}\n")
        textarea.insert(END, f"\n Customer Name: {nameEntry.get()}\n")
        textarea.insert(END, f"\n Phone Number: {phoneEntry.get()}\n")
        textarea.insert(END, "\n*******************************************************")
        textarea.insert(END, "Product\t\t\tQuantity\t\t\tPrice")
        textarea.insert(END, "\n*******************************************************")
        if bathsoapEntry.get()!="0":
            textarea.insert(END, f"\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Kes")
        if hairsprayEntry.get()!="0":
            textarea.insert(END, f"\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Kes")
        if facecreamEntry.get()!="0":
            textarea.insert(END, f"\nFace Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Kes")
        if facewashEntry.get()!="0":
            textarea.insert(END, f"\nFace Wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Kes")
        if hairgelEntry.get()!="0":
            textarea.insert(END, f"\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Kes")
        if bodylotionEntry.get()!="0":
            textarea.insert(END, f"\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Kes")

        if riceEntry.get()!="0":
            textarea.insert(END, f"\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Kes")
        if oilEntry.get()!="0":
            textarea.insert(END, f"\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Kes")
        if ungaEntry.get()!="0":
            textarea.insert(END, f"\nUnga\t\t\t{ungaEntry.get()}\t\t\t{ungaprice} Kes")
        if wheatEntry.get()!="0":
            textarea.insert(END, f"\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Kes")
        if sugarEntry.get()!="0":
            textarea.insert(END, f"\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Kes")
        if TeaEntry.get()!="0":
            textarea.insert(END, f"\nTea\t\t\t{TeaEntry.get()}\t\t\t{teaprice} Kes")

        if afiaEntry.get()!="0":
            textarea.insert(END, f"\nAfia\t\t\t{afiaEntry.get()}\t\t\t{afiaprice} Kes")
        if pepsiEntry.get()!="0":
            textarea.insert(END, f"\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Kes")
        if spriteEntry.get()!="0":
            textarea.insert(END, f"\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Kes")
        if quencherEntry.get()!="0":
            textarea.insert(END, f"\nQuencher\t\t\t{quencherEntry.get()}\t\t\t{quencherprice} Kes")
        if cocacolaEntry.get()!="0":
            textarea.insert(END, f"\nCocacola\t\t\t{cocacolaEntry.get()}\t\t\t{cocacolaprice} Kes")
        if delmonteEntry.get()!="0":
            textarea.insert(END, f"\nDelmonte\t\t\t{delmonteEntry.get()}\t\t\t{delmonteprice} Kes")
        textarea.insert(END, "\n*******************************************************")

        if cosmetictaxEntry.get()!="0.0Kes":
            textarea.insert(END, f"\ncosmetictax\t\t\t\t {cosmetictaxEntry.get()}")
        if grocerytaxEntry.get()!="0.0Kes":
            textarea.insert(END, f"\ngrocerytax\t\t\t\t {grocerytaxEntry.get()}")
        if drinkstaxEntry.get()!="0.0Kes":
            textarea.insert(END, f"\ndrinkstax\t\t\t\t {drinkstaxEntry.get()}")
        textarea.insert(END, f"\n\nTotal Bill\t\t\t\t {totalbill}")
        textarea.insert(END, "\n*******************************************************")

        save_bill()

def total():
    global soapprice, hairsprayprice, facecreamprice, facewashprice, hairgelprice, bodylotionprice
    global riceprice, oilprice, ungaprice, wheatprice, sugarprice, teaprice
    global afiaprice, pepsiprice, spriteprice, quencherprice, cocacolaprice, delmonteprice
    global totalbill

    #cosmetics price calculations
    soapprice=int(bathsoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*50
    facewashprice=int(facewashEntry.get())*100
    hairsprayprice=int(hairsprayEntry.get())*150
    hairgelprice=int(hairgelEntry.get())*80
    bodylotionprice=int(bodylotionEntry.get())*60

    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticpriceEntry.delete(0, END)
    cosmeticpriceEntry.insert(0, f"{totalcosmeticprice} Kes")
    cosmetictax=totalcosmeticprice * 0.12
    cosmetictaxEntry.delete(0, END)
    cosmetictaxEntry.insert(0, str(cosmetictax) + "Kes")

    #grocery price calculations
    riceprice = int(riceEntry.get())*30
    oilprice = int(oilEntry.get())*100
    ungaprice = int(ungaEntry.get())*120
    wheatprice = int(wheatEntry.get())*50
    sugarprice = int(sugarEntry.get())*140
    teaprice = int(TeaEntry.get())*80
    totalgroceryprice=riceprice+oilprice+ungaprice+wheatprice+sugarprice+teaprice
    grocerypriceEntry.delete(0, END)
    grocerypriceEntry.insert(0, f"{totalgroceryprice} Kes")
    grocerytax=totalgroceryprice * 0.05
    grocerytaxEntry.delete(0, END)
    grocerytaxEntry.insert(0, str(grocerytax) + "Kes")

    #drinks price calculations
    afiaprice = int(afiaEntry.get())*50
    pepsiprice = int(pepsiEntry.get())*50
    spriteprice = int(spriteEntry.get())*50
    quencherprice = int(quencherEntry.get())*50
    cocacolaprice = int(cocacolaEntry.get())*50
    delmonteprice = int(delmonteEntry.get())*50
    totaldrinksprice = afiaprice+pepsiprice+spriteprice+quencherprice+cocacolaprice+delmonteprice
    drinkspriceEntry.delete(0, END)
    drinkspriceEntry.insert(0, f"{totaldrinksprice} Kes")
    drinkstax=totaldrinksprice * 0.08
    drinkstaxEntry.delete(0, END)
    drinkstaxEntry.insert(0, str(drinkstax) + "Kes")


    totalbill = totalcosmeticprice + totalgroceryprice + totaldrinksprice + cosmetictax + grocerytax + drinkstax    

#GUI part
root = Tk()
root.title("Retail Billing System")
root.geometry("1360x800")
headingLabel=Label(root, text="Retail Billing System", font=("times new roman", 30, "bold"),
                   bg="gray20", fg="gold", bd=12, relief="groove")
headingLabel.pack(fill=X, pady=10)

customer_details_frame=LabelFrame(root, text="Customer Details", font=("times new roman", 15, "bold"),
                                  fg="gold", bd=8, relief="groove", bg="gray20")
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame, text="Name", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
nameLabel.grid(row=0, column=0, padx=20)

nameEntry=Entry(customer_details_frame, font=("arial", 15), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=8)

phoneLabel=Label(customer_details_frame, text="Phone", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
phoneLabel.grid(row=0, column=2, padx=20, pady=2)

phoneEntry=Entry(customer_details_frame, font=("arial", 15), bd=7, width=18)
phoneEntry.grid(row=0, column=3, padx=8)


billnumberLabel=Label(customer_details_frame, text="Bill Number", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
billnumberLabel.grid(row=0, column=4, padx=20, pady=2)

billnumberEntry=Entry(customer_details_frame, font=("arial", 15), bd=7, width=18)
billnumberEntry.grid(row=0, column=5, padx=8)

searchButton=Button(customer_details_frame, text="SEARCH", font=("arial", 12, "bold"), bd=7, width=10, command=search_bill)
searchButton.grid(row=0, column=6, padx=20, pady=8)


productsFrame=Frame(root)
productsFrame.pack()

cosmeticsFrame=LabelFrame(productsFrame, text="Cosmetics", font=("times new roman", 15, "bold"),
                                  fg="gold", bd=8, relief="groove", bg="gray20")
cosmeticsFrame.grid(row=0, column=0)

bathsoapLabel=Label(cosmeticsFrame, text="Bath Soap", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
bathsoapLabel.grid(row=0, column=0, pady=9, padx=10, sticky="w")

bathsoapEntry=Entry(cosmeticsFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
bathsoapEntry.grid(row=0, column=1,pady=9, padx=10)
bathsoapEntry.insert(0, 0)

facecreamLabel=Label(cosmeticsFrame, text="Face Cream", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
facecreamLabel.grid(row=1, column=0, pady=9, sticky="w")
facecreamEntry=Entry(cosmeticsFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
facecreamEntry.grid(row=1, column=1,pady=9, padx=10)
facecreamEntry.insert(0, 0)

facewashLabel=Label(cosmeticsFrame, text="Face Wash", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
facewashLabel.grid(row=2, column=0, pady=9, sticky="w")
facewashEntry=Entry(cosmeticsFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
facewashEntry.grid(row=2, column=1,pady=9, padx=10)
facewashEntry.insert(0, 0)

hairsprayLabel=Label(cosmeticsFrame, text="Hair Spray", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
hairsprayLabel.grid(row=3, column=0, pady=9, sticky="W")
hairsprayEntry=Entry(cosmeticsFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
hairsprayEntry.grid(row=3, column=1, pady=9, padx=10, sticky="W")
hairsprayEntry.insert(0, 0)

hairgelLabel=Label(cosmeticsFrame, text="Hair Gel", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
hairgelLabel.grid(row=4, column=0, pady=9, sticky="W")
hairgelEntry=Entry(cosmeticsFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
hairgelEntry.grid(row=4, column=1, pady=9, padx=10, sticky="W")
hairgelEntry.insert(0, 0)

bodylotionLabel=Label(cosmeticsFrame, text="Body Lotion", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
bodylotionLabel.grid(row=5, column=0, pady=9, sticky="W")
bodylotionEntry=Entry(cosmeticsFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
bodylotionEntry.grid(row=5, column=1, pady=9, padx=10, sticky="W")
bodylotionEntry.insert(0, 0)


groceryFrame=LabelFrame(productsFrame, text="Grocery", font=("times new roman", 15, "bold"),
                                  fg="gold", bd=8, relief="groove", bg="gray20")
groceryFrame.grid(row=0, column=1)

riceLabel=Label(groceryFrame, text="Rice", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
riceLabel.grid(row=0, column=0, pady=9, sticky="W")
riceEntry=Entry(groceryFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
riceEntry.grid(row=0, column=1, pady=9, padx=10, sticky="W")
riceEntry.insert(0, 0)

oilLabel=Label(groceryFrame, text="Oil", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
oilLabel.grid(row=1, column=0, pady=9, sticky="W")
oilEntry=Entry(groceryFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
oilEntry.grid(row=1, column=1, pady=9, padx=10)
oilEntry.insert(0, 0)


ungaLabel=Label(groceryFrame, text="Unga", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
ungaLabel.grid(row=2, column=0, pady=9, sticky="W")
ungaEntry=Entry(groceryFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
ungaEntry.grid(row=2, column=1, pady=9, padx=10)
ungaEntry.insert(0, 0)

wheatLabel=Label(groceryFrame, text="Wheat", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
wheatLabel.grid(row=3, column=0, pady=9, sticky="W")
wheatEntry=Entry(groceryFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
wheatEntry.grid(row=3, column=1, pady=9, padx=10)
wheatEntry.insert(0, 0)

sugarLabel=Label(groceryFrame, text="Sugar", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
sugarLabel.grid(row=4, column=0, pady=9, sticky="W")
sugarEntry=Entry(groceryFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
sugarEntry.grid(row=4, column=1, pady=9, padx=10)
sugarEntry.insert(0, 0)

TeaLabel=Label(groceryFrame, text="Tea", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
TeaLabel.grid(row=5, column=0, pady=9, sticky="W")
TeaEntry=Entry(groceryFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
TeaEntry.grid(row=5, column=1, pady=9, padx=10)
TeaEntry.insert(0, 0)


drinksFrame=LabelFrame(productsFrame, text="Cold Drinks", font=("times new roman", 15, "bold"),
                                  fg="gold", bd=8, relief="groove", bg="gray20")
drinksFrame.grid(row=0, column=2)

afiaLabel=Label(drinksFrame, text="Afia", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
afiaLabel.grid(row=0, column=0, pady=9, sticky="W")
afiaEntry=Entry(drinksFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
afiaEntry.grid(row=0, column=1, pady=9, padx=10)
afiaEntry.insert(0, 0)

pepsiLabel=Label(drinksFrame, text="Pepsi", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
pepsiLabel.grid(row=1, column=0, pady=9, sticky="W")
pepsiEntry=Entry(drinksFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
pepsiEntry.grid(row=1, column=1, pady=9, padx=10)
pepsiEntry.insert(0, 0)

spriteLabel=Label(drinksFrame, text="Sprite", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
spriteLabel.grid(row=2, column=0, pady=9, sticky="W")
spriteEntry=Entry(drinksFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
spriteEntry.grid(row=2, column=1, pady=9, padx=10)
spriteEntry.insert(0, 0)

quencherLabel=Label(drinksFrame, text="Quencher", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
quencherLabel.grid(row=3, column=0, pady=9, sticky="W")
quencherEntry=Entry(drinksFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
quencherEntry.grid(row=3, column=1, pady=9, padx=10)
quencherEntry.insert(0, 0)

cocacolaLabel=Label(drinksFrame, text="Cocacola", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
cocacolaLabel.grid(row=4, column=0, pady=9, sticky="W")
cocacolaEntry=Entry(drinksFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
cocacolaEntry.grid(row=4, column=1, pady=9, padx=10)
cocacolaEntry.insert(0, 0)

delmonteLabel=Label(drinksFrame, text="Delmonte", font=("times new roman", 15, "bold"), bg="gray20",
                fg="white")
delmonteLabel.grid(row=5, column=0, pady=9, sticky="W")
delmonteEntry=Entry(drinksFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
delmonteEntry.grid(row=5, column=1, pady=9, padx=10)
delmonteEntry.insert(0, 0)

billframe=Frame(productsFrame, bd=5, relief=GROOVE)
billframe.grid(row=0, column=3, padx=10)

billareaLabel=Label(billframe, text="Bill Area", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textarea=Text(billframe, height=18, width=55, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root, text="Bill Menu", font=("times new roman", 14, "bold"),
                                  fg="gold", bd=8, relief="groove", bg="gray20")
billmenuFrame.pack()

cosmeticpriceLabel=Label(billmenuFrame, text="Cosmetic Price", font=("times new roman", 14, "bold"), bg="gray20",
                fg="white")
cosmeticpriceLabel.grid(row=0, column=0, pady=6, sticky="W")

cosmeticpriceEntry=Entry(billmenuFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
cosmeticpriceEntry.grid(row=0, column=1, pady=6, padx=10)

grocerypriceLabel=Label(billmenuFrame, text="Grocery Price", font=("times new roman", 14, "bold"), bg="gray20",
                fg="white")
grocerypriceLabel.grid(row=1, column=0, pady=6, sticky="W")

grocerypriceEntry=Entry(billmenuFrame, font=("times new roman", 14, "bold"), width=10, bd=5)
grocerypriceEntry.grid(row=1, column=1, pady=6, padx=10)

drinkspriceLabel=Label(billmenuFrame, text="Drinks Price", font=("times new roman", 14, "bold"), bg="gray20",
                fg="white")
drinkspriceLabel.grid(row=2, column=0, pady=6, sticky="W")

drinkspriceEntry=Entry(billmenuFrame, font=("times new roman", 14, "bold"), width=10, bd=5)
drinkspriceEntry.grid(row=2, column=1, pady=6, padx=10)


cosmetictaxLabel=Label(billmenuFrame, text="Cosmetic Tax", font=("times new roman", 14, "bold"), bg="gray20",
                fg="white")
cosmetictaxLabel.grid(row=0, column=2, pady=6, sticky="W")

cosmetictaxEntry=Entry(billmenuFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
cosmetictaxEntry.grid(row=0, column=3, pady=6, padx=10)

grocerytaxLabel=Label(billmenuFrame, text="Grocery Tax", font=("times new roman", 14, "bold"), bg="gray20",
                fg="white")
grocerytaxLabel.grid(row=1, column=2, pady=6, sticky="W")

grocerytaxEntry=Entry(billmenuFrame, font=("times new roman", 14, "bold"), width=10, bd=5)
grocerytaxEntry.grid(row=1, column=3, pady=6, padx=10)

drinkspriceLabel=Label(billmenuFrame, text="Drinks Price", font=("times new roman", 14, "bold"), bg="gray20",
                fg="white")
drinkspriceLabel.grid(row=2, column=0, pady=6, sticky="W")

drinkspriceEntry=Entry(billmenuFrame, font=("times new roman", 14, "bold"), width=10, bd=5)
drinkspriceEntry.grid(row=2, column=1, pady=6, padx=10)

cosmeticpriceLabel=Label(billmenuFrame, text="Cosmetic Price", font=("times new roman", 14, "bold"), bg="gray20",
                fg="white")
cosmeticpriceLabel.grid(row=0, column=0, pady=6, sticky="W")

cosmeticpriceEntry=Entry(billmenuFrame, font=("times new roman", 15, "bold"), width=10, bd=5)
cosmeticpriceEntry.grid(row=0, column=1, pady=6, padx=10)

grocerypriceLabel=Label(billmenuFrame, text="Grocery Price", font=("times new roman", 14, "bold"), bg="gray20",
                fg="white")
grocerypriceLabel.grid(row=1, column=0, pady=6, sticky="W")

grocerypriceEntry=Entry(billmenuFrame, font=("times new roman", 14, "bold"), width=10, bd=5)
grocerypriceEntry.grid(row=1, column=1, pady=6, padx=10)

drinkstaxLabel=Label(billmenuFrame, text="Drinks Tax", font=("times new roman", 14, "bold"), bg="gray20",
                fg="white")
drinkstaxLabel.grid(row=2, column=2, pady=6, sticky="W")

drinkstaxEntry=Entry(billmenuFrame, font=("times new roman", 14, "bold"), width=10, bd=5)
drinkstaxEntry.grid(row=2, column=3, pady=6, padx=10)

buttonFrame=Frame(billmenuFrame, bd=8, relief=GROOVE)
buttonFrame.grid(row=0, column=4, rowspan=3)

totalButton=Button(buttonFrame, text="Total", font=("arial", 16, 'bold'), bg="gray20", fg="white",
                   bd=5, width=8, pady=10, command=total)
totalButton.grid(row=0, column=0, pady=20, padx=5)

billButton=Button(buttonFrame, text="Bill", font=("arial", 16, 'bold'), bg="gray20", fg="white",
                   bd=5, width=8, pady=10, command=bill_area)
billButton.grid(row=0, column=1, pady=20, padx=5)

emailButton=Button(buttonFrame, text="Email", font=("arial", 16, 'bold'), bg="gray20", fg="white",
                   bd=5, width=8, pady=10, command=send_email)
emailButton.grid(row=0, column=2, pady=20, padx=5)

printButton=Button(buttonFrame, text="Print", font=("arial", 16, 'bold'), bg="gray20", fg="white",
                   bd=5, width=8, pady=10, command=print_bill)
printButton.grid(row=0, column=3, pady=20, padx=5)

clearButton=Button(buttonFrame, text="Clear", font=("arial", 16, 'bold'), bg="gray20", fg="white",
                   bd=5, width=8, pady=10, command=clear)
clearButton.grid(row=0, column=4, pady=20, padx=5)
root = mainloop()