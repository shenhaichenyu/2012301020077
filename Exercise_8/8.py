#basic packges needed
#matplotlib - for plot 2D lines
#numpy - for math 
import matplotlib.pyplot as plt
import numpy as np
# class EULER
# use EULER METHOD to solve the pendulum
# para. & var.  :    
# intial value 
class EULER(object):
    #def __init__(self, _theta0=10., _omg0=0, _t0=0., _l=9.8/(4*(np.pi)**2),_g=9.8, _dt=0.01, _time=4.):
       # self.theta, self.omg, self.t = [_theta0], [_omg0], [_t0]
       # self.l, self.g, self.dt, self.time, self.n= _l, _g, _dt, _time, int(_time/_dt)
       # self.E = [0.5*((self.l*_omg0)**2+self.g*se
    def __init__(self,_t0=0.,_dt=0.01,_time=15.,_x0=1.,_v0=0):
        self.x,self.t,self.v=[_x0],[_t0],[_v0]
        self.dt=_dt
        self.n=int(_time/_dt)
    def calculate(self):
        for i in range(self.n):
            self.v.append(self.v[-1]-self.x[-1]*self.dt)
            self.x.append(self.x[-1]+self.v[-2]*self.dt)
            self.t.append(self.t[-1]+self.dt)
            #self.E.append(0.5*((self.l*self.omg[-1])**2+self.g*self.l*(self.theta[-1])**2))
    def plot_x(self,_ax):
        _ax.plot(self.t, self.x, '--',label='Euler Method')
    #def plot_E(self,_ax):
       #_ax.plot(self.t,self.E,'--',label='Euler Method')
# class CROMER
# use EULER-CROMER METHOD to solve the pendulum
# para. & var.  :    
#initial value        
class CROMER(EULER):
    def calculate(self):
        for i in range(self.n):
            self.v.append(self.v[-1]-self.x[-1]*self.dt)
            self.x.append(self.x[-1]+self.v[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
            #self.E.append(0.5*((self.l*self.omg[-1])**2+self.g*self.l*(self.theta[-1])**2))
    def plot_x(self,_ax):
        _ax.plot(self.t, self.x, '--',label='Euler-Cromer Method')
    #def plot_E(self,_ax):
        #_ax.plot(self.t,self.E,'--',label='Euler-Cromer Method')
#class RUNGE_RUNGE_22
# use 2nd Runge-Kutta Method to solve the pendulum
# para. & var.  :
#initial value
class RUNGE_RUNGE_22(EULER):
    def calculate(self):
        for i in range(self.n):
            self.t2=self.t[-1]+self.dt/2
            self.v2=self.v[-1]-self.x[-1]*self.dt/2
            self.x2=self.x[-1]+self.v2*self.dt
            self.t.append(self.t[-1]+self.dt)
            self.v.append(self.v[-1]-self.x2*self.dt)
            self.x.append(self.x[-1]+self.v[-1]*self.dt)
    def plot_x(self,_ax):
        _ax.plot(self.t, self.x, '--',label='2-Runge-Kutta Method')
    #def plot_E(self,_ax):
       #_ax.plot(self.t,self.E,'--',label='2nd-order Runge-Kutta')
# class RUNGE_RUNGE_44
# use 4th Runge-Kutta Method to solve the pendulum
# para. & var.  :
#initial value
class RUNGE_RUNGE_44(EULER):
    def calculate(self):
        for i in range(self.n):
            self.t1,self.t2,self.t3,self.t4=self.t[-1],self.t[-1]+self.dt/2.,self.t[-1]+self.dt/2.,self.t[-1]+self.dt
            self.v1=self.v[-1]
            self.x1=self.x[-1]+self.v1*self.dt
            self.v2=self.v1-self.x1*self.dt/2
            self.x2=self.x[-1]+self.v2*self.dt
            self.v3=self.v1-self.x2*self.dt/2
            self.x3=self.x[-1]+self.v3*self.dt
            self.v4=self.v1-self.x3*self.dt/2
            self.x4=self.x[-1]+self.v4*self.dt
            self.t.append(self.t[-1]+self.dt)
            self.v.append(self.v[-1]+1./6.*(-self.x1-2.*self.x2-2.*self.x3-self.x4)*self.dt)
            self.x.append(self.x[-1]+self.v[-1]*self.dt)
    def plot_x(self,_ax):
     _ax.plot(self.t, self.x, '--',label='4-Runge-Kutta Method')
 # self.E.append(0.5*((self.l*self.omg[-1])**2+self.g*self.l*(self.theta[-1])**2))
   # def plot_E(self,_ax):
       # _ax.plot(self.t,self.E,'--',label='4th-order Runge-Kutta')       
# plot :
#        ax1 - time dependence of angel
#        ax2 - time dependence of energy
# both EULER & EULER CROMER METHOD &RUNGE_KUTTA are used
fig= plt.figure(figsize=(14,7))
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)
comp= EULER()
comp.calculate()
comp.plot_x(ax1)
comp= CROMER()
comp.calculate()
comp.plot_x(ax1)
comp=RUNGE_RUNGE_22()
comp.calculate()
comp.plot_x(ax2)
comp=RUNGE_RUNGE_44()
comp.calculate()
comp.plot_x(ax2)
t=np.linspace(0,15,30)
x=np.cos(t)
ax1.plot(t,x,'--',label='Analysis')
ax2.plot(t,x,'--',label='Analysis')
#ax2.text(0.5,350,'Period:  '+r'$ \tau $'+' = 1s',fontsize=14)
ax1.set_title('the different result between different method ',fontsize=14)
ax2.set_title('the different result between different method ',fontsize=14)
ax1.set_xlabel('time/t',fontsize=14)
ax1.set_ylabel('displacement',fontsize=14)
ax2.set_xlabel('time/t',fontsize=14)
ax2.set_ylabel('displacement',fontsize=14)
ax1.legend(fontsize=12,loc='best')
ax2.legend(fontsize=12,loc='best')
plt.show(fig)
