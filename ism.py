from os import system, path
from sys import argv, argc

def install(package_dir: str):
    system(f"cp {package_dir} /usr/share/redline_ism/{package_dir}")
    system(f"sudo sh {package_dir}/install.sh")

def remove(package_name: str):
    system(f"sudo sh /usr/share/redline_ism/{package_name}/remove.sh")
    if path.isfile(f"/usr/share/redline_ism/{package_name}/full-remove.sh"):
        system(f"sudo cp /usr/share/redline_ism/{package_name}/full-remove.sh /usr/share/redline_ism/full-remove-scripts/{package_name}-full-remove.sh")
    system(f"sudo rm -rf /usr/share/redline_ism/{package_name}")

def full_remove(package_name: str):
    remove(package_name)
    system(f"sudo sh /usr/share/full_remove_scripts/{package_name}-full-remove.sh")
    system(f"sudo rm -rf /usr/share/full_remove_scripts/{package_name}-full-remove.sh")

def user_install(package_dir: str):
    system(f"cp {package_dir} ~/.local/share/redline_ism/{package_dir}")
    system(f"sh {package_dir}/user-install.sh")


def user_remove(package_dir: str):
    ... # TODO


if argc > 1:
    argument = argv[1]

    if argument == "install":
        if path.isfile(f"{argv[2]}/install.sh"):
            if(input(f"Install {argv[2]} systemwide? (root needed) y/n").lower == "y"):
                install(argv[2])
        elif path.isfile(f"{argv[2]}/user-install.sh"):
            if(input(f"No systemwide install script available. Install {argv[2]} for this user only? y/n").lower == "y"):
                user_install(argv[2])
        else:
            print("No installation script found.")

    elif argument == "user-install":
        if path.isfile(f"{argv[2]}/user-install.sh"):
            if(input(f"Install {argv[2]} for this user only? y/n").lower == "y"):
                user_install(argv[2])
        elif path.isfile(f"{argv[2]}/install.sh"):
            if(input(f"No local installation script available. Install {argv[2]} systemwide (root needed)? y/n").lower == "y"):
                install(argv[2])


        
    elif argument == "remove":
            if path.isfile(f"/usr/share/redline_ism/{argv[2]}/remove.sh"):
                if(input(f"Remove {argv[2]}? y/n").lower == "y"):
                    remove(argv[2])

            else:
                print("No removal script found.")

    elif argument == "full-remove":
        if path.isfile(f"/usr/share/redline_ism/{argv[2]}/remove.sh"):
            if path.isfile(f"/usr/share/redline_ism/{argv[2]}/full-remove.sh"):
                if(input(f"Fully remove {argv[2]}? (root needed) y/n").lower == "y"):
                    full_remove(argv[2])
            else:
                if(input(f"No full removal script available. Remove {argv[2]}? (root needed) y/n").lower == "y"):
                    remove(argv[2])

    else:
        print("Invalid argument")

else:
    print("Usage:\nism install <package_folder>: install package from downloaded folder\nism remove <package_name>: remove installed package\nism full-remove <package_name>: fully remove installed package and its configuration files")