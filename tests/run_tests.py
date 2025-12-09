#!/usr/bin/env python3
"""
Run all Kipio tests
"""
import sys
import subprocess
import os

def run_tests():
    """Execute all tests"""
    print("Running Kipio tests...")
    print("=" * 6)
    
    project_root = os.path.dirname(os.path.dirname(__file__)) \
                   if os.path.basename(os.path.dirname(__file__)) == 'tests' \
                   else os.path.dirname(__file__)

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/", "-v"],
        cwd=project_root,
        capture_output=True,
        text=True
    )
    
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    
    print("=" * 60)
    print(f"Exit code: {result.returncode}")
    return result.returncode == 0

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
