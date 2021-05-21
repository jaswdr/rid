from uuid import uuid4

from jaswdr_rid import exceptions

RID_PREFFIX = "rid"
RID_SEP = ":"


class Resource:
    def __init__(
        self,
        partition: str,
        service: str,
        region: str,
        account_id: str,
        resource_type: str,
        resource_id: str = None,
    ):
        self.partition = partition
        self.service = service
        self.region = region
        self.account_id = account_id
        self.resource_type = resource_type
        if not resource_id:
            resource_id = str(uuid4())
        self.resource_id = resource_id

    def __str__(self):
        return RID_SEP.join(self.fields())

    def fields(self):
        return (
            RID_PREFFIX,
            self.partition,
            self.service,
            self.region,
            self.account_id,
            self.resource_type,
            str(self.resource_id),
        )

    @staticmethod
    def from_string(resource_id: str):
        if not resource_id.startswith(RID_PREFFIX):
            raise exceptions.NotResourceError(resource_id)

        if resource_id.count(RID_SEP) != 6:
            raise exceptions.InvalidResourceError(resource_id)

        split = resource_id.split(RID_SEP)
        return Resource(*split[1:])

    def __eq__(self, other):
        if not isinstance(other, Resource):
            return False

        return self.fields() == other.fields()
