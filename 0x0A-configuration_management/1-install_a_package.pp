#Puppet manifest to install Flask through pip3
package { 'Flask':
ensure => '2.1.0',
provider => 'pip3',
}
