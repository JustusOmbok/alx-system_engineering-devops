# Ensure Nginx pack is installed
# Ensure nginx service is running and enabled
# Ensure nginx is listening on port 80
# Create a custom index.html file
# Configure 301 redirect

exec { 'update system':
  command => '/usr/bin/apt-get update'
}

package { 'nginx':
  ensure => 'installed',
  require => Exec['update system']
}

file {'/var/www/html/index.html':
  content => 'Hello World!'
}

exec {'redirect_me':
  command => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

service {'nginx':
  ensure => running,
  require => Package['nginx']
}
