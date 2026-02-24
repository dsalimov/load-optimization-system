# cost_calculator.py

def calculate_profit(revenue, costs):
    """
    Calculate the profit from trucking loads.
    
    Parameters:
    revenue (float): Total revenue earned from the load.
    costs (float): Total costs incurred for the load.

    Returns:
    float: Profit from the load.
    """
    return revenue - costs

def calculate_profit_margin(profit, revenue):
    """
    Calculate the profit margin as a percentage.

    Parameters:
    profit (float): Profit from the load.
    revenue (float): Total revenue earned from the load.

    Returns:
    float: Profit margin percentage.
    """
    if revenue == 0:
        return 0.0
    return (profit / revenue) * 100

def estimate_costs(distance, rate_per_mile):
    """
    Estimate the total costs for a trucking load based on distance and rate per mile.

    Parameters:
    distance (float): Distance of the load in miles.
    rate_per_mile (float): Cost rate per mile.

    Returns:
    float: Estimated total costs.
    """
    return distance * rate_per_mile
