$setup = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    DEBIAN_FRONTEND=noninteractive sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >> /etc/apt/sources.list.d/postgresql.list'
    DEBIAN_FRONTEND=noninteractive apt-get update
SCRIPT

$dependencies = <<SCRIPT
    DEBIAN_FRONTEND=noninteractive apt-get -y install python-software-properties
    DEBIAN_FRONTEND=noninteractive apt-get install -y libpq-dev
    DEBIAN_FRONTEND=noninteractive apt-get install -y postgresql-9.3 postgresql-server-dev-9.3 postgresql-9.3-postgis-2.1 libpq-dev
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-dev libjpeg-dev zlib1g-dev
    DEBIAN_FRONTEND=noninteractive apt-get install -y python-virtualenv virtualenvwrapper
    DEBIAN_FRONTEND=noninteractive apt-get install binutils libproj-dev gdal-bin
    DEBIAN_FRONTEND=noninteractive apt-get install php5-cli php5-pgsql
SCRIPT

Vagrant.configure('2') do |config|

    config.vm.box = 'precise64'
    config.vm.box_url = "http://files.vagrantup.com/" + config.vm.box + ".box"
    config.vm.provision "shell", path: "provision.sh"

    config.ssh.forward_agent = true
    # Forward the dev server port
    config.vm.network :forwarded_port, host: 8000, guest: 8000
    config.vm.network :forwarded_port, host: 5433, guest: 5432

end
