def search(count):
    left = 0
    right = float(count[1])
    result = 0
    while right-left > 0.0000000001:
        mid = (left + right) / 2
        cur = mid
        prev = float(count[1])
        flag = True
        for i in range(3, int(count[0])+1):
            next = 2 * cur - prev + 2
            if next > 0:
                flag = True
            else:
                flag = False
                break
            prev = cur
            cur = next
        if flag:
            right = mid
            result =cur
        else:
            left = mid
    return result

def inputData():
    with open('input.txt','r', encoding = 'utf8') as inputData:
        count = inputData.read().split()
    return count

def outputData(result):
    with open('output.txt', 'w', encoding = 'utf8') as outputData:
        outputData.write(str(result))
    return

def main():
    count = inputData()
    result = search(count)
    outputData(result)

if __name__ == '__main__':
    main()