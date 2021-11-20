def estimate_value(budget, exchange_rate):
    return float(budget) / float(exchange_rate)



def get_change(budget, exchanging_value):
    return float(budget) - float(exchanging_value)


def get_value(denomination, number_of_bills):
    return int(denomination) * int(number_of_bills)
    

def get_number_of_bills(budget, denomination):
    return int(float(budget) // int(denomination))


def exchangeable_value(budget, exchange_rate, spread, denomination):
    true_exchange_rate = exchange_rate + ((spread/100) * exchange_rate)
    
    foreign_budget = budget / true_exchange_rate
    
    amount_possible_to_be_turned_into_denomination_value = (foreign_budget // denomination) * denomination
    
    possible_exchangeable_value = amount_possible_to_be_turned_into_denomination_value
    
    return possible_exchangeable_value



def unexchangeable_value(budget, exchange_rate, spread, denomination):
    true_exchange_rate = exchange_rate + ((spread/100) * exchange_rate)
    
    foreign_budget = budget // true_exchange_rate
    
    amount_not_possible_to_be_turned_into_denomination_value = foreign_budget % denomination
   
    remained_unexchangeable_value = amount_not_possible_to_be_turned_into_denomination_value
    
    return remained_unexchangeable_value