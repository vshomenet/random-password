**Generate random password for users in system Linux on based "Google Authenticator"**

This program creates a user in the system, creates a home directory for him and automatically changes his password every 30 seconds.

**Build**
> git clone https://github.com/vshomenet/random-password.git \
> cd random-password\
> ./build.sh 

After building in the "build" directory, you will have an executable file and deb-package.

**How to use**
> **rpass -h** \
>_Show help_ \
> **rpass -a my_name** \
> _Add a user "my_name" to the system, create a password, create home directory /home/my_name and create a QR code_ \
> **rpass -d my_name** \
> _Delete a user "my_name" from system and delete home directory /home/my_name_ \
> **rpass -c my_name** \
> _Change algorithm generate password for user "my_name" and generate new QR-code_ 

**Install from repository**
> **Add repository keys** \
>_wget -O - http://repository.vshome.net/debian/keyFile | apt-key add -_ \
> **Add repository in sources.list** \
>_echo "deb http://repository.vshome.net/debian/ osrelease main" >> /etc/apt/sources.list_ \
> **Install** \
> _apt-get update && apt-get install rpass_

**NOTE**
1. Make sure the time is synchronized on your computer and device where Google Authenticator is installed
2. Do not set the root password if you do not have physical access to the computer

