import sys
import time
import os
from typing import Tuple

CIRCLE = "o"
SQUARE = "c"
TEST_EXTENSION = ".md"
TIME_LIMIT = 1
MAX_LEN = 30


def error(m: str):
    sys.stderr.write(f"Error: {m}\n")
    sys.exit(1)


def show(s: str) -> str:
    if len(s) <= MAX_LEN:
        return s
    else:
        return s[:MAX_LEN] + "..."


try:
    from entregable4 import process
except Exception as e:
    error(f"Exception while importing maxDiff:\n{e}")


def read_problem(fname: str) -> Tuple[int, str]:
    base, ext = os.path.splitext(fname)
    if ext != TEST_EXTENSION:
        error(f"The extension of {fname} is not {TEST_EXTENSION}")
    parts = base.split("_")
    try:
        solution = int(parts[-1])
    except Exception as e:
        error(f"The name of the file does not contain the size of the solution. Is this a correct test?")
    try:
        with open(fname) as f:
            problem = f.readline().strip()
    except Exception as e:
        error(f"Exception while reading {fname}:\n{e}")
    return solution, problem
    

def check_solution(solution: int, problem: str):
    try:
        t1 = time.process_time()
        answer = process(problem)
        t2 = time.process_time()
    except Exception as e:
        error(f"Exception raised while calling process with string {show(problem)}:\n{e}")
    try:
        found, b, e = answer
    except TypeError as e:
        error(f"I cannot unpack the result of process ({answer}), is it a tuple?")
    if found != solution:
        error(f"Bad solution, expected {solution} but found {found}")
    if b < 0 or b >= len(problem):
        error(f"Bad interval for the solution, the first component {b} is out of range")
    if e < 0 or e > len(problem):
        error(f"Bad interval for the solution, the second component {e} is out of range")
    ci = 0
    sq = 0
    for i in range(b, e):
        if problem[i] == CIRCLE:
            ci += 1
        else:
            sq += 1
    d = abs(sq - ci)
    if found != d:
        error(f"The reported interval has a difference of {d} instead of {solution}")
    if t2 - t1 > TIME_LIMIT:
        error(f"Time limit exceeded. Total time: {t}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        error("bad number of parameters, I need just the test file")
    fname = sys.argv[1]
    solution, problem = read_problem(fname)
    check_solution(solution, problem)
    print("OK")
