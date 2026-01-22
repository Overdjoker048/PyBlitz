from sys import stdout, argv
from time import perf_counter_ns
from proto import compilator

if len(argv) < 2:
    stdout.write("Usage: python main.py <python_file_to_execute> [-doc] [-gui] [-asr] [-o <output name>]\n")
else:
    filename = argv[1]
    stdout.write(f"\033[38;2;34;107;223m[Compiling] \033[38;2;58;187;146m{filename}\033[0m\n")
    doc = False
    gui = False
    statue = 0
    for i in argv:
        match i:
            case "gui": gui = True
            case "doc": doc = True    

    code = open(argv[1], encoding="utf-8").read()
    start = perf_counter_ns()
    try:
        exec(code)
    except Exception as e:
        stdout.write(f"{e}\n")
        statue = 1
    end = perf_counter_ns()
    stdout.write(f"\033[38;2;34;107;223m[Done] \033[38;2;58;187;146mexited with \033[38;2;150;150;255mcode={statue} \033[38;2;58;187;146min \033[38;2;255;135;82m{(end-start)/1_000_000_000} \033[38;2;58;187;146mseconds\033[0m\n")
