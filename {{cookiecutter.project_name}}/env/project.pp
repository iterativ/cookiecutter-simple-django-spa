# packages install
class { 'djserver':
}

# install PostgreSQL
class { 'postgresql':
}

# setup backup for PostgreSQL
backup::postgres_backup { 'postgres_backup':
    require => Class['postgresql']
}

# install rabbit mq and delete guest user
package { 'rabbitmq-server':
    ensure => installed
}

# base dependencies
$base_libs = ['libjpeg62', 'libjpeg62-dev', 'libfreetype6', 'libfreetype6-dev', 'libpcre3-dev', 'zlib1g-dev',
    'libxml2', 'libxml2-dev', 'libssl-dev']
$geo_libs = ['geoip-bin', 'libgeos-dev']

# django server dependencies
package { $base_libs:
    ensure  => installed,
    require => Class['djserver']
}

package { $geo_libs:
    ensure  => latest,
    require => Class['djserver']
}
