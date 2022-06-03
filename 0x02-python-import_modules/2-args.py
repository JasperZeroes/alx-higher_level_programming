    #!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if num == 1:
        print("{} arguments.".format(num - 1))
    elif num == 2:
        print("{} argument:".format(num - 1))
    else:
        print("{} arguments:".format(num - 1))

    for i in range(1, num):
        print("{}: {}".format(i, sys.argv[i]))
    
    
    '''parser = argparse.ArgumentParser()
    parser.add_argument("number1", help = "first number")
    parser.add_argument("number2", help = "second number")
    parser.add_argument("operation", help = "operation")

    args = parser.parse_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)
    print(len(args))'''

    '''if args.operation == "add":
        result = int(args.number1) + int(args.number2)
        print("Result:", result)
    elif args.operation == "subtract":
        result = int(args.number1) - int(args.number2)
        print("Result:", result)
    elif args.operation == "multiply":
        result = int(args.number1) * int(args.number2)
        print("Result:", result)
    elif args.operation == "division":
        result = int(args.number1) / int(args.number2)
        print("Result:", int(result))
    else:
        print("Unsupported Operation")'''
