'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- Feel free to add new helper functions, but DO NOT modify/delete the given functions. 

- You MUST complete the functions defined below, except the ones that are already defined. 
'''
def mapping(item):
    item_name=""
    cost=0
    if item==0:
            item_name="Tshirt"
            cost=500
    elif item==1:
            item_name="Trousers"
            cost=600
    elif item==2:
            item_name="Scarf"
            cost=250
    elif item==3:
            item_name="Smartphone"
            cost=20000
    elif item==4:
            item_name="iPad"
            cost=30000
    elif item==5:
            item_name="Laptop"
            cost=50000
    elif item==6:
            item_name="Eggs"
            cost=5
    elif item==7:
            item_name="Chocolate"
            cost=10
    elif item==8:
            item_name="Juice"
            cost=100
    elif item==9:
            item_name="Milk"
            cost=45
    return(item_name,cost)
def show_menu():
    '''
    Description: Prints the menu as shown in the PDF
    
    Parameters: No paramters
    
    Returns: No return value
    '''
    a="""
=================================================\n
                   MY BAZAAR
=================================================
Hello! Welcome to my grocery store!
Following are the products available in the shop:

-------------------------------------------------
CODE | DESCRIPTION |   CATEGORY   | COST (Rs)
-------------------------------------------------
  0  | Tshirt      | Apparels     | 500
  1  | Trousers    | Apparels     | 600
  2  | Scarf       | Apparels     | 250
  3  | Smartphone  | Electronics  | 20,000
  4  | iPad        | Electronics  | 30,000
  5  | Laptop      | Electronics  | 50,000
  6  | Eggs        | Eatables     | 5
  7  | Chocolate   | Eatables     | 10
  8  | Juice       | Eatables     | 100
  9  | Milk        | Eatables     | 45
------------------------------------------------

  """
    print(a)
    
def get_regular_input():
    '''
    Description: Takes space separated item codes (only integers allowed). 
    Include appropriate print statements to match the output with the 
    screenshot provided in the PDF.
    
    Parameters: No parameters
    
    Returns: Returns a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i. 
    '''
    print("""-------------------------------------------------
 ENTER ITEMS YOU WISH TO BUY
-------------------------------------------------""")
    s=input("Enter the item codes (space-separated): ")
    items=list(map(int,s.split()))
    #items contains the list of all the item codes ordered by the customer
    for i in items:
        if not(i>=0 and i<10) or i !=int(i):
            print("You entered an invalid code: ",i)
            break
    k=[]
    count=0;
    for i in range(10):
        for j in range(len(items)):
            if i==items[j]: #checks for item codes to be valid, that is in range(0,10) and then appends to k
                count+=1
        k.append(count)
        count=0    
    return(k)
    



def get_bulk_input():
    '''
    Description: Takes inputs (only integers allowed) from a bulk buyer. 
    For details, refer PDF. Include appropriate print statements to match 
    the output with the screenshot provided in the PDF.
    
    Parameters: No parameters
    
    Returns: Returns a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.
    '''
    k=[0,0,0,0,0,0,0,0,0,0]
    while(True):
        s=input("Enter code and quantity (leave blank to stop): ")
        if(s==""):
            break
        s=s.split()
        s=list(map(int,s))
        desc,cost=mapping(s[0])
        if (s[0] not in range(10) and (not(s[1]>=0 and int(s[1])==s[1]))):
            print("Invalid code and quantity. Try again.")
        elif not(s[0] >=0 and s[0]<=9 and (int(s[0])==s[0])):
            print("Invalid code. Try again.")
        elif not(s[1]>=0 and int(s[1])==s[1]) :
            print("Invalid quantity. Try again.")
        else:
            print("You added ",s[1],desc)
            k[s[0]]=k[s[0]] + s[1] 
    print(k)
    print("Your order has been finalized.")
    return k
    
    


def print_order_details(quantities):
    '''
    Description: Prints the details of the order in a manner similar to the
    sample given in PDF.
    
    Parameters: Takes a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.
    
    Returns: No return value
    '''
  
    print("""
-------------------------------------------------
 ORDER DETAILS
------------------------------------------------- """)
    k=1
    for i in range(10):
        if quantities[i]>=1:
            item_name,cost=mapping(i)
            print("[",k,"]",item_name,"x",quantities[i],"=","Rs",cost,"*",quantities[i],"=","Rs",cost*quantities[i])
            k+=1

    


def calculate_category_wise_cost(quantities):
    '''
    Description: Calculates the category wise cost using the quantities
    provided. Include appropriate print statements to match the output with the
    screenshot provided in the PDF.
    
    Parameters: Takes a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.
    
    Returns: A 3-tuple of integers in the following format: 
    (apparels_cost, electronics_cost, eatables_cost)
    '''
    print("""
          -------------------------------------------------
CATEGORY-WISE COST
-------------------------------------------------
""")
    apparels_cost=electronics_cost=eatables_cost=0
    for i in range(10):
        desc,cost=mapping(i)
        cost=cost*quantities[i]
        if i in range(3):
            apparels_cost=(apparels_cost + cost)
        elif i in range(3,6) :
            electronics_cost=(cost+electronics_cost)
        else:
            eatables_cost=(eatables_cost+cost)
    # quantities contain no of items of each item of code equal to its index
    print("Apparels = Rs ",apparels_cost)
    print("Electronics = Rs",electronics_cost)  
    print("Eatables = Rs",eatables_cost)
    k=(apparels_cost,electronics_cost,eatables_cost)
    return(k)
    


def get_discount(cost, discount_rate):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS. 
    This function must be used whenever you are calculating discounts.
    
    Parameters: Takes 2 parameters:
    - cost: Integer
    - discount_rate: Float: 0 <= discount_rate <= 1

    Returns: The discount on the cost provided.
    '''
    return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    '''
    Description: Calculates the discounted category-wise price, if applicable. 
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.
    
    Parameters: Takes 3 integer parameters:
    - apparels_cost:     cost for the category 'Apparels'
    - electronics_cost: cost for the category 'Electronics'
    - eatables_cost:     cost for the category 'Eatables'
    
    Returns: A 3-tuple of integers in the following format: 
    (discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost). 
    '''
    discount_rate=0.1
    discounted_apparels_cost=apparels_cost
    discounted_electronics_cost=electronics_cost
    discounted_eatables_cost=eatables_cost
    print("""
-------------------------------------------------
DISCOUNTS
-------------------------------------------------""")
    total_discount=0
    if apparels_cost>=2000:
        discounted_apparels_cost = apparels_cost-get_discount(apparels_cost, discount_rate)
        print("[APPAREL]  Rs ",apparels_cost,"- Rs",get_discount(apparels_cost, discount_rate),"="," Rs",discounted_apparels_cost)
        total_discount=total_discount+get_discount(apparels_cost, discount_rate)
    if electronics_cost>=25000:
        discounted_electronics_cost= electronics_cost-get_discount(electronics_cost,discount_rate)
        print("[ELECTRONICS]  Rs ",electronics_cost,"- Rs",get_discount(electronics_cost, discount_rate),"="," Rs",discounted_electronics_cost)
        total_discount=total_discount+get_discount(electronics_cost, discount_rate)   
    if eatables_cost>=500:
        discounted_eatables_cost=eatables_cost-get_discount(eatables_cost,discount_rate)
        print("[EATABLES]  Rs ",eatables_cost,"- Rs",get_discount(eatables_cost, discount_rate),"="," Rs",discounted_eatables_cost)
        total_discount=total_discount+get_discount(eatables_cost, discount_rate)
    k=(discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost)
    print("""
TOTAL DISCOUNT= Rs """,total_discount)
    print("TOTAL COST = Rs ",sum(k))
    
    return(k)

    


def get_tax(cost, tax):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS. 
    This function must be used whenever you are calculating discounts.
    
    Parameters: Takes 2 parameters:
    - cost: Integer
    - tax:     Float: 0 <= tax <= 1

    Returns: The tax on the cost provided.
    '''
    return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    '''
    Description: Calculates the total cost including taxes.
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.
    
    Parameters: Takes 3 integer parameters:
    - apparels_cost:     cost for the category 'Apparels'
    - electronics_cost: cost for the category 'Electronics'
    - eatables_cost:     cost for the category 'Eatables' 
    
    Returns: A 2-tuple of integers in the following format: 
    (total_cost_including_tax, total_tax)
    '''
    apparels_tax=0.1;electronics_tax=0.15;eatables_tax=0.05
    print("""
-------------------------------------------------
TAX
-------------------------------------------------
""")
    print("[APPAREL]  Rs",apparels_cost,"*",apparels_tax,"= Rs",get_tax(apparels_cost,apparels_tax))
    print("[ELECTRONICS]  Rs",electronics_cost,"*",electronics_tax,"= Rs",get_tax(electronics_cost,electronics_tax))
    print("[EATABLES]  Rs",eatables_cost,"*",eatables_tax,"= Rs",get_tax(eatables_cost,eatables_tax))
    total_tax=get_tax(apparels_cost,apparels_tax)+get_tax(electronics_cost,electronics_tax)+get_tax(eatables_cost,eatables_tax)
    total_cost_including_tax=apparels_cost+electronics_cost+eatables_cost+total_tax
    print("""
TOTAL TAX =  Rs""",total_tax)
    print("TOTAL COST = Rs",total_cost_including_tax)
    k=(total_cost_including_tax,total_tax)
    return(k)
 

def apply_coupon_code(total_cost):
    '''
    Description: Takes the coupon code from the user as input (case-sensitive). 
    For details, refer the PDF. Include appropriate print statements to match 
    the output with the screenshot provided in the PDF.
    
    Parameters: The total cost (integer) on which the coupon is to be applied.
    
    Returns: A 2-tuple of integers:
    (total_cost_after_coupon_discount, total_coupon_discount)
    '''
    print("""-------------------------------------------------
COUPON CODE
-------------------------------------------------
""")

    k=0
    while(True):
        s=input("Enter coupon code (else leave blank): ")
        if s=="CHILL50" :
            if total_cost>=50000:
                k=total_cost*0.5
                if(k>=10000):
                    k=10000
                print("[CHILL50","min(10000, Rs",total_cost,"* 0.5) = Rs",k)
                break
            else:
                print("You are not eligible for the coupon code")
        elif s=="HELLE25":
            if total_cost>=25000:
                k=total_cost*0.25
                if(k>=5000):
                    k=5000
                print("[HELLE25","min(5000, Rs",total_cost,"*0.25) = Rs",k)
                break
            else:
                print("You are not eligible for the coupon code")
        elif s=="":
            print("No coupon code applied.")
            break
        else:
            print("Invalid coupon code. Try again.")
    total_cost_after_coupon_discount=total_cost-k        
    print(""" 
TOTAL COUPON DISCOUNT = Rs """,k)
    print("TOTAL COST = Rs",total_cost_after_coupon_discount)
    coupon_details=(total_cost_after_coupon_discount,k)
    return(coupon_details)
            
       
            
           
        
        

def main():
    '''
    Description: This is the main function. All production level codes usually
    have this function. This function will call the functions you have written
    above to design the logic. You will see how splitting your code into specialised
    functions makes the code easier to read, write and debug. Include appropriate 
    print statements to match the output with the screenshots provided in the PDF.
    
    Parameters: No parameters
    
    Returns: No return value
    '''
    show_menu()  
    def entercond():
        s=input("Would you like to buy in bulk? (y or Y / n or N): ")
        if s=="y" or s=="Y" :
            quantities = get_bulk_input()
            return quantities
        elif s=="n"or s=="N":
            quantities = get_regular_input()
            return quantities
        else:
            entercond()
    quantities= entercond()
    print_order_details(quantities)
    cat_cost = calculate_category_wise_cost(quantities)
    disc_cost=calculate_discounted_prices(cat_cost[0],cat_cost[1],cat_cost[2])
    tax_info=calculate_tax(disc_cost[0],disc_cost[1],disc_cost[2])
    #tax_info contains total final cost and total tax
    coupon_details=apply_coupon_code(tax_info[0])
    print("\nThank you for visiting!")
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()