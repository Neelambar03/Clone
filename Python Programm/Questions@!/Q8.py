# 8.write a Python program that sleeps for 20 seconds and allows the user to edit the file during that time. After 20 seconds, it should read the file and print its content.

import time

# Module definition
def sleep_for_20_seconds():
    print("The program will sleep for 20 seconds. You can edit the file during this time.")
    time.sleep(20)
    print("20 seconds are over. Checking for changes in the file...")

# Main program
if __name__ == "__main__":
    sleep_for_20_seconds()
    try:
        with open(__file__, 'r') as file:
            content = file.read()
            print("\nUpdated content of the file:")
            print(content)
    except Exception as e:
        print(f"Error reading the file: {e}")