from os import system, path
from sys import argv, argc

if argc > 1:
    argument = argv[1]
    if argument == "install":
        package_dir = argv[2]
        if path.isfile(f"{package_dir}/install.sh"):
            system(f"cp {package_dir} /usr/share/redline_ism/{package_dir}")
            system(f"sudo sh {package_dir}/install.sh")
    elif argument == "remove":
        if(input(f"Remove {package_name}? y/n").lower == "y"):
            package_name = argv[2]
            if path.isfile(f"/usr/share/redline_ism/{package_name}/remove.sh"):
                system(f"sudo sh /usr/share/redline_ism/{package_name}/remove.sh")
else:
    print("Usage:\nism install <package_folder>: install package from downloaded folder")