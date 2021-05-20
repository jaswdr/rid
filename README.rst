# Resources naming package
> Create unique and trackable resources ids

## Getting Started

Install the resources package.

```bash
$ pip install resources
```

Generate new resources ids.

```python
import resources

generator = resources.Generator(
    partition="prod",
    service="my_service",
    region="eu-west-1",
    account_id="1",
)

_id = generator.id()

print(_id)
```
