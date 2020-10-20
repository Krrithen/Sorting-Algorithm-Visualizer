import time

def merge_sort(data,drawData,timeTick):
    merge_sort_algo(data,0,len(data)-1,drawData,timeTick)



def merge_sort_algo(data,left,right,drawData,timeTick):
    if left < right:
        middle = (left+right) // 2
        merge_sort_algo(data,left,middle,drawData,timeTick)
        merge_sort_algo(data,middle+1,right,drawData,timeTick)
        merge(data,left,middle,right,drawData,timeTick)


def merge(data,left,middle,right,drawData,timeTick):

    drawData(data,colorArray(len(data),left,middle,right))
    time.sleep(timeTick)

    leftpart = data[left:middle+1]
    rightpart = data[middle+1:right+1]

    leftIdx=rightIdx = 0

    for dataIdx in range(left,right+1):
        if leftIdx < len(leftpart) and rightIdx<len(rightpart):
            if leftpart[leftIdx]<=rightpart[rightIdx]:
                data[dataIdx]=leftpart[leftIdx]
                leftIdx+=1
            else:
                data[dataIdx] = rightpart[rightIdx]
                rightIdx+=1

        elif leftIdx < len(leftpart):
            data[dataIdx] = leftpart[leftIdx]
            leftIdx+=1
        else:
            data[dataIdx]= rightpart[rightIdx]
            rightIdx +=1

    drawData(data,["green" if x >= left and x <=right else "white" for x in range (len(data))])
    time.sleep(timeTick)



def colorArray(length , left,middle,right):
    colorArray=[]

    for  i in range(length):
        if i>=left and i <=right:
            if i>=left and i<=middle:
                colorArray.append("yellow")
            else:
                colorArray.append("orange")
        else:
            colorArray.append("white")
    return colorArray