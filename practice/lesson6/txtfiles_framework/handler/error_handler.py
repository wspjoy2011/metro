def check_errors(filename):
    """Check for exceptions with file"""
    try:
        with open(filename, 'r'):
            pass
    except FileNotFoundError as error:
        return error
    except UnicodeDecodeError:
        return 'Application works only with txt files'
