try:
    arr=[1]
    l_3= arr[3]
    result = 10/2
except ZeroDivisionError as e:
    print("Number cannot be dived by Zero")
except Exception as e:
    print("Catches all errors",e)
else:
    print("Only runs if there is no error in try block.")
finally:
    print("Runs every time whether error occurs or not.")
