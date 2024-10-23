import unittest
import os
from isleep.core import interruptible_sleep

class TestISleep(unittest.TestCase):

    def test_interruptible_sleep(self):
        # Create a pipe (reader and writer).
        read_fd, write_fd = os.pipe()

        try:
            # Wrap the read end in a file-like object.
            read_stream = os.fdopen(read_fd)

            # Ensure the sleep completes without interruption (no input).
            interruptible_sleep(0.1, input_stream=read_stream)
        finally:
            # Close the file descriptors after the test.
            os.close(write_fd)
            read_stream.close()

if __name__ == "__main__":
    unittest.main()
