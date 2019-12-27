# create 2-D array
# 1. x = [[foo for i in range(10)] for j in range(10)]
# 2. import numpy
#    matrix = numpy.empty((10, 10))
import copy

Allocation = []
Max = []
Need = []
print("请输入进程数目")
m = int(input())
print("请输入各进程名称")
Proc = input().strip().split()
print("请输入资源种类数目")
n = int(input())
print("请输入各资源名称")
Res = input().strip().split()
print("顺序输入为已为各进程分配的各个资源数目")
for i in range(m):
    res = input().strip().split()
    res = [int(i) for i in res]
    Allocation.append(res)
print("输入进程所需最大的各个资源数目")
Max = [list(map(int, input().strip().split())) for i in range(m)]
print("输入各个资源剩余可用数目")
Available = list(map(int, input().strip().split()))
Need = [[Max[i][j] - Allocation[i][j] for j in range(n)] for i in range(m)]
Available_ = copy.deepcopy(Available)

"""
Proc = [p1,p2,p3,p4,p5]
Res =  [A,B,C,D]
All = [5][4]
Avail = [4] 5
Max = [5][4]
Need = [5][4]
"""
def get_seq():
    safe_seq = []
    
    # 遍历两遍进程列表——>所有情况
    for k in  range(len(Proc)):
        for i in range(len(Proc)):
            if Proc[i] not in safe_seq:
                secure = 1
                #　若 Need > Available
                #　无法添加到安全序列
                for j in range(len(Res)):
                    if (Need[i][j] > Available[j]):
                        secure = 0
                        break
                # 否则 Avail += Allocation
                # 更新可用资源
                if secure:
                    for j in range(len(Res)):
                        Available[j] += Allocation[i][j]
                    safe_seq.append(Proc[i])
    if (len(safe_seq) != len(Proc)):
        print("不存在安全序列,以下进程不能被执行：")
        cant = [item for item in Proc if item not in safe_seq]
        print(cant)
        return False
    else:
        print("存在安全序列如下：")
        print(safe_seq)
        return True

def compare(list1, list2):
    for i in range(0, len(list1)):
        if list1[i] > list2[i]:
            return False
    return True

if __name__ == "__main__":
    secure=True
    get_seq()
    while (True):
        print("请输入请求进程及资源")
        p = int(input())
        request = list(map(int, input().strip().split()))
        #### 检查1
        if compare(request,Need[p]):
            #### 检查2
            if compare(request,Available_):
                #在 分配的边缘试探
                Available = copy.deepcopy(Available_)
                for j in range(0,len(request)):
                    Available[j] -= request[j]
                    Allocation[p][j] += request[j]
                    Need[p][j] -= request[j]
                Available_=copy.deepcopy(Available)
                #分配之后要安全呐！
                if not get_seq():
                    print("分配失败")
            else:
                print("尚无够用资源，等待吧！")
        else:
            print("请求已超过所宣布的最大值")
          


