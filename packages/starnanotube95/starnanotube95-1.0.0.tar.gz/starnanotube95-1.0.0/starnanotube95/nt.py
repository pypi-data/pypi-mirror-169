#coding=utf-8
#碳纳米管类
#2022.01.18 by Spectre Lee
#init, str, add
#.length2energe(lamda) 输入波长(单位nm)，返回能量(eV)
#.diameter(n,m) 返回碳管直径
#.angle(n,m) 返回手性角
#http://nmns.net.cn/cnt_assign 详细参数可以访问该网站查询
#部分算法参考了孙斯达的源代码
#str(Nanotube(n,m)) or print(class(n,m)) 可以输出(n,m)的直径，rbm峰，手性角，金半，每个Eii以及每个Eii对应的波长
#Nanotube(n,m).d .rbm .a_reg .a_deg .isSemi .Eii 可以得到上边的信息
#Nanotube(n,m).resonance(laser,rbm) 判断某激光波长激发出来的rbm是否可以指认为(n,m)型的碳纳米管

import numpy as np
from scipy import constants as sc

#RBM和直径之间的转换系数
rbmParams = (
(235.9, 5.5),
(217.8, 15.7),
((204, 27),(200, 26),(228, 0)),#悬空碳管比较特殊
(227.0, 0.3),
(223.5, 12.5),
(218, 18.3),
)

# env 0-5 分别代表了以下测试环境的碳纳米管，会影响RBM和d之间的转换
# 0'SWNTs on SiOx/Si substrates'
# 1'SWNT arrays on quartz substrates'
# 2'Air-suspended SWNTs'
# 3'"Super-growth" SWNTs'
# 4'SDS-dispersed SWNTs'
# 5'ssDNA-dispersed SWNTs'


#根据直径和手性角，计算Eii的各种系数
#0 1 2环境
env0Params = (
  [ 3.170, 0.764, 0.286 ], #M11
  [ 6.508, 2.768, 0.928 ], #M22
  [ 9.857, 6.228, 1.692 ], #M33
  [ 1.194, 0.179, 0.053 ], #S11
  [ 2.110, 0.388, 0.154 ], #S22
  [ 4.286, 1.230, 0.412 ], #S33
  [ 5.380, 1.922, 0.644 ], #S44
  [ 7.624, 3.768, 1.024 ], #S55
  [ 8.734, 4.921, 1.479 ], #S66
)
#第四个修正项
delta = (0.04, 0.1, 0)

#环境3
env3Params = (
  [ 0.09, -0.07 ],#S11
  [ -0.18, 0.14 ],#S22
  [ -0.19, 0.29 ],#M11
  [ 0.49, -0.33 ],#S33
  [ -0.43, 0.59 ],#S44
  [ -0.6, 0.57 ]  #M22
)
e3a,e3b,e3c = 1.074, 0.467, 0.812
e3p = (0,0,0,0.059,0.059,0.059)

#环境45
e4r = ((0,0.04575,-0.08802),(0,-0.18290,0.17050))
e45delta = (0,0.02)

class Nanotube:
    def __init__(self, n=6, m=5, env=0):#构造函数，n,m值可以唯一确定一个碳纳米管,env为碳纳米管所在的环境0硅基底 1石英 2悬空 3垂直阵列 4SDS 5NDA
        self.n, self.m, self.env = int(n), int(m), int(env)
        self.d = self.diameter(self.n,self.m,self.env)
        self.a_rad = self.angle(self.n,self.m)
        self.a_deg = self.angle_degree(self.n,self.m)
        self.isSemi = self.isSemi(self.n,self.m)
        self.mod = (2*n+m) % 3
        self.Eii = self.Eii(env,n,m)
        if self.mod == 0:
            self.rbm = self.d2rbm(self.d,self.env,p=1)
        else:
            self.rbm = self.d2rbm(self.d,self.env,p=0)

    def __str__(self):#标准打印格式
        output = f'({self.n},{self.m}), '+'{:.3f}nm, {:.1f}/cm, {:.1f}Deg'.format(self.d,self.rbm, self.a_deg)
        if(self.isSemi): output += ', Semi-conductive' 
        else: output += ', Metalic'
        for key in self.Eii.keys():
            output += ', {}: {:.3f}eV|{:.1f}nm'.format(key,self.Eii[key],self.energe2length(self.Eii[key]))  
        return output
    def __add__(self, other):#重载了加法
        return self(self.n+other.n, self.m+other.m)

    def length2energe(self, wavelength):#波长到能量
        return sc.h*sc.c/(wavelength*1e-9)/sc.e
    def energe2length(self, energe):#波长到能量
        return sc.h*sc.c/(energe*sc.e) * 1e9
    def __rbmAB(self,env,p=0):
        if(env==2): 
            return rbmParams[env][p]
        else: 
            return rbmParams[env]

    def rbm2d(self,rbm,env=None,p=0):#RBM到直径
        if(env==None): env=self.env
        A, b = self.__rbmAB(env,p)
        return A/(rbm-b)
    def d2rbm(self,d,env=None,p=0):#直径到
        if(env==None): env=self.env
        A, b = self.__rbmAB(env,p)
        return A/d + b

    def isSemi(self,n=0,m=0):
        if(n==0): n=self.n
        if(m==0): m=self.m#相当于重载了
        if((2*n+m)%3==0): return False
        else: return True

    def diameter(self,n=0,m=0,env=None):#根据nm计算碳纳米管直径
        if(n==0): n=self.n
        if(m==0): m=self.m#相当于重载了
        if(env==None): env=self.env
        if(env==4): return 0.144*np.sqrt(3*(m*m+n*n+m*n))/sc.pi #SDS包裹的CNTCC键长改变
        return 0.142*np.sqrt(3*(m*m+n*n+m*n))/sc.pi

    def angle(self,n=0,m=0):#手性角
        if(n==0): n=self.n
        if(m==0): m=self.m
        return np.arctan( np.sqrt(3)*m / (2*n+m) )
    def angle_degree(self,n=0,m=0):#角度制和弧度制
        if(n==0): n=self.n
        if(m==0): m=self.m
        return np.rad2deg(self.angle(self.n,self.m))
    def mod(self,n=0,m=0):#0金属管 1 2是两种半导体管
        if(n==0): n=self.n
        if(m==0): m=self.m
        return (2*n+m)%3

    def Eii(self,env=None,n=0,m=0):
        if(n==0): n=self.n
        if(m==0): m=self.m
        if(env==None): env=self.env
        d = self.diameter(n,m,env)
        a = np.cos( 3 * self.angle(n,m) ) #cos3θ
        mod = (2*n + m)%3#不清楚为什么调用内部函数会出问题，先这么用吧。
        dict={}#用于记录Eii
        if env in (0,1,2):
            if mod == 0:
                for i in (0,1,2):
                    dict['M'+str(i*10+i+11)+'+'] = env0Params[i][0]/d - env0Params[i][1]/(d*d) + env0Params[i][2]/(d*d)*a - delta[env]
                    dict['M'+str(i*10+i+11)+'-'] = env0Params[i][0]/d - env0Params[i][1]/(d*d) - env0Params[i][2]/(d*d)*a - delta[env]
            elif mod == 1:
                for i in (0,1,2,3,4,5):
                    dict['S'+str(i*10+i+11)] = env0Params[3+i][0]/d - env0Params[3+i][1]/(d*d) - env0Params[3+i][2]/(d*d)*a * (i%2-0.5)*2 - delta[env]
            elif mod == 2:
                for i in (0,1,2,3,4,5):
                    dict['S'+str(i*10+i+11)] = env0Params[3+i][0]/d - env0Params[3+i][1]/(d*d) + env0Params[3+i][2]/(d*d)*a * (i%2-0.5)*2 - delta[env]
        elif env==3:
            def sgeii(p,m):
                return e3a * (p+1)/d * ( 1+e3b*np.log10(e3c/(p+1)*d) ) + env3Params[p][m] / (d*d) *a + e3p[p]*(p+1)/d
            if mod == 0:
                dict['M11+'],dict['M11-'],dict['M22+'],dict['M22-'] = sgeii(2,1),sgeii(2,0),sgeii(5,1),sgeii(5,0)
            else:
                dict['S11'],dict['S22'],dict['S33'],dict['S44'] = sgeii(0,mod-1),sgeii(1,mod-1),sgeii(3,mod-1),sgeii(4,mod-1)
        elif env in (4,5):
            if mod != 0:
                dict['S11'] = 1 / (0.1270 + 0.8606 * d) + e4r[0][mod] / (d * d) * a - e45delta[env-4]
                dict['S22'] = 1 / (0.1174 + 0.4644 * d) + e4r[1][mod] / (d * d) * a - e45delta[env-4]
        return dict

    def resonance(self,laserlength,rbm,env=None,e_err=0.1,d_err=0.1):#根据激光波长和rbm判断是否为该class代表的碳纳米管,注意处理悬空碳纳米管的情况
        if(env==None): env=self.env
        result = []
        energe = self.length2energe(laserlength)
        if env != 2:
            if np.abs( self.d-self.rbm2d(rbm,env) )>d_err:#直径相差大于容差，直接pass
                return result
            for key in self.Eii.keys():#判断能量是否匹配
                if np.abs( energe - self.Eii[key] )<e_err:
                    result.append(key)
        if(env==2):
            for key in self.Eii.keys():#判断能量是否匹配
                if np.abs( energe - self.Eii[key] )<e_err:
                    if key in ('S11','S22'):
                        if np.abs( self.d-self.rbm2d(rbm,env,0) )<d_err:
                            result.append(key)
                    elif key in ('M11+','M11-'):
                        if np.abs( self.d-self.rbm2d(rbm,env,1) )<d_err:
                            result.append(key)
                    else:
                        if np.abs( self.d-self.rbm2d(rbm,env,2) )<d_err:
                            result.append(key)
        return result

if __name__ == '__main__':
    print("Please input (n,m) of target nanotube:")
    n = int(input("n = "))
    m = int(input("m = "))
    print(Nanotube(n,m))


