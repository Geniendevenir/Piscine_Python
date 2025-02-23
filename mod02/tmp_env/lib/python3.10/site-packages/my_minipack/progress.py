import time
import sys

def ft_progress(lst):
    total = len(lst)
    start_time = time.time()  # Start timing

    for i, num in enumerate(lst):
        percent = (i + 1) / total * 100  # Compute progress percentage
        elapsed_time = time.time() - start_time  # Compute elapsed time
        eta = (elapsed_time / (i + 1)) * (total - (i + 1)) if i > 0 else 0  # Estimate remaining time

        # Progress bar with ETA
        bar = "=" * int(percent // 4) + ">" # Adjust length to fit within 50 characters
        #sys.stdout.write(f"\r[{bar:<10}] {percent:.2f}% ETA: {eta:.2f}s")
        sys.stdout.write(f"\rETA: {eta:.2f}s [{percent:.2f}%] [{bar:<25}] | elapsed time {elapsed_time:.2f}s")
        sys.stdout.flush()
        yield num  # Yield the current value
    #print()  # Move to new line when complete

# Example usage
listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
