# This project is based on working of mall#
#Different sections and their biling system#
print ("             __   __  __  __       __      __   __  __   __       __")
print (" WELCOME TO | __ |  ||  || __ |   |__  __ | __ |  || __ | __ |   |__")
print ("            |__| |__||__||__| |__ |__     |__| |__||__| |__| |__ |__")
ta=0
def info():
    file=open ("mall_info", "w+")
    print ("Customer Details")
    name=input("Please Enter Your Name : ")
    file.write("Customer Name:   ")
    file.write(name+"\n")
    file.close()
def menu():
    print('''        Shopping Centres:)
      1.Clothing
      2.Food Stall
      3.Home Applinces
      4.Cosmetics
      5.Stationary
      6.Fun Zone
      7.Mastermind
      8.Exit''')

class clothing:
    mp=700.00
    wp=800.00
    kp=500.00
    def __init__(self):
        self.men=0
        self.women=0
        self.kid=0
    def items(self):
        print ("          'WELCOME TO CLOTHING SECTION'",'\n')
        print('''
                         ======================
                         |Men's Wear   |700.00|
                         |Women's Wear |800.00|
                         |Kid's Wear   |500.00|
                         ======================
                         ''')
    def input (self):
        
        self.men=int(input("No. of men's wear item:"))
        self.women=int(input("No. of women's item:"))
        self.kid=int(input("No. of kid's item:"))
        self.tw=self.men+self.women+self.kid
        self.ab=("MW:",self.men,"WW:",self.women,"KW:",self.kid)
    def price (self):
        self.mp=clothing.mp*self.men
        self.wp=clothing.wp*self.women
        self.kp=clothing.kp*self.kid
        
    def bill (self):
        file=open("mall_info","a+")
        self.bill=self.mp+self.wp+self.kp
        print("Clothing Bill: ",self.bill,'\n')
        print("          'Thanks For Shopping'") 
        file.write("Clothing_Bill:    ")
        file.write(str(self.bill)+"\n")
        file.close()
      
    

def menu_card ():
        print ("          'WELCOME TO FOOD STALL'",'\n')
        print (" <-->OuR mEnU cArD<-->",'\n')
        print ('''
                   -------------------------------------
                  |1. momos(10 piece)         : Rs.70.00  |
                   -------------------------------------
                  |2. chowmein(full plate)    : Rs.120.00 |
                   -------------------------------------
                  |3. pizza                   : Rs.170.00 |
                   -------------------------------------
                  |4. coke(600 mL)            : Rs.45.00  |
                   -------------------------------------
                  |5. pasta                   : Rs.90.00  |
                   -------------------------------------
                  |6. burger                  : Rs.40.00  |
                  -------------------------------------
                  |7. spring roll             : Rs.100.00 |
                   -------------------------------------
                  |8. mcpuff                  : Rs.40.00  |
                   -------------------------------------
                  |9. ice cream               : Rs.55.00  |
                   -------------------------------------
                  |10. french fries           : Rs.80.00  |
                   -------------------------------------
                   ''')
        
        l1=[1,2,3,4,5,6,7,8,9,10]
        l2=[70,120,170,45,90,40,100,40,55,80]
        l3=["Momos","Chowmein","Pizza","Coke","Pasta","Burger","Spring roll","Mcpuff","Icecream","French fries"]
        c="y"
        t=0
        while c=="y":
            c=input("Do you want to buy anything? (y/n)")
            if c=="y":
                a=int(input("Your order please:"))
                if a==l1[a-1]:
                    g=l3[a-1]
                    qty=int(input("Please mention the quantity:"))
                    s=l2[a-1]*qty
                    print (s)
                    t+=s
                    
                
            else:
                break
        print ("Food Bill: ",t,'\n')
        print ("          'Thanks For Shopping'")
        file=open("mall_info","a+")
        file.write("Food Stall Bill:  ")
        file.write(str(t)+"\n")
        file.close()
        fz=open("food_zone","w+")
        fz.write(str(g)+"\n")
        fz.write(str(qty)+"\n")
        fz.write(str(t))
        fz.close()
        
        return (t)
    
        
def home_appliances():
    print ("          'WELCOME TO HOME APPLIANCES SECTION'",'\n')
    print (" <-->aPpLiAnCeS aVaIlAbLe ArE aS fOlLoWs:<-->",'\n')
    h={'JUICER':1750,'LAPTOP':35000,'OVEN':7000,'LCD':25000,'REFRIGERATOR':20000,'WASHING MACHINE':12000,'AC':20000}
    print('''
              =============================================
              |S.NO|     ITEMS          |     PRICE        |
              =============================================
              | 1. |    Juicer          |     1800.00      |
              =============================================
              | 2. |    Laptop          |     15,00,00     |
              =============================================
              | 3. |    Oven            |     7000.00      |
              =============================================
              | 4. |    Lcd             |     25,000       |
              =============================================
              | 5. |    Refrigerator    |     20,000       |
              =============================================
              | 6. |    Washing_Machine |     12,000       |
              =============================================
              | 7. |    Air_Conditioner |     20,000       |
              =============================================
          ''')
    print("\n")

 
    c="y"
    l=0
    while c=="y":
        c=input("Do You Want To Buy Anything? (y/n)")
        if c=="y":
            a=input("What do you want to buy (mention the name of item):=")
            x=a.upper()
            p=h.get(x,"Sorry Not Available")
            qty=int(input("Please mention the quantity:"))
            s=p*qty
            print(s)
            l+=s
           
        else:
            break
    print ("Home Appliances Bill:",l,'\n')
    print ("          'Thank You  For Coming :-)'",'\n')
    file=open("mall_info","a+")
    file.write("Home Appliances Bill:  ")
    file.write(str(l)+"\n")
    file.close()
    ha=open("home_appliances","w")
    ha.write(str(a)+"\n")
    ha.write(str(qty)+"\n")
    ha.write(str(l))
    ha.close()
    return (l)

def cosmetic():
    print ("          'WELCOME TO COSMETIC SECTION'",'\n')
    print (" <--> OuR cOlLeCtIoN<-->",'\n')
    t1=('necklace','ring','bangle','anklet','earings')
    print ('''
              =============================================
              |S.NO|     ITEMS          |     PRICE        |
              =============================================
              | 1. |    Necklace        |     50,000       |
              =============================================
              | 2. |    Ring            |     20,000       |
              =============================================
              | 3. |    Bangle          |     10,000       |
              =============================================
              | 4. |    Anklet          |     15,000       |
              =============================================
              | 5. |    Earings         |     5,000        |
              =============================================''')
    
    print ("\n")
    t2=(50000,20000,10000,15000,5000)
    a="y"
    p=0
    while a=="y":
        a=input("Do You Want To Buy? (y/n)")
        if a=="y":
            x=input("What You Want To Buy:( mention the name):= ")
            qty=int(input("How Many Items:"))
            r=0
            if x in t1:
                for i in range (len(t1)):
                    if x==t1[i]:
                        r=i
                        c=t2[i]*qty
                        print (c)
                        p+=c
                
        else:
            break

    print ("Cosmetic Bill:",p,'\n')
    print ("          'Thanks For Shopping'",'\n')
    file=open("mall_info","a+")
    file.write("Cosmetic Bill:  ")
    file.write(str(p)+"\n")
    file.close()
    ck=open("cosmetics","w")
    ck.write(str(x)+"\n")
    ck.write(str(qty)+"\n")
    ck.write(str(p))
    ck.close()
    return (p)

def stationary():
    print ("WELCOME TO STATIONARY SECTION","\n")
    t1=["notebook","pencil set","pens","colors","sketches","files","sheets"]
    t2=[40,55,50,120,145,40,90]
    
    print ('''
              -------------------------------------
             | Sno.    Stationary Items      Price |
              -------------------------------------
             |   1.       notebook            40   |
              -------------------------------------
             |   2.      pencil set           55   |
              -------------------------------------
             |   3.        pens               50   |
              -------------------------------------
             |   4.       colors             120   |
              -------------------------------------
             |   5.       sketches           145   |
              -------------------------------------
             |   6.        files              40   |
              -------------------------------------
             |   7.       sheets              90   |
              -------------------------------------''')
    

    print ("\n")
    a="y"
    p=0
    while a=="y":
        a=input("Do You Want To Buy? (y/n)")
        if a=="y":
            x=input("What You Want To Buy: (mention the name of item);= ")
            qty=int(input("How Many Items:"))
            r=0
            if x in t1:
                for i in range (len(t1)):
                    if x==t1[i]:
                        r=i
                        c=t2[i]*qty
                        print (c)
                        p+=c
                
        else:
            break

    print ("Cosmetic Bill:",p,'\n')
    print ("          'Thanks For Shopping'",'\n')
    file=open("mall_info","a+")
    file.write("Cosmetic Bill:  ")
    file.write(str(p)+"\n")
    file.close()
    st=open("stationary","w")
    st.write(str(x)+"\n")
    st.write(str(qty)+"\n")
    st.write(str(p))
    st.close()
    return (p)
        
    

    
def fun_zone():
    print ("          'WELCOME TO YO-YO FUN ZONE'",'\n')
    print (" Answer The Following Questions And Get Maximun Discount",'\n')
    Q1= '''1.Which of the following cat has magical pocket ?
 a) Oggy    b) Doraemon    c) Tom    d) Kiyo'''
    Q2='''2.Which vegetable Schinchan doesn't like ?
 a) Capsicum    b)Tomato    c)Potato    d)Carrot'''
    Q3= '''3.Ash's favourite pockemon is _______ ?
 a) Onix    b) Meaww    c) Bublasaur    d) Pikachu'''
    Q4= '''4.Whom does Nobita afraid the most?
 a) Giyan    b) Sunio    c) Dekisuki    d) Shizuka'''
    Q5='''5.What is Shinchan dog's name?
 a) Tommy    b) Tuffy    c) Shero   d) Bruno'''
    D=["b","a","d","a","c"]
    l=[Q1,Q2,Q3,Q4,Q5]
    p=0
    ca=0
   
    for i in range (5):
        print (l[i])
        try:
            ans=input("Answer: ")
            if ans==D[i]:
                print ("Hurray!!Correct Answer.. :)")
                p+=5
                ca+=1
            else:
                print("Ooops! Incorrect Answer.. :(")
                p-=1
                print ("Correct Answer : ",D[i])
        except:
            print ("Invalid Answer")
    print (" No. of correct answers : ",ca,'\n',"Your total score : ",p,'\n')
    file=open("mall_info","a+")
    file.write("Discount_offered:   ")
    file.write(str(p )+'%'+"\n")
    file.close()
    return (p)
    
def mastermind():
    print ("Welcome to mastermind",'\n')
    import random
    k=random.randint(1000,9999)
    key=open("key","w+")
    key.write(str(k))
    key.close()
    l1=list(str(k))
    print('''
"Guess the key and win the prize",'\n',"You have to guess a four digit number",'\n',
"You will be provided with 10 guess"
''')
    g=1
    for j in range (10):
        n=int(input("Guess"))
        l2=list(str(n))
        if len(l2)==4:
            for i in range(4):
                if l1[i]==l2[i]:
                    print (l1[i],"exist at ",(i+1),"position")
           
            if l1==l2:
                print("You guessed the key:",k,'\n',"It took you",g,"guesses.",'\n')
                print ("CONGRATS!!! SURPRIZE FOR YOU",'\n')
                for i in range (1):
                    print ("      __      __     ")
                for i in range(2):
                    print ("     \  /    \  /    ")
                for i in range (1):
                    print (" -------------------")
                for i in range (3):
                    print ("|        | |        |")
                for i in range (1):
                    print ("|------SURPRIZE-----|")
                for i in range (3):
                    print ("|        | |        |")
                for i in range (1):
                    print (" -------------------")
                break
    
        else:
            print("The number should be a four digit integer value")
        g+=1
    else:
        print("You lose :-(")
        print ("The correct number is",k)    
    
l1=list(str(0))*3
l2=list(str(0))*3
l3=list(str(0))*3
l4=list(str(0))*3
    
info()
menu()
while True:
    c=int(input("Your Desire Shopping Centre:"))
    if c==1:
        a=clothing()
        a.items()
        a.input()
        a.price()
        a.bill()
        ta+=int(a.bill)
        do=0
    elif c==2:
        ta+=menu_card()
        do=0
        fz=open("food_zone","r")
        f=fz.read()
        l1=f.split('\n')
    elif c==3:
        ta+=home_appliances()
        do=0
        ha=open("home_appliances","r")
        h=ha.read()
        l2=h.split("\n")
    elif c==4:
        ta+=cosmetic()
        do=0
        ck=open("cosmetics","r")
        c=ck.read()
        l3=c.split("\n")
    elif c==5:
        ta+=stationary()
        do=0
        st=open("stationary","r")
        s=st.read()
        l4=s.split("\n")
    elif c==6:
        do=int (ta*(fun_zone()/100))
    elif c==7:
        mastermind()
    elif c==8:                         
        break
        print ('''
                " You choose for exit",'\n',"Google-Goggle Team thanks you for shopping",'\n',
                  "You are welcome to come again",'\n\n',"Your bill is as follows:"
               ''')
    else:
        print("Ooops!! Wrong choice :(")


file=open("mall_info","r")
data=file.read()
record=data.split('\n')

print ("=============================================================================")
print ("{0:<3}{1:<74}{2:<3}". format("|",record[0],"|"))
print ("{0:<77}{1:<3}". format("|","|"))
print ("=============================================================================")
print ("{0:<3}{1:<5}{2:<3}{3:<20}{4:<3}{5:<20}{6:<3}{7:<10}{8:<3}{9:<7}{10:<3}". format("|","Sno.","|","Shopping center","|","Items","|","Quantity","|","Price","|"))
print ("=============================================================================")
print ("{0:<3}{1:<5}{2:<3}{3:<20}{4:<3}{5:<20}{6:<3}{7:<10}{8:<3}{9:<7}{10:<3}". format ("|","1.","|","Clothing","|","Men/Women/Kids","|",str(a.tw),"|",str(a.bill),"|"))
print ("=============================================================================")
print ("{0:<3}{1:<5}{2:<3}{3:<20}{4:<3}{5:<20}{6:<3}{7:<10}{8:<3}{9:<7}{10:<3}". format("|","2.","|","Food Zone","|",str (l1[0]),"|",str (l1[1]),"|",str (l1[2]),"|"))
print ("=============================================================================")
print ("{0:<3}{1:<5}{2:<3}{3:<20}{4:<3}{5:<20}{6:<3}{7:<10}{8:<3}{9:<7}{10:<3}". format("|","3.","|","Home Appliances","|",str(l2[0]),"|",str(l2[1]),"|",str(l2[2]),"|"))
print ("=============================================================================")
print ("{0:<3}{1:<5}{2:<3}{3:<20}{4:<3}{5:<20}{6:<3}{7:<10}{8:<3}{9:<7}{10:<3}". format("|","4.","|","Cosmetics","|",str(l3[0]),"|",str(l3[1]),"|",str(l3[2]),"|"))
print ("=============================================================================")
print ("{0:<3}{1:<5}{2:<3}{3:<20}{4:<3}{5:<20}{6:<3}{7:<10}{8:<3}{9:<7}{10:<3}". format("|","5.","|","Stationary","|",str(l4[0]),"|",str(l4[1]),"|",str(l4[2]),"|"))
print ("=============================================================================")
print ("{0:<11}{1:<56}{2:<3}{3:<7}{4:<3}". format("|","Total","|",str(ta),"|"))
print ("{0:<11}{1:<56}{2:<3}{3:<7}{4:<3}". format("|","Discount","|",str(do),"|"))
print ("=============================================================================")
print ("{0:<11}{1:<56}{2:<3}{3:<7}{4:<3}". format("|","Total Bill With Discount","|",str(ta-do),"|"))
print ("=============================================================================")

        
            
            







        
            
            







    

 


    

      
