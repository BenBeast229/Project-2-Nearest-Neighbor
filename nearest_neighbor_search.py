import numpy as np
import time

# Cross-validation to test the accuracy of the algorithm
def leave_one_out_cross_validation(data, current_set, feature_to_add): 
    number_correctly_classified = 0
    
    # Combine current set of features with the feature to add
    features_to_use = current_set + [feature_to_add]
    
    # Iterate through each row in the dataset
    for i in range(data.shape[0]):
        object_to_classify = data[i, features_to_use]  # Object to classify (selected features)
        label_object_to_classify = data[i, 0]  # Label of object to classify (assuming label is in the first column)
        
        nearest_neighbor_distance = float('inf')  # Initialize distance to infinity
        nearest_neighbor_location = -1  # Initialize location to an invalid index
        
        # Iterate through each other object in the dataset
        for j in range(data.shape[0]):
            if j != i:
                distance = np.linalg.norm(object_to_classify - data[j, features_to_use])
                
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = j
        
        nearest_neighbor_label = data[nearest_neighbor_location, 0]  # Label of the nearest neighbor
        
        if label_object_to_classify == nearest_neighbor_label:
            number_correctly_classified += 1
    
    accuracy = (number_correctly_classified / data.shape[0]) * 100
    return accuracy

# Starts with an empty set of features and adds one feature at a time
def forward_selection(data): 
    current_set_of_features = []  # Empty set of features
    best_overall_accuracy = 0
    best_feature_subset = []
    
    print(f"This dataset has {data.shape[1] - 1} features (not including the class attribute), with {data.shape[0]} instances.\n")
    
    full_feature_accuracy = leave_one_out_cross_validation(data, current_set_of_features, 1)
    print(f"Running nearest neighbor with all {data.shape[1] - 1} features, using “leaving-one-out” evaluation, I get an accuracy of {full_feature_accuracy:.1f}%\n")
    print("Beginning search.\n")
    
    # Iterate through each level of the search tree
    for i in range(1, data.shape[1]):
        feature_to_add_at_this_level = None
        best_so_far_accuracy = 0
        
        # Iterate through each feature
        for j in range(1, data.shape[1]):
            if j not in current_set_of_features:
                accuracy = leave_one_out_cross_validation(data, current_set_of_features, j)
                print(f"    Using feature(s) {current_set_of_features + [j]} accuracy is {accuracy:.1f}%")
                
                # Check if accuracy is better than the best so far
                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_this_level = j
                    
        if feature_to_add_at_this_level is not None:
            current_set_of_features.append(feature_to_add_at_this_level)  # Add the best feature to the current set
            print(f"\nFeature set {current_set_of_features} was best, accuracy is {best_so_far_accuracy:.1f}%\n")
            
            if best_so_far_accuracy > best_overall_accuracy:
                best_overall_accuracy = best_so_far_accuracy
                best_feature_subset = current_set_of_features.copy()
        
    print(f"Finished search! The best feature subset is {best_feature_subset}, which has an accuracy of {best_overall_accuracy:.1f}%")
        
# Starts with all features and removes one feature at a time
def backward_elimination(data): 
    current_set_of_features = list(range(1, data.shape[1]))  # Full set of features
    best_feature_subset = current_set_of_features.copy()
    best_overall_accuracy = 0
    
    print(f"This dataset has {data.shape[1] - 1} features (not including the class attribute), with {data.shape[0]} instances.\n")
    
    full_feature_accuracy = leave_one_out_cross_validation(data, current_set_of_features, 1)
    print(f"Running nearest neighbor with all {data.shape[1] - 1} features, using “leaving-one-out” evaluation, I get an accuracy of {full_feature_accuracy:.1f}%\n")
    print("Beginning search.\n")
    
    # Iterate through each level of the search tree
    for i in range(1, data.shape[1]):
        feature_to_remove_at_this_level = None
        best_so_far_accuracy = 0
        
        # Iterate through each feature
        for j in range(1, data.shape[1]):
            if j in current_set_of_features:
                # Create a copy of the current set of features and remove the feature to test
                current_set_of_features_copy = current_set_of_features.copy()
                current_set_of_features_copy.remove(j)
                
                accuracy = leave_one_out_cross_validation(data, current_set_of_features_copy, 0)
                print(f"    Using feature(s) {current_set_of_features_copy} accuracy is {accuracy:.1f}%")
                
                # Check if accuracy is better than the best so far
                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_remove_at_this_level = j
        
        if feature_to_remove_at_this_level is not None:
            current_set_of_features.remove(feature_to_remove_at_this_level)  # Remove the best feature from the current set
            print(f"\nFeature set {current_set_of_features} was best, accuracy is {best_so_far_accuracy:.1f}%\n")
            
            if best_so_far_accuracy > best_overall_accuracy:
                best_overall_accuracy = best_so_far_accuracy
                best_feature_subset = current_set_of_features
        
    print(f"Finished search! The best feature subset is {best_feature_subset}, which has an accuracy of {best_overall_accuracy:.1f}%")

# Main function to run the feature selection algorithm and allow user to choose options.
def main():
    print("Welcome to Benjamin Lim's Feature Selection Algorithm!")
    print("Please select the dataset you would like to use:")
    print("1. Small Dataset")  # loads small dataset
    print("2. Large Dataset")  # loads large dataset
    
    choice = input("\nChoose 1 for small dataset or 2 for large dataset: ")  # user input
    
    while choice != '1' and choice != '2':  # checks if user input is valid
        print("Invalid choice. Please select a valid option.")
        choice = input("\nChoose 1 for small dataset or 2 for large dataset: ")  # ask again if invalid
    
    if choice == '1':
        data = np.loadtxt('CS170_Small_Data__51.txt')  # loads small dataset
    elif choice == '2':
        data = np.loadtxt('CS170_Large_Data__109.txt')  # loads large dataset
    
    print("\nChoose an algorithm to use:")
    print("1. Forward Selection")
    print("2. Backward Elimination")
    
    choice = input("\nChoose 1 for Forward Selection or 2 for Backward Elimination: ")
    
    while choice != '1' and choice != '2':  # checks for algorithm selection
        print("Invalid choice. Please select a valid option.")
        choice = input("\nChoose 1 for Forward Selection or 2 for Backward Elimination: ")  # ask again if invalid
    
    start_time = time.time()  # Start timer
    
    if choice == '1':
        forward_selection(data)  # runs forward selection with selected dataset
    elif choice == '2':
        backward_elimination(data)  # runs backward elimination with selected dataset
    
    end_time = time.time()  # End timer
    elapsed_time = end_time - start_time  # Calculate time taken
    
    # Convert time taken to hours, minutes, and seconds
    hours, rem = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(rem, 60)
    print(f"Algorithm took {int(hours):02}:{int(minutes):02}:{int(seconds):2f} to complete.")  # Print time taken

if __name__ == "__main__":
    main()