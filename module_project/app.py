from module_project.subpackage1 import foo1
from module_project.subpackage2 import foo2
from module_project.subpackage1.subpackage11 import foo11

def main():
    foo1.foo1_print()
    foo2.foo2_print()
    foo11.foo11_print()

if(__name__ == '__main__'):
    main()