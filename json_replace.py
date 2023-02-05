import re, enum, ast


class Replacement(enum.Enum):
    TO_UPPERCASE = 1
    TO_LOWERCASE = 2
    UPPERCASE_TO_UNDERSCORE = 3
    UPPERCASE_TO_UNDERSCORE_UPPERCASE = 4
    UPPERCASE_TO_UNDERSCORE_LOWERCASE = 5
    LOWERCASE_TO_UNDERSCORE_UPPERCASE = 6
    LOWERCASE_TO_UNDERSCORE_LOWERCASE = 7
    UPPERCASE_TO = 8
    LOWERCASE_TO = 9


class JSONReplace:
    def __init__(self, json_content) -> None:
        if type(json_content) == dict:
            self.json_content = json_content
        elif type(json_content) == str:
            self.json_content = ast.literal_eval(json_content)
        else:
            raise TypeError(f'json_content must be str json or dict type, got {type(json_content)} type')
        

    def replace_key(self, *args) -> None:
        if len(args)<1:
            raise(f"replace key must take minimum 1 argument")
        print(f'args0: {args[0]}')
        if args[0] in [val for val in Replacement]:
            print(f'args0: {args[0]}')
            if args[0] == Replacement.TO_UPPERCASE :
                self.reformat_all_keys(self.json_content, '([a-z])', lambda x: x.group(1).upper())
            if args[0] == Replacement.TO_LOWERCASE:
                self.reformat_all_keys(self.json_content, '([A-Z])', lambda x: x.group(1).lower())
            if args[0] == Replacement.UPPERCASE_TO_UNDERSCORE:
                self.reformat_all_keys(self.json_content, '([A-Z])', '_')
            if args[0] == Replacement.UPPERCASE_TO_UNDERSCORE_UPPERCASE:
                self.reformat_all_keys(self.json_content, '([A-Z])', r'_\1')
            if args[0] == Replacement.UPPERCASE_TO_UNDERSCORE_LOWERCASE:
                self.reformat_all_keys(self.json_content, '([A-Z])',lambda x: f"_{x.group(1).lower()}")
            if args[0] == Replacement.LOWERCASE_TO_UNDERSCORE_UPPERCASE:
                self.reformat_all_keys(self.json_content, '([a-z])', lambda x: f"_{x.group(1).upper()}")
            if args[0] == Replacement.LOWERCASE_TO_UNDERSCORE_LOWERCASE:
                self.reformat_all_keys(self.json_content, '([a-z])', r'_\1')
            if args[0] == Replacement.UPPERCASE_TO:
                if len(args)<2:
                    raise AttributeError(f'missing second argument of args when using UPPERCASE_TO \n give the string to replace UPPERCASE as additional argument')
                else:
                    self.reformat_all_keys(self.json_content, '([A-Z])', args[1])
            if args[0] == Replacement.LOWERCASE_TO:
                if len(args)<2:
                    raise AttributeError(f'missing second argument of args when using LOWERCASE_TO \n give the string to replace LOWERCASE as additional argument')
                else:
                    self.reformat_all_keys(self.json_content, '([a-z])', args[1])
        elif args[0] in [val.value for val in Replacement]:
            raise AttributeError(f'please pass a name present in Replacement: {list(Replacement)}')
        else:
            raise AttributeError(f'please pass a name present in Replacement: {list(Replacement)}')


    def reformat_all_keys(self, d, regex_from, regex_to):
        for key in list(d.keys()):
            if isinstance(d[key], dict):
                self.reformat_all_keys(d[key], regex_from, regex_to)
            if key != re.sub(regex_from, regex_to,key):
                d[re.sub(regex_from, regex_to,key)] = d.pop(key)