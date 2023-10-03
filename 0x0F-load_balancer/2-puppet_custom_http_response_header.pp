# Updates packages repos
# Installs Nginx
# Allows nginx through firewall
# Creates custom http response header
# Creates html; file
# Reloads and restarts nginx

exec { 'apt-update':
  command => 'apt-get update',
  path    => '/usr/bin',
  user    => 'root',
  notify  => Service['nginx'],
}

package { 'nginx':
  ensure => 'installed',
  require => Exec['apt-update'],
}

class { 'ufw':
  enable => true,
}

ufw::allow { 'Nginx HTTP':
  port    => 80,
  proto   => 'tcp',
  comment => 'Allow Nginx HTTP',
  require => 'Class['ufw'],
}

file { '/etc/nginx/conf.d/custom_http_header.conf':
  ensure   => 'present',
  content  => 'location / {\n add_header X-Served-By $hostname;\n}\n",
  require  => Package['nginx'],
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'present',
  content => 'Hello World!',
  require => Package['nginx'],
}

service { 'nginx':
  ensure     => 'running',
  enable     => true,
  require    => [File['/etc/nginx/conf.d/custom_http_header.conf'], File['/var/www/html/index.nginx-debian.html']],
  subscribe  => Exec['apt-update'],
}
