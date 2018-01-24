def right_justify(s):
    total_length = 70
    current_length = len(s)
    current_string = s
    while current_length < total_length:
       current_string = " " + current_string
       current_length = len(current_string)
    print(current_string)
