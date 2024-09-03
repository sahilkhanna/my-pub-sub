from . import module

print("Called from __init__.py")

class Project:
    def main(self):
        print(f'this is main {self}')
        b = module.Bar()
        print(f'this is bar {b}')
        
        pass