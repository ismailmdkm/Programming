from decimal import DivisionByZero
print("*"*70)
file_name = input("Enter file to open: ")
dividend = 25
divisor = input("Enter divisor: ")
try:
    f = open(file_name)
    result = dividend/int(divisor)
    if f.name == "corrupt_file.txt":
        f.close()
        raise Exception('It is a corrupt file')
except FileNotFoundError as e:
    print('Error:', e)
except (TypeError, DivisionByZero) as e:
    print("Error: ", e)
except Exception as e:
    print("Error: ", e)
except:
    print("Sorry, something went wrong")
else:
    print(f.read())
    f.close()
    print(result)
finally:
    print("Executing Finally...")
print("Am outside exception")
