"""
Config Generator for VOIP Phones
Arnold Dechamps 2022
"""
from Scripts import c79407960
from Scripts import c79117906

def main():
    """
    This function is the main one. Makes selections to choose what plugin to use
    :return: 0
    """
    print("Hello, what phone system would you like to provision?")
    print(" * 1) Cisco 7940")
    print(" * 2) Cisco 7960")
    print(" * 3) Cisco 7911")
    print(" * 4) Cisco 7906")

    phone_choice = input("Choice : ")

    if phone_choice == "1" or phone_choice == "2":
        c79407960.main()

    elif phone_choice == "3" or phone_choice == "4":
        c79117906.main()

    else:
        print("Invalid option.")

    return 0

if __name__ == '__main__':
    main()