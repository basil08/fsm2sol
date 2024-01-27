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
    # add the custom data types namely T_custom
    buffer += "\t// Variable definitions"
    buffer += "\n\t{0}".format(';\n'.join([e for e in inp['T_custom']]))
    variables = [inp['type_C'][i]
        + " " + inp['access_C'][i]
        + " " + inp['C'][i] for i in range(len(inp['type_C']))]
    buffer += "\n\t{0}".format(';\n\t'.join(variables))
    buffer += ";\n\n" 
    return buffer

def stateDef(inp, buffer):

    buffer += "\t// State definitions"
    states = ', '.join(inp['S'])
    buffer += "\n\tenum States {{ {0}  }};".format(states)
    buffer += "\n\tStates private state = States.{0};\n".format(inp['S0'])
    return buffer

def transitionDef(inp, buffer):
    trs = inp['transitions']
    buffer += "\n\t// Transition definitions "
    for tr in trs:
        buffer += add_transition(trs[tr])

    return buffer

def add_transition(tr):
    """
    Adds one transition to the buffer
    """
    # TODO: ensure len(tr['I']) == len(tr['type_I'])
    print(tr)
    variables = ', '.join(tr['type_I'][i] + " " + tr['access_I'][i] + " " + tr['I'][i] for i in range(len(tr['I'])))
    returns = " returns ({})".format(', '.join([e for e in tr['returns']]))
    guards = "require ({});".format("&&".join(tr['t_guards']))
    stmts = ";\n\t".join(tr['t_stmts'])

    buffer = "\n\t {0} {1} ({2}) {3} {4} {{\n \
        {5}  \
        {7} \
        {8} \
        {6} \
        }}\n".format(
            "function" if not tr['isConst'] else "",
            tr['name'] ,
            variables,
            "payable" if tr['payable'] else "",
            returns if len(tr['returns']) > 0 else "",
            "requires(state == States.{});\n".format(tr['t_from']) if tr['t_from'] else "",
            "state = States.{};\n".format(tr['t_to']) if tr['t_to'] else "",
            guards if len(tr['t_guards']) > 0 else "",
            stmts + ";" if len(tr['t_stmts']) > 0 else "",
        )

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
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("input", nargs='+', help="path to input YAML file(s) specifying FSM(s)")
    args = arg_parser.parse_args()

    if len(args.input) > 0:
        for input_file in args.input:
            try:
                with open(input_file, "r") as file:
                    input_fsm = yaml.safe_load(file)
                    output_sol = transform2sol(input_fsm)
                    # TODO: what if input_fsm['name] is not defined?
                    with open('{}.sol'.format(input_fsm['name']), "w") as output:
                        output.write(output_sol)
                        print("[+] Written {}.sol file".format(input_fsm['name']))
            except FileNotFoundError as e:
                print("Cannot find file: {} :/".format(e.filename))

if __name__ == "__main__":
    main()