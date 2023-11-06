import argparse

argparser = argparse.ArgumentParser(description="A simple CLI program with subcommands")

subparsers = argparser.add_subparsers(title="commands", dest="command", description="is this description ever seen?")

# Sub Command 1: generate_tcl
parser_command1 = subparsers.add_parser("generate_tcl", help="Generate the Tcl script used by Vivado to create BD, synthesis, implement and generate bitstream!")
parser_command1.add_argument("--hdlgen", help="Path to HDLGen file")

# Sub Command 2: run_vivado
parser_command2 = subparsers.add_parser("run_vivado", help="Runs the Tcl script created by the generate_tcl command!")
parser_command2.add_argument("--hdlgen", help="Path to HDLGen file")

# Parse the command-line arguments
args = argparser.parse_args()

# Run commands:
if args.command == "generate_tcl":
    if args.hdlgen:
        print(f"Executing generate_tcl with argument: {args.hdlgen}")
    else:
        print("Error: No path to HDLGen project specified")
elif args.command == "run_vivado":
    if args.hdlgen:
        print(f"Executing run_vivado with argument: {args.hdlgen}")
    else:
        print("Error: No path to HDLGen project specified")
else:
    print("No command specified")