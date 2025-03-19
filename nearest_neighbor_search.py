import numpy as np
import time

#base search algorithm to use within both forward selection and backward elimination
def nearest_neighbor_search(data): 
    # Implement nearest neighbor search logic here
    pass

#cross validation to test the accuracy of the algorithm
def leave_one_out_cross_validation(data): 
    #implement leave one out cross validation logic here
    pass

#starts with an empty set of features and adds one feature at a time
def forward_selection(data): 
    current_set_of_features = [] #empty set of features
    
    #iterates through each level of the search tree
    for i in range(1, data.shape[1]):
        print("On the " + str(i) + "th level of the search tree")
        feature_to_add_at_this_level = None
        best_so_far_accuracy = 0
        
        #iterates through each feature
        for j in range(1, data.shape[1]):
            if j not in current_set_of_features:
                print("--Considering adding the " + str(j) + " feature")
                
                temp = current_set_of_features + [j] #creates a copy of the current set with the feature j
                accuracy = leave_one_out_cross_validation(data)
                
                #checks if accuracy is better than the best so far
                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_this_level = j
        
        if feature_to_add_at_this_level is not None:
            current_set_of_features.append(feature_to_add_at_this_level)  # Add the best feature to the current set
            print("On level " + str(i) + " I added feature " + str(feature_to_add_at_this_level) + " to the current set")
        else:
            print("No feature was added at level " + str(i))

#starts with all features and removes one feature at a time
def backward_elimination(data): 
    current_set_of_features = [list(range(1, data.shape[1]))] #full set of features
    
    #iterates through each level of the search tree
    for i in range(1, data.shape[1]):
        print("On the " + str(i) + "th level of the search tree")
        feature_to_remove_at_this_level = None
        best_so_far_accuracy = 0
        
        #iterates through each feature
        for j in range(1, data.shape[1]):
            if j in current_set_of_features:
                print("--Considering removing the " + str(j) + " feature")
                
                #Creates a copy of the current set without the feature j
                temp = current_set_of_features.copy()
                temp.remove(j)
                
                accuracy = leave_one_out_cross_validation(data)
                
                #checks if accuracy is better than the best so far
                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_remove_at_this_level = j
                    
        if feature_to_remove_at_this_level is not None:
            current_set_of_features.remove(feature_to_remove_at_this_level)  # Remove the best feature from the current set
            print("On level " + str(i) + " I removed feature " + str(feature_to_remove_at_this_level) + " from the current set")
        else:
            print("No feature was removed at level " + str(i))

# Main function to run the feature selection algorithm and allow user to choose options.
def main():
    print("Welcome to Benjamin Lim's Feature Selection Algorithm!")
    print("Please select the dataset you would like to use:")
    print("1. Small Dataset") #loads small dataset
    print("2. Large Dataset") #loads large dataset
    
    choice = input("Choose 1 for small dataset or 2 for large dataset.") #user input
    
    while choice != '1' or choice != '2': #checks if user input is valid
        if choice == '1':
            data = np.loadtxt('CS170_Small_Data__51.txt') #loads small dataset
        elif choice == '2':
            data = np.loadtxt('CS170_Large_Data__109.txt') #loads large dataset
        else:
            print("Invalid choice. Please select a valid option.")
            
    print("Choose an algorithm to use:")
    print("1. Forward Selection")
    print("2. Backward Elimination")
    
    choice = input("Choose 1 for Forward Selection or 2 for Backward Elimination.")
    
    while choice != '1' or choice != '2': #checks for algorithm selection
        if choice == '1':
            start_time = time.time() #starts timer
            forward = forward_selection(data) #runs forward selection with selected dataset
            end_time = time.time()
            print("Time taken: " + str(end_time - start_time) + " seconds")
        elif choice == '2':
            start_time = time.time() #starts timer
            backward = backward_elimination(data) #runs backward elimination with selected dataset
            end_time = time.time()
            print("Time taken: " + str(end_time - start_time) + " seconds")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()