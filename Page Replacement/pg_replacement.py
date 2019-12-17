def input_():
    print("请输入页框数目、最大逻辑页号、随机访问序列长度和置换算法：")
    n_frame = int(input())
    Max = int(input())
    length = int(input())
    alg = input()
    sequence=[]
    from random import randrange
    for i in range(0,length):
        sequence.append(randrange(Max))
    return n_frame,Max,length,sequence,alg


def input_2():
    print("请输入页框数目、最大逻辑页号、访问序列和置换算法：")
    n_frame = int(input())
    Max = int(input())
    sequence = list(map(int, input().strip().split()))
    alg = input()
    return n_frame, Max, sequence, alg
    

FIFO = 'FIFO'
LRU = 'LRU'
CLOCK = 'CLOCK'

class PageFrame(object):
    def __init__(self, num,alg):
        # super(ClassName, self).__init__(*args))
        self.num = num
        if alg == CLOCK:
            self.pos = 0
            self.page = []
            self.second_chance = []
        else:
            self.page = []
        self.alg = alg
        
    # num 页框数量
    # page 页面
    #my_list.append(my_list.pop(0))
# To the right:

# my_list.insert(0, my_list.pop())
    #
    def page_replacement(self, page_number):
        result = getattr(self, self.alg)(*[page_number])
        return result
    def FIFO(self, page_number):
        if page_number in self.page:
            self.print_in(page_number)
            return 1
        else:
            self.page.append(page_number)
            if len(self.page) > self.num:
                out = self.page[0]
                del (self.page[0])
                self.print_out(page_number,out)  
            else:
                self.print_out(page_number, -1)
            return 0
    def LRU(self, page_number):
        if page_number in self.page:
            self.page.remove(page_number)
            self.page.insert(0, page_number)
            self.print_in(page_number)
            return 1
        else:
            self.page.insert(0, page_number)

            if len(self.page) > self.num:
                pop = self.page.pop()
                self.print_out(page_number,pop)   
            else:
                self.print_out(page_number,-1)         
            return 0
    def CLOCK(self, page_number):

        if page_number in self.page:
            self.print_in(page_number)
            self.second_chance[self.page.index(page_number)] = 1
            return 1
        else:
            if len(self.page) < self.num:
                self.page.append(page_number)
                self.second_chance.append(0)
                self.pos += 1
                self.pos %= self.num
                self.print_out(page_number,-1)
                
            else:
                while self.second_chance[self.pos] != 0:
                    self.second_chance[self.pos] = 0
                    self.pos += 1
                    self.pos %= self.num
                out=self.page[self.pos]
                self.page[self.pos] = page_number
                self.print_out(page_number, out) 
                self.pos += 1
                self.pos %= self.num
            return  0
                    
    def print_in(self, page_number):
        print("访问 " + str(page_number) + " 在内存中，页面情况为" + str(self.page))
    def print_out(self, page_number, out):
        if out == -1:
            print("访问 " + str(page_number) + " 缺页无换出，页面情况为" + str(self.page))
        else:
            print("访问 " + str(page_number) + " 缺页，"+str(out)+"被换出，页面情况为" + str(self.page))
        
if __name__ == "__main__":
    # n_frame, Max, length, sequence,alg = input_()
    n_frame, Max, sequence, alg = input_2()
    length=len(sequence)
    page_frame = PageFrame(n_frame, alg)
    in_page = 0
    for i in sequence:
        res = page_frame.page_replacement(i)
        in_page += res
    print("缺页率为"+str((length-in_page)/length))