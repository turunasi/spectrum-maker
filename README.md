# Usege
## 1. Clone source code
```sh
bash-3.2$ pwd
/Users/<USER NAME>
bash-3.2$ git clone https://github.com/turunasi/spectrum-maker.git
```
## 2. Create a container using docker-compose
```sh
bash-3.2$ cd spectrum-maker
bash-3.2$ docker-compose up -d
```
## 3. Edit python file
```sh
bash-3.2$ cd src
bash-3.2$ vim spectrum.py
```
## 4. Enter the container
```sh
bash-3.2$ cd ..
bash-3.2$ docker-compose exec python bash
```
## 5. Execute python file
```sh
root@32c33db47066:/src# python spectrum.py
```
## 6. Confirm animation.gif
```sh
root@32c33db47066:/src# exit
bash-3.2$ cd src
bash-3.2$ ls
animation.gif requirements.txt spectrum.py
```
## 7. Delete the container
```sh
bash-3.2$ cd ..
bash-3.2$ docker-compose down -v
Stopping reiwaseda_python_1 ... done
Removing reiwaseda_python_1 ... done
Removing network reiwaseda_default
bash-3.2$ docker-compose ps
Name   Command   State   Ports
------------------------------
```
# Output
![animation.gif](src/animation.gif)
