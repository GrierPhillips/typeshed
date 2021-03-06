from typing import Any, Dict, List, Mapping, Sequence


class _WriteResult(object):
    def __init__(self, acknowledged: bool) -> None: ...
    def _raise_if_unacknowledged(self, property_name: str) -> None: ...
    @property
    def acknowledged(self) -> bool: ...

class InsertOneResult(_WriteResult):
    def __init__(self, inserted_id: Sequence[Any], acknowledged: bool) -> None: ...
    @property
    def inserted_id(self) -> List[Any]: ...

class InsertManyResult(_WriteResult):
    def __init__(self, inserted_ids: Any, acknowledged: bool) -> None: ...
    @property
    def inserted_ids(self) -> Any: ...

class UpdateResult(_WriteResult):
    def __init__(self, raw_result: Mapping[str, Any], acknowledged: bool) -> None: ...
    @property
    def raw_result(self) -> Dict[str, Any]: ...
    @property
    def matched_count(self) -> int: ...
    @property
    def modified_count(self) -> int: ...
    @property
    def upserted_id(self) -> Any: ...

class DeleteResult(_WriteResult):
    def __init__(self, raw_result: Mapping[str, Any], acknowledged: bool) -> None: ...
    @property
    def raw_result(self) -> Dict[str, Any]: ...
    @property
    def deleted_count(self) -> int: ...

class BulkWriteResult(_WriteResult):
    def __init__(self, bulk_api_result: Mapping[str, Any], acknowledged: bool)\
        -> None: ...
    @property
    def bulk_api_result(self) -> Dict[str, Any]: ...
    @property
    def inserted_count(self) -> int: ...
    @property
    def matched_count(self) -> int: ...
    @property
    def modified_count(self) -> int: ...
    @property
    def deleted_count(self) -> int: ...
    @property
    def upserted_count(self) -> int: ...
    @property
    def upserted_ids(self) -> Dict[Any, Any]: ...
