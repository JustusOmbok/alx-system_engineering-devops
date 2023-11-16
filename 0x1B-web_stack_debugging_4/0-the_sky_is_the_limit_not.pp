# Changes the ULIMIT of the runing app
exec { 'fixes-nginx':
  # Changing ULIMIT value
  command => '/bin/sed -i "s/15/4000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

# Starting nginx
exec { 'nginx-is-started':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d/',
}
