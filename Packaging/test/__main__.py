# Import module function from module
from package.module import print_fn 
from package.subpackage.submodule import num_arr
# Call function
def main():
    print(print_fn())
    print(num_arr())
    
if __name__ == "__main__":
    main()
