# Changes ""phpp"" to ""php""

exec{ 'fixes_500_error':
  command => "sed -i s/phpp/php/g /var/www/html/wp-settings.php",
  path    => "/usr/local/bin/:/bin/"
}
