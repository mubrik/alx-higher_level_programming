#!/usr/bin/python3
import dis
import marshal


def main():
    with open('hidden_4.pyc', 'rb') as f:
        f.seek(16)
        for instruction in dis.get_instructions(marshal.load(f)):
            if not instruction.opname == "STORE_NAME":
                continue
            elif not str(instruction.argval).startswith("_"):
                print(instruction.argval)


if __name__ == "__main__":
    main()
