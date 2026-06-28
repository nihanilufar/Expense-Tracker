from fastapi import FastAPI

tracker = FastAPI()
expenses = []  #empty list
id_counter = 1


@tracker.post("/expenses")
def add_expense(title : str,amount : int,category: str):
    global id_counter


    expense = {
        "id" : id_counter,
        "title" : title,
        "amount" : amount,
        "category" : category

    }
    expenses.append(expense)
    id_counter = id_counter + 1

    return {"message": "expense added succesfully","expense": expense}

@tracker.get("/expenses")
def view_expenses():
    return {"expense":expenses}

@tracker.put("/expenses/{id}")
def edit_expenses(id : int, title : str, amount : int, category : str):
    for expense in expenses:
        if expense["id"] == id:
            expense["title"] = title
            expense["amount"] = amount
            expense["category"] = category
            return {"message": "expense updated", "expense" : expense}
        
    return {"not found"}
    

@tracker.delete("/expenses/{id}")
def delete_expenses(id : int, title : str, amount : int, category : str):
    for expense in expenses:
        if expense["id"] == id:
            expenses.remove(expense)
            return {"message":"expense deleted", "expense" : expense}
            
            


    return {"expense not found"}




   
    




