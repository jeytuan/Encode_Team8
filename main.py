import os

def run_script(script_path, args=None):
    """
    Function to run a given script with optional arguments.
    """
    command = f"python {script_path}"
    if args:
        command += " " + " ".join(args)
    os.system(command)

def main():
    print("Welcome to the AI Chef Collective!")
    
    # Map of script names or identifiers to their paths
    scripts = {
        "zGWyGM_jeytuan": "zGWyGM_jeytuan/speedboi.py",
        # Add other scripts here following the same pattern
        # "team_member": "directory/script.py"
    }

    while True:
        # Let the user choose which chef personality to interact with
        print("\nChoose a chef personality to interact with:")
        for key in scripts.keys():
            print(f"- {key}")

        choice = input("Enter your choice (or 'exit' to quit): ").strip()
        if choice.lower() == 'exit':
            break

        if choice in scripts:
            script_path = scripts[choice]
            dish = input("Type the name of the dish you want a recipe for:\n")
            run_script(script_path, [dish])
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
