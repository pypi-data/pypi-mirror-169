import numpy as np
class Bdouble_tractor:
    M = 6550
    I = 6604
    n = 3
    s = 0
    r = -2.427
    mj = [700,1100,1100]
    ksj = [4e5,1e6,1e6]
    csj = [10e3,20e3,20e3]
    lj = [1.523,-1.727,-3.127]
    ktj = [1.75e6, 3.5e6, 3.5e6]
    ctj = [10e3,10e3, 10e3]
class Bdouble_trailer1:
    M = 18397
    I = 10488
    n = 3
    r = -2.931
    s = 5.369
    mj = [750, 750, 750]
    ksj = [1e6,1e6,1e6]
    csj = [20e3, 20e3, 20e3]
    lj = [-1.531, -2.931, -4.331]
    ktj = [3.5e6, 3.5e6, 3.5e6]
    ctj = [10e3,10e3, 10e3]
class Bdouble_trailer2:
    M = 27375
    I = 15488
    n = 3
    r = 0
    s = 5.895
    mj = [750, 750, 750]
    ksj = [1e6, 1e6, 1e6]
    csj = [20e3, 20e3, 20e3]
    lj = [-1.705, -3.105, -4.505]
    ktj = [3.5e6, 3.5e6, 3.5e6]
    ctj = [10e3,10e3, 10e3]
class Bdouble:
    def __init__(self,Bdouble_tractor,Bdouble_trailer1,Bdouble_trailer2):
        self.Bdouble_tractor = Bdouble_tractor
        self.Bdouble_trailer1 = Bdouble_trailer1
        self.Bdouble_trailer2 = Bdouble_trailer2
        self.M1 = Bdouble_tractor.M
        self.M2 = Bdouble_trailer1.M
        self.M3 = Bdouble_trailer2.M
        self.mj1 = Bdouble_tractor.mj
        self.mj2 = Bdouble_trailer1.mj
        self.mj3 = Bdouble_trailer2.mj
        self.l1 = Bdouble_tractor.lj
        self.l2 = Bdouble_trailer1.lj
        self.l3 = Bdouble_trailer2.lj
        self.ks1 = Bdouble_tractor.ksj
        self.ks2 = Bdouble_trailer1.ksj
        self.ks3 = Bdouble_trailer2.ksj
        self.kt1 = Bdouble_tractor.ktj
        self.kt2 = Bdouble_trailer1.ktj
        self.kt3 = Bdouble_trailer2.ktj
        self.cs1 = Bdouble_tractor.csj
        self.cs2 = Bdouble_trailer1.csj
        self.cs3 = Bdouble_trailer2.csj
        self.ct1 = Bdouble_tractor.ctj
        self.ct2 = Bdouble_trailer1.ctj
        self.ct3 = Bdouble_trailer2.ctj
        self.I1 = Bdouble_tractor.I
        self.I2 = Bdouble_trailer1.I
        self.I3 = Bdouble_trailer2.I
        self.r1 = Bdouble_tractor.r
        self.r2 = Bdouble_trailer1.r
        self.r3 = Bdouble_trailer2.r
        self.s1 = Bdouble_tractor.s
        self.s2 = Bdouble_trailer1.s
        self.s3 = Bdouble_trailer2.s
        self.nv = 4
        self.nvy1 = Bdouble_tractor.n
        self.nvy2 = Bdouble_trailer1.n
        self.nvy3 = Bdouble_trailer2.n
        self.nvy = Bdouble_tractor.n+Bdouble_trailer1.n+Bdouble_trailer2.n
        self.totalen = -self.r1 - self.r2 + self.s2 + self.s3 + np.abs(self.l1[0]) + np.abs(self.l3[2])
        z1 = self.totalen - np.abs(self.l1[0])
        wheel = [[self.totalen, z1 - np.abs(self.l1[1]), z1 - np.abs(self.l1[2])]]
        z2 = z1 + self.r1 - self.s2
        whee2 = [[z2 - np.abs(self.l2[0]), z2 - np.abs(self.l2[1]), z2 - np.abs(self.l2[2])]]
        z3 = z2 + self.r2 - self.s3
        whee3 = [[z3 - np.abs(self.l3[0]), z3 - np.abs(self.l3[1]), z3 - np.abs(self.l3[2])]]
        self.wheel = np.concatenate(([wheel], [whee2], [whee3]),axis=None)
        #self.wheel = np.hstack([wheel,whee2,whee3])

    @property
    def Mass_matrix(self):
        mass = [[0 for i in range(self.nv)] for j in range(self.nv)]
        mass[0][0] = self.M1+self.I2/self.s2**2+(self.r2/self.s2/self.s3)**2*self.I3
        mass[0][1]=-self.r1/self.s2**2*self.I2-self.r1*(self.r2/self.s2/self.s3)**2*self.I3
        mass[0][2]=-1/self.s2**2*self.I2+(self.r2/self.s2/self.s3**2)*(1-self.r2/self.s2)*self.I3
        mass[0][3]=-self.r2/self.s2/self.s3**2*self.I3
        mass[1][1]=self.I1+self.r1**2/self.s2**2*self.I2+self.I3*(self.r1*self.r2/self.s2/self.s3)**2
        mass[1][2]=self.r1/self.s2**2*self.I2-(self.r1*self.r2/self.s2/self.s3**2)*(1-self.r2/self.s2)*self.I3
        mass[1][3]=self.r1*self.r2/self.s2/self.s3**2*self.I3
        mass[2][2]=self.M2+1/self.s2**2*self.I2+self.I3*(1-self.r2/self.s2)**2/self.s3**2
        mass[2][3]=-self.I3*(1-self.r2/self.s2)/self.s3**2
        mass[3][3]=self.M3+self.I3/self.s3**2
        Mass_vehicle=mass+np.transpose(mass)-np.eye(4)*np.diag([mass[0][0],mass[1][1],mass[2][2],mass[3][3]])
        Mass_wheel = np.diag(np.concatenate((self.mj1,self.mj2,self.mj3),axis=None))
        Mass=np.vstack([np.hstack([Mass_vehicle,np.zeros((4,9))]),np.hstack([np.zeros((9,4)),Mass_wheel])])
        return Mass

    @property
    def Stiffness_matrix(self):
        Kv = [[0 for i in range(self.nv)] for j in range(self.nv)]
        Kv[0][0]=np.sum(self.ks1)+sumkl2(self.ks2,self.l2)/self.s2**2+sumkl2(self.ks3,self.l3)*(self.r2/self.s2/self.s3)**2
        Kv[0][1]=-sumkl(self.ks1,self.l1)-sumkl2(self.ks2,self.l2)*self.r1/self.s2**2-sumkl2(self.ks3,self.l3)*self.r1*(self.r2/self.s2/self.s3)**2
        Kv[0][2]=sumkls(self.ks2,self.l2,self.s2)+sumkl2(self.ks3,self.l3)*self.r2/self.s2/self.s3**2*(1-self.r2/self.s2)
        Kv[0][3]=self.r2/self.s2*sumkls(self.ks3,self.l3,self.s3)
        Kv[1][1]=sumkl2(self.ks1,self.l1)+sumkl2(self.ks2,self.l2)*self.r1**2/self.s2**2+sumkl2(self.ks3,self.l3)*(self.r1*self.r2/self.s2/self.s3)**2
        Kv[1][2]=-sumkls(self.ks2,self.l2,self.s2)*self.r1-sumkl2(self.ks3,self.l3)*self.r1*self.r2/self.s2/self.s3**2*(1-self.r2/self.s2)
        Kv[1][3]=-self.r1*self.r2/self.s2*sumkls(self.ks3,self.l3,self.s3)
        Kv[2][2]=sumkls2(self.ks2,self.l2,self.s2)+(1-self.r2/self.s2)**2/self.s3**2*sumkl2(self.ks3,self.l3)
        Kv[2][3]=sumkls(self.ks3,self.l3,self.s3)*(1-self.r2/self.s2)
        Kv[3][3]=sumkls2(self.ks3,self.l3,self.s3)
        K_vehicle = Kv + np.transpose(Kv) - np.eye(4) * np.diag([Kv[0][0], Kv[1][1], Kv[2][2], Kv[3][3]])
        K_wheel = np.diag(np.concatenate((np.add(self.ks1,self.kt1), np.add(self.ks2,self.kt2), np.add(self.ks3,self.kt3)), axis=None))
        Kgv = [[0 for i in range(self.nvy)] for j in range(self.nv)]
        Kgv[0][0:self.nvy1]=scare(self.ks1,-1)
        Kgv[0][self.nvy1:self.nvy1+self.nvy2] = scare2(self.ks2,self.l2,-1/self.s2)
        Kgv[0][self.nvy1+ self.nvy2:self.nvy] = scare2(self.ks3, self.l3, -self.r2/self.s3/self.s2)
        Kgv[1][0:self.nvy1] = scare2(self.ks1, self.l1,1)
        Kgv[1][self.nvy1:self.nvy1 + self.nvy2] = scare2(self.ks2, self.l2, self.r1 / self.s2)
        Kgv[1][self.nvy1 + self.nvy2:self.nvy] = scare2(self.ks3, self.l3, self.r1*self.r2 / self.s3 / self.s2)
        Kgv[2][self.nvy1:self.nvy1 + self.nvy2] = scare3(self.ks2, self.l2, self.s2,-1)
        Kgv[2][self.nvy1 + self.nvy2:self.nvy] = scare2(self.ks3, self.l3, (self.r2 / self.s2-1)/ self.s3 )
        Kgv[3][self.nvy1 + self.nvy2:self.nvy] = scare3(self.ks3, self.l3, self.s3, -1)
        KK = np.vstack([np.hstack([K_vehicle, Kgv]), np.hstack([np.transpose(Kgv), K_wheel])])
        return KK

    @property
    def Damping_matrix(self):
        Kv = [[0 for i in range(self.nv)] for j in range(self.nv)]
        Kv[0][0] = np.sum(self.cs1) + sumkl2(self.cs2, self.l2) / self.s2 ** 2 + sumkl2(self.cs3, self.l3) * (
                    self.r2 / self.s2 / self.s3) ** 2
        Kv[0][1] = -sumkl(self.cs1, self.l1) - sumkl2(self.cs2, self.l2) * self.r1 / self.s2 ** 2 - sumkl2(self.cs3,
                                                                                                           self.l3) * self.r1 * (
                               self.r2 / self.s2 / self.s3) ** 2
        Kv[0][2] = sumkls(self.cs2, self.l2, self.s2) + sumkl2(self.cs3, self.l3) * self.r2 / self.s2 / self.s3 ** 2 * (
                    1 - self.r2 / self.s2)
        Kv[0][3] = self.r2 / self.s2 * sumkls(self.cs3, self.l3, self.s3)
        Kv[1][1] = sumkl2(self.cs1, self.l1) + sumkl2(self.cs2, self.l2) * self.r1 ** 2 / self.s2 ** 2 + sumkl2(
            self.cs3, self.l3) * (self.r1 * self.r2 / self.s2 / self.s3) ** 2
        Kv[1][2] = -sumkls(self.cs2, self.l2, self.s2) * self.r1 - sumkl2(self.cs3,
                                                                          self.l3) * self.r1 * self.r2 / self.s2 / self.s3 ** 2 * (
                               1 - self.r2 / self.s2)
        Kv[1][3] = -self.r1 * self.r2 / self.s2 * sumkls(self.cs3, self.l3, self.s3)
        Kv[2][2] = sumkls2(self.cs2, self.l2, self.s2) + (1 - self.r2 / self.s2) ** 2 / self.s3 ** 2 * sumkl2(self.cs3,
                                                                                                              self.l3)
        Kv[2][3] = sumkls(self.cs3, self.l3, self.s3) * (1 - self.r2 / self.s2)
        Kv[3][3] = sumkls2(self.cs3, self.l3, self.s3)
        K_vehicle = Kv + np.transpose(Kv) - np.eye(4) * np.diag([Kv[0][0], Kv[1][1], Kv[2][2], Kv[3][3]])
        K_wheel = np.diag(
            np.concatenate((np.add(self.cs1, self.ct1), np.add(self.cs2, self.ct2), np.add(self.cs3, self.ct3)),
                           axis=None))
        Kgv = [[0 for i in range(self.nvy)] for j in range(self.nv)]
        Kgv[0][0:self.nvy1] = scare(self.cs1, -1)
        Kgv[0][self.nvy1:self.nvy1 + self.nvy2] = scare2(self.cs2, self.l2, -1 / self.s2)
        Kgv[0][self.nvy1 + self.nvy2:self.nvy] = scare2(self.cs3, self.l3, -self.r2 / self.s3 / self.s2)
        Kgv[1][0:self.nvy1] = scare2(self.cs1, self.l1, 1)
        Kgv[1][self.nvy1:self.nvy1 + self.nvy2] = scare2(self.cs2, self.l2, self.r1 / self.s2)
        Kgv[1][self.nvy1 + self.nvy2:self.nvy] = scare2(self.cs3, self.l3, self.r1 * self.r2 / self.s3 / self.s2)
        Kgv[2][self.nvy1:self.nvy1 + self.nvy2] = scare3(self.cs2, self.l2, self.s2, -1)
        Kgv[2][self.nvy1 + self.nvy2:self.nvy] = scare2(self.cs3, self.l3, (self.r2 / self.s2 - 1) / self.s3)
        Kgv[3][self.nvy1 + self.nvy2:self.nvy] = scare3(self.cs3, self.l3, self.s3, -1)
        KK = np.vstack([np.hstack([K_vehicle, Kgv]), np.hstack([np.transpose(Kgv), K_wheel])])
        return KK
    @property
    def Staticforce_vector(self):
        F1 = [5.664e3]
        F2 = [4.108e3]
        F3 = [4.108e3]
        F4 = [4.195e3]
        F5 = [4.195e3]
        F6 = [4.195e3]
        F7 = [4.416e3]
        F8 = [4.416e3]
        F9 = [4.416e3]
        F1 = [5.664e3]
        F2 = [7.714e3]#[4.108e3]
        F3 = [7.714e3]#[4.108e3]
        F4 = [6.479e3]#[4.195e3]
        F5 = [6.479e3]#[4.195e3]
        F6 = [6.479e3]#[4.195e3]
        F7 = [6.398e3]#[4.416e3]
        F8 = [6.397e3]#[4.416e3]
        F9 = [6.397e3]#[4.416e3]

        F_v=[F1,F2,F3,F4,F5,F6,F7,F8,F9]
        F_v=np.transpose(np.array(F_v))

        return F_v*9.81
def scare(k,s):
    return np.dot(k,np.diag([1,1,1])*s)
def scare2(k,l,s):
    kl=np.dot(k,np.diag(l))
    return np.dot(kl,np.diag([1,1,1])*s)
def scare3(k,l,s1,s2):
    ll=[1,1,1]-np.dot(l,np.diag([1,1,1])/s1)

    return scare(np.dot(k,np.diag(ll)),s2)
def sumkl(k,l):
    return np.dot(k,np.transpose(l))
def sumkl2(k,l):
    return np.dot(k,np.transpose(np.square(l)))
def sumkls(k,l,s):
    ll=[1,1,1]-np.dot(l,np.diag([1,1,1])/s)
    l2=np.dot(l,np.diag(ll))
    return np.dot(k,np.transpose(l2))/s
def sumkls2(k,l,s):
    ll=[1,1,1]-np.dot(l,np.diag([1,1,1])/s)
    l2=np.dot(ll,np.diag(ll))
    return np.dot(k,np.transpose(l2))
print(Bdouble_tractor.M)
