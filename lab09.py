# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    #  give me the indexes that if you add together as a combination will give the parameter number, assuming one pair and the first in the tuple is less than the second
    # i.e: two_sum([2, 7, 11, 15], 18)   # returns [1, 2]   (7 + 11)
    # there is an obvious brute force way, since only one pair just keep checking until one pair works
   
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    for firstindex,selectednumber in enumerate(nums):
        for secondindex,othernumber in enumerate(nums):
            if (secondindex <= firstindex):
                continue
            
            if (selectednumber + othernumber) == target:
                # if (selectednumber < othernumber):
                    ## i < j
                    # print((firstindex,secondindex))
                    return [firstindex, secondindex]
                # else:
                #     ## i > j
                #     print("second")
                #     print((secondindex,firstindex))
                #     return [secondindex, firstindex]
                


def max_profit(prices):
    # Outline:
    # look for lowest number for lowest buy, then for highest number for highest sell, if number makes no sense to buy return 0, cant look before i
    # i.e max_profit([67,89,10,24,56]), 10 lowest, 89 highest make 79 profit return that
    # you can also brute force for just checking min and max and the difference can just be checked after
    
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    
    min: int = 100000000
    minindex: int = 0
        
    for firstindex, firstmoney in enumerate(prices):
        
        if (min > firstmoney): 
                min = firstmoney
                minindex = firstindex
        
        
    max: int = 0
    maxindex = 0
    for firstindex, firstmoney in enumerate(prices):
        if (firstindex <= minindex):
                continue
            
        if (firstmoney > max):
            max = firstmoney
            maxindex = firstindex
            
    # print("maxindex: ",maxindex)
    # print(max)
    # print(min)
    if (max <= min):
        return 0
    else:
        return max - min
            
    
        
        
        


def max_subarray(nums):
    # Outline:
    # find the largest in a row consecutive number calculation that would give the highest number from a list
    # nums = {2, -8, 5, 6, -2, 3, -10, 4};, 5 + 6 - 2 + 3 = 12
    # brute force just find every possible combination is obvious
    newnums = nums
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    
    biggesttotal = nums[0]

    for index, value in enumerate(nums):
        total = value

        for secondindex in range(index + 1, len(nums)):
            total += nums[secondindex]

            if total > biggesttotal:
                biggesttotal = total

        if value > biggesttotal:
            biggesttotal = value
    return biggesttotal 
    # biggesttotal = 0 
    # biggestindex = 0   
    # for index, value in enumerate(nums):
    #     total = value
    #     for secondindex, secondvalue in enumerate(nums):
    #         if (secondindex <= index):
    #             continue
            
    #         total += secondvalue
    #         if (secondindex == len(nums) - 1):
    #             if (biggesttotal < total):
    #                 print(total)
    #                 biggesttotal = total
    #                 biggestindex = index
                    
    # return biggesttotal
            
            


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline:
    # see if there is corresponding bracket with its symbol and check if the correct position is placed everywhere otherwise something wrong return false
    # i.e: is_balanced("({[]})")  # returns True
    # maybe store the symbols so you know when they should be placed and check if they are not stored using what remembered
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
     
    stack = []

    opposites = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for symbol in s:

        # Opening bracket: store it
        if symbol in "([{":
            stack.append(symbol)

        # Closing bracket: check most recent opening bracket
        else:
            if not stack:
                return False

            if stack[-1] != opposites[symbol]:
                return False

            stack.pop()

    return len(stack) == 0 
    # if s == "" or s == '':
    #     return None
              
    # for firstindex, symbol in enumerate(s):
        
    #     oppositesymbol = ""
        
    #     if symbol == "{":
    #         oppositesymbol = "}"
    #     elif symbol == "}":
    #         oppositesymbol = "{"
    #     elif symbol == "(":
    #         oppositesymbol = ")"
    #     elif symbol == ")":
    #         oppositesymbol = "("
    #     elif symbol == "[":
    #         oppositesymbol == "]"
    #     elif symbol == "]":
    #         oppositesymbol == "["    
            
    #     if oppositesymbol == "":
    #         return None
        
    #     for index,othersymbol in enumerate(s):
    #         if (index <= firstindex):
    #             continue
            
    #         if (othersymbol == oppositesymbol):
    #             continue
            
    #         if (othersymbol == symbol):
    #             return False
            
    #         if (index == len(s)):
    #             return False
            
    #     return True
            


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]


if __name__ == "__main__":
    main()
