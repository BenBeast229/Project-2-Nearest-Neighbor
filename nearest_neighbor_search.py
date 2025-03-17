import pandas as pd

def nearest_neighbor_search(data): #base search algorithm to use within both forward selection and backward elimination
    # Implement nearest neighbor search logic here
    pass

def leave_one_out_cross_validation(data): #cross validation to test the accuracy of the algorithm
    #implement leave one out cross validation logic here
    pass

def forward_selection(data): #starts with an empty set of features and adds one feature at a time
    # Implement forward selection logic here
    pass

def backward_elimination(data): #starts with all features and removes one feature at a time
    # Implement backward elimination logic here
    pass

def main():
    # Main function to run the feature selection algorithm and allow user to choose options.
    print("Welcome to Benjamin Lim's Feature Selection Algorithm!")
    print("Please select the dataset you would like to use:")
    print("1. Small Dataset") #loads small dataset
    print("2. Large Dataset") #loads large dataset
    
    choice = input("Choose 1 for small dataset or 2 for large dataset.") #user input
    
    while choice != '1' or choice != '2': #checks if user input is valid
        if choice == '1':
            data = pd.read_csv('CS170_Small_Data__51.txt') #loads small dataset
        elif choice == '2':
            data = pd.read_csv('CS170_Large_Data__109.txt') #loads large dataset
        else:
            print("Invalid choice. Please select a valid option.")
            
    print("Choose an algorithm to use:")
    print("1. Forward Selection")
    print("2. Backward Elimination")
    
    choice = input("Choose 1 for Forward Selection or 2 for Backward Elimination.")
    
    while choice != '1' or choice != '2': #checks for algorithm selection
        if choice == '1':
            forward = forward_selection(data) #runs forward selection with selected dataset
        elif choice == '2':
            backward = backward_elimination(data) #runs backward elimination with selected dataset
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()