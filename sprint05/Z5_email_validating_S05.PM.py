import re
regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
def valid_email(str):
    try:
        if not re.fullmatch(regex,str):
            raise
        else:
            return "Email is valid"
    except:
        return "Email is not valid"
print(valid_email("exam@ple@sourcepath.com"))