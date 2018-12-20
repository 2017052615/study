class people_name:  ## 사람의 이름과 길이가 들어갈 클래스
    name = ""
    length =""
    def __init__(self, name, length): ##생성자로서 이름과 이름길이가 파라미터로 주어지면 이 클래스의 이름과 길이가 갱신된다.
        self.name = name
        self.length =length
    def L(self):                              ##  L O V E 의 갯수를 구해서 return 해준다.
        L=0
        for i in range(0, self.length): ## 0부터 이름길이까지 for문을 돌려 이름에 L이 있으면 L의 갯수에 +1을 해준다
            if(self.name[i]=="L"):
                L = L+1
        return L   ## 다 구한 L값을 return해준다.
    def O(self):
        O=0
        for i in range(0, self.length):
            if(self.name[i]=="O"):
                O = O+1
        return O
    def V(self):
        V=0
        for i in range(0, self.length):
            if(self.name[i]=="V"):
                V = V+1
        return V
    def E(self):
        E=0
        for i in range(0, self.length):
            if(self.name[i]=="E"):
                E = E+1
        return E
