#!/usr/bin/env python3

import os
import signal
import subprocess
import sys
import threading
import atexit
from pathlib import Path
from typing import Union


def wait_for(fn: Callable[[], bool], timeout_s: int, delay_s=1)-> Union[bool, float]:
    time_started = time.time()
    while time.time() - time_started < timeout_s:
        if fn():
            return time.time()-time_started
        time.sleep(delay_s)
    return False


class TTYDuplicator():
    def __init__(self, real_tty: Path, log_file: Path):
        self._the_thread = threading.Thread(target=self._run)
        self._the_thread.setDaemon(True)
        self.real_tty = real_tty
        # Has to be reproducible to support multiple instances
        self.fake_tty = Path("/tmp") / f"{real_tty.stem}.duplicated"
        self.log_file = log_file
        self.tmp_file = Path(str(self.fake_tty) + ".tmp")
        self._stop_event = threading.Event()
        self._subproc: Optional[subprocess.Popen] = None
        atexit.register(self.stop)

    def start(self):
        self._the_thread.start()
        wait_for(self.exists, 1, delay_s=0.1)

    def stop(self):
        if self._subproc:
            self._stop_event.set()
            os.killpg(os.getpgid(self._subproc.pid), signal.SIGTERM)
            self._subproc.wait()
            self._subproc = None
            self._the_thread.join()
            self._cleanup()

    def exists(self):
        return self.fake_tty.exists()

    def _dup_tty(self):
        command = f'''socat \
            '{self.real_tty},raw,echo=0' \
            'SYSTEM:tee {self.log_file} \
            | socat - "PTY,link={self.fake_tty},raw,echo=0,waitslave,ignoreeof" \
            | tee {self.tmp_file}'
        '''
        self._subproc = subprocess.Popen(
            command, shell=True, stderr=sys.stderr, stdout=sys.stdout, start_new_session=True)

    def _cleanup(self):
        """Should not be required, but might be in case the socat process fails"""
        for file in [self.fake_tty, self.tmp_file]:
            try:
                os.remove(file)
            except FileNotFoundError:
                pass

    def _run(self):
        if self.exists():
            return
        while True:
            self._dup_tty()
            self._subproc.wait()
            if self._stop_event.isSet():
                break
            print("dup_tty stopped")
            with open(self.log_file, "a", encoding="utf-8") as logfile:
                logfile.write(f"#################### TTY {self.real_tty} DISAPPEARED\n")
        # Cleanup
        try:
            self.tmp_file.unlink()
            self.fake_tty.unlink()
        except FileNotFoundError:
            pass
