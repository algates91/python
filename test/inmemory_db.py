
from uuid import uuid4, UUID
from request import TaskRead


tasks:dict[UUID, TaskRead] = {}
dummy_id = uuid4()
tasks[dummy_id] = TaskRead(completed=False, id=dummy_id, title="dummy task")

def get_store() -> dict[UUID, TaskRead]:
    return tasks