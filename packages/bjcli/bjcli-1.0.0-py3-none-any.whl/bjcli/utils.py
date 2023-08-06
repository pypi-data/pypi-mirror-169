import os
from typing import Union


def create_workers(workers: int) -> Union[set[int], None]:
    pids = set()

    for i in range(workers):
        print(f'Forking worker #{i + 1}')

        pid = os.fork()

        print(f'Forked worker #{i + 1}')

        if pid > 0:
            #  On master

            pids.add(pid)
        elif pid == 0:
            #  In worker

            return None
    
    return pids
