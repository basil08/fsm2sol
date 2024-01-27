import yaml
import argparse

def defaultOpening(inp, buffer):
    """
    Add the default opening 
    """
    if 'name' not in inp.keys() or not inp['name']:
        inp['name'] = 'Untitled'
    buffer += "contract {0} {{ \n\tuint private creationTime = now; \n".format(inp['name'])        
    return buffer

def defaultClosing(inp, buffer):
    buffer += "\n}"
    return buffer

def variableDef(inp, buffer):
    return buffer

def stateDef(inp, buffer):
    return buffer

def transitionDef(inp, buffer):
    return buffer

def transform2sol(inp):
    """
    generate a [input].sol file in the `CWD`
    assumes that input is a well-formed FSM
    """
    buffer = ''
    buffer = defaultOpening(inp, buffer)
    buffer = variableDef(inp, buffer)
    buffer = stateDef(inp, buffer)
    buffer = transitionDef(inp, buffer)
    buffer = defaultClosing(inp, buffer)
    return buffer

def main():
    # take a .fsm file
    # parse it
    # generate a .sol file

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("input", help="path to input YAML file specifying FSM")
    args = arg_parser.parse_args()

    if args.input:
        with open(args.input, "r") as file:
            input_fsm = yaml.safe_load(file)
            output_sol = transform2sol(input_fsm)
            with open('{}.sol'.format(input_fsm['name']), "w") as output:
                output.write(output_sol)
                print("[+] Written .sol file")


if __name__ == "__main__":
    main()