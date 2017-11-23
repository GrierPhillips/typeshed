from typing import Any, Dict, Optional, Union


class CollationStrength(object):
    PRIMARY: int = 1
    SECONDARY: int = 2
    TERTIARY: int = 3
    QUATERNARY: int = 4
    IDENTICAL: int = 5
class CollationAlternate(object):
    NON_IGNORABLE: str = 'non-ignorable'
    SHIFTED: str = 'shifted'
class CollationMaxVariable(object):
    PUNCT: str = 'punct'
    SPACE: str = 'space'
class CollationCaseFirst(object):
    UPPER: str = 'upper'
    LOWER: str = 'lower'
    OFF: str = 'off'
class Collation(object):
    def __init__(self, locale: str,
                 caseLevel: Optional[bool] = None,
                 caseFirst: Optional[str] = None,
                 strength: Optional[int] = None,
                 numericOrdering: Optional[bool] = None,
                 alternate: Optional[str] = None,
                 maxVariable: Optional[str] = None,
                 normalization: Optional[bool] = None,
                 backwards: Optional[bool] = None,
                 **kwargs: Any) -> None: ...
    @property
    def document(self) -> Dict[str, Any]: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
def validate_collation_or_none(value: Any) -> Union[Dict[str, Any], None]: ...
