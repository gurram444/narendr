def range_function(intial_value,end_value,step_value):

    while end_value > intial_value:
        print(intial_value)
        intial_value += step_value
        if  intial_value > end_value:
            break

range_function(1,20,2)
