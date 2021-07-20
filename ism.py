from os import system, path
from sys import argv, argc

def install(package_dir: str):
    system(f"cp {package_dir} /usr/share/redline_ism/{package_dir}")
    system(f"sudo sh {package_dir}/install.sh")

if argc > 1:
    argument = argv[1]

    if argument == "install":
        if path.isfile(f"{argv[2]}/install.sh"):
            if(input(f"Install {argv[2]} systemwide? y/n").lower == "y"):
                install(argv[2])
        
    elif argument == "remove":
        if(input(f"Remove {package_name}? y/n").lower == "y"):
            package_name = argv[2]
            if path.isfile(f"/usr/share/redline_ism/{package_name}/remove.sh"):
                system(f"sudo sh /usr/share/redline_ism/{package_name}/remove.sh")
    elif argument == "full-remove":

else:
    print("Usage:\nism install <package_folder>: install package from downloaded folder")