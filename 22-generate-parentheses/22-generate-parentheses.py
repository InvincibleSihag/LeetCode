class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        output = []
        
        def helper(cur, count_dict):
            # print(cur, count_dict)
            if sum(count_dict.values()) == n*2:
                output.append(cur)
                return
            if count_dict["("] == n:
                count_dict[")"] += 1
                helper(cur+")", count_dict)
                count_dict[")"] -= 1
            elif count_dict[")"] > count_dict["("]:
                return
            else:
                count_dict["("] += 1
                helper(cur+"(", count_dict)
                count_dict["("] -= 1
                count_dict[")"] += 1
                helper(cur+")", count_dict)
                count_dict[")"] -= 1
                
        helper("(", {"(":1, ")": 0})
        return output
        