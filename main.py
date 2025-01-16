import json
import os

# Load or initialize data from data.json
def load_data():
    if os.path.exists('data.json'):
        with open('data.json', 'r') as f:
            return json.load(f)
    else:
        return {'income': [], 'expenses': [], 'budgets': {}, 'savings_goals': {}}

# Save the data back to data.json
def save_data(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

# Function to add income
def add_income(data):
    amount = float(input("Enter the income amount: $"))
    source = input("Enter the income source: ")
    data['income'].append({'amount': amount, 'source': source})
    save_data(data)
    print(f"Added income: ${amount} from {source}")

# Function to add an expense
def add_expense(data):
    amount = float(input("Enter the expense amount: $"))
    category = input("Enter the expense category (e.g., groceries, rent, utilities): ")
    data['expenses'].append({'amount': amount, 'category': category})
    save_data(data)
    print(f"Added expense: ${amount} for {category}")

# Function to set a budget for a category
def set_budget(data):
    category = input("Enter the budget category (e.g., groceries, entertainment): ")
    amount = float(input(f"Enter the budget amount for {category}: $"))
    data['budgets'][category] = amount
    save_data(data)
    print(f"Set budget of ${amount} for {category}")

# Function to set a savings goal
def set_savings_goal(data):
    goal_name = input("Enter the savings goal (e.g., vacation, emergency fund): ")
    target_amount = float(input(f"Enter the target amount for {goal_name}: $"))
    data['savings_goals'][goal_name] = {'target': target_amount, 'current': 0}
    save_data(data)
    print(f"Set savings goal for {goal_name}: ${target_amount}")

# Function to add to savings goal
def add_to_savings_goal(data):
    goal_name = input("Enter the savings goal name: ")
    if goal_name not in data['savings_goals']:
        print(f"No goal found with the name {goal_name}.")
        return
    amount = float(input(f"Enter the amount to add to {goal_name}: $"))
    data['savings_goals'][goal_name]['current'] += amount
    save_data(data)
    print(f"Added ${amount} to savings goal {goal_name}. Current: ${data['savings_goals'][goal_name]['current']}")

# Function to view financial summary
def view_summary(data):
    print("\n---- Financial Summary ----")
    
    # Total income
    total_income = sum(item['amount'] for item in data['income'])
    print(f"Total Income: ${total_income}")
    
    # Total expenses
    total_expenses = sum(item['amount'] for item in data['expenses'])
    print(f"Total Expenses: ${total_expenses}")
    
    # Savings progress
    print("\n--- Savings Goals ---")
    for goal, info in data['savings_goals'].items():
        print(f"{goal}: ${info['current']}/{info['target']}")
    
    # Budget Status
    print("\n--- Budgets ---")
    for category, budget in data['budgets'].items():
        expenses_for_category = sum(item['amount'] for item in data['expenses'] if item['category'] == category)
        remaining_budget = budget - expenses_for_category
        print(f"{category}: Budgeted: ${budget}, Spent: ${expenses_for_category}, Remaining: ${remaining_budget}")
    print("-----------------------\n")

# Main program loop
def main():
    data = load_data()
    
    while True:
        print("---- Personal Budget Manager ----")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Set Budget")
        print("4. Set Savings Goal")
        print("5. Add to Savings Goal")
        print("6. View Summary")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")
        
        if choice == '1':
            add_income(data)
        elif choice == '2':
            add_expense(data)
        elif choice == '3':
            set_budget(data)
        elif choice == '4':
            set_savings_goal(data)
        elif choice == '5':
            add_to_savings_goal(data)
        elif choice == '6':
            view_summary(data)
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
