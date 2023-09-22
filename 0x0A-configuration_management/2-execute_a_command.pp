#Puppet manifest to kill process 'killmenow'
exec { 'pkill':
  command     => 'pkill -f killmenow',
  provider        => 'shell',
  }
