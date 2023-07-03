from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root = Tk()
root.geometry("900x500")
#----------------Burger_image----------
burger = ImageTk.PhotoImage(Image.open ("burger1.png"))
burger_image=Label(root)
burger_image["image"]=burger
burger_image.place(relx=0.7, rely=0.5,anchor=CENTER)

#----------------Heading Rdonalds----------
label_heading=Label(root,text="Rdonalds", font=("times",40,"bold"),fg="Orange")
label_heading.place(relx=0.12, rely=0.1,anchor=CENTER)
#----------------Label_Select_Dish----------
label_select_dish=Label(root,text="Select Dish",font=("times",15))
label_select_dish.place(relx=0.06, rely=0.2,anchor=CENTER)
#----------------drop down_main dish----------
dish_list=["burger","iced_americano"]
dish_dropdown = ttk.Combobox(root ,state = "readonly",values = dish_list)
dish_dropdown.place(relx=0.25, rely=0.2, anchor= CENTER)
#----------------Label_Select_Add-Ons-----------
label_select_addons=Label(root,text="Select Add-Ons",font=("times",15))
label_select_addons.place(relx=0.08, rely=0.5,anchor=CENTER)
#----------------drop_down_toppings---------------
toppings=[]
toppings_dropdown = ttk.Combobox(root,state = "readonly",values = toppings) 
toppings_dropdown.place(relx=0.25, rely=0.5, anchor= CENTER)
#----------------Amount---------------
dish_amount=Label(root,font=("times",15,"bold"))
dish_amount.place(relx=0.2,rely=0.75,anchor=CENTER)

class parent():
    def __init__(self):
     print("this is parent class")
     
    def menu(dish):
        if dish=="burger":
            print("You can add following toppings")
            toppings=["cheese","jalapeno"]
            toppings_dropdown["values"]=toppings
            print("More cheese | Add jalapeno")
        elif dish=="iced_americano":
            toppings=["chocolate","caramel"]
            toppings_dropdown["values"]=toppings
            print("Add chocolate flavour | Add caramel flavour")
        else:   
            print("please enter valid dish")
            
    def final_amount(dish, add_ons):
        if dish=="burger" and add_ons=="cheese":
            dish_amount["text"]="You need to pay 250 USD"
            print("You need to pay 250 USD")
        elif dish=="burger" and add_ons=="jalapeno":
            dish_amount["text"]="You need to pay 350 USD"
            print("You need to pay 350 USD")
        elif dish=="iced_americano" and add_ons=="chocolate":
            dish_amount["text"]="You need to pay 250 USD"
            print("You need to pay 250 USD")
        elif dish=="iced_americano" and add_ons=="caramel":
            dish_amount["text"]="You need to pay 450 USD"
            print("You need to pay 450 USD")
            
            
class child1(parent):
    def __init__(self,dish):
        self.new_dish = dish
        
    def  get_menu(self):
        new_dish=dish_dropdown.get()
        parent.menu(new_dish)
        
class child2(parent):
    def __init__(self,dish,addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        new_dish=dish_dropdown.get()
        addons=toppings_dropdown.get()
        parent.final_amount(new_dish,addons)
        
child1_object =child1(dish_dropdown.get())
child1_object.get_menu()
child2_object = child2(toppings_dropdown.get(),dish_dropdown.get())
child2_object.get_final_amount()  

btn_addons = Button(root,text="Check Add-Ons",command=child1_object.get_menu,bg="Blue", fg="white",relief = FLAT)
btn_addons.place(relx=0.06,rely=0.3,anchor=CENTER)

btn_amount = Button(root,text="Amount",command=child2_object.get_final_amount,bg="Blue", fg="white",relief = FLAT)
btn_amount.place(relx=0.04,rely=0.6, anchor=CENTER)

root.mainloop()