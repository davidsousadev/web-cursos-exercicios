```sh
     python3 setup.py --command-packages=stdeb.command bdist_deb
     dpkg-deb -c deb_dist/python3-yourapp_0.1-1_all.deb
     sudo dpkg -i deb_dist/python3-yourapp_0.1-1_all.deb 

```