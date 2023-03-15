#!/usr/bin/env python3

import sys, os


alive_cells      = "*"
dead_cells       = " "
grid_size        = 30
gens_to_sim      = 30
file_out_path    = '110_out.txt'

RULE = {
    '111': 0b0, 
    '110': 0b1, 
    '101': 0b1, 
    '100': 0b0, 
    '011': 0b1,
    '010': 0b1,
    '001': 0b1,
    '000': 0b0
}

def format_line(gen: list[int]):
    return ''.join([dead_cells if x == 0 else alive_cells for x in gen])

def write_outfile(buf: list[str]):
    with open('output/'+file_out_path, 'w') as fout:
        for line in buf:
            fout.write(line+'\n')

def generate() -> list[str]:
    size = grid_size
    generations = gens_to_sim
    this_gen = [0] * size
    next_gen = [0] * size
    buf = []

    #set up first gen
    this_gen[-1] = 1

    buf.append(format_line(this_gen))

    for i in range(generations):
        for i, x in enumerate(this_gen):
            if i == 0:
                next_gen[0] = RULE.get(str(x) + str(this_gen[1]) + str(this_gen[2]))
            elif i == (size-1):
                next_gen[i] = RULE.get(str(this_gen[i-2]) + str(this_gen[i-1]) + str(x))
            else:
                next_gen[i] = RULE.get(str(this_gen[i-1]) + str(x) +  str(this_gen[i+1]))
       
        buf.append(format_line(next_gen))
        this_gen = next_gen
    
    write_outfile(buf)

def usage():
    print(f'USAGE: {sys.argv[0]} -o <name of output file> generates a rule 110 and writes it to a file.')
    print('optional flags') 
    print('-w <width of field> default is 30 chars')
    print('-g <number of generations to simulate> default is 30')
    print('-a <char for alive cells> default is `*`')
    print('-d <char for dead cells> default is ` `')
    print('-h print this help menu')

def check_flags():
    if len(sys.argv) > 1:    
        args = sys.argv[1:]
        for i, a in enumerate(args):
            match a:
                case '-o':
                    try:
                        global file_out_path
                        file_out_path = args[i+1] 
                    except:
                        print("No argument provided for `-o`")
                        print(args)
                        exit(1)
                case '-w':
                    try:
                        global grid_size
                        grid_size = int(args[i+1])
                    except:
                        print("No argument provided for `-w`")
                        print(args)
                        exit(1)
                case '-g':
                    try:
                        global gens_to_sim
                        gens_to_sim = int(args[i+1])
                    except:
                        print("No argument provided for `-g`")
                        print(args)
                        exit(1)
                case '-a':
                    try:
                        global alive_cells
                        alive_cells = args[i+1]
                    except:
                        print("No argument provided for `-a`")
                        print(args)
                        exit(1)
                case '-d':
                    try:
                        global dead_cells
                        dead_cells = args[i+1]
                    except:
                        print("No argument provided for `-d`")
                        print(args)
                        exit(1) 
                case '-h':
                    usage()
                case _:
                    pass


def make_outdir():
    pwd = os.getcwd()
    if(not os.path.exists(pwd+'/output')):
        os.mkdir('output')

def main():
    check_flags()
    make_outdir()
    generate()
    






if __name__ == "__main__":
    main()