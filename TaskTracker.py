import argparse

def AddTask():
    pass

def UpdateTask():
    pass

def DeleteTask():
    pass

def ListTasks():
    print("I am here")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CLI Tool that helps track tasks"
    )

    # 2. Define expected command-line arguments
    # Positional argument (required)
    parser.add_argument(
        "list", 
        help="The name of the person to greet."
    )
    
     

    # 3. Parse the arguments provided by the user
    args = parser.parse_args()
    if args.list == "all":
        ListTasks()
    