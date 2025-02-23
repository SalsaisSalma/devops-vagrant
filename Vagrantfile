# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "debian/bookworm64"


  # Port Forwarding 
  config.vm.network "forwarded_port", guest: 5000, host: 8080
  
  config.vm.provision "file", source: "hello.py", \
    destination: "~/hello.py"
  
  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt update -y
    sudp apt upgrade -y

    sudo apt install git nano vim python-is-python3 python3-venv python3-pip -y
    python -m venv flask_venv
    source flask_venv/bin/activate
    pip install Flask

  SHELL


  # config.vm.provision "shell", inline: <<-SHELL
  #   source flask_venv/bin/activate
  #   flask --app hello run --host=0.0.0.0
  # SHELL

end
