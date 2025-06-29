from typing import List
import inspect

def log_function_call():
    frame = inspect.currentframe().f_back
    func_name = frame.f_code.co_name
    args, varargs, varkw, values = inspect.getargvalues(frame)

    # Positional arguments
    pos_args = [repr(values[arg]) for arg in args]

    # *args (if any)
    if varargs:
        pos_args += [repr(v) for v in values.get(varargs, [])]

    # **kwargs (if any)
    kwargs = values.get(varkw, {})
    kwarg_strs = [f"{k}={repr(v)}" for k, v in kwargs.items()]

    all_args_str = ", ".join(pos_args + kwarg_strs)
    return f"{func_name}({all_args_str})"


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Space Complexity: O(n)
            O(n) possible recursive stacks for the depth of the tree
            And also O(n) for the `curr_str` list
        """
        result = []
        curr_str = []

        def backtrack(right_count, left_count):
            print(f"\n!!\tStart of {log_function_call()}\t!!")
            if right_count == left_count == n:
                result.append("".join(curr_str))  # this join will be O(2n)
                print(f"Appending {curr_str} to results, and returning None")
                return None
            if right_count > left_count:
                print(f'Appending ")", curr_str = {curr_str + [")"]}')
                curr_str.append(')')
                print(f'Calling backtrack({right_count}, {left_count + 1})')
                backtrack(right_count, left_count + 1)
                print(f'backtrack({right_count}, {left_count + 1}) has returned inside the if right_count > left_count: check, popping curr_str and turning it into {curr_str[:-1]}')
                curr_str.pop()
                print(f"Now proceeding to check if right_count < n inside {log_function_call()}")
            else:
                print(f"{log_function_call()} failed right_count > left_count check")
            if right_count < n:
                print(f'Appending "(", curr_str = {curr_str + ["("]}')
                curr_str.append('(')
                print(f'Calling backtrack({right_count + 1}, {left_count})')
                backtrack(right_count + 1, left_count)
                print(f'backtrack({right_count + 1}, {left_count}) has returned inside the if right_count < n: check, popping curr_str and turning it into {curr_str[:-1]}')
                curr_str.pop()
            else:
                print(f"{log_function_call()} failed right_count < n")
            print(f"!!\tEnd of {log_function_call()}\t!!\n")

        backtrack(0, 0)
        return result


if __name__ == '__main__':
    s = Solution()
    s.generateParenthesis(3)
