class col:
    def __init__(self):
        self.list = [False]*20
        self.top = 0

    def pos(self, pos):
        return self.list[pos]

    def eliminate(self, height):
        self.list.pop(height)
        self.list.append(False)

    def fall_1(self):
        if self.top <= 19:
            self.eliminate(self.top)
        
    def is_full(self):
        return self.list[-1]

    def light(self,row):
        self.list[row] = True

    def func2(self):
        a = self.top
        if self.list[a+1] == False and True in self.list[a:]:
            return True     # 可以下落
        else:
            return False    # 不能下落
    def __str__(self):
        return 'aaaa'


class Screen:
    def __init__(self):
        self.width = 10
        self.s = [None]*self.width
        for i in range(self.width):
            self.s[i] = col()

    def can_elim(self,height):
        result = True
        for i in range(self.width):
            if self.s[i].pos[height] == False:
                result = False
        return result

    def elim(self):
        '''消除所有满行'''
        for i in range(20):
            if slef.can_elim(19-i) == True:
                for j in range(self.width):
                    self.s[j].eliminate(19-i)

    def ground(self,shape):
        '''
        判断一个形状是否还能下落
        shape  - 一个存储形状坐标的list(0-9)
        result - 能否下落'''
        result = False

        
        shape1 = []
        for i in shape:
            if i not in shape1:
                shape1 += [i]

                
        for j in shape1:
            if self.s[j].func2() == False:
                result = True # 不能下落 
        return result

    def fall_s(self,shape):
        
        shape1 = []
        for i in shape:
            if i not in shape1:
                shape1 += [i]
                
        if self.ground(shape1) == False:
            for i in range(self.width):
                self.s[i].fall_1()
            # pass        # 下落一格
            
        else:
            for i in shape1:
                new_top = 19
                while self.s[i].pos(new_top) == False:
                    new_top -= 1
                self.s[i].top = new_top
            #pass        # 修改col.top
            
    def _enter(self,shape):
        result = False
        for i in shape:
            cur_col = self.s[i]
            if cur_col.pos(-1) == cur_col.pos(-2) == False:
                result = True
        if result == True:
            for j in shape:
                if self.s[j].pos(-1) == True:
                    self.s[j].light(-2)
                else:
                    self.s[j].light(-1)
        
                

    def _over(self,shape):
        over = False
        for i in shape:
            if self.s[i].func2() == False:
                over = True
        return over

    def print_pos(self):
        '''
        返回一个list，包括所有可以打印的坐标
        '''
        list1 = []
        for i in range(self.width):
            for j in range(20):
                if self.s[i].pos(j) == True:
                    pos_x = 34 * i +2
                    pos_y = (19-j) *34 + 2
                    list1 += [[pos_x,pos_y]]
        return list1

            
    # 增加 enter 程序，输入横坐标出现次数来确定形状，先行判定这一列是否占满。
    # 修改 fall_s 程序。
            
            
        
