#Configure web servers for deployment of web_static
# Install Nginx
class { 'nginx':
  package_ensure => 'latest',
  service_ensure => 'running',
  service_enable => true,
}

# Set up web server for deployment of web_static
file { '/data/web_static/releases/test/':
  ensure => 'directory',
}

file { '/data/web_static/shared':
  ensure => 'directory',
}

file { '/data/web_static/releases/test/index.html':
  content => 'Holberton School',
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/',
  force  => true,
}

file { '/data/':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Nginx configuration
file { '/etc/nginx/sites-available/default':
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}",
  notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure     => 'running',
  subscribe  => File['/etc/nginx/sites-available/default'],
}
