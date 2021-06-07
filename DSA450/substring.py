outputs = ""
inputs = "abcd"


def printSubsequence(inputs, outputs):
    if len(inputs) == 0:
        print(outputs, end=", ")
        return
    # print(inputs[1:])
    printSubsequence(inputs[1:], outputs + inputs[0])
    printSubsequence(inputs[1:], outputs)


printSubsequence(inputs, outputs)
