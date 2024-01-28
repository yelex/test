# class SingletonClass(object):
#   def __new__(cls):
#     if not hasattr(cls, 'instance'):
#       cls.instance = super(SingletonClass, cls).__new__(cls)
#     return cls.instance
   
# class SingletonChild(SingletonClass):
#     def __init__(self) -> None:
#     #    super().__init__()
#        self.is_tor = False
#     pass
   
# singleton = SingletonClass()  
# child = SingletonChild()
# print(child is singleton)
 
# singleton.is_tor = True
# print(child.is_tor)
from globals.global_state import Global


print('Global is_vprok_tor:', Global().is_tor_vprok)
global_ = Global()
global_.is_tor_vprok = True
print('Global().is_tor_vprok: ', global_.is_tor_vprok)