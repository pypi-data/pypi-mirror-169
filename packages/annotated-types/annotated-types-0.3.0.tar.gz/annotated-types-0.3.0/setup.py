# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['annotated_types']

package_data = \
{'': ['*']}

extras_require = \
{':python_full_version < "3.9.0"': ['typing-extensions>=4.0.0,<5.0.0']}

setup_kwargs = {
    'name': 'annotated-types',
    'version': '0.3.0',
    'description': 'Reusable constraint types to use with typing.Annotated',
    'long_description': '# annotated-types\n\n[![CI](https://github.com/annotated-types/annotated-types/workflows/CI/badge.svg?event=push)](https://github.com/annotated-types/annotated-types/actions?query=event%3Apush+branch%3Amain+workflow%3ACI)\n[![pypi](https://img.shields.io/pypi/v/annotated-types.svg)](https://pypi.python.org/pypi/annotated-types)\n[![versions](https://img.shields.io/pypi/pyversions/annotated-types.svg)](https://github.com/annotated-types/annotated-types)\n[![license](https://img.shields.io/github/license/annotated-types/annotated-types.svg)](https://github.com/annotated-types/annotated-types/blob/main/LICENSE)\n\n[PEP-593](https://peps.python.org/pep-0593/) added `typing.Annotated` as a way of\nadding context-specific metadata to existing types, and specifies that\n`Annotated[T, x]` _should_ be treated as `T` by any tool or library without special\nlogic for `x`.\n\nThis package provides metadata objects which can be used to represent common\nconstraints such as upper and lower bounds on scalar values and collection sizes,\na `Predicate` marker for runtime checks, and [non-normative](https://developer.mozilla.org/en-US/docs/Glossary/non-normative)\ndescriptions of how we intend these metadata to be interpreted. In some cases,\nwe also note alternative representations which do not require this package.\n\n## Install\n\n```bash\npip install annotated-types\n```\n\n## Examples\n\n```python\nfrom typing import Annotated\nfrom annotated_types import Gt, Len, Predicate\n\nclass MyClass:\n    age: Annotated[int, Gt(18)]                         # Valid: 19, 20, ...\n                                                        # Invalid: 17, 18, "19", 19.0, ...\n    factors: list[Annotated[int, Predicate(is_prime)]]  # Valid: 2, 3, 5, 7, 11, ...\n                                                        # Invalid: 4, 8, -2, 5.0, "prime", ...\n\n    my_list: Annotated[list[int], 0:10]                 # Valid: [], [10, 20, 30, 40, 50]\n                                                        # Invalid: (1, 2), ["abc"], [0] * 20\n    your_set: Annotated[set[int], Len(0, 10)]           # Valid: {1, 2, 3}, ...\n                                                        # Invalid: "Well, you get the idea!"\n```\n\n## Documentation\n\n_While `annotated-types` avoids runtime checks for performance, users should not\nconstruct invalid combinations such as `MultipleOf("non-numeric")` or `Annotated[int, Len(3)]`.\nDownstream implementors may choose to raise an error, emit a warning, silently ignore\na metadata item, etc., if the metadata objects described below are used with an\nincompatible type - or for any other reason!_\n\n### Gt, Ge, Lt, Le\n\nExpress inclusive and/or exclusive bounds on orderable values - which may be numbers,\ndates, times, strings, sets, etc. Note that the boundary value need not be of the\nsame type that was annotated, so long as they can be compared: `Annotated[int, Gt(1.5)]`\nis fine, for example, and implies that the value is an integer x such that `x > 1.5`.\nNo interpretation is specified for special values such as `nan`.\n\nWe suggest that implementors may also interpret `functools.partial(operator.le, 1.5)`\nas being equivalent to `Gt(1.5)`, for users who wish to avoid a runtime dependency on\nthe `annotated-types` package.\n\nTo be explicit, these types have the following meanings:\n\n* `Gt(x)` - value must be "Greater Than" `x` - equivalent to exclusive minimum\n* `Ge(x)` - value must be "Greater than or Equal" to `x` - equivalent to inclusive minimum\n* `Lt(x)` - value must be "Less Than" `x` - equivalent to exclusive maximum\n* `Le(x)` - value must be "Less than or Equal" to `x` - equivalent to inclusive maximum\n\n### Interval\n\n`Interval(gt, ge, lt, le)` allows you to specify an upper and lower bound with a single\nmetadata object. `None` attributes should be ignored, and non-`None` attributes\ntreated as per the single bounds above.\n\n### MultipleOf\n\n`MultipleOf(multiple_of=x)` might be interpreted in two ways:\n\n1. Python semantics, implying `value % multiple_of == 0`, or\n2. [JSONschema semantics](https://json-schema.org/draft/2020-12/json-schema-validation.html#rfc.section.6.2.1),\n   where `int(value / multiple_of) == value / multiple_of`.\n\nWe encourage users to be aware of these two common interpretations and their\ndistinct behaviours, especially since very large or non-integer numbers make\nit easy to cause silent data corruption due to floating-point imprecision.\n\nWe encourage libraries to carefully document which interpretation they implement.\n\n### Len\n\n`Len()` implies that `min_inclusive <= len(value) < max_exclusive`.\nWe recommend that libraries interpret `slice` objects identically\nto `Len()`, making all the following cases equivalent:\n\n* `Annotated[list, :10]`\n* `Annotated[list, 0:10]`\n* `Annotated[list, None:10]`\n* `Annotated[list, slice(0, 10)]`\n* `Annotated[list, Len(0, 10)]`\n* `Annotated[list, Len(max_exclusive=10)]`\n\nAnd of course you can describe lists of three or more elements (`Len(min_inclusive=3)`),\nfour, five, or six elements (`Len(4, 7)` - note exclusive-maximum!) or *exactly*\neight elements (`Len(8, 9)`).\n\nImplementors: note that Len() should always have an integer value for\n`min_inclusive`, but `slice` objects can also have `start=None`.\n\n### Timezone\n\n`Timezone` can be used with a `datetime` or a `time` to express which timezones\nare allowed. `Annotated[datetime, Timezone(None)]` must be a naive datetime.\n`Timezone[...]` ([literal ellipsis](https://docs.python.org/3/library/constants.html#Ellipsis))\nexpresses that any timezone-aware datetime is allowed. You may also pass a specific\ntimezone string or `timezone` object such as `Timezone(timezone.utc)` or\n`Timezone("Africa/Abidjan")` to express that you only allow a specific timezone,\nthough we note that this is often a symptom of fragile design.\n\n### Predicate\n\n`Predicate(func: Callable)` expresses that `func(value)` is truthy for valid values.\nUsers should prefer the statically inspectable metadata above, but if you need\nthe full power and flexibility of arbitrary runtime predicates... here it is.\n\nWe provide a few predefined predicates for common string constraints:\n`IsLower = Predicate(str.islower)`, `IsUpper = Predicate(str.isupper)`, and\n`IsDigit = Predicate(str.isdigit)`. Users are encouraged to use methods which\ncan be given special handling, and avoid indirection like `lambda s: s.lower()`.\n\nSome libraries might have special logic to handle known or understandable predicates,\nfor example by checking for `str.isdigit` and using its presence to both call custom\nlogic to enforce digit-only strings, and customise some generated external schema.\n\nWe do not specify what behaviour should be expected for predicates that raise\nan exception.  For example `Annotated[int, Predicate(str.isdigit)]` might silently\nskip invalid constraints, or statically raise an error; or it might try calling it\nand then propogate or discard the resulting\n`TypeError: descriptor \'isdigit\' for \'str\' objects doesn\'t apply to a \'int\' object`\nexception.  We encourage libraries to document the behaviour they choose.\n\n### Integrating downstream types with `GroupedMetadata`\n\nImplementers may choose to provide a convenience wrapper that groups multiple pieces of metadata.\nThis can help reduce verbosity and cognitive overhead for users.\nFor example, an implementer like Pydantic might provide a `Field` or `Meta` type that accepts keyword arguments and transforms these into low-level metadata:\n\n```python\nfrom dataclasses import dataclass\nfrom typing import Iterator\nfrom annotated_types import GroupedMetadata, Ge\n\n@dataclass\nclass Field(GroupedMetadata):\n    ge: int | None = None\n    description: str | None = None\n\n    def __iter__(self) -> Iterator[object]:\n        # Iterating over a GroupedMetadata object should yield annotated-types\n        # constraint metadata objects which describe it as fully as possible,\n        # and may include other unknown objects too.\n        if self.ge is not None:\n            yield Ge(self.ge)\n        if self.description is not None:\n            yield Description(self.description)\n```\n\nLibraries consuming annotated-types constraints should check for `GroupedMetadata` and unpack it by iterating over the object and treating the results as if they had been "unpacked" in the `Annotated` type.  The same logic should be applied to the [PEP 646 `Unpack` type](https://peps.python.org/pep-0646/), so that `Annotated[T, Field(...)]`, `Annotated[T, Unpack[Field(...)]]` and `Annotated[T, *Field(...)]` are all treated consistently.\n\nOur own `annotated_types.Interval` class is a `GroupedMetadata` which unpacks itself into `Gt`, `Lt`, etc., so this is not an abstract concern.\n\n### Consuming metadata\n\nWe intend to not be perspcriptive as to _how_ the metadata and constraints are used, but as an example of how one might parse constraints from types annotations see our [implementation in `test_main.py`](https://github.com/annotated-types/annotated-types/blob/f59cf6d1b5255a0fe359b93896759a180bec30ae/tests/test_main.py#L94-L103).\n\nIt is up to the implementer to determine how this metadata is used.\nYou could use the metadata for runtime type checking, for generating schemas or to generate example data, amongst other use cases.\n\n## Design & History\n\nThis package was designed at the PyCon 2022 sprints by the maintainers of Pydantic\nand Hypothesis, with the goal of making it as easy as possible for end-users to\nprovide more informative annotations for use by runtime libraries.\n\nIt is deliberately minimal, and following PEP-593 allows considerable downstream\ndiscretion in what (if anything!) they choose to support. Nonetheless, we expect\nthat staying simple and covering _only_ the most common use-cases will give users\nand maintainers the best experience we can. If you\'d like more constraints for your\ntypes - follow our lead, by defining them and documenting them downstream!\n',
    'author': 'Samuel Colvin',
    'author_email': 's@mulecolvin.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/annotated-types/annotated-types',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7.0,<4.0.0',
}


setup(**setup_kwargs)
