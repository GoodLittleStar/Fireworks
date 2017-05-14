#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 13 09:25:40 2017
Tan Y, Zhu Y. Fireworks algorithm for optimization[C]// 
International Conference on Advances in Swarm Intelligence. Springer-Verlag, 2010:355-364.
@author: star
"""

from FireWork import FireWork
import copy
import random

class Population:
    """
    population
    """
    epsino=1e-30
    
    def __init__(self,PopSize,m_para,a_para,b_para,A_para,mm_para,RealBound,InitBound,vardim,FunName):
        self.m=m_para
        self.a=a_para
        self.b=b_para
        self.A=A_para
        self.mm=mm_para
        self.RealBound=RealBound
        self.InitBound=InitBound
        self.popsize=PopSize
        self.vardim=vardim
        self.pop=[]
        self.MaxFitness=0.
        self.MinFitness=0.
        self.FunName=FunName
        
    def inilitialize(self):
        for i in range(0,self.popsize):
            ind=FireWork(self.vardim,self.InitBound)
            ind.initialize()
            ind.evaluate(self.FunName)
            self.pop.append(ind)
            
    def UpdateMaxFintess(self):
        self.MaxFitness=self.pop[0].fitness
        for i in range(1,self.popsize):
            if self.MaxFitness<self.pop[i].fitness:
                self.MaxFitness=self.pop[i].fitness
    def UpdateMinFitness(self):
        self.MinFitness=self.pop[0].fitness
        for i in range(1,self.popsize):
            if self.MinFitness>self.pop[i].fitness:
                self.MinFitness=self.pop[i].fitness
    def CalculateSi(self):
        """
        Refer to equation (3)
        """
        self.UpdateMaxFintess()
        temp=0.
        for i in range(0,self.popsize):
            temp=temp+self.MaxFitness-self.pop[i].fitness
        for i in range(0,self.popsize):
            self.pop[i].si=self.m*(self.MaxFitness-self.pop[i].fitness+self.epsino)/(temp+self.epsino)
            if self.pop[i].si<self.a*self.m:
                self.pop[i].si=round(self.a*self.m)
            elif self.pop[i].si>self.b*self.m:
                self.pop[i].si=round(self.b*self.m)
            else:
                self.pop[i].si=round(self.pop[i].si)
    def CalculateExpo(self):
        """
        Refer to equation (4)
        """
        self.UpdateMinFitness()
        temp=0.
        for i in range(0,self.popsize):
            temp=temp+self.pop[i].fitness-self.MinFitness
        for i in range(0,self.popsize):
            self.pop[i].Ai=self.A*(self.pop[i].fitness-self.MinFitness+self.epsino)/(temp+self.epsino)
    
    def Explosion(self):
        """
        Refer to Algorithm 1 in the orginal paper
        """
        for k in range(0,self.popsize):
            newpop=[]
            for i in range(0,self.pop[k].si):
                spark=copy.deepcopy(self.pop[k])
                z=round(self.vardim*random.uniform(0,1))
                dim_list=range(self.vardim)
                rand_z=random.sample(dim_list,z)
                h=self.pop[k].Ai*random.uniform(-1,1)
                for j in rand_z:
                    spark.location[j]+=h
                    if spark.location[j]<self.RealBound[0] or spark.location[j]>self.RealBound[1]:
                        spark.location[j]=self.RealBound[0]+abs(spark.location[j])%(self.RealBound[1]-self.RealBound[0])
                spark.evaluate(self.FunName)
                newpop.append(spark)
            self.pop+=newpop
        
    def Mutation(self):
        """
        Refer to Algorithm 2 in the orginal paper
        """
        newpop=[]
        currentsize=len(self.pop)
        for k in range(0,self.mm):
            randindex=random.randint(0,currentsize-1)
            spark=copy.deepcopy(self.pop[randindex])
            z=round(self.vardim*random.uniform(0,1))
            dim_list=range(self.vardim)
            rand_z=random.sample(dim_list,z)
            g=random.gauss(1,1)
            for j in rand_z:
                spark.location[j]*=g
                if spark.location[j]<self.RealBound[0] or spark.location[j]>self.RealBound[1]:
                        spark.location[j]=self.RealBound[0]+abs(spark.location[j])%(self.RealBound[1]-self.RealBound[0])
            spark.evaluate(self.FunName)
            newpop.append(spark)
        self.pop+=newpop
            
    def FindBest(self):
        index=0
        currentsize=len(self.pop)
        for i in range(1,currentsize):
            if self.pop[i].fitness<self.pop[index].fitness:
                index=i
        return index
    
    def Selection(self):
        newpop=[]
        newpop.append(self.best)
        for i in range(0,len(self.pop)):
            dis=0.
            for j in range(0,len(self.pop)):
                dis+=self.pop[i].distance(self.pop[j])
            self.pop[i].Ri=dis
        sr=0.
        for i in range(0,len(self.pop)):
            sr+=self.pop[i].Ri
        px=[]
        sum1=0.
        for i in range(0,len(self.pop)):
            sum1+=self.pop[i].Ri/sr
            px.append(sum1)
        for i in range(0,self.popsize):
            rr=random.uniform(0,1)
            index=0;
            for j in range(0,len(self.pop)):
                if j==0 and rr<px[j]:
                    index=j
                elif rr>=px[j] and rr<px[j+1]:
                    index=j+1
            newpop.append(self.pop[index])
        self.pop=newpop

    def Run(self,MaxEva):
        self.inilitialize()
        bestindex=0
        self.best=copy.deepcopy(self.pop[bestindex])
        
        while FireWork.EvaNum<MaxEva:
            self.CalculateSi()
            self.CalculateExpo()
            self.Explosion()
            self.Mutation()
            bestindex=self.FindBest()
            if self.best.fitness>self.pop[bestindex].fitness:
                self.best=copy.deepcopy(self.pop[bestindex])
            self.Selection()
            print("Current pop size is %d Evaluation time is %d best fitness is %f"%(len(self.pop),FireWork.EvaNum,self.best.fitness))
            if self.best.fitness<self.epsino:
                break
            
        print("Best fitness %f"%self.best.fitness)
        print(self.best.location)
    
        

if __name__=="__main__":
    realbound=[-100.,100.]
    initbound=[30.,50.]
    func="F9"
    n=5
    m=50
    a=0.04
    b=0.8
    A_=40
    m_=5
    vardim=30
    maxeva=10000
    FAW=Population(n,m,a,b,A_,m_,realbound,initbound,vardim,func)
    FAW.Run(maxeva)
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        