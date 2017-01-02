Role Name
=========

Installs Nginx as reverse proxy on Ubuntu. This role is a wrapper with some defaults for [geerlingguy.nginx](https://github.com/geerlingguy/ansible-role-nginx).

Requirements
------------

The Role is tested for Ubuntu 16.04. 

Role Variables
--------------

`nginx_proxy_pass`: The proxy pass for the Nginx location  

Dependencies
------------

- geerlingguy:nginx

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: FlxPeters.nginx-proxy, nginx_proxy_pass: "http://localhost:9000" }

Test
----

This roles uses Molecule to test. You can run the tests like this:

    molecule test
    
The tests are based on Docker and Testinfra.

License
-------

MIT

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
