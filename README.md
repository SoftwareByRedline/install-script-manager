# install-script-manager UNDER DEVELOPMENT! NOT WORKING YET!
Install script manager for GNU/Linux. Mostly proof of concept until developers start to release compatible packages.
Write standalone install and remove scripts that can be easily managed with this simple program. Release for any distribution through this system.

## Manage scripts
It works like a package manager on the surface.
### Install programs
Download the compatible archive (I propose the `.ism.tar.gz` extension) from the Internet and extract it.

From the extracted folder's parent directory run:

`sudo ism install package` (replace `package` with the extracted folder's name, that is the package name)

Some programs might support user-only installation:

`sudo ism user-install package`
### Remove programs:
From anywhere run:

`sudo ism remove package` (replace `package` with the package name)

To fully remove with configuration files:

`sudo ism full-remove package`

If you installed for a user only:

`sudo ism user-remove package`

There is no user-full-remove option yet.
## Create packages
Create an archive with the following contents:
- Program files
- `install.sh` (optional if you have `user-install.sh`) - shell script to install your program globally (will be run as root)
- `remove.sh`- (if you have `install.sh`) shell script to remove the globally installed program (will be run as root)
- `user-install.sh` (optional if you have `install.sh`) - shell script to install your program for the active user only (will not be run as root)
- `user-remove.sh` (if you have `user-install.sh`) - shell script to remove the user-only installed program (will not be run as root)
- `full-remove.sh` (only if you have `install.sh`, optional) - shell script to remove the globally installed program and its configuration files (will be run as root)

Name the archive with the extension `.ism.tar.gz`.
