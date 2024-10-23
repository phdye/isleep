import unittest
import subprocess
import sys
import time
import threading

class TestISleepCLI(unittest.TestCase):
    def test_isleep_command(self):
        # Run the `isleep` command with 0.1 seconds as input
        result = subprocess.run(
            [sys.executable, "-m", "isleep", "0.1"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # Check that the command completed successfully
        self.assertEqual(result.returncode, 0)
        self.assertIn("Sleeping for 0.1 seconds...", result.stdout)
        self.assertIn("Completed without interruption.", result.stdout)

    def test_isleep_interrupt(self):
        # This test simulates pressing a key during sleep
        def run_isleep():
            time.sleep(0.1)  # Let the sleep start
            print("Simulating key press.")
        
        # Start the isleep command in a separate thread
        thread = threading.Thread(target=run_isleep)
        thread.start()

        # Run the isleep command for 1 second
        result = subprocess.run(
            [sys.executable, "-m", "isleep", "1"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # Ensure the isleep command was interrupted
        self.assertEqual(result.returncode, 0)
        self.assertIn("Interrupted! Exiting early.", result.stdout)

        # Clean up the thread
        thread.join()

if __name__ == "__main__":
    unittest.main()
