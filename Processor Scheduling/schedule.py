# /* input
# 作业编号 作业名称 提交时间(h:m:s)  要求服务运行时间（分钟）
# 1      JA       02:40:15     20.5 
# 2      JB       02:50:30     30.8      
# 3      JC       02:55:55     10.6      
# 4      JD       03:00:23     24.8      
# 5      JE       03:05:18     6.5        
# */
### 不考虑提交时间比其前面所有作业服务完成时间还大的情况
def FCFS(procs):
    procs.sort(key=lambda x: x.AT, reverse=False)
    time = procs[0].AT
    wtime=0
    print("FCFS process scheduling:")
    for proc in procs:
        proc.ST = time
        time += proc.RT
        proc.ET=time
        proc.WT = proc.ST - proc.AT
        proc.CT = proc.ET - proc.AT
        proc.print_basic()
def SJF(procs):
    
    def insert(lft, dif,num,RT):
        i = 0
        while (True):
            dif -= lft[i][0]
            if (dif > 0):
                lft[i][0] = 0
                print(lft[i][1]+" ended")
                i+=1
            else:
                dif += lft[i][0]
                lft[i][0] -= dif
                break
        print(num+" added")
        lft.insert(i + 1, [RT, num])
        lft.sort(key=lambda x: x[0], reverse=False)
        return lft
    procs.sort(key=lambda x: x.AT, reverse=False)
    time = procs[0].AT
    print("SJF process scheduling:")
    lft=[]
    lft.append([procs[0].RT, procs[0].num])
    print(lft)
    for i in range(0, len(procs) - 1):
        p_next=procs[i+1]
        time_dif = procs[i+1].AT-procs[i].AT
        lft = insert(lft, time_dif,p_next.num,p_next.RT)
        print(lft)
        
    
    def prior(now, next):
        if now > next:
            return 1
        else:
            return 0 
class Proc:
    num = 0
    AT = 0#提交时间 seconds input
    ST = 0#开始时间 AT_init+sum(RT_before)
    RT=0 #要求服务运行时间 seconds input
    ET=0 #完成时间 ST+RT
    WT = 0 #等待时间 ST-AT>0 else 0 
    CT = 0  #周转时间 ET-AT
    lft=0 #剩余T
    name = ""
    def init(self,content):
        self.num, self.name, self.AT, self.RT = content
        self.lft=self.RT
    def to_HMS(self, seconds):
        h, s = seconds // 3600, seconds % 3600
        m, s = s // 60, s % 60
        return str(h) + ":" + str(m) + ":" + str(s)
    def print_basic(self):
        print(self.name + " starts working at " + self.to_HMS(self.ST))
        print("it lasts " + str(self.RT) + " secs")
        print("it ends at " + self.to_HMS(self.ET))
        print("it waits for " + str(self.WT)+  " secs")
        print("It Turn around "+str(self.CT))
    def print_statistics(self):
        #ACT= sum(CT)/jobs
        #AWCT
        print("ACT = 0#平均周转时间 CT/JOBS \
               AWCT = 0#平均带权周转时间")
if __name__ == "__main__":
    procs=[]
    with open("text.txt", "r") as f:
        line=f.readline()
        while(line):
            content = line.split()
            proc = Proc()
            splits = content[2].split(":")
            content[2] = int(splits[0]) * 3600 + int(splits[1]) * 60 + int(splits[2])
            content[3]=int(float(content[3])*60)
            proc.init(content)
            procs.append(proc)
            line=f.readline()
    FCFS(procs)


              