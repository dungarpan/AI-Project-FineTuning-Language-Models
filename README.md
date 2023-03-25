<h2> New York University Tandon School of Engineering <br> Computer Science and Engineering <br> CS-GY 6613 Project: FineTuning-Language-Models </h2>
<h4>Name: Arpan Chatterjee<br>Email: ac9839@nyu.edu<br>ID Number: N14082602</h4>
<hr>
<b>Docker Installation instructions for a Windows 11 machine:</b>


* Go to the website: https://www.docker.com/products/docker-desktop/


* Click on the button “Download Docker Desktop Windows” to download Docker Desktop on Windows.


* Double-click Docker Desktop Installer.exe to run the installer. When prompted, ensure the Use WSL 2 instead of Hyper-V option on the Configuration page is selected or not depending on your choice of backend.


* If your system only supports one of the two options, you will not be able to select which backend to use.


* Follow the instructions on the installation wizard to authorize the installer and proceed with the install.


* When the installation is successful, click Close to complete the installation process.


* If your admin account is different to your user account, you must add the user to the docker-users group. Run Computer Management as an administrator and navigate to Local Users and Groups > Groups > docker-users. Right-click to add the user to the group. Log out and log back in for the changes to take effect.


We now need to enable WSL 2 for Windows. Developers can access the power of both Windows and Linux at the same time on a Windows machine. The Windows Subsystem for Linux (WSL) lets developers install a Linux distribution (such as Ubuntu, OpenSUSE, Kali, Debian, Arch Linux, etc) and use Linux applications, utilities, and Bash command-line tools directly on Windows, unmodified, without the overhead of a traditional virtual machine or dual boot setup.

* Open PowerShell or Windows Command Prompt in administrator mode by right-clicking and selecting "Run as administrator" and type in the command:

* wsl --install

This command will enable the features necessary to run WSL and install the Ubuntu distribution of Linux.

