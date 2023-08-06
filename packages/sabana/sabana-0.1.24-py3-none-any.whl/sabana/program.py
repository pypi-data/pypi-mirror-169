# Copyright 2022 Sabana Technologies, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.protobuf.json_format import MessageToDict
from sabana import requests as sabana_req
from sabana.common import CommonError


class ProgramError(Exception):
    pass


class Program:
    """
    Program: Holds a series of operations to be executed on a Sabana Instance.
    """

    def __init__(self):
        self.req = sabana_req.execute_request()

    def __del__(self):
        del self.req

    def clear(self):
        self.__del__()
        self.req = sabana_req.execute_request()

    def to_dict(self):
        return MessageToDict(self.req)

    def err_msg(inst):
        return f"error - {inst}: check your arguments"

    def err_msg_txt(inst, txt):
        return f"error - {inst}: {txt}"

    def err_msg_from_e(inst, e):
        return Program.err_msg_txt(inst, str(e))

    def buffer_alloc(self, name=None, size=None, mmio_name=None, mmio_offset=None):
        func_name = "buffer_alloc"
        try:
            self.req.requests.append(
                sabana_req.buffer_alloc(name, size, mmio_name, mmio_offset)
            )
        except CommonError as e:
            raise ProgramError(Program.err_msg_from_e(func_name, e))
        except Exception:
            raise ProgramError(Program.err_msg(func_name))

    def buffer_write(self, data, name=None, offset=None):
        func_name = "buffer_write"
        try:
            self.req.requests.append(sabana_req.buffer_write(name, offset, data))
        except CommonError as e:
            raise ProgramError(Program.err_msg_from_e(func_name, e))
        except Exception:
            raise ProgramError(Program.err_msg(func_name))

    def buffer_wait(self, data, name=None, offset=None, timeout=None):
        func_name = "buffer_wait"
        try:
            self.req.requests.append(
                sabana_req.buffer_wait(name, offset, data, timeout)
            )
        except CommonError as e:
            raise ProgramError(Program.err_msg_from_e(func_name, e))
        except Exception:
            raise ProgramError(Program.err_msg(func_name))

    def buffer_read(self, name=None, offset=None, dtype=None, shape=None):
        func_name = "buffer_read"
        try:
            self.req.requests.append(sabana_req.buffer_read(name, offset, dtype, shape))
        except CommonError as e:
            raise ProgramError(Program.err_msg_from_e(func_name, e))
        except Exception:
            raise ProgramError(Program.err_msg(func_name))

    def buffer_dealloc(self, name=None):
        func_name = "buffer_dealloc"
        try:
            self.req.requests.append(sabana_req.buffer_dealloc(name))
        except CommonError as e:
            raise ProgramError(Program.err_msg_from_e(func_name, e))
        except Exception:
            raise ProgramError(Program.err_msg(func_name))

    def mmio_alloc(self, name=None, size=None, base_address=None):
        func_name = "mmio_alloc"
        if not isinstance(size, int) or size % 4:
            raise ProgramError(
                Program.err_msg_txt(func_name, "size must be an integer multiple of 4")
            )
        if size > 0x10000:
            raise ProgramError(
                Program.err_msg_txt(
                    func_name, f"size needs to be less than {0x10000} bytes"
                )
            )
        if size < 0:
            raise ProgramError(
                Program.err_msg_txt(func_name, "size needs to be a positive number")
            )
        if base_address != 0xA0000000:
            raise ProgramError(
                Program.err_msg_txt(func_name, "base address must be 0xa0000000")
            )

        try:
            self.req.requests.append(sabana_req.mmio_alloc(name, size))
        except CommonError as e:
            raise ProgramError(Program.err_msg_from_e(func_name, e))
        except Exception:
            raise ProgramError(Program.err_msg(func_name))

    def mmio_write(self, data, name=None, offset=None):
        func_name = "mmio_write"
        if not isinstance(offset, int):
            raise ProgramError(
                Program.err_msg_txt(func_name, "offset must be a positive integer")
            )
        elif offset % 4:
            raise ProgramError(
                Program.err_msg_txt(func_name, "offset must be multiple of 4")
            )
        try:
            self.req.requests.append(sabana_req.mmio_write(name, offset, data))
        except CommonError as e:
            raise ProgramError(Program.err_msg_from_e(func_name, e))
        except Exception:
            raise ProgramError(Program.err_msg(func_name))

    def mmio_wait(self, data, name=None, offset=None, timeout=None):
        func_name = "mmio_wait"
        if not isinstance(offset, int):
            raise ProgramError(
                Program.err_msg_txt(func_name, "offset must be a positive integer")
            )
        elif offset % 4:
            raise ProgramError(
                Program.err_msg_txt(func_name, "offset must be multiple of 4")
            )
        try:
            self.req.requests.append(sabana_req.mmio_wait(name, offset, data, timeout))
        except CommonError as e:
            raise ProgramError(Program.err_msg_from_e(func_name, e))
        except Exception:
            raise ProgramError(Program.err_msg(func_name))

    def mmio_read(self, name=None, offset=None, dtype=None, shape=None):
        func_name = "mmio_read"
        if not isinstance(offset, int):
            raise ProgramError(
                Program.err_msg_txt(func_name, "offset must be a positive integer")
            )
        elif offset % 4:
            raise ProgramError(
                Program.err_msg_txt(func_name, "offset must be multiple of 4")
            )
        try:
            self.req.requests.append(sabana_req.mmio_read(name, offset, dtype, shape))
        except CommonError as e:
            raise ProgramError(Program.err_msg_from_e(func_name, e))
        except Exception:
            raise ProgramError(Program.err_msg(func_name))

    def mmio_dealloc(self, name=None):
        func_name = "mmio_dealloc"
        try:
            self.req.requests.append(sabana_req.mmio_dealloc(name))
        except CommonError as e:
            raise ProgramError(Program.err_msg_from_e(func_name, e))
        except Exception:
            raise ProgramError(Program.err_msg(func_name))

    def dma_send_alloc(self, name=None):
        func_name = "dma_send_alloc"
        try:
            self.req.requests.append(sabana_req.dma_send_alloc(name))
        except CommonError as e:
            raise ProgramError(Program.err_msg_from_e(func_name, e))
        except Exception:
            raise ProgramError(Program.err_msg(func_name))

    def dma_send_write(self, name=None, src=None):
        func_name = "dma_send_write"
        try:
            self.req.requests.append(sabana_req.dma_send_write(name, src))
        except CommonError as e:
            raise ProgramError(Program.err_msg_from_e(func_name, e))
        except Exception:
            raise ProgramError(Program.err_msg(func_name))

    def dma_send_wait(self, name=None, timeout=None):
        func_name = "dma_send_wait"
        try:
            self.req.requests.append(sabana_req.dma_send_wait(name, timeout))
        except CommonError as e:
            raise ProgramError(Program.err_msg_from_e(func_name, e))
        except Exception:
            raise ProgramError(Program.err_msg(func_name))

    def dma_send_dealloc(self, name=None):
        func_name = "dma_send_dealloc"
        try:
            self.req.requests.append(sabana_req.dma_send_dealloc(name))
        except CommonError as e:
            raise ProgramError(Program.err_msg_from_e(func_name, e))
        except Exception:
            raise ProgramError(Program.err_msg(func_name))

    def dma_recv_alloc(self, name=None):
        func_name = "dma_recv_alloc"
        try:
            self.req.requests.append(sabana_req.dma_recv_alloc(name))
        except CommonError as e:
            raise ProgramError(Program.err_msg_from_e(func_name, e))
        except Exception:
            raise ProgramError(Program.err_msg(func_name))

    def dma_recv_read(self, name=None, dst=None):
        func_name = "dma_recv_read"
        try:
            self.req.requests.append(sabana_req.dma_recv_read(name, dst))
        except CommonError as e:
            raise ProgramError(Program.err_msg_from_e(func_name, e))
        except Exception:
            raise ProgramError(Program.err_msg(func_name))

    def dma_recv_wait(self, name=None, timeout=None):
        func_name = "dma_recv_wait"
        try:
            self.req.requests.append(sabana_req.dma_recv_wait(name, timeout))
        except CommonError as e:
            raise ProgramError(Program.err_msg_from_e(func_name, e))
        except Exception:
            raise ProgramError(Program.err_msg(func_name))

    def dma_recv_dealloc(self, name=None):
        func_name = "dma_recv_dealloc"
        try:
            self.req.requests.append(sabana_req.dma_recv_dealloc(name))
        except CommonError as e:
            raise ProgramError(Program.err_msg_from_e(func_name, e))
        except Exception:
            raise ProgramError(Program.err_msg(func_name))
