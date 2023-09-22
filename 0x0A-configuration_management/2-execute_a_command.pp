#Puppet manifest to kill process 'killmenow'
exec { 'killmenow':
  command     => 'pkill -f "killmenow"',
  path        => '/usr/bin',
  }
