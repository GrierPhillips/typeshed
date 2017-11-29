from typing import (Any, Callable, Dict, Iterable, Iterator, List, Mapping,
                    Optional, Tuple, Union)

import bson
from bson.codec_options import CodecOptions
from pymongo.bulk import BulkOperationBuilder
from pymongo.collation import Collation
from pymongo.command_cursor import CommandCursor
from pymongo.common import BaseObject
from pymongo.cursor import Cursor
from pymongo.database import Database
from pymongo.operations import IndexModel, _WriteOp
from pymongo.pool import SocketInfo
from pymongo.read_concern import DEFAULT_READ_CONCERN, ReadConcern
from pymongo.read_preferences import _ServerMode
from pymongo.results import (BulkWriteResult, DeleteResult, InsertManyResult,
                             InsertOneResult, UpdateResult)
from pymongo.write_concern import WriteConcern


class ReturnDocument(object):
    BEFORE: bool = False
    AFTER: bool = True
class Collection(BaseObject):
    def __init__(
        self,
        database: Database,
        name: str,
        create: Optional[bool] = False,
        codec_options: Optional[CodecOptions] = None,
        read_preference: Optional[_ServerMode] = None,
        write_concern: Optional[WriteConcern] = None,
        read_concern: Optional[ReadConcern] = None,
        **kwargs: Any) -> None: ...
    def _socket_for_reads(self) -> Iterator[Tuple[SocketInfo, bool]]: ...
    def _socket_for_primary_reads(self)\
        -> Iterator[Tuple[SocketInfo, bool]]: ...
    def _socket_for_writes(self) -> Iterator[SocketInfo]: ...
    def _command(
        self,
        sock_info: SocketInfo,
        command: Dict[str, Any],
        slave_ok: bool = False,
        read_preference: Optional[_ServerMode] = None,
        codec_options: Optional[CodecOptions] = None,
        check: bool = True,
        allowable_errors: Optional[List[str]] = None,
        read_concern: Optional[ReadConcern] = DEFAULT_READ_CONCERN,
        write_concern: Optional[WriteConcern] = None,
        parse_write_concern_error: bool = False,
        collation: Optional[Collation] = None) -> Dict[str, Any]: ...
    def __create(
        self,
        options: Dict[str, Any],
        collation: Collation) -> None: ...
    def __getattr__(self, name: str) -> 'Collection': ...
    def __getitem__(self, name: str) -> 'Collection': ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    @property
    def full_name(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def database(self) -> Database: ...
    def with_options(
        self,
        codec_options: Optional[CodecOptions] = None,
        read_preference: Optional[_ServerMode] = None,
        write_concern: Optional[WriteConcern] = None,
        read_concern: Optional[ReadConcern] = None)\
        -> 'Collection': ...
    def initialize_unordered_bulk_op(
        self,
        bypass_document_validation: bool = False)\
        -> BulkOperationBuilder: ...
    def initialize_ordered_bulk_op(
        self,
        bypass_document_validation: bool = False)\
        -> BulkOperationBuilder: ...
    def bulk_write(
        self,
        requests: List[_WriteOp],
        ordered: bool = True,
        bypass_document_validation: bool = False)\
        -> BulkWriteResult: ...
    def _legacy_write(
        self,
        sock_info: SocketInfo,
        name: str,
        cmd: Dict[str, Any],
        acknowledged: bool,
        op_id: int,
        bypass_doc_val: bool,
        func: Callable[[Any], Any],
        *args: Any) -> Dict[str, Any]: ...
    def _insert_one(
        self,
        sock_info: SocketInfo,
        doc: Dict[str, Any],
        ordered: bool,
        check_keys: bool,
        manipulate: bool,
        write_concern: WriteConcern,
        op_id: int,
        bypass_doc_val: bool) -> Any: ...
    def _insert(
        self,
        sock_info: SocketInfo,
        docs: Dict[str, Any],
        ordered: bool = True,
        check_keys: bool = True,
        manipulate: bool = False,
        write_concern: Optional[WriteConcern] = None,
        op_id: Optional[int] = None,
        bypass_doc_val: bool = False)\
        -> Any: ...
    def insert_one(
        self,
        document: Any,
        bypass_document_validation: bool = False)\
        -> InsertOneResult: ...
    def insert_many(
        self,
        documents: Iterable[Any],
        ordered: bool = True,
        bypass_document_validation: bool = False)\
        -> InsertManyResult: ...
    def _update(self, sock_info: SocketInfo, criteria: Dict[str, Any],
                document: Dict[str, Any], upsert: bool = False,
                check_keys: bool = True, multi: bool = False,
                manipulate: bool = False,
                write_concern: Optional[WriteConcern] = None,
                op_id: Optional[int] = None, ordered: bool = True,
                bypass_doc_val: bool = False,
                collation: Optional[Collation] = None) -> Dict[str, Any]: ...
    def replace_one(
        self,
        filter: Dict[str, Any],
        replacement: Dict[str, Any],
        upsert: bool = False,
        bypass_document_validation: bool = False,
        collation: Optional[Collation] = None) -> UpdateResult: ...
    def update_one(
        self,
        filter: Dict[str, Any],
        update: Dict[str, Any],
        upsert: bool = False,
        bypass_document_validation: bool = False,
        collation: Optional[Collation] = None) -> UpdateResult: ...
    def update_many(self, filter: Dict[str, Any], update: Dict[str, Any],
                    upsert: bool = False,
                    array_filters: Optional[List[Any]] = None,
                    bypass_document_validation: bool = False,
                    collation: Optional[Collation] = None)\
        -> UpdateResult: ...
    def drop(self) -> None: ...
    def _delete(
            self, sock_info: SocketInfo, criteria: Dict[str, Any],
            multi: bool, write_concern: Optional[WriteConcern] = None,
            op_id: Optional[int] = None, ordered: bool = True,
            collation: Optional[Collation] = None) -> Dict[str, Any]: ...
    def delete_one(self, filter: Dict[str, Any],
                   collation: Optional[Collation] = None)\
        -> DeleteResult: ...
    def delete_many(self, filter: Dict[str, Any],
                    collation: Optional[Collation] = None)\
        -> DeleteResult: ...
    def find_one(self, filter: Optional[Dict[str, Any]] = None,
                 *args: Any, **kwargs: Any)\
        -> Union[Dict[str, Any], None]: ...
    def find(self, *args: Any, **kwargs: Any) -> Cursor: ...
    def parallel_scan(self, num_cursors: int, **kwargs: Any)\
        -> List[CommandCursor]: ...
    def _count(self, cmd: Mapping[str, Any],
               collation: Optional[Collation] = None) -> int: ...
    def count(self, filter: Optional[Mapping[str, Any]] = None, **kwargs: Any)\
        -> int: ...
    def create_indexes(self, indexes: List[IndexModel],
                       **kwargs: Any) -> List[str]: ...
    def __create_index(self, keys: List[Tuple[str, Union[int, str]]],
                       index_options: Dict[str, Any]) -> None: ...
    def create_index(self, keys: Union[str, List[Tuple[str, Union[int, str]]]],
                     **kwargs: Any) -> str: ...
    def ensure_index(
        self,
        key_or_list: Union[str, List[Tuple[str, Union[int, str]]]],
        cache_for: int = 300,
        **kwargs: Any) -> Union[str, None]: ...
    def drop_indexes(self) -> None: ...
    def drop_index(self, index_or_name: Any) -> None: ...
    def reindex(self) -> Dict[str, Any]: ...
    def list_indexes(self) -> CommandCursor: ...
    def index_information(self) -> Dict[str, Any]: ...
    def options(self) -> Dict[str, Any]: ...
    def _aggregate(self, pipeline: List[Dict[str, Any]], **kwargs: Any)\
        -> CommandCursor: ...
    def aggregate(self, pipeline: List[Dict[str, Any]], **kwargs: Any)\
        -> CommandCursor: ...
    def group(self, key: Union[List[str], Dict[str, Any], bson.Code],
              condition: Dict[str, Any], initial: Any, reduce: str,
              finalize: str = None, **kwargs: Any)\
        -> List[Dict[str, Any]]: ...
    def rename(self, new_name: str, **kwargs: Any) -> None: ...
    def distinct(self, key: str, filter: Optional[Dict[str, Any]] = None,
                 **kwargs: Any) -> List[Any]: ...
    def map_reduce(self, map: str, reduce: str,
                   out: Union[str, Dict[str, Any]],
                   full_response: bool = False,
                   **kwargs: Any)\
        -> Union[Dict[str, Any], Database, 'Collection']: ...
    def inline_map_reduce(
        self,
        map: str,
        reduce: str,
        full_response: bool = False,
        **kwargs: Any) -> Dict[str, Any]: ...
    def __find_and_modify(
        self,
        filter: Dict[str, Any],
        projection: Union[List[str], Dict[str, bool]],
        sort: List[Tuple[str, Union[int, str]]],
        upsert: Optional[bool] = None,
        return_document: bool = ReturnDocument.BEFORE,
        **kwargs: Any) -> Dict[str, Any]: ...
    def find_one_and_delete(
        self,
        filter: Dict[str, Any],
        projection: Optional[Union[List[str], Dict[str, bool]]] = None,
        sort: Optional[List[Tuple[str, Union[int, str]]]] = None,
        **kwargs: Any) -> Dict[str, Any]: ...
    def find_one_and_replace(
        self,
        filter: Dict[str, Any],
        replacement: Dict[str, Any],
        projection: Optional[Union[List[str], Dict[str, bool]]] = None,
        sort: Optional[List[Tuple[str, Union[int, str]]]] = None,
        upsert: bool = False,
        return_document: bool = ReturnDocument.BEFORE,
        **kwargs: Any) -> Dict[str, Any]: ...
    def find_one_and_update(
        self,
        filter: Dict[str, Any],
        update: Dict[str, Any],
        projection: Optional[Union[List[str], Dict[str, bool]]] = None,
        sort: Optional[List[Tuple[str, Union[int, str]]]] = None,
        upsert: bool = False,
        return_document: bool = ReturnDocument.BEFORE,
        **kwargs: Any) -> Dict[str, Any]: ...
    def save(self, to_save: Dict[str, Any], manipulate: bool = True,
             check_keys: bool = True, **kwargs: Any) -> Any: ...
    def insert(self, doc_or_docs: Dict[str, Any], manipulate: bool = True,
               check_keys: bool = True, continue_on_error: bool = False,
               **kwargs: Any) -> Any: ...
    def update(self, spec: Dict[str, Any], document: Dict[str, Any],
               upsert: bool = False, manipulate: bool = False,
               multi: bool = False, check_keys: bool = True,
               **kwargs: Any) -> Dict[str, Any]: ...
    def remove(self, spec_or_id: Optional[Dict[str, Any]] = None,
               multi: bool = True, **kwargs: Any) -> Dict[str, Any]: ...
    def find_and_modify(self,
        query: Dict[str, Any] = {},
        update: Dict[str, Any] = None,
        upsert: bool = False,
        sort: Optional[List[Tuple[str, Union[int, str]]]] = None,
        full_response: bool = False,
        manipulate: bool = False,
        **kwargs: Any) -> Dict[str, Any]: ...
    def __iter__(self) -> 'Collection': ...
    def __next__(self) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> None: ...
