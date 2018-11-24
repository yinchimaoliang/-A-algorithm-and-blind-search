import random
import sys
import time
sys.setrecursionlimit(1000000)
class point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

class main_func():
    def __init__(self):
        self.tm = [[]]
        self.test_map = []
        self.visited = []
    def input_tm(self):#从input.txt中获取输入数据
        points = []
        try:
            f = open("input.txt", 'r')
            x_len = int(f.readline())
            y_len = int(f.readline())
            # 输入障碍点个数
            num = int(f.readline())
            # 输入起始终止坐标:
            self.S_x, self.S_y = map(int, f.readline().split())
            self.E_x, self.E_y = map(int, f.readline().split())

            for i in range(x_len + 2):
                if i != 0:
                    self.tm.append([])
                for j in range(y_len + 2):
                    self.tm[i].append('.')
                    if i == 0 or i == x_len + 1 or j == 0 or j == y_len + 1:
                        self.tm[i][j] = '#'
                    else:
                        if (i != self.S_x or j != self.S_y) and (i != self.E_x or j != self.E_y):
                            points.append(point(i, j))

            self.tm[self.S_x][self.S_y] = 'S'
            self.tm[self.E_x][self.E_y] = 'E'
            randomIndex = random.sample(range(0, len(points)), num)
            for i in randomIndex:
                self.tm[points[i].x][points[i].y] = '#'
        except:
            print("输入文件格式出错")
            exit()
    def judge_visited(self,p):#判断点p是否被访问过
        for i in self.visited:
            if i.x == p.x and i.y == p.y:
                return True
        return False
    def find_path(self,p):#递归寻找路径
        if self.judge_visited(p) or self.tm[p.x][p.y] == '#':
            return False
        else:
            self.visited.append(p)
            if self.tm[p.x][p.y] == 'E':
                return True
            else:
                po = []
                re = []
                result = False
                #增加斜向路径，根据当前节点和目标节点不同的位置关系，确定不同的优先级队列
                po.append(point(p.x+1,p.y+1))
                po.append(point(p.x + 1, p.y - 1))
                po.append(point(p.x - 1, p.y + 1))
                po.append(point(p.x - 1, p.y - 1))
                po.append(point(p.x + 1, p.y))
                po.append(point(p.x - 1, p.y))
                po.append(point(p.x, p.y + 1))
                po.append(point(p.x, p.y - 1))
                if p.x < self.E_x and p.y == self.E_y:
                    index = [4,0,1,6,7,2,3,5]
                if p.x > self.E_x and p.y == self.E_y:
                    index = [5,2,3,6,7,4,0,1]
                if p.x == self.E_x and p.y < self.E_y:
                    index = [6,0,2,4,5,7,1,3]
                if p.x == self.E_x and p.y > self.E_y:
                    index = [7,1,3,6,4,5,2,0]
                if p.x < self.E_x and p.y < self.E_y:
                    index = [0,4,6,1,2,5,7,3]
                if p.x < self.E_x and p.y > self.E_y:
                    index = [1,4,7,0,3,5,6,2]
                if p.x > self.E_x and p.y > self.E_y:
                    index = [3,7,5,2,1,6,4,0]
                if p.x > self.E_x and p.y < self.E_y:
                    index = [2,6,5,3,0,7,4,1]
                for i in index:
                    if i < len(po) and po[i] != 0:
                        re.append(self.find_path(po[i]))
                for j in re:
                    result = result or j
                if result:
                    self.tm[p.x][p.y] = '*'
                return result
    def print_path(self):#将结果输出到output.txt文件中
        self.tm[self.S_x][self.S_y] = 'S'
        f = open("output.txt", 'w')
        for line in self.tm:
            print(''.join(line))
            f.write(''.join(line))
            f.write('\n')
    def main(self):
        self.input_tm()
        if self.find_path(point(self.S_x,self.S_y)):
            self.print_path()
        else:
            print("无路径")

start = time.time()
t = main_func()
t.main()
end = time.time()
print(end-start)