#!/usr/bin/env python3

import time
import sys
import subprocess
import os

def run_condenser_with_timing():
    """Run the condenser script and measure total execution time."""
    
    print("🚀 Starting Condenser with timing...")
    print("=" * 50)
    
    # Record start time
    start_time = time.time()
    
    try:
        # Run the condenser script
        result = subprocess.run([
            sys.executable, 'direct_subset.py', '-v'
        ], 
        capture_output=False,  # Let output go to console
        text=True,
        cwd=os.getcwd()
        )
        
        # Record end time
        end_time = time.time()
        
        # Calculate runtime
        total_runtime = end_time - start_time
        
        print("\n" + "=" * 50)
        print("⏱️  TIMING RESULTS")
        print("=" * 50)
        print(f"Total Runtime: {total_runtime:.2f} seconds")
        print(f"Total Runtime: {total_runtime/60:.2f} minutes")
        print(f"Total Runtime: {total_runtime/3600:.2f} hours")
        
        if result.returncode == 0:
            print("✅ Condenser completed successfully!")
        else:
            print(f"❌ Condenser failed with exit code: {result.returncode}")
            
        return result.returncode == 0
        
    except KeyboardInterrupt:
        end_time = time.time()
        total_runtime = end_time - start_time
        print(f"\n⏹️  Script interrupted after {total_runtime:.2f} seconds")
        return False
    except Exception as e:
        end_time = time.time()
        total_runtime = end_time - start_time
        print(f"\n❌ Error occurred after {total_runtime:.2f} seconds: {e}")
        return False

if __name__ == "__main__":
    success = run_condenser_with_timing()
    sys.exit(0 if success else 1) 