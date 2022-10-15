# -*- coding: utf-8 -*-
def pkg_is_installed(host):
    package = host.package('mysql')

    assert package.is_installed


def test_service_is_running(host):
    service = host.service('mysql')

    assert service.is_running
    assert service.is_enabled
