from typing import List

def maxNumberOfAlloys(n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
    """
    You are the owner of a company that creates alloys using various types of metals. There are n different types of metals available, and you have access to k machines that can be used to create alloys. Each machine requires a specific amount of each metal type to create an alloy.
    
    For the ith machine to create an alloy, it needs composition[i][j] units of metal of type j. Initially, you have stock[i] units of metal type i, and purchasing one unit of metal type i costs cost[i] coins.
    
    Given integers n, k, budget, a 1-indexed 2D array composition, and 1-indexed arrays stock and cost, your goal is to maximize the number of alloys the company can create while staying within the budget of budget coins.
    
    All alloys must be created with the same machine.
    
    Return the maximum number of alloys that the company can create.
    
    Example 1:
    
    Input: n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,0], cost = [1,2,3]
    Output: 2
    Explanation: It is optimal to use the 1st machine to create alloys.
    To create 2 alloys we need to buy the:
    - 2 units of metal of the 1st type.
    - 2 units of metal of the 2nd type.
    - 2 units of metal of the 3rd type.
    In total, we need 2 * 1 + 2 * 2 + 2 * 3 = 12 coins, which is smaller than or equal to budget = 15.
    Notice that we have 0 units of metal of each type and we have to buy all the required units of metal.
    It can be proven that we can create at most 2 alloys.
    
    Example 2:
    
    Input: n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,100], cost = [1,2,3]
    Output: 5
    Explanation: It is optimal to use the 2nd machine to create alloys.
    To create 5 alloys we need to buy:
    - 5 units of metal of the 1st type.
    - 5 units of metal of the 2nd type.
    - 0 units of metal of the 3rd type.
    In total, we need 5 * 1 + 5 * 2 + 0 * 3 = 15 coins, which is smaller than or equal to budget = 15.
    It can be proven that we can create at most 5 alloys.
    
    Example 3:
    
    Input: n = 2, k = 3, budget = 10, composition = [[2,1],[1,2],[1,1]], stock = [1,1], cost = [5,5]
    Output: 2
    Explanation: It is optimal to use the 3rd machine to create alloys.
    To create 2 alloys we need to buy the:
    - 1 unit of metal of the 1st type.
    - 1 unit of metal of the 2nd type.
    In total, we need 1 * 5 + 1 * 5 = 10 coins, which is smaller than or equal to budget = 10.
    It can be proven that we can create at most 2 alloys.
    
    
    Constraints:
    
     * 1 <= n, k <= 100
     * 0 <= budget <= 108
     * composition.length == k
     * composition[i].length == n
     * 1 <= composition[i][j] <= 100
     * stock.length == cost.length == n
     * 0 <= stock[i] <= 108
     * 1 <= cost[i] <= 100
    """
    ### Canonical solution below ###
    pass

### Unit tests below ###
def check(candidate):
    assert candidate(3, 2, 15, [[1, 1, 1], [1, 1, 10]], [0, 0, 0], [1, 2, 3]) == 2
    assert candidate(3, 2, 15, [[1, 1, 1], [1, 1, 10]], [0, 0, 100], [1, 2, 3]) == 5
    assert candidate(2, 3, 10, [[2, 1], [1, 2], [1, 1]], [1, 1], [5, 5]) == 2
    assert candidate(4, 4, 17, [[10, 10, 1, 5], [9, 7, 7, 1], [6, 3, 5, 9], [2, 10, 2, 7]], [9, 8, 2, 7], [9, 2, 6, 10]) == 1
    assert candidate(4, 9, 55, [[8, 3, 4, 2], [3, 9, 5, 5], [1, 7, 9, 8], [7, 6, 5, 1], [4, 6, 9, 4], [6, 8, 7, 1], [5, 10, 3, 4], [10, 1, 2, 4], [10, 3, 7, 2]], [9, 1, 10, 0], [3, 4, 9, 9]) == 1
    assert candidate(10, 10, 142, [[5, 3, 7, 3, 5, 5, 1, 6, 4, 3], [4, 8, 10, 8, 8, 3, 10, 6, 3, 8], [10, 2, 5, 10, 9, 2, 8, 5, 10, 7], [10, 8, 8, 8, 10, 8, 9, 6, 1, 8], [6, 2, 2, 3, 6, 3, 1, 10, 5, 8], [10, 7, 3, 10, 7, 6, 6, 10, 4, 5], [10, 2, 8, 10, 1, 8, 7, 6, 6, 7], [4, 1, 9, 6, 8, 8, 7, 1, 1, 4], [10, 9, 1, 2, 6, 4, 6, 8, 9, 4], [5, 6, 7, 2, 7, 10, 7, 8, 3, 5]], [0, 6, 3, 0, 0, 8, 1, 2, 8, 6], [2, 2, 2, 7, 4, 2, 10, 8, 9, 8]) == 1
    assert candidate(9, 3, 90, [[10, 9, 1, 3, 3, 5, 5, 10, 7], [2, 6, 4, 9, 9, 1, 9, 6, 7], [1, 4, 7, 6, 7, 7, 10, 6, 6]], [3, 10, 10, 8, 10, 5, 7, 1, 2], [9, 8, 10, 9, 9, 3, 9, 5, 8]) == 1
    assert candidate(8, 4, 196, [[5, 2, 3, 4, 7, 3, 3, 1], [1, 5, 9, 9, 6, 1, 9, 7], [5, 8, 3, 10, 2, 4, 8, 7], [9, 9, 5, 9, 6, 8, 4, 3]], [3, 5, 3, 6, 1, 5, 8, 1], [4, 5, 4, 9, 4, 8, 7, 5]) == 2
    assert candidate(2, 5, 48, [[6, 3], [9, 5], [1, 9], [1, 8], [3, 3]], [4, 8], [10, 1]) == 5
    assert candidate(3, 8, 50, [[10, 8, 5], [9, 8, 8], [2, 3, 1], [6, 2, 7], [5, 5, 3], [3, 5, 6], [8, 2, 9], [10, 2, 1]], [3, 9, 5], [1, 10, 6]) == 4
    assert candidate(6, 1, 195, [[4, 7, 7, 9, 6, 9]], [7, 4, 1, 4, 4, 0], [6, 6, 9, 10, 7, 9]) == 0
    assert candidate(10, 4, 149, [[9, 10, 1, 7, 6, 4, 9, 5, 7, 8], [9, 7, 2, 10, 7, 9, 10, 10, 1, 8], [1, 10, 9, 3, 5, 6, 6, 1, 8, 4], [9, 6, 2, 3, 9, 10, 6, 8, 7, 3]], [5, 0, 7, 5, 7, 8, 2, 2, 6, 10], [7, 5, 3, 3, 10, 9, 9, 3, 6, 8]) == 1
    assert candidate(5, 3, 110, [[5, 8, 9, 3, 10], [10, 10, 2, 1, 9], [7, 8, 2, 3, 4]], [7, 3, 4, 8, 4], [2, 2, 6, 5, 7]) == 2
    assert candidate(2, 3, 12, [[5, 9], [7, 8], [1, 1]], [0, 9], [8, 5]) == 1
    assert candidate(9, 5, 172, [[8, 8, 7, 6, 5, 3, 6, 10, 8], [9, 5, 4, 5, 9, 9, 2, 8, 5], [1, 9, 7, 8, 4, 10, 5, 1, 2], [10, 10, 4, 4, 5, 5, 5, 5, 9], [7, 10, 4, 7, 9, 6, 3, 1, 8]], [5, 0, 10, 0, 0, 8, 10, 9, 8], [3, 7, 6, 10, 10, 5, 2, 10, 6]) == 0
    assert candidate(7, 10, 31, [[10, 6, 2, 1, 6, 3, 9], [9, 7, 1, 4, 3, 3, 6], [4, 8, 3, 10, 7, 2, 10], [8, 1, 3, 3, 9, 3, 6], [6, 3, 2, 4, 9, 7, 5], [4, 2, 10, 2, 9, 8, 2], [9, 3, 6, 1, 3, 8, 1], [9, 5, 6, 9, 4, 10, 3], [1, 8, 8, 2, 5, 4, 10], [1, 6, 6, 6, 10, 6, 4]], [3, 9, 10, 4, 4, 8, 9], [6, 6, 9, 2, 1, 9, 6]) == 1
    assert candidate(4, 9, 103, [[5, 9, 6, 3], [1, 5, 7, 5], [5, 4, 10, 6], [2, 2, 4, 6], [1, 1, 2, 2], [10, 6, 5, 4], [9, 7, 8, 9], [3, 7, 8, 2], [8, 2, 4, 4]], [7, 7, 7, 3], [4, 7, 6, 10]) == 5
    assert candidate(10, 1, 197, [[7, 6, 6, 1, 2, 4, 8, 6, 4, 10]], [1, 3, 2, 1, 3, 4, 2, 6, 1, 1], [10, 6, 2, 1, 6, 2, 6, 5, 9, 8]) == 0
    assert candidate(10, 4, 152, [[1, 7, 1, 3, 9, 6, 8, 9, 10, 4], [8, 8, 9, 3, 10, 10, 4, 3, 2, 2], [3, 6, 4, 6, 1, 9, 4, 1, 4, 5], [2, 5, 1, 8, 3, 10, 6, 3, 8, 4]], [7, 2, 9, 6, 9, 4, 6, 6, 3, 6], [8, 2, 3, 9, 1, 10, 1, 9, 5, 4]) == 1
    assert candidate(6, 9, 72, [[1, 10, 8, 5, 4, 3], [6, 7, 3, 6, 10, 3], [10, 9, 8, 6, 2, 10], [8, 9, 10, 7, 9, 10], [2, 7, 2, 7, 6, 9], [4, 2, 8, 2, 7, 9], [2, 1, 1, 8, 8, 9], [5, 7, 1, 7, 3, 5], [4, 4, 4, 3, 10, 4]], [3, 3, 1, 6, 10, 8], [1, 8, 9, 8, 3, 3]) == 1
    assert candidate(1, 10, 177, [[6], [3], [8], [8], [7], [7], [4], [5], [10], [1]], [2], [7]) == 27
    assert candidate(2, 6, 196, [[6, 5], [7, 10], [3, 10], [5, 8], [5, 7], [5, 6]], [6, 3], [3, 4]) == 5
    assert candidate(7, 9, 148, [[5, 8, 7, 7, 5, 8, 4], [8, 6, 2, 6, 3, 3, 2], [5, 6, 9, 6, 6, 2, 5], [8, 2, 10, 5, 4, 5, 10], [2, 8, 10, 4, 9, 6, 1], [4, 1, 2, 2, 5, 5, 5], [9, 9, 1, 4, 1, 4, 4], [3, 8, 4, 4, 10, 4, 6], [8, 2, 8, 4, 5, 5, 10]], [7, 8, 7, 9, 3, 8, 2], [7, 5, 4, 5, 1, 3, 10]) == 2
    assert candidate(8, 5, 151, [[5, 9, 10, 2, 8, 10, 2, 8], [1, 5, 8, 9, 3, 4, 6, 6], [10, 10, 10, 6, 1, 7, 9, 4], [6, 7, 6, 2, 10, 8, 6, 10], [5, 2, 6, 2, 8, 1, 6, 2]], [0, 6, 2, 2, 9, 8, 0, 3], [6, 7, 4, 6, 10, 3, 5, 1]) == 1
    assert candidate(8, 3, 187, [[1, 4, 8, 6, 8, 5, 1, 4], [10, 9, 4, 3, 1, 2, 5, 9], [4, 10, 7, 8, 7, 7, 1, 9]], [2, 6, 4, 0, 2, 8, 2, 3], [9, 2, 5, 7, 6, 10, 2, 7]) == 1
    assert candidate(1, 3, 90, [[5], [3], [9]], [5], [10]) == 4
    assert candidate(10, 5, 91, [[7, 8, 3, 2, 9, 3, 4, 4, 2, 3], [3, 2, 4, 1, 4, 5, 10, 9, 10, 7], [1, 4, 3, 4, 9, 5, 2, 2, 9, 9], [6, 9, 9, 6, 2, 7, 1, 10, 5, 3], [10, 7, 8, 2, 2, 2, 9, 6, 1, 4]], [9, 5, 5, 0, 0, 8, 1, 4, 5, 3], [7, 3, 6, 4, 10, 10, 5, 4, 2, 1]) == 0
    assert candidate(8, 3, 97, [[3, 3, 7, 1, 5, 5, 8, 2], [10, 5, 1, 3, 1, 5, 1, 5], [7, 2, 2, 10, 7, 10, 6, 8]], [1, 1, 8, 3, 0, 1, 0, 6], [4, 1, 4, 5, 5, 3, 5, 4]) == 1
    assert candidate(9, 3, 19, [[5, 9, 4, 6, 6, 1, 4, 5, 3], [6, 9, 2, 3, 5, 4, 1, 4, 5], [6, 10, 5, 4, 7, 5, 3, 4, 3]], [8, 7, 6, 3, 4, 7, 7, 0, 4], [10, 8, 1, 6, 9, 7, 3, 7, 3]) == 0
    assert candidate(8, 2, 168, [[5, 7, 8, 6, 7, 4, 10, 8], [3, 7, 7, 4, 8, 9, 9, 9]], [6, 4, 5, 10, 2, 5, 3, 8], [5, 1, 10, 3, 4, 4, 7, 4]) == 1
    assert candidate(3, 3, 108, [[6, 1, 10], [5, 3, 6], [2, 8, 7]], [3, 9, 7], [4, 2, 3]) == 3
    assert candidate(10, 5, 197, [[7, 2, 9, 6, 2, 3, 8, 9, 10, 10], [2, 1, 7, 7, 3, 1, 3, 8, 1, 2], [4, 5, 1, 3, 6, 3, 2, 4, 4, 6], [8, 5, 9, 10, 8, 3, 7, 10, 1, 7], [8, 3, 2, 4, 1, 5, 3, 6, 9, 6]], [5, 2, 9, 8, 1, 3, 6, 4, 2, 3], [6, 6, 10, 4, 9, 5, 2, 6, 4, 6]) == 2
    assert candidate(8, 8, 90, [[6, 6, 9, 7, 6, 7, 7, 5], [5, 10, 4, 2, 8, 5, 6, 6], [7, 7, 1, 10, 3, 3, 2, 2], [7, 9, 8, 10, 7, 10, 8, 2], [7, 1, 2, 2, 1, 2, 3, 6], [2, 8, 10, 10, 6, 2, 6, 3], [3, 2, 2, 2, 4, 7, 4, 3], [2, 5, 3, 2, 3, 7, 6, 4]], [1, 1, 6, 10, 3, 0, 8, 6], [3, 2, 1, 3, 2, 3, 8, 7]) == 2
    assert candidate(4, 7, 87, [[8, 8, 5, 3], [7, 8, 8, 9], [1, 7, 3, 10], [4, 3, 9, 8], [4, 7, 2, 2], [5, 8, 2, 2], [6, 1, 2, 7]], [3, 7, 9, 8], [6, 3, 1, 4]) == 2
    assert candidate(2, 3, 184, [[7, 1], [6, 7], [4, 6]], [1, 6], [8, 2]) == 4
    assert candidate(4, 3, 25, [[7, 4, 5, 3], [10, 8, 1, 2], [6, 4, 3, 4]], [1, 3, 0, 5], [1, 2, 6, 4]) == 1
    assert candidate(10, 8, 33, [[3, 2, 9, 8, 3, 7, 10, 2, 6, 7], [6, 6, 5, 6, 3, 3, 4, 6, 5, 7], [6, 8, 5, 10, 8, 4, 1, 8, 4, 2], [7, 10, 7, 10, 4, 4, 10, 7, 5, 3], [2, 6, 3, 3, 8, 8, 2, 6, 4, 2], [2, 2, 2, 4, 8, 2, 7, 3, 7, 4], [10, 9, 7, 9, 9, 2, 3, 9, 2, 1], [8, 9, 10, 7, 10, 9, 7, 2, 3, 8]], [0, 2, 5, 5, 8, 2, 5, 9, 1, 1], [3, 4, 10, 5, 8, 8, 8, 9, 8, 7]) == 0
    assert candidate(7, 9, 8, [[5, 4, 8, 9, 2, 2, 2], [2, 8, 7, 6, 8, 10, 3], [6, 8, 4, 4, 5, 4, 10], [5, 3, 7, 8, 2, 2, 9], [8, 4, 3, 2, 6, 4, 3], [5, 2, 8, 5, 4, 5, 10], [9, 5, 4, 9, 6, 5, 7], [10, 1, 6, 7, 2, 7, 5], [3, 6, 9, 9, 3, 7, 6]], [3, 9, 1, 5, 1, 7, 9], [5, 7, 1, 6, 8, 3, 9]) == 0
    assert candidate(1, 3, 96, [[4], [8], [3]], [0], [6]) == 5
    assert candidate(4, 2, 113, [[6, 9, 5, 7], [4, 9, 7, 1]], [4, 1, 0, 4], [9, 2, 3, 5]) == 2
    assert candidate(6, 6, 97, [[9, 3, 10, 2, 6, 3], [9, 4, 3, 7, 1, 7], [10, 10, 9, 2, 1, 6], [4, 5, 2, 3, 3, 10], [2, 6, 8, 3, 6, 1], [4, 9, 6, 10, 3, 10]], [2, 8, 10, 8, 9, 0], [4, 5, 6, 3, 10, 1]) == 2
    assert candidate(9, 6, 18, [[5, 10, 2, 4, 3, 3, 2, 10, 3], [2, 7, 1, 7, 10, 7, 8, 8, 7], [6, 2, 10, 2, 4, 3, 4, 8, 9], [5, 7, 2, 10, 6, 10, 4, 10, 3], [1, 9, 4, 4, 9, 9, 4, 2, 6], [7, 5, 1, 4, 10, 9, 2, 2, 3]], [5, 4, 0, 1, 1, 6, 1, 8, 0], [8, 1, 6, 5, 10, 4, 10, 9, 7]) == 0
    assert candidate(2, 10, 197, [[8, 1], [7, 4], [2, 3], [10, 3], [6, 3], [9, 8], [8, 7], [3, 4], [2, 6], [4, 5]], [5, 9], [10, 2]) == 10
    assert candidate(10, 4, 115, [[4, 6, 5, 10, 9, 5, 2, 2, 10, 1], [6, 7, 2, 2, 4, 10, 3, 8, 3, 7], [1, 9, 10, 5, 4, 6, 2, 1, 8, 4], [7, 10, 9, 5, 10, 6, 9, 5, 8, 4]], [7, 8, 8, 8, 6, 10, 7, 8, 2, 3], [3, 5, 1, 8, 7, 7, 10, 4, 7, 8]) == 1
    assert candidate(6, 3, 168, [[1, 2, 10, 5, 5, 8], [1, 3, 6, 1, 3, 6], [8, 5, 6, 6, 5, 10]], [7, 0, 3, 1, 6, 8], [5, 6, 2, 5, 3, 1]) == 4
    assert candidate(4, 1, 13, [[6, 10, 1, 10]], [2, 9, 7, 3], [7, 8, 5, 5]) == 0
    assert candidate(1, 3, 144, [[4], [10], [9]], [10], [1]) == 38
    assert candidate(8, 4, 34, [[9, 1, 1, 9, 1, 10, 6, 4], [10, 8, 6, 5, 7, 5, 2, 9], [7, 4, 5, 10, 7, 2, 6, 2], [3, 8, 3, 6, 9, 9, 10, 5]], [9, 9, 6, 5, 5, 7, 5, 4], [7, 4, 2, 2, 8, 10, 10, 4]) == 0
    assert candidate(10, 3, 64, [[7, 2, 7, 4, 4, 6, 8, 3, 5, 6], [10, 10, 6, 5, 4, 7, 5, 1, 3, 2], [10, 10, 8, 4, 6, 8, 9, 1, 8, 10]], [8, 9, 7, 3, 10, 6, 6, 0, 6, 10], [7, 8, 4, 6, 9, 7, 7, 8, 2, 9]) == 1
    assert candidate(9, 5, 37, [[7, 5, 8, 5, 3, 1, 4, 10, 6], [4, 5, 5, 5, 7, 4, 2, 8, 1], [3, 8, 3, 6, 7, 9, 10, 2, 7], [5, 3, 5, 1, 10, 3, 4, 10, 6], [6, 2, 9, 3, 10, 6, 3, 9, 7]], [1, 4, 1, 7, 10, 8, 8, 3, 6], [7, 4, 2, 7, 3, 10, 9, 8, 10]) == 0
    assert candidate(3, 10, 67, [[5, 3, 10], [7, 5, 4], [3, 9, 9], [10, 2, 9], [9, 4, 8], [8, 5, 7], [5, 2, 3], [1, 7, 2], [3, 9, 1], [7, 1, 4]], [2, 9, 4], [4, 9, 1]) == 3
    assert candidate(4, 7, 113, [[6, 10, 4, 10], [7, 8, 1, 1], [1, 5, 4, 1], [4, 7, 8, 9], [7, 9, 2, 4], [5, 1, 10, 4], [3, 3, 9, 4]], [0, 5, 5, 10], [1, 10, 8, 4]) == 2
    assert candidate(10, 7, 128, [[5, 1, 1, 4, 5, 9, 2, 9, 2, 2], [6, 10, 4, 8, 3, 10, 8, 4, 5, 10], [3, 3, 8, 5, 2, 6, 4, 5, 4, 8], [5, 5, 4, 1, 3, 2, 10, 5, 3, 10], [9, 4, 2, 4, 2, 4, 7, 7, 1, 4], [9, 2, 10, 5, 1, 5, 5, 9, 5, 6], [10, 7, 9, 1, 4, 7, 6, 7, 5, 7]], [3, 8, 4, 5, 3, 5, 4, 10, 4, 9], [4, 1, 8, 4, 2, 9, 1, 2, 1, 10]) == 2
    assert candidate(1, 7, 48, [[1], [5], [9], [6], [4], [2], [4]], [6], [1]) == 54
    assert candidate(9, 4, 21, [[7, 2, 7, 7, 8, 1, 6, 7, 3], [8, 10, 4, 3, 7, 2, 3, 2, 5], [6, 9, 3, 2, 7, 6, 10, 6, 5], [10, 2, 4, 10, 7, 9, 5, 8, 6]], [9, 10, 5, 2, 10, 9, 8, 10, 10], [6, 5, 2, 8, 10, 1, 2, 7, 1]) == 1
    assert candidate(8, 8, 164, [[8, 8, 7, 7, 4, 8, 8, 3], [8, 1, 5, 9, 4, 5, 10, 8], [6, 3, 7, 5, 5, 5, 8, 7], [7, 1, 6, 2, 6, 10, 5, 6], [9, 10, 1, 10, 3, 8, 9, 9], [1, 5, 5, 4, 5, 10, 5, 9], [8, 3, 5, 3, 5, 4, 7, 1], [10, 2, 3, 6, 2, 4, 8, 6]], [10, 3, 10, 2, 1, 4, 8, 8], [2, 9, 7, 7, 4, 3, 2, 10]) == 2
    assert candidate(1, 6, 149, [[4], [8], [1], [9], [1], [9]], [6], [7]) == 27
    assert candidate(6, 7, 136, [[8, 9, 8, 5, 9, 8], [4, 2, 1, 9, 3, 8], [6, 8, 3, 1, 9, 9], [8, 1, 4, 5, 2, 7], [4, 5, 6, 3, 4, 9], [5, 9, 8, 2, 1, 10], [10, 10, 9, 9, 2, 8]], [4, 1, 2, 9, 9, 2], [8, 1, 7, 8, 1, 1]) == 2
    assert candidate(6, 1, 55, [[3, 5, 3, 8, 9, 8]], [9, 7, 0, 1, 9, 4], [3, 3, 1, 1, 1, 2]) == 1
    assert candidate(3, 1, 195, [[7, 3, 7]], [0, 10, 7], [7, 6, 10]) == 2
    assert candidate(1, 8, 69, [[8], [9], [10], [10], [4], [4], [7], [6]], [10], [9]) == 4
    assert candidate(9, 2, 176, [[8, 10, 1, 2, 6, 3, 5, 7, 7], [4, 6, 4, 8, 4, 5, 3, 6, 6]], [10, 9, 1, 3, 10, 1, 10, 5, 2], [3, 8, 8, 2, 5, 6, 5, 8, 1]) == 1
    assert candidate(8, 3, 17, [[3, 1, 4, 8, 7, 8, 5, 5], [7, 10, 6, 6, 3, 10, 10, 9], [5, 6, 7, 1, 4, 7, 5, 1]], [0, 4, 0, 4, 4, 9, 2, 1], [10, 1, 3, 9, 9, 3, 1, 10]) == 0
    assert candidate(1, 9, 109, [[8], [10], [4], [3], [9], [7], [9], [8], [7]], [10], [9]) == 7
    assert candidate(7, 6, 130, [[4, 2, 10, 2, 2, 9, 4], [9, 4, 8, 8, 4, 9, 9], [9, 10, 7, 8, 7, 1, 4], [8, 2, 5, 5, 6, 4, 7], [9, 8, 4, 3, 8, 6, 2], [1, 2, 3, 9, 4, 10, 1]], [10, 1, 7, 10, 1, 10, 5], [3, 7, 6, 5, 1, 5, 7]) == 2
    assert candidate(1, 8, 48, [[5], [6], [10], [9], [2], [8], [9], [8]], [9], [5]) == 9
    assert candidate(10, 3, 124, [[5, 8, 7, 1, 7, 7, 5, 4, 5, 2], [9, 1, 2, 8, 2, 8, 3, 5, 2, 4], [7, 4, 6, 4, 4, 2, 4, 10, 4, 8]], [9, 8, 7, 0, 9, 1, 4, 3, 1, 1], [9, 3, 5, 4, 3, 5, 2, 10, 7, 4]) == 1
    assert candidate(7, 10, 177, [[1, 8, 4, 1, 9, 7, 4], [8, 1, 3, 3, 9, 4, 5], [8, 5, 4, 2, 9, 9, 10], [2, 10, 3, 3, 3, 10, 8], [6, 3, 1, 3, 7, 1, 7], [3, 5, 7, 6, 8, 10, 10], [2, 10, 10, 2, 2, 7, 7], [3, 2, 10, 9, 4, 1, 2], [2, 7, 1, 8, 2, 7, 10], [10, 9, 2, 8, 10, 1, 4]], [0, 3, 5, 10, 0, 9, 9], [3, 5, 4, 8, 10, 1, 2]) == 1
    assert candidate(6, 3, 135, [[7, 8, 3, 4, 10, 5], [6, 5, 10, 3, 1, 1], [5, 2, 9, 9, 8, 1]], [10, 0, 5, 1, 0, 7], [3, 10, 3, 3, 3, 8]) == 1
    assert candidate(10, 1, 131, [[10, 2, 8, 4, 3, 6, 10, 8, 8, 6]], [1, 7, 10, 1, 4, 8, 4, 6, 7, 0], [1, 10, 9, 3, 9, 8, 3, 2, 9, 6]) == 1
    assert candidate(10, 7, 79, [[3, 8, 9, 10, 7, 3, 8, 4, 2, 2], [7, 9, 1, 1, 2, 1, 8, 7, 5, 7], [5, 9, 6, 2, 9, 4, 10, 1, 8, 5], [4, 3, 7, 2, 4, 7, 4, 6, 2, 10], [4, 5, 2, 5, 5, 2, 7, 7, 1, 8], [9, 2, 9, 4, 9, 4, 7, 3, 4, 4], [8, 4, 10, 8, 2, 8, 7, 5, 6, 10]], [0, 4, 5, 5, 7, 9, 9, 7, 3, 0], [10, 8, 1, 2, 7, 7, 4, 7, 6, 6]) == 0
    assert candidate(8, 7, 86, [[10, 5, 6, 8, 9, 10, 6, 5], [7, 8, 9, 9, 3, 3, 9, 4], [5, 4, 4, 4, 10, 2, 6, 3], [9, 7, 1, 10, 10, 4, 4, 6], [10, 9, 10, 3, 4, 2, 9, 4], [2, 1, 4, 8, 3, 6, 4, 1], [1, 8, 2, 2, 3, 3, 10, 8]], [0, 6, 0, 5, 6, 0, 10, 1], [7, 9, 10, 10, 5, 5, 7, 1]) == 1
    assert candidate(6, 8, 48, [[10, 2, 1, 4, 9, 1], [5, 10, 6, 3, 3, 9], [10, 10, 10, 9, 2, 9], [1, 5, 2, 2, 10, 9], [7, 9, 10, 5, 10, 3], [3, 3, 10, 5, 6, 2], [6, 6, 6, 8, 9, 9], [2, 4, 2, 7, 3, 3]], [5, 6, 5, 1, 3, 5], [4, 3, 8, 6, 1, 7]) == 1
    assert candidate(2, 8, 44, [[8, 5], [1, 6], [3, 10], [4, 6], [5, 8], [10, 5], [7, 5], [5, 1]], [8, 0], [8, 6]) == 2
    assert candidate(9, 3, 107, [[8, 1, 9, 10, 10, 5, 4, 9, 1], [8, 10, 6, 8, 10, 2, 10, 9, 4], [9, 6, 4, 7, 10, 2, 7, 4, 2]], [9, 2, 4, 1, 1, 3, 8, 9, 0], [6, 2, 8, 3, 1, 3, 5, 9, 9]) == 1
    assert candidate(3, 5, 125, [[10, 8, 9], [10, 7, 8], [7, 7, 6], [9, 2, 5], [8, 4, 6]], [8, 3, 1], [4, 10, 10]) == 1
    assert candidate(6, 10, 118, [[10, 7, 8, 10, 5, 9], [2, 4, 4, 5, 4, 2], [6, 7, 2, 6, 3, 10], [3, 8, 10, 8, 1, 6], [2, 9, 3, 8, 5, 5], [1, 6, 8, 1, 7, 7], [4, 9, 1, 8, 9, 5], [9, 4, 10, 4, 1, 4], [1, 5, 10, 2, 5, 3], [2, 1, 3, 3, 2, 9]], [9, 6, 2, 2, 6, 5], [2, 1, 7, 5, 10, 9]) == 2
    assert candidate(1, 2, 148, [[1], [8]], [4], [2]) == 78
    assert candidate(5, 5, 91, [[2, 4, 10, 5, 5], [4, 3, 8, 8, 10], [9, 6, 2, 7, 3], [7, 7, 3, 6, 6], [6, 4, 5, 3, 4]], [6, 4, 7, 3, 3], [4, 10, 9, 7, 3]) == 1
    assert candidate(8, 5, 143, [[8, 3, 3, 6, 2, 5, 8, 9], [6, 8, 3, 6, 4, 10, 10, 6], [9, 6, 10, 9, 6, 5, 1, 1], [1, 1, 10, 3, 4, 10, 2, 2], [10, 6, 4, 9, 9, 3, 9, 2]], [2, 1, 4, 5, 6, 8, 2, 8], [1, 8, 3, 9, 9, 7, 1, 8]) == 1
    assert candidate(4, 9, 172, [[9, 2, 2, 2], [4, 5, 3, 2], [4, 6, 1, 9], [5, 3, 3, 5], [2, 4, 3, 9], [7, 4, 4, 3], [1, 3, 2, 6], [7, 2, 5, 4], [4, 4, 2, 2]], [6, 7, 5, 2], [2, 8, 5, 2]) == 5
    assert candidate(5, 2, 110, [[2, 8, 10, 7, 4], [5, 3, 5, 5, 5]], [6, 8, 8, 1, 6], [8, 5, 8, 6, 7]) == 1
    assert candidate(3, 10, 21, [[9, 8, 5], [2, 9, 9], [2, 6, 8], [7, 4, 10], [10, 8, 6], [2, 6, 5], [6, 6, 8], [4, 7, 7], [8, 9, 10], [6, 1, 7]], [6, 4, 10], [7, 9, 4]) == 1
    assert candidate(5, 1, 176, [[5, 6, 2, 5, 4]], [1, 4, 3, 10, 7], [10, 9, 9, 8, 10]) == 1
    assert candidate(9, 1, 112, [[10, 4, 3, 5, 2, 10, 10, 8, 9]], [4, 4, 3, 0, 5, 0, 7, 6, 2], [7, 9, 8, 9, 2, 6, 10, 5, 5]) == 0
    assert candidate(8, 9, 41, [[10, 6, 7, 3, 6, 9, 9, 8], [5, 9, 5, 2, 4, 10, 2, 5], [4, 10, 9, 3, 5, 10, 7, 1], [8, 3, 1, 4, 2, 5, 3, 1], [1, 10, 10, 10, 7, 1, 10, 4], [6, 9, 7, 10, 8, 7, 6, 9], [4, 9, 10, 4, 10, 7, 1, 7], [3, 5, 9, 5, 2, 8, 3, 10], [8, 7, 1, 9, 3, 8, 6, 3]], [5, 4, 10, 10, 7, 8, 7, 6], [5, 1, 10, 4, 9, 9, 4, 6]) == 1
    assert candidate(2, 10, 2, [[9, 6], [10, 1], [7, 3], [5, 5], [7, 6], [10, 2], [7, 3], [7, 6], [7, 3], [2, 7]], [6, 10], [1, 4]) == 1
    assert candidate(2, 7, 168, [[8, 2], [4, 7], [8, 3], [1, 6], [3, 3], [9, 7], [8, 4]], [1, 7], [5, 3]) == 8
    assert candidate(8, 9, 195, [[2, 5, 4, 2, 2, 4, 4, 1], [5, 4, 5, 8, 9, 1, 2, 5], [1, 10, 3, 9, 6, 7, 1, 3], [4, 10, 3, 3, 6, 4, 7, 6], [4, 3, 10, 2, 7, 8, 4, 9], [4, 1, 6, 2, 8, 7, 3, 3], [10, 7, 5, 2, 1, 5, 4, 5], [7, 4, 3, 10, 4, 10, 1, 2], [9, 7, 9, 8, 9, 2, 3, 10]], [1, 1, 7, 10, 1, 6, 3, 9], [1, 4, 7, 6, 4, 5, 5, 2]) == 3
    assert candidate(7, 6, 167, [[2, 2, 3, 4, 6, 2, 4], [5, 7, 3, 7, 4, 6, 7], [5, 7, 4, 10, 5, 1, 1], [2, 3, 10, 6, 9, 5, 6], [3, 9, 7, 8, 5, 10, 2], [6, 7, 8, 8, 1, 6, 6]], [10, 10, 8, 9, 7, 8, 4], [2, 6, 1, 9, 9, 9, 8]) == 2
    assert candidate(6, 9, 73, [[1, 1, 9, 4, 1, 7], [6, 8, 7, 7, 6, 2], [2, 1, 5, 10, 2, 5], [3, 10, 7, 7, 5, 10], [6, 1, 6, 8, 4, 6], [3, 10, 10, 9, 8, 2], [10, 8, 7, 7, 4, 2], [10, 2, 3, 8, 7, 4], [7, 5, 9, 10, 4, 3]], [1, 9, 8, 6, 10, 6], [6, 3, 9, 7, 1, 4]) == 1
    assert candidate(5, 3, 128, [[4, 6, 5, 5, 1], [1, 4, 8, 8, 7], [3, 3, 5, 4, 5]], [6, 8, 8, 0, 2], [2, 4, 9, 7, 6]) == 2
    assert candidate(10, 7, 96, [[9, 3, 10, 2, 8, 6, 1, 7, 2, 4], [2, 10, 4, 5, 5, 3, 7, 5, 2, 10], [8, 7, 7, 10, 6, 6, 3, 2, 3, 8], [8, 1, 5, 4, 7, 8, 1, 9, 2, 10], [6, 7, 10, 9, 8, 8, 8, 3, 1, 2], [1, 6, 9, 1, 8, 4, 9, 4, 9, 7], [5, 6, 5, 2, 1, 8, 9, 4, 3, 6]], [4, 6, 3, 0, 7, 0, 7, 10, 8, 10], [4, 3, 6, 5, 6, 2, 7, 3, 1, 3]) == 1
    assert candidate(5, 9, 81, [[4, 4, 9, 5, 5], [7, 9, 10, 6, 8], [4, 7, 4, 2, 10], [2, 9, 6, 9, 8], [2, 5, 7, 3, 4], [4, 9, 9, 2, 5], [5, 6, 1, 2, 9], [5, 3, 8, 7, 8], [8, 6, 9, 9, 3]], [2, 9, 6, 5, 3], [3, 3, 8, 7, 6]) == 1
    assert candidate(10, 10, 102, [[9, 4, 10, 4, 9, 4, 3, 2, 2, 4], [10, 8, 3, 4, 5, 6, 4, 10, 2, 7], [4, 1, 10, 9, 4, 5, 7, 9, 6, 8], [1, 5, 9, 7, 8, 5, 10, 3, 8, 7], [6, 2, 10, 2, 8, 10, 7, 5, 10, 7], [7, 2, 2, 6, 8, 7, 9, 10, 6, 8], [9, 4, 8, 3, 10, 3, 2, 5, 6, 6], [3, 1, 3, 5, 10, 5, 8, 8, 1, 10], [6, 4, 3, 9, 3, 8, 8, 6, 3, 5], [8, 9, 1, 2, 7, 8, 1, 10, 8, 1]], [3, 6, 1, 3, 3, 7, 7, 2, 2, 2], [3, 10, 9, 7, 1, 3, 2, 9, 7, 3]) == 0
    assert candidate(6, 6, 115, [[2, 5, 8, 6, 2, 3], [7, 10, 7, 2, 10, 5], [2, 7, 10, 10, 3, 8], [3, 3, 8, 4, 3, 10], [10, 10, 4, 10, 4, 3], [8, 9, 9, 5, 7, 5]], [7, 1, 10, 7, 6, 2], [3, 8, 9, 7, 8, 4]) == 1
    assert candidate(8, 10, 19, [[7, 6, 3, 10, 2, 9, 7, 2], [5, 10, 3, 3, 10, 6, 6, 10], [10, 4, 9, 10, 10, 7, 7, 9], [10, 6, 9, 3, 4, 9, 9, 5], [7, 1, 3, 4, 8, 2, 8, 8], [9, 2, 3, 1, 1, 2, 2, 5], [2, 6, 9, 3, 7, 9, 5, 8], [3, 10, 5, 2, 8, 5, 8, 10], [8, 10, 1, 1, 2, 1, 7, 8], [10, 8, 4, 8, 5, 5, 10, 2]], [6, 0, 9, 2, 5, 0, 10, 8], [2, 4, 9, 8, 4, 10, 3, 1]) == 0
    assert candidate(7, 10, 179, [[10, 5, 2, 6, 5, 2, 7], [1, 6, 8, 2, 4, 8, 3], [8, 6, 1, 2, 7, 7, 4], [4, 1, 9, 6, 3, 8, 10], [7, 6, 3, 5, 3, 4, 2], [8, 10, 9, 3, 8, 1, 5], [5, 4, 1, 7, 7, 6, 3], [10, 9, 8, 1, 10, 4, 8], [9, 4, 6, 2, 3, 3, 9], [6, 5, 2, 3, 10, 6, 8]], [9, 0, 2, 10, 3, 7, 6], [6, 2, 7, 10, 1, 2, 7]) == 2
    assert candidate(9, 10, 123, [[4, 9, 5, 9, 9, 4, 8, 10, 10], [3, 1, 5, 8, 4, 4, 8, 6, 3], [5, 7, 2, 8, 2, 7, 3, 9, 5], [9, 4, 6, 7, 2, 3, 4, 3, 3], [3, 6, 2, 1, 3, 7, 10, 7, 3], [2, 6, 9, 7, 5, 7, 3, 10, 1], [1, 7, 10, 6, 9, 6, 6, 9, 8], [10, 8, 2, 1, 6, 8, 3, 8, 6], [6, 5, 1, 3, 5, 1, 2, 3, 1], [8, 2, 6, 1, 8, 8, 3, 2, 1]], [2, 6, 3, 4, 6, 1, 7, 2, 6], [5, 5, 9, 1, 5, 10, 4, 1, 2]) == 2
    assert candidate(6, 1, 161, [[4, 6, 9, 8, 5, 5]], [7, 4, 5, 1, 9, 4], [6, 5, 5, 6, 3, 1]) == 1


def test_check():
    check(maxNumberOfAlloys)


### Metadata below ###
# question_id = 3095
# question_title = Maximum Number of Alloys
# question_title_slug = maximum-number-of-alloys
# question_difficulty = Medium
# question_category = Algorithms
# question_likes = 227
# question_dislikes = 36