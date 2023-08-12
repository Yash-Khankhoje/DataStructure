testCases = ["[ab+(x{})]", "{{])", "}{", "([)]{}","","[[{}()][]](){}"]
formated_testCases = []
replacable_Chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*1234567890-=_+\|:;?/.>,<'
for testCase in testCases:
    formated_test_case = ''
    for subString in testCase:
        if(subString not in replacable_Chars):
            formated_test_case += subString
    formated_testCases.append(formated_test_case)
            
output_list = []

for test_case in formated_testCases:
    my_stack = []
    for sub_string in test_case:
        if sub_string in '[{(':
            my_stack.append(sub_string)

        elif len(my_stack) > 0 and ((sub_string == '}' and my_stack[-1] == '{') or 
                                    (sub_string == ']' and my_stack[-1] == '[') or 
                                    (sub_string == ')' and my_stack[-1] == '(')):
            my_stack.pop()
        else:
            output_list.append(False)
            my_stack.append(sub_string)
            break
    if len(my_stack) == 0:
        output_list.append(True)

print(output_list)


