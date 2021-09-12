#The first program after completion of the course

def Can_CakeBaking(amount_paid):

    """
    the prices Items is:
    *-one eeg: 2$--->we need two egg-->4$
    *-one cup flour:5$--->we need cup of flour-->5$
    *-one cup sugure:7$--->we need two cups of sugure-->14
    *-One bag of baking soda:1$--we need four bag of baking soda-->4$
    """
    #Purchase Priorities: sugure-->flour--->eggs-->baking soda.

    Rest=0  #The rest of the money

    

    #Check if you have all the money to buy all the items,if yes
    if (amount_paid>=27):

        return "Yes, cake can be baked without problems :)"+"The Rest your money "+str(Rest)

    #Check if you have all the money to buy all the items,if No
    elif (amount_paid<27):
    #Follow the purchase priorities
       
        
        #You can choose three options,
        Optiona=int(input("Enter your choose 1-if($24 to $26) or 2-if($21 to $23) or 3-if($15.5 to $18.5): "))
        #detail=input("we can Enter 'detail+number' if you Want waht you get ti")

       #If you have the money between $24 and $26 you can buy (sugar, flour, eggs, less baking soda bag)
        if (Optiona==1):

            amount_paid-=14#for sugure
            amount_paid-=5 #for flour
            amount_paid-=4 #eggs
            print("The your Rest= ",amount_paid)
            bag=int(input("Enter the amount needed (1 to 3) for baking soda bags: "))
            
            amount_paid-=bag# the amount bag baking soda
            
            Rest=amount_paid

            return "Yes,cake can be baked with less baking soda :)"+"The Rest your money= "+str(Rest)

        #If you have the money between $21 and $23 you can buy (sugar, flour, less amount eggs,without baking soda) 
        elif (Optiona==2):

            amount_paid-=14#for sugure
            amount_paid-=5 #for flour
            print("The your Rest= ",amount_paid)
            amount_eeg=int(input("Enter the amount needed (1 or 2) for eggs: "))
            amount_paid-=(amount_eeg*2)
            Rest=amount_paid
            
            return "Yes ,cake can be baked with less eggs and without baking soda :)"+"The Rest your money= $"+str(Rest)

        #If you have the money between $15.5 and 18.5 you can buy (sugar, less flour,without egg,without baking soda) 
        elif (Optiona==3):
            

            amount_paid-=14#for sugure
            print("The your Rest= ",amount_paid)
            amount_flour=float(input("Enter the amount of flour you need for baking (0.25 to 0.9): "))
            amount_paid-=(amount_flour*5)
            Rest=amount_paid
            
            return "Yes ,cake can be baked with less flour and without  eggs and baking soda :)"+"The Rest your money=$"+str(Rest)

    # If you have money under $15, you can only buy (sugar)     
    else:

        return "Cake cannot be baked without flour, without eggs and baking soda :)" + "the rest of your money= $" + str (Rest)
        
        #Complete_code
        #Thank you :)



        
        





















#List_items=['sugar','baking soda','flour','eggs']