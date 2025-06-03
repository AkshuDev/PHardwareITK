import sys
import threading
import inspect
import queue
import socket

class MemBlock:
    """A Memory Block class used to define protected sections of RAM (Virtual RAM)"""
    def __init__(self, size:int, access:list[str], name:str="BLOCK", seek:int=0):
        """Init func

        Args:
            size (int): The size of the protected region in bytes.
            access (str): The __file__ variable of the file that can access this region.
            name (str, optional): Name of the region. Defaults to "BLOCK".
            seek (int, optional): Address where the region starts. Defaults to 0.
        """
        self.size = size
        self.access = access
        self.name = name
        self.seek = seek
        self.end_seek = seek + size

class Process_Data:
    """A Class for VRam Mapping Data for processes
    """
    def __init__(self, Pid:int, process:object, *params):
        """The init func

        Args:
            Pid (int): The Unique ID given to every func (Process ID).
            process (object): The function to run as a process.
            *params: Params to the process.
        """
        self.Pid = Pid
        self.process:object = process
        self.params = params

class Execution_Data:
    """Execution Data Class
    """
    def __init__(self, heap_size:int=6, stack_size:int=6, heap_reserve:int=1, stack_reserve:int=1, data_size:int=8) -> None:
        """Init func

        Args:
            heap_size (int, optional): MAX Heap size including Heap Reserve in bytes. Defaults to 6.
            stack_size (int, optional): MAX Stack size including Stack Reserve in bytes. Defaults to 6.
            heap_reserve (int, optional): Reserved Heap in bytes. Defaults to 1.
            stack_reserve (int, optional): Reserved Stack in bytes. Defaults to 1.
            data_size (int, optional): Size of initialized data in bytes. Defaults to 8.
        """

        self.heap_reserve:int = heap_reserve
        self.stack_reserve:int = stack_reserve
        self.heap_size:int = heap_size
        self.stack_size:int = stack_size
        self.data_size:int = data_size
        self.vmem_size:int = heap_size + stack_size + data_size

class Memory:
    """A Memory Class.

    Memory Layout ->

    System Memory -> 64 bytes (Blocked)

    Process Memory -> User-Defined, Default 64 bytes (Open)

    -- Program Memory (Virtual Memory) -> Per Process , User - Defined (Blocked)

    Rest of the Memory -> User-Defined (Open)
    """
    def __init__(self, size:int, proc_sector_size:int=64, Block:list[MemBlock]=None, debug:bool=False) -> None:
        """Initialization function.
        NOTE: RAM in this class refers to a part of mapped RAM known as Virtual Memory that every program has.

        Args:
            size (int): The size of RAM in bytes.
            proc_sector_size (int): The size of RAM dedicated to processes in bytes. Defaults to 64.
            Block (list[MemBlock]): The protected regions if any. Defaults to None.
        """
        self.size:int = size + 64 + proc_sector_size# Size + System Size + Process Sector Size
        self.ram:bytearray = bytearray(size)
        self.current_addr:int = 0x0
        self.mem_blocks:list[MemBlock] = Block
        
        self.proc_sector_size = proc_sector_size

        self.sys_block:MemBlock = MemBlock(64, [__file__], "_WIN32-PR", 0)

        self.debug = debug

        if self.mem_blocks:
            if self._init_blocks() == False:
                exit()

    def _get_running_file(self) -> None:
        """DO NOT USE!"""
        import inspect
        stack = inspect.stack()

        for frame in stack[1:]:  # Skip self
            caller_locals = frame.frame.f_locals
            if "self" in caller_locals:
                if caller_locals["self"].__class__ == self.__class__:
                    continue  # Skip internal calls within the same class
            return frame.filename  # First external caller

        return None  # No external caller found (edge case)

    def _init_sys_ram(self) -> None:
        """DO NOT USE!"""
        pass

    def _init_blocks(self) -> bool:
        """DO NOT USE!"""
        for block_p in self.mem_blocks:
            addr = block_p.seek
            size = block_p.size

            end_seek = addr + size

            if addr >= self.sys_block.seek and addr <= self.sys_block.end_seek:
                if self.debug: print(f"PHardwareITK/Memory/_platform/_win32: ERROR -> block named [{block_p.name}] overlapes a system block named -> {self.sys_block.name}")
                return False

            for block in self.mem_blocks:
                if block_p == block:
                    continue

                if addr >= block.seek and addr <= block.end_seek:
                    if self.debug: print(f"PHardwareITK/Memory/_platform/_win32: ERROR -> block named [{block_p.name}] overlapes a block named -> {block.name}")
                    return False

                if end_seek >= block.seek and end_seek <= block.end_seek:
                    if self.debug: print(f"PHardwareITK/Memory/_platform/_win32: ERROR -> block named [{block_p.name}] overlapes a block named -> {block.name}")
                    return False

                if addr < block.seek and end_seek > block.end_seek:
                    if self.debug: print(f"PHardwareITK/Memory/_platform/_win32: ERROR -> block named [{block_p.name}] overlapes a block named -> {block.name}")
                    return False

        return True

    def _CFBlock(self, addr:int, size:int) -> bool:
        file =  self._get_running_file()

        end_seek = addr + size

        if addr >= self.sys_block.seek and addr <= self.sys_block.end_seek:
            if not self.sys_block.access == file:
                if self.debug: print(f"PHardwareITK/Memory/_platform/_win32: ERROR -> Address comes under a system block named -> {self.sys_block.name}")
                return False

        if not self.mem_blocks == None:
            for block in self.mem_blocks:
                if addr >= block.seek and addr <= block.end_seek:
                    if not file in block.access:
                        if self.debug: print(f"PHardwareITK/Memory/_platform/_win32: ERROR -> Address comes under a block named -> {block.name}")
                        return False

                if end_seek >= block.seek and end_seek <= block.end_seek:
                    if not file in block.access:
                        if self.debug: print(f"PHardwareITK/Memory/_platform/_win32: ERROR -> End of Data comes under a block named -> {block.name}")
                        return False

                if addr < block.seek and end_seek > block.end_seek:
                    if not file in block.access:
                        if self.debug: print(f"PHardwareITK/Memory/_platform/_win32: ERROR -> Data comes under a block named -> {block.name}")
                        return False

        return True

    def write_ram(self, data:bytes, addr:int=None, size:int=0) -> bool:
        """Writes data to a address. If addr is None, writes data at current addr. Size argument if present just appends data with 0"""
        if addr:
            self.current_addr = addr

        if self._CFBlock(addr, len(data) + size) == False:
            return False
		
        if size:
            append_ = 0
            data = data + append_.to_bytes(size, "little")
		
        self.ram[self.current_addr:self.current_addr + len(data)] = data
        return True

    def get_ram(self, size:int, addr:int=None) -> bytes:
        """Gets data from a part of RAM

        Args:
            size (int): The size of data to get
            addr (int, optional): The address of data (start). If None, uses current address. Defaults to None.

        Returns:
            bytes: The retrieved data
        """
        if addr:
            self.current_addr = addr

        if self._CFBlock(addr, size) == False:
            return b""

        return self.ram[self.current_addr : self.current_addr + size]

    def serialize(self) -> str:
        attribs = {"size": self.size, "proc_sector_size": self.proc_sector_size, "blocks": self.mem_blocks}
        import json
        return json.dumps(attribs)

class Process:
    """A Class for the Proc Handling (DO NOT USE!)"""
    def __init__(self, mem:Memory, exec_data:Execution_Data, ProcessData:Process_Data, addr:int=0) -> None:
        """Init func
        """
        self.lock = threading.Lock()

        self.mem:Memory = mem
        self.exec_data:Execution_Data = exec_data
        self.ProcessData:Process_Data = ProcessData
        self.pid:int = ProcessData.Pid
        self.ram:bytearray = mem.ram

        self.vram_seek = addr

        # Allocation Segments
        self.data_seek:int = addr
        self.stack_seek:int = self.data_seek + exec_data.data_size + 1
        self.heap_seek:int = self.stack_seek + exec_data.stack_size + 1
        self.text_seek:int = self.heap_seek + exec_data.heap_size + 1

        self.allocs = {} # Var address mapping

    def __setattr__(self, name:str, value:int):
        if name in ["lock", "mem", "exec_data", "ProcessData", "pid", "ram", "vram_seek", "data_seek", "text_seek", "heap_seek", "stack_seek", "allocs"]:
            super().__setattr__(name, value)
            return

        with self.lock: #Ensure Thread safety
            if isinstance(value, bytes): # Text Segment
                addr = self.text_seek
                self.text_seek += len(value)
            else:
                size = len(value.to_bytes((value.bit_length() // 8) + 1, 'little'))

                if self._is_uninitialized(name):
                    addr = self.heap_seek
                    self.heap_seek += size
                else:
                    addr = self.data_seek
                    self.data_seek += size

                if addr >= self.exec_data.vmem_size:
                    print(f"Process {self.pid}: ERROR -> Memory Overflow! Process is now stopping")
                    return

            self.mem.write_ram(value.to_bytes(size, 'little'), addr)
            self.allocs[name] = addr

    def __getattr__(self, name):
        if name in ["lock", "mem", "exec_data", "ProcessData", "pid", "ram", "vram_seek", "data_seek", "text_seek", "heap_seek", "stack_seek", "allocs"]:
            raise RuntimeError(f"Unexpected lookup for {name}!")
        if name in self.allocs:
            addr = self.allocs[name]
            return int.from_bytes(self.mem.get_ram(4, addr), 'little')
        else:
            raise AttributeError(f"{name} not found!")

    def _is_uninitialized(self, name):
        stack = inspect.stack()
        for frame in stack:
            if "self" in frame.frame.f_locals:
                if frame.frame.f_locals["self"].__class__ == self.__class__:
                    return False  # Already initialized
        return True  # Uninitialized

class Process_Manager:
    "Process Handling with Scheduling"

    def __init__(self, mem:Memory):
        self.mem:Memory = mem
        self.procs:dict[Process] = {}
        self.ready_queue = queue.Queue()
        self.lock = threading.Lock()
        self.current_addr = 65

    def add_proc(self, exec_data:Execution_Data, process_data:Process_Data) -> None:
        """Create and Add a New Process"""
        with self.lock:
            proc = Process(self.mem, exec_data, process_data, self.current_addr)
            self.procs[process_data.Pid] = proc
            self.ready_queue.put(proc)
            self.current_addr += exec_data.vmem_size + 1
            print(f"Process {process_data.Pid} has been added!")

    def run_next(self) -> None:
        """Execute Next Process in Queue"""
        proc = None
        with self.lock:
            if self.ready_queue.empty():
                print("No processes left to execute!")
                return

            proc:Process = self.ready_queue.get()
            # Call func
            try:
                out = proc.ProcessData.process(*proc.ProcessData.params)
            except Exception as e:
                print (f"Process {proc.ProcessData.Pid} has returned a error ->\n{e}\n")
                self.stop_proc(proc.ProcessData.Pid)
        self.stop_proc(proc.ProcessData.Pid)

    def stop_proc(self, pid:int):
        """Stop Running process"""
        with self.lock:
            if pid in self.procs:
                proc:Process = self.procs[pid]

                cleanup_val = 0
                current_mem = self.mem.current_addr

                # Cleanup Memory
                self.mem.write_ram(cleanup_val.to_bytes(proc.exec_data.vmem_size, 'little'), proc.vram_seek)

                self.mem.current_addr = current_mem

                del self.procs[pid]

    def start_debug_server(self, host:str="127.0.0.1", port:int=65432) -> None:
        """Start a TCP server in a background thread to serve debug commands."""
        def handle_client(conn, addr) -> None:
            with conn:
                conn.sendall(b"Connected to Process Manager debug terminal.\nType 'help' for commands.\n> ")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break

                    cmd = data.decode().strip()
                    if cmd == "exit":
                        conn.sendall(b"Goodbye!\n")
                        break
                    elif cmd == "list":
                        response = self._get_process_list_str()
                    elif cmd.startswith("info "):
                        pid_str = cmd[5:].strip()
                        response = self._get_process_info_str(pid_str)
                    elif cmd == "help":
                        response = ("Commands:\n"
                                    "  list - list all processes\n"
                                    "  info <pid> - show info on process\n"
                                    "  exit - exit this debug session\n")
                    else:
                        response = "Unknown command. Type 'help'.\n"

                    conn.sendall(response.encode() + b"\n> ")

        def server() -> None:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((host, port))
                s.listen()
                print(f"Debuuging Server running on {host}:{port}")
                while True:
                    conn, addr = s.accept()
                    threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
        threading.Thread(target=server, daemon=True).start()

    def _get_process_list_str(self):
        with self.lock:
            if not self.procs:
                return "No processes running."
            lines = ["Processes:"]
            for pid in self.procs.keys():
                lines.append(f"  PID: {pid}")
            return "\n".join(lines)

    def _get_process_info_str(self, pid_str):
        try:
            pid = int(pid_str, 0)
        except ValueError:
            return "Invalid PID."
        with self.lock:
            proc = self.procs.get(pid)
            if not proc:
                return f"No process with PID {pid}."
            lines = [
                f"Process {pid}:",
                f"  VRAM Addr: {proc.vram_seek}",
                f"  Data Segment Start: {proc.data_seek}",
                f"  Stack Segment Start: {proc.stack_seek}",
                f"  Heap Segment Start: {proc.heap_seek}",
                f"  Text Segment Start: {proc.text_seek}",
                f"  Allocated Vars: {list(proc.allocs.keys())}",
                f"  Allocs (var -> addr): {proc.allocs}",
            ]
            return "\n".join(lines)
