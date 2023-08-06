# SPDX-FileCopyrightText: 2022-present Marcelo Trylesinski <marcelotryle@gmail.com>
#
# SPDX-License-Identifier: MIT


from __future__ import annotations

from typing import Mapping

# T = TypeVar("T")

JSONValue = (
    str | int | float | bool | None | list["JSONValue"] | Mapping[str, "JSONValue"]
)
JSONType = Mapping[str, JSONValue] | list[JSONValue]
