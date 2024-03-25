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
        "q4IJUj_ppjd": "q4IJUj_ppjd/hipHopChefGPT.py",
        "DPY2vn_tben140": "DPY2vn_tben140/gordon.py",
        # Add other scripts here following the same pattern
        # "team_member": "directory/script.py"
    }

    # Convert scripts to a list of tuples for easy indexing
    scripts_list = list(scripts.items())

    while True:
        print("\nChoose a chef personality to interact with:")
        for index, (key, _) in enumerate(scripts_list, start=1):
            print(f"{index}. {key}")

        choice_input = input("Enter your choice number (or 'exit' to quit): ").strip()
        if choice_input.lower() == 'exit':
            break

        # Convert choice to integer and validate
        try:
            choice_index = int(choice_input) - 1  # Adjust for 0-based indexing
            if choice_index >= 0 and choice_index < len(scripts_list):
                script_key, script_path = scripts_list[choice_index]
                dish = input(f"Type the name of the dish you want a recipe for ({script_key}):\n")
                run_script(script_path, [dish])
            else:
                print("Invalid choice, please enter a number from the list.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()