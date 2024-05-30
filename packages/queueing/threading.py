""" Threading system """

import asyncio
import threading
from typing import Any


class Threading:
    """
    Threading class for asynchronous tasking

    attributes:
        loop: asyncio loop
        thread: a separate thread from main thread
        process_count: how much current process are being processed
        max_process_count: the maximum process to be processed at the same time

    methods:
        start_thread_loop(asyncio_loop) -> None
        start_thread() -> None
        stop_thread() -> None
        begin_process() -> None
        end_process() -> None
        is_available() -> is_available(bool)
        run_async(function,*args) -> None
    """

    loop: asyncio.AbstractEventLoop | None = None
    thread: threading.Thread | None = None

    process_count: int = 0
    max_process_count: int = 3

    @classmethod
    def start_thread_loop(cls, asyncio_loop: asyncio.AbstractEventLoop) -> None:
        """
        Starts an asyncio loop

        :param asyncio_loop: asyncio event loop
        :return: None
        """
        asyncio.set_event_loop(asyncio_loop)
        asyncio_loop.run_forever()

    @classmethod
    def start_thread(cls) -> None:
        """
        Starts the thread

        :return: None
        """
        cls.loop = asyncio.new_event_loop()
        cls.thread = threading.Thread(target=cls.start_thread_loop, args=(cls.loop,))
        cls.thread.start()

    @classmethod
    def stop_thread(cls) -> None:
        """
        Stop the thread

        :return: None
        """
        if cls.loop is not None and cls.thread is not None:
            cls.loop.call_soon_threadsafe(cls.loop.stop)
            cls.thread.join()

    @classmethod
    def begin_process(cls) -> None:
        """
        Begin a process, reducing process quota

        :return: None
        """
        cls.process_count += 1

    @classmethod
    def end_process(cls) -> None:
        """
        End a process, reverts the quota back

        :return: None
        """
        cls.process_count -= 1

    @classmethod
    def is_available(cls) -> bool:
        """
        Check if available for a process to be run in the limited quota

        :return: is_available(bool)
        """
        if cls.process_count < cls.max_process_count:
            return True
        return False

    @classmethod
    def run_async(cls, function: Any, *args: Any) -> None:
        """
        Run an asynchronous task in the separate thread

        :param function: the function you want to run
        :param args: the arguments for the function
        :return: None
        """
        cls.loop.call_soon_threadsafe(asyncio.create_task, function(*args))
