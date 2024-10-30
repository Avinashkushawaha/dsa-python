
def calculate_good_name_distance(name, good_string):
    total_distance = 0
    last_good_letter = good_string[0]  # Initially, the first letter of good string
    
    for char in name:
        if char in good_string:
            # No change needed if the character is already a good letter
            last_good_letter = char  # Update the last good letter used
            continue
        
        # If the character is not in the good string, find the nearest good letter
        nearest_good_letter = None
        min_distance = float('inf')
        
        for good_char in good_string:
            # Calculate distance from char to good_char
            distance = abs(ord(char) - ord(good_char))
            if distance < min_distance:
                min_distance = distance
                nearest_good_letter = good_char
            elif distance == min_distance:
                # If distances are equal, choose based on previous good letter
                prev_distance = abs(ord(last_good_letter) - ord(good_char))
                if nearest_good_letter is not None:
                    current_prev_distance = abs(ord(last_good_letter) - ord(nearest_good_letter))
                    if prev_distance < current_prev_distance:
                        nearest_good_letter = good_char
        
        # Update total distance and last good letter used
        total_distance += min_distance
        last_good_letter = nearest_good_letter
    
    return total_distance

# Example usage
name = "student"
good_string = "aeiou"  # Example good string with vowels
total_distance = calculate_good_name_distance(name, good_string)
print("Total distance for the name:", total_distance)
