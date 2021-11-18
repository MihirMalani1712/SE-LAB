import tool

j = 0

def testCases(length, options, password):
    global j
    j += 1
    print("Case {}:".format(j))
    if(tool.checkLength(length)):
        feedback = tool.validatePassword(length, options, password)
        tool.setFeedback(feedback)
    print('\n')


testCases('', [], '')
testCases('0', [], '')
testCases('-1', [], '')
testCases('a', [], '')
testCases('2', [], 'pqr')
testCases('3', [], 'pqr')
testCases('2', ["uppercase", "lowercase", "digit","special"],'a1')
testCases('5',["uppercase", "lowercase", "digit","special"],'Qw1v7')
testCases('4', ["uppercase", "lowercase", "digit"], 'Is9q')
