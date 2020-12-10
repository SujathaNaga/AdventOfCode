from time import sleep, time
import cProfile
import pstats
import datetime
from io import StringIO

def get_file_contents(filename, add_last_empty_entry=True):
    rows = []
    with open(filename,"r") as file:
        for line in file:
            rows.append(line.rstrip()) # remove trailing newline whitespaces etc
    
    if add_last_empty_entry:
        # add empty last line so that all the entries will be processed properly in some puzzles where the file ends exactly at the last input line
        rows.append('')
    
    return rows

class profiler:
    start_time = 0
    elapsed = 0
    pr = cProfile.Profile()
    profile_file = 0

g_profiler = profiler()

def start_profiling():
    global g_profiler
    g_profiler.start_time = time()
    #filename = ("log-" + datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S") + ".txt")
    filename = ("log.txt")
    g_profiler.profile_file = open(filename, "w")
    g_profiler.pr.enable()

def end_profiling():
    global g_profiler
    g_profiler.pr.disable()
    g_profiler.elapsed = time() - g_profiler.start_time
    s = StringIO()
    sortby = 'cumulative'
    profile_stats = pstats.Stats(g_profiler.pr, stream=s).sort_stats(sortby)
    profile_stats.print_stats()
    g_profiler.profile_file.write(f'\n----------------------------------------------\n')
    g_profiler.profile_file.write(f'elapsed time for  profile: {g_profiler.elapsed}\n')
    g_profiler.profile_file.write(s.getvalue())
    print(f'\nelapsed time: {g_profiler.elapsed}\n')