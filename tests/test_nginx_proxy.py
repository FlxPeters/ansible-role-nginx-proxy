from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_nginx_running_and_enabled(Service):
    nginx = Service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled


def test_nginx_listining_on_80(Socket):
    socket = Socket("tcp://0.0.0.0:80")
    assert socket.is_listening
