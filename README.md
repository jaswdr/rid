# Resources naming package
> Create unique and trackable resources ids

## Getting Started

Install the resources package.

```bash
$ pip install jaswdr-rid
```

Generate new resources ids.

```python
from jaswdr_rid import Resource

resource = Resource(
    partition="prod",
    service="my_service",
    region="eu-west-1",
    account_id="1",
    resource_type="user"
)

print(str(resource))
# 'rid:prod:my_service:eu-west-1:1:user:21a59a0e-36bb-4592-84de-d13e3bbea982'
```
