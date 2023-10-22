airport_data = {}
while True:
    print("Airport Data Program")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Select an option (1/2/3): ")

    if choice == '1':
        icao_code = input("Enter the ICAO code of the airport: ")
        airport_name = input("Enter the name of the airport: ")
        airport_data[icao_code] = airport_name
        print("Airport data saved.")
    elif choice == '2':
        icao_code = input("Enter the ICAO code to fetch airport information: ")
        if icao_code in airport_data:
            print(f"The name of the airport with ICAO code {icao_code} is {airport_data[icao_code]}.")
        else:
            print(f"Airport with ICAO code {icao_code} not found.")
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")