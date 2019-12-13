# create 2-D array
# 1. x = [[foo for i in range(10)] for j in range(10)]
# 2. import numpy
#    matrix = numpy.empty((10, 10))

'''
5
P0 P1 P2 P3 P4
3
A B C
0 1 0
2 0 0
3 0 2
2 1 1
0 0 2
2 1 3
3 2 2
4 0 2
2 2 2
2 3 3
1 0 1
'''

m = int(input())
Proc = input().strip().split()
n = int(input())
Res = input().strip().split()
Allocation = [list(map(int, input().strip().split())) for i in range(m)]
Max = [list(map(int, input().strip().split())) for i in range(m)]
Available = list(map(int, input().strip().split()))
Need = [[Max[i][j] - Allocation[i][j] for j in range(n)] for i in range(m)]

"""
Proc = [p1,p2,p3,p4,p5]
Res =  [A,B,C,D]
All = [5][4]
Avail = [4]
Max = [5][4]
Need = [5][4]
"""
if __name__ == "__main__":
    safe_seq = []
    # 遍历两遍进程列表——>所有情况
    for k in  range(len(Proc)):
        for i in range(len(Proc)):
            if Proc[i] not in safe_seq:
                flag = 1
                #　若 Need > Available
                #　无法添加到安全序列
                for j in range(len(Res)):
                    if(Need[i][j] > Available[j]):
                        flag = 0
                        break
                # 否则 Avail += Allocation
                # 更新可用资源
                if flag:
                    for j in range(len(Res)):
                        Available[j] += Allocation[i][j]
                    safe_seq.append(Proc[i])
    if (len(safe_seq) != len(Proc)):
        print("不存在安全序列,以下不能被执行：")
        cant = [item for item in Proc if item not in safe_seq]
        print(cant)
    else:
        print("存在安全序列如下：")
        print(safe_seq)
