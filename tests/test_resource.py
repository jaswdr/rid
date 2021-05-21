import pytest

from jaswdr_rid import InvalidResourceError, NotResourceError, Resource, __version__


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
    assert resource.partition == "partition"
    assert resource.service == "service"
    assert resource.region == "region"
    assert resource.account_id == "account_id"
    assert resource.resource_type == "resource_type"
    assert resource.resource_id == "resource_id"


def test_can_be_compared():
    assert _resource(1) == _resource(1)
    assert _resource(1) != _resource(2)


def test_return_false_when_comparing_to_no_resource():
    assert _resource(1) != {}
