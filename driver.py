from argparse import ArgumentParser
import subprocess
import ast
import subprocess

def run_python_script(script_args,script_path):
    """
    Runs a Python script using subprocess.
    Args:
        script_path: str; the path to the Python script.
        script_args: list; a list of command line arguments for the script.
    Return: The entire output of the Python script.
    """
    command = ['python', script_path] + script_args
    process = subprocess.Popen(command, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output.decode('utf-8')  # Return the output as a string

# Example usage


#我还需要一个函数，来把args dict整合并且传递给python
def configure_python_command_line(args_dict):
    """
    Builds a list of command line arguments for running a Python script.
    Args:
        args_dict: a dictionary of script arguments.
    Returns:
        A list of command line arguments.
    """
    clargs = []

    # Extract the script file name from args_dict
    script = args_dict.pop('script')

    # Iterate over args_dict to build command line arguments
    for arg, value in args_dict.items():
        # Handle boolean arguments
        if isinstance(value, bool):
            clargs.append(f'{str(value).upper()}')
        # Handle other types of arguments
        else:
            clargs.append(f'{value}')

    # Insert the script file at the beginning of clargs
    clargs.insert(0, script)
    return clargs



def main():
    parser = ArgumentParser()
    script_path = 'ED_score_for_hpc.py'  # Your Python script path
    parser.add_argument('-arg1', '--arg1', default=1, type=float)

    args_dict = vars(parser.parse_args())
    args_dict['script'] = 'ED_score_for_hpc.py'
    #print(args_dict)
    clargs =configure_python_command_line(args_dict)
    python_result = run_python_script(clargs,script_path)
   
    python_result = python_result.split('\n')
   # print(python_result)
    python_result.remove('')

    python_result1 = ', '.join(str(x) for x in python_result)
    list_python_result1 = eval(python_result1)
    python_result2 = ', '.join(str(x) for x in list_python_result1)
    print(python_result2)


if __name__ == "__main__":
    main()


