from itertools import tee
from collections import defaultdict

class Bank:
    def __init__(self, name, net_amount=0):
        self.name = name
        self.net_amount = net_amount
        self.types = set()

def get_min_index(list_of_net_amounts):
    min_index = -1
    min_amount = float('inf')
    for i, bank in enumerate(list_of_net_amounts):
        if bank.net_amount != 0 and bank.net_amount < min_amount:
            min_index = i
            min_amount = bank.net_amount
    return min_index

def get_simple_max_index(list_of_net_amounts):
    max_index = -1
    max_amount = float('-inf')
    for i, bank in enumerate(list_of_net_amounts):
        if bank.net_amount != 0 and bank.net_amount > max_amount:
            max_index = i
            max_amount = bank.net_amount
    return max_index

def get_max_index(list_of_net_amounts, min_index, input_banks, max_num_types):
    max_index = -1
    max_amount = float('-inf')
    matching_type = ""
    
    for i, bank in enumerate(list_of_net_amounts):
        if bank.net_amount == 0 or bank.net_amount < 0:
            continue
        
        intersection = list(list_of_net_amounts[min_index].types & bank.types)
        
        if len(intersection) != 0 and bank.net_amount > max_amount:
            max_index = i
            max_amount = bank.net_amount
            matching_type = intersection[0]
    
    return max_index, matching_type

def print_ans(ans_graph, num_banks, input_banks):
    print("\nThe transactions for minimum cash flow are as follows:\n")
    for i in range(num_banks):
        for j in range(num_banks):
            if i == j:
                continue

            if ans_graph[i][j][0] != 0 and ans_graph[j][i][0] != 0:
                if ans_graph[i][j][0] == ans_graph[j][i][0]:
                    ans_graph[i][j] = (0, "")
                    ans_graph[j][i] = (0, "")
                elif ans_graph[i][j][0] > ans_graph[j][i][0]:
                    ans_graph[i][j] = (ans_graph[i][j][0] - ans_graph[j][i][0], ans_graph[i][j][1])
                    ans_graph[j][i] = (0, "")
                    print(f"{input_banks[i].name} pays Rs {ans_graph[i][j][0]} to {input_banks[j].name} via {ans_graph[i][j][1]}")
                else:
                    ans_graph[j][i] = (ans_graph[j][i][0] - ans_graph[i][j][0], ans_graph[j][i][1])
                    ans_graph[i][j] = (0, "")
                    print(f"{input_banks[j].name} pays Rs {ans_graph[j][i][0]} to {input_banks[i].name} via {ans_graph[j][i][1]}")
            elif ans_graph[i][j][0] != 0:
                print(f"{input_banks[i].name} pays Rs {ans_graph[i][j][0]} to {input_banks[j].name} via {ans_graph[i][j][1]}")
            elif ans_graph[j][i][0] != 0:
                print(f"{input_banks[j].name} pays Rs {ans_graph[j][i][0]} to {input_banks[i].name} via {ans_graph[j][i][1]}")

            ans_graph[i][j] = (0, "")
            ans_graph[j][i] = (0, "")
    print("\n")

def minimize_cash_flow(num_banks, input_banks, index_of, num_transactions, graph, max_num_types):
    list_of_net_amounts = [Bank(input_banks[i].name) for i in range(num_banks)]
    
    for b in range(num_banks):
        amount = 0
        for i in range(num_banks):
            amount += graph[i][b]
        for j in range(num_banks):
            amount -= graph[b][j]
        list_of_net_amounts[b].net_amount = amount
        list_of_net_amounts[b].types = input_banks[b].types
    
    ans_graph = [[(0, "") for _ in range(num_banks)] for _ in range(num_banks)]
    
    num_zero_net_amounts = sum(1 for bank in list_of_net_amounts if bank.net_amount == 0)
    
    while num_zero_net_amounts != num_banks:
        min_index = get_min_index(list_of_net_amounts)
        max_index, matching_type = get_max_index(list_of_net_amounts, min_index, input_banks, max_num_types)
        
        if max_index == -1:
            ans_graph[min_index][0] = (abs(list_of_net_amounts[min_index].net_amount), next(iter(input_banks[min_index].types)))
            simple_max_index = get_simple_max_index(list_of_net_amounts)
            ans_graph[0][simple_max_index] = (abs(list_of_net_amounts[min_index].net_amount), next(iter(input_banks[simple_max_index].types)))
            list_of_net_amounts[simple_max_index].net_amount += list_of_net_amounts[min_index].net_amount
            list_of_net_amounts[min_index].net_amount = 0
        else:
            transaction_amount = min(abs(list_of_net_amounts[min_index].net_amount), list_of_net_amounts[max_index].net_amount)
            ans_graph[min_index][max_index] = (transaction_amount, matching_type)
            list_of_net_amounts[min_index].net_amount += transaction_amount
            list_of_net_amounts[max_index].net_amount -= transaction_amount
        
        if list_of_net_amounts[min_index].net_amount == 0:
            num_zero_net_amounts += 1
        if list_of_net_amounts[max_index].net_amount == 0:
            num_zero_net_amounts += 1
    
    print_ans(ans_graph, num_banks, input_banks)

def main():
    print("\n\t\t\t\t********************* Welcome to CASH FLOW MINIMIZER SYSTEM ***********************\n\n\n")
    print("This system minimizes the number of transactions among multiple banks in the different corners of the world that use different modes of payment. There is one world bank (with all payment modes) to act as an intermediary between banks that have no common mode of payment. \n\n")
    num_banks = int(input("Enter the number of banks participating in the transactions.\n"))
    
    input_banks = []
    index_of = {}
    
    print("Enter the details of the banks and transactions as stated:")
    print("Bank name, number of payment modes it has and the payment modes.")
    print("Bank name and payment modes should not contain spaces")
    
    max_num_types = 0
    for i in range(num_banks):
        if i == 0:
            print("World Bank: ", end="")
        else:
            print(f"Bank {i}: ", end="")
        
        bank_name = input().split()
        name = bank_name[0]
        num_types = int(bank_name[1])
        types = set(bank_name[2:])
        
        if i == 0:
            max_num_types = num_types
        
        bank = Bank(name)
        bank.types = types
        input_banks.append(bank)
        index_of[name] = i
    
    num_transactions = int(input("Enter number of transactions.\n"))
    graph = [[0] * num_banks for _ in range(num_banks)]
    
    print("Enter the details of each transaction as stated:")
    print("Debtor Bank, creditor Bank and amount")
    print("The transactions can be in any order")
    for i in range(num_transactions):
        print(f"{i}th transaction: ", end="")
        transaction = input().split()
        debtor, creditor, amount = transaction[0], transaction[1], int(transaction[2])
        graph[index_of[debtor]][index_of[creditor]] = amount
    
    minimize_cash_flow(num_banks, input_banks, index_of, num_transactions, graph, max_num_types)

if __name__ == "__main__":
    main()
