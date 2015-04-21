class { 'postgresql':
}

postgresql::role { "{{ cookiecutter.project_name }}_vagrant":
    ensure    => present,
    password  => "test",
    require   => Class["postgresql"]
}

class { 'rabbitmq':
}

rabbitmq::vhost { '{{ cookiecutter.project_name }}_vagrant_vhost':
    ensure => present,
}

rabbitmq::user { '{{ cookiecutter.project_name }}_vagrant':
    ensure   => present,
    password => "test",
    user_tag => management,
}

rabbitmq::permissions { '{{ cookiecutter.project_name }}_vagrant@{{ cookiecutter.project_name }}_vagrant_vhost':
    user  => '{{ cookiecutter.project_name }}_vagrant',
    vhost => '{{ cookiecutter.project_name }}_vagrant_vhost',
    conf  => '.*',
    write => '.*',
    read  => '.*',
}

rabbitmq::user { 'guest':
    ensure => absent,
}
