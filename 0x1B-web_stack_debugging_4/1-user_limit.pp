# Puppet file increases hard and soft limit for holberton user
exec { 'limit-for-hard-file-incresed':
  command => 'sed -i "/^holberton hard/s/5/4000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'limit-for-soft-file-increased':
  command => 'sed -i "/^holberton soft/s/4/3000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
