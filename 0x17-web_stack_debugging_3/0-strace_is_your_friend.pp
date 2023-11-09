exec { 'fixes_500_error':
  command => "/bin/sed -i 's/\\.phpp/\\.php/g' /var/www/html/wp-settings.php",
  path    => ["/bin"],
  onlyif  => "/bin/test -f /var/www/html/wp-settings.php",
}
