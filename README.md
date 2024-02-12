# palpi

Repository for my Palworld server infra and data

## PalWorld
> Palworld is an upcoming action-adventure, survival, and monster-taming game created and published by Japanese developer Pocket Pair. The game is set in an open world populated with animal-like creatures called "Pals", which players can battle and capture to use for base building, traversal, and combat.  
Source [Wikipedia](https://en.wikipedia.org/wiki/Palworld)

## Infra

### Hardware
Raspberry Pi 4B 8Go

### Install
#### Tools
```sh
sudo apt install python3-pip
sudo apt install python-is-python3
pip install RPi.GPIO
```

#### Docker

```sh
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo docker run hello-world
```

### Scripts
#### Fan control PWM

1. Ensuring the GPIO lib is isntalled : `pip freeze | grep RPi.GPIO`
1. Creating a systemd service file : `sudo nano /etc/systemd/system/pwm_fan_control.service`
1. Ajouter le contenu :
    ```ini
    [Unit]
    Description=My Python Script Service
    After=network.target

    [Service]
    User=palpi
    ExecStart=/usr/bin/python /home/palpi/palpi/scripts/pwm_fan_control.py
    WorkingDirectory=/home/palpi/palpi/scripts
    StandardOutput=null
    StandardError=null

    [Install]
    WantedBy=multi-user.target
    ```
1. Reloading systemctl : `sudo systemctl daemon-reload `
1. Enabling our service : `sudo systemctl enable pwm_fan_control.service`
1. Starting our service : `sudo systemctl start pwm_fan_control.service`
1. Checking our service : `sudo systemctl status pwm_fan_control.service`

TIPS :
- You can stress the CPU to increase the temp with `fulload() { dd if=/dev/zero of=/dev/null | dd if=/dev/zero of=/dev/null | dd if=/dev/zero of=/dev/null  | dd if=/dev/zero of=/dev/null & }; fulload; read; killall dd`
The more `| dd if=/dev/zero of=/dev/null ` the higher it will reach
- You can check the temp with `vcgencmd measure_temp|sed 's/[^0-9.]//g'`



## Data
### Migrate data from Xbox Game Pass (XGP) to Dedicated Server
