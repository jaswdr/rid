import pytest

from resources import InvalidResourceError, NotResourceError, Resource, __version__


def test_version():
    assert __version__ == "0.1.0"


def _resource(resource_id=None):
    return Resource(
        partition="partition",
        service="service",
        region="region",
        resource_type="resource_type",
        account_id="account_id",
        resource_id=resource_id,
    )


def test_resource_instanciable():
    assert _resource()


def test_resource_can_generate_id():
    got = str(_resource(1))
    assert got == "rid:partition:service:region:account_id:resource_type:1"


def test_resource_can_generate_empty_id():
    preffix = "rid:partition:service:region:account_id:resource_type:"
    got = str(_resource())
    assert got.startswith(preffix)
    assert got != preffix


def test_resource_raise_not_resource_error():
    with pytest.raises(NotResourceError):
        Resource.from_string("x:")


def test_resource_raise_invalid_resource_error():
    with pytest.raises(InvalidResourceError):
        Resource.from_string("rid:a:b:c:d:e")


def test_resource_from_string():
    resource = Resource.from_string(
        "rid:partition:service:region:account_id:resource_type:resource_id"
    )
    assert resource.in_partition("partition")
    assert resource.is_service("service")
    assert resource.in_region("region")
    assert resource.belongs_to("account_id")
    assert resource.is_resource_type("resource_type")
    assert resource.has_id("resource_id")


def test_can_be_compared():
    assert _resource(1) == _resource(1)
    assert _resource(1) != _resource(2)


def test_return_false_when_comparing_to_no_resource():
    assert _resource(1) != {}


def test_in_partition():
    assert _resource().in_partition("partition")


def test_is_service():
    assert _resource().is_service("service")


def test_in_region():
    assert _resource().in_region("region")


def test_belongs_to():
    assert _resource(1).belongs_to("account_id")


def test_is_resource_type():
    assert _resource().is_resource_type("resource_type")


def test_has_id():
    assert _resource(1).has_id(1)
