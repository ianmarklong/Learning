def arithmetic_arranger(problems, show_answers=False):
    limit = 5
    validOps = ['+','-']
    line1 = ''
    line2 = ''
    line3 = ''
    answers = ''

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for problem in problems:
        first,operator,second = problem.split(' ')
        if not operator in validOps:
            return("Error: Operator must be '+' or '-'.")
        if not first.isdigit() or not second.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(first) > 4 or len(second) > 4:
            return 'Error: Numbers cannot be more than four digits.'
#all error handling done
        #find longest operand
        longest = max(len(first),len(second))
        width = longest + 2

        one = (' '*(width-len(first))+first)
        two = operator+' '+ (' '*(width-2-len(second))+second)
        three = '-'*width

        line1 += one + "    "
        line2 += two + '    '
        line3 += three + '    '

        if show_answers == True:
            if operator == '+':
                answer = int(first)+int(second)
            else: 
                answer = int(first)-int(second)
            answer = str(answer)
            answer = ' '*(width-len(answer))+answer
            answers += str(answer) + '    '

   
    if show_answers == True:
        problems = line1.rstrip()+'\n'+line2.rstrip()+'\n'+line3.rstrip()+'\n'+answers.rstrip()
        return problems

    else:
        problems = line1.rstrip()+'\n'+line2.rstrip()+'\n'+line3.rstrip()
        return problems
    
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))