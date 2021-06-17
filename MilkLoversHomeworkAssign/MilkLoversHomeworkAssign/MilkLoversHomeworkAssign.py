#===========================================================
#
#  Title:       Milk Lovers Grocery Store.py
#  Course:      CPS 120 Section 03
#  Homework:    Three
#  Author:      Lauren Acton
#  Date:        February 16, 2021
#  Description:
#       < Calculated cost of milk purchased >
#
#===========================================================

print ("Milk Lovers Grocery Store\n")

# Declare and Initialize Variables

WholeMilk = "Whole"
TwoPercent = "2%"
SkimMilk = "Skim"

WholeMilkCost = 4.00
TwoPercentMilkCost = 3.50
SkimMilkCost = 3.00 

# Input
MilkType = input("Enter the milk type (w=whole; t=2percent; s=skim): ")
Quantity = float (input("Enter the gallons: "))


# Processing Section 

if(MilkType == "w" or MilkType == "W"):
    print(f"Milk type Purchased: {WholeMilk:>7s}")
    print(f"Gallon Purchased: {Quantity:10.0f}")
    print(f"Cost per Gallon: ${WholeMilkCost:10.2f}")
    print(f"Total:           ${(Quantity * WholeMilkCost):10.2f}")
elif(MilkType == "t" or MilkType == "T"):
    print(f"Milk type Purchased: {TwoPercent:>8s}")
    print(f"Gallon Purchased: {Quantity:10.0f}")
    print(f"Cost per Gallon: ${TwoPercentMilkCost:10.2f}")
    print(f"Total:           ${(Quantity * TwoPercentMilkCost):10.2f}")
elif(MilkType == "s" or MilkType == "S"):
    print(f"Milk type Purchased: {SkimMilk:>7s}")
    print(f"Gallon Purchased: {Quantity:10.0f}")
    print(f"Cost per Gallon: ${SkimMilkCost:10.2f}")
    print(f"Total:           ${(Quantity * SkimMilkCost):10.2f}")
else:
    print("Invalid Milk Type")


# End of Application
print("\nEnd of Milk Lovers Grocery Store")
