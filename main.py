# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from opcua import Server
import lief
from joblib import Memory


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    binary = lief.parse("C:\\Windows\\explorer.exe")

    # Define a location to store cache
    location = '~/Desktop/temp/cache_dir'
    memory = Memory(location, verbose=0)

    server = Server()
    server.set_endpoint("opc.tcp://127.0.0.1:12345")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
