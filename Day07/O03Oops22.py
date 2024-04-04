
from abc import ABC, abstractmethod

class Employee(ABC):

    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Manager's Job......")

class Developer(Employee):

    def doJob(self):
        print("Developers Job......")

def Bankjob(emp):
    print("Bank job started......")
    emp.doJob()
    print("Bank job completed......")
    print("-" * 60)

Micheal = Manager()
David = Developer()

Bankjob(Micheal)        # manager's job
Bankjob(David)          # developer's job

