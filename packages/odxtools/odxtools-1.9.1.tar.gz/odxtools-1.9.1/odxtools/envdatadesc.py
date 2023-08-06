# SPDX-License-Identifier: MIT
# Copyright (c) 2022 MBition GmbH

from dataclasses import dataclass
from typing import List, Optional

from .utils import make_ref
from .globals import logger
from .dataobjectproperty import DopBase

from .decodestate import DecodeState
from .encodestate import EncodeState
from .exceptions import DecodeError, EncodeError

class EnvironmentDataDescription(DopBase):
    """This class represents Environment Data Description, which is a complex DOP
    that is used to define the interpretation of environment data."""

    def __init__(self,
                 env_data_refs: List[str],
                 param_snref: Optional[str] = None,
                 param_snpathref: Optional[str] = None,
                 **kwargs):
        super().__init__(**kwargs)

        self.bit_length = None
        self.env_data_refs = env_data_refs
        self.param_snref = param_snref
        self.param_snpathref = param_snpathref

    def _build_id_lookup(self):
        id_lookup = {}
        id_lookup.update({self.id: self})
        return id_lookup

    def __repr__(self) -> str:
        return (
            f"EnvironmentDataDescription('{self.short_name}', "
            + ", ".join(
                [
                    f"id='{self.id}'",
                    f"param_snref='{self.param_snref}'",
                    f"param_snpathref='{self.param_snpathref}'",
                    f"env_data_refs='{self.env_data_refs}'",
                ]
            )
            + ")"
        )

    def convert_physical_to_bytes(self, physical_value, encode_state: EncodeState, bit_position: int) -> bytes:
        """Convert the physical value into bytes.

        Since environmental data is supposed to never appear on the
        wire, this method just raises an EncodeError exception.
        """
        raise EncodeError("EnvironmentDataDescription DOPs cannot be encoded or decoded")

    def convert_bytes_to_physical(self, decode_state: DecodeState, bit_position: int = 0):
        """Extract the bytes from the PDU and convert them to the physical value.

        Since environmental data is supposed to never appear on the
        wire, this method just raises an DecodeError exception.
        """
        raise DecodeError("EnvironmentDataDescription DOPs cannot be encoded or decoded")


def read_env_data_desc_from_odx(et_element):
    """Reads Environment Data Description from Diag Layer."""
    id = et_element.get("ID")
    short_name = et_element.find("SHORT-NAME").text
    long_name = et_element.find("LONG-NAME").text
    param_snref = None
    if et_element.find("PARAM-SNREF") is not None:
        param_snref = et_element.find("PARAM-SNREF").get("SHORT-NAME")
    param_snpathref = None
    if et_element.find("PARAM-SNPATHREF") is not None:
        param_snpathref = et_element.find("PARAM-SNPATHREF").get("SHORT-NAME-PATH")
    env_data_refs = []
    env_data_refs.extend([
        make_ref(env_data_ref)
        for env_data_ref in et_element.iterfind("ENV-DATA-REFS/ENV-DATA-REF")
    ])
    # ODX 2.0.0 says ENV-DATA-DESC could contain a list of ENV-DATAS
    env_data_refs.extend([
        env_data.get("ID")
        for env_data in et_element.iterfind("ENV-DATAS/ENV-DATA")
    ])
    logger.debug("Parsing ENV-DATA-DESC " + short_name)

    env_data_desc = EnvironmentDataDescription(
        id=id,
        short_name=short_name,
        long_name=long_name,
        param_snref=param_snref,
        param_snpathref=param_snpathref,
        env_data_refs=env_data_refs,
    )

    return env_data_desc
