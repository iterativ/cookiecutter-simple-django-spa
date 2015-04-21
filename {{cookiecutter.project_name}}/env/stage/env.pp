class { 'postgresql':
}

postgresql::role { "{{ cookiecutter.project_name }}_stage":
    ensure    => present,
    password  => "pw_postgresql_{{ cookiecutter.project_name }}_f67GFu2kwmreLgNw",
    require   => Class["postgresql"]
}

postgresql::database { "{{ cookiecutter.project_name }}_stage":
    ensure  => present,
    owner   => "{{ cookiecutter.project_name }}_stage",
    require => Postgresql::Role["{{ cookiecutter.project_name }}_stage"]
}

class { 'rabbitmq':
}

rabbitmq::vhost { '{{ cookiecutter.project_name }}_stage_vhost':
    ensure => present,
}

rabbitmq::user { '{{ cookiecutter.project_name }}_stage':
    ensure   => present,
    password => "pw_rabbitmq_{{ cookiecutter.project_name }}_cNgrRRkZ9T6eKCLe",
    user_tag => management,
}

rabbitmq::permissions { '{{ cookiecutter.project_name }}_stage@{{ cookiecutter.project_name }}_stage_vhost':
    user  => '{{ cookiecutter.project_name }}_stage',
    vhost => '{{ cookiecutter.project_name }}_stage_vhost',
    conf  => '.*',
    write => '.*',
    read  => '.*',
}

rabbitmq::user { 'guest':
    ensure => absent,
}

# clean up django session
cron { django_clearsessions_{ { cookiecutter.project_name }}_stage:
command => "/srv/www/{{ cookiecutter.project_name }}/stage/{{ cookiecutter.project_name }}-env/bin/python /srv/www/{{ cookiecutter.project_name }}/stage/manage.py clearsessions",
user    => root,
hour    => 2,
minute  => 0
}
