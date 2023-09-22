#Puppet manifest to kill process 'killmenow'
exec { 'killmenow':
  command     => 'pkill killmenow',
  provider    => 'shell',
  creates     => '/killmenow',
  path        => '/usr/bin',
  }
