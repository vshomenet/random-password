#! /bin/bash
echo "Start update and install python..."
apt-get update -y && apt-get install -y python python-pip python3 python3-pip
echo "Start install libraries..."
python3 -m pip install -U pip
python3 -m pip install -U setuptools
pip install pyinstaller
pip install configparser
pip install argparse
pip install qrcode[pil]
echo "Start builds bin-file..."
mkdir ./build
cd ./Scripts
pyinstaller -D -F -n rpass -c "rpass.py"
cd ..
mkdir ./rpass/sbin
cp ./Scripts/dist/rpass ./rpass/sbin
cp ./Scripts/dist/rpass ./build
echo "Start builds deb package"
chmod 0755 ./rpass/DEBIAN/preinst
chmod 0755 ./rpass/DEBIAN/prerm
chmod 0755 ./rpass/DEBIAN/postinst
chmod 0755 ./rpass/DEBIAN/postrm
dpkg-deb --build rpass
cp rpass.deb ./build/
echo "Clean..."
rm -rf ./Scripts/__pycache__
rm -rf ./Scripts/build
rm -rf ./Scripts/dist
rm ./Scripts/rpass.spec
rm -rf ./rpass/sbin
rm rpass.deb
echo "Finish"
