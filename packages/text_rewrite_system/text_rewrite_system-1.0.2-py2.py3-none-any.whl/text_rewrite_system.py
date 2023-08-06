"""
Generates Python functions capable of rewriting text according to pre-defined rules.
"""

__version__ = "1.0.2"

import json
import re
import argparse

from sys import argv

from lark import Lark, Transformer, Token

class RTTransformer(Transformer):
    def rt(self, content):
        if len(content) == 2:
            (name, values) = content
            args = dict()
        elif len(content) == 3:
            (name, args, values) = content
        return {"name": name, "arguments": args, "rules": values}

    def fname(self, fname):
        (fname,) = fname
        return fname.value

    def farguments(self, args):
        return dict(args)

    def fargument(self, arg):
        (key,value,) = arg
        return (key.value, value.value)

    def pairs(self, pairs):
        return list(pairs)

    def callable(self, c):
        return ("callable", ''.join(c))
    
    def argument(self, a):
        return ''.join(a)

    def pair_tc(self, terms):
        k, v = terms
        return {"type": v[0], "original": k[1], "converted": v[1]}

    def pair_conditional(self, terms):
        k, c = terms
        return {"type": "conditional", "original": k[1]} | c

    def term(self, s : Token):
        if len(s) > 0:
            return ("term", s[0].value.strip('"'))
        else:
            return ("term", "")

    def conditional(self, c):
        (cond, (if_true_t, if_true_v), (if_false_t, if_false_v),) = c
        return {"condition": cond, "if_true": {"type": if_true_t, "converted": if_true_v}, "if_false": {"type": if_false_t, "converted": if_false_v}}

    def conditional_no_else(self, c):
        (cond, (if_true_t, if_true_v),) = c
        return {"condition": cond, "if_true": {"type": if_true_t, "converted": if_true_v}}

    def cond_in(self, c):
        return ' '.join(c)

    def cond_call(self, c):
        ((_,call),) = c
        return call

grammar = r"""
rt : _DEFRT fname ("(" farguments ")")? pairs _ENDRT

fname : CNAME

farguments : fargument+
fargument : CNAME "=" /\w+/

pairs : pair+
pair : term "=>" (term | callable) -> pair_tc
     | term "=>" (conditional | conditional_no_else) -> pair_conditional
!callable : (CNAME ".")* CNAME "(" (argument ",")* argument ")"
!argument : ("$" INT) | ESCAPED_STRING | CNAME

conditional : condition "?" (term | callable) ":" (term | callable)
conditional_no_else : condition "?" (term | callable)

!condition : argument ("not"? "in" | "==" | "!=") argument -> cond_in
           | callable -> cond_call

term : ESCAPED_STRING

_DEFRT : "defrt"
_ENDRT : "endrt"

%import common.WS
%import common.CNAME
%import common.ESCAPED_STRING
%import common.INT

%ignore WS
"""

def convert_file(filename, output_file=None):

    parser = Lark(grammar, start="rt", parser='lalr')

    with open(filename, encoding="UTF-8") as f:
        content = f.read()

    imports_re = re.search(r"import re", content) != None

    def convert(s):
        global imports_re

        p = parser.parse(s.group(0))
        d = RTTransformer().transform(p)
        l_str = json.dumps(d["rules"], indent=4, ensure_ascii=False)

        return (f"""
def {d['name']}(text):
    conversions = {l_str}

    aux = "➡️" + text

    while re.search(r"➡️\\Z", aux) == None:
        matched = False
        for c in conversions:
            k = re.sub(r"{{(.*?)(?<!\\\\)}}", r"(\\1)", re.sub(r"{{}}",r"((?:\\\\w|['-]\\\\w)+)", c["original"]))
            match = re.search(fr"➡️{{k}}", aux, re.IGNORECASE)
            if not match: 
                continue
            """
    + ("""
            matched_text = match.group(0).lstrip("➡️")
            first_word = matched_text.split()[0]
            if matched_text.istitle():
                sanitizer = lambda x: str.title(x)
            elif first_word[0].isupper() and (first_word[1:].islower() or len(first_word) == 1 and first_word != "I"):
                sanitizer = lambda x: str.upper(x[0]) + x[1:]
            else:
                sanitizer = lambda x: x
            
            """ if d["arguments"].get("case") == "smart" else 
        """
            sanitizer = lambda x: x
        """)
    + (f"""
            if c["type"] == "conditional":
                cond = re.sub(r"\\$(\\d)", r"match.group(\\1)", c["condition"])
                if eval(cond):
                    c = c["if_true"]
                elif "if_false" in c:
                    c = c["if_false"]
                else:
                    continue
            """ 
        if "conditional" in (x["type"] for x in d["rules"]) else "")
    + f"""
            match c["type"]:
                case "term":
                    v = 'f"' + re.sub(r"\\$(\\d)",r"{{_x[\\1]}}", c["converted"]) + '"'
                case "callable":
                    v = re.sub(r"\\$(\\d)", r"_x[\\1]", c["converted"])
            (aux,i) = re.subn(fr"➡️{{k}}", lambda m: sanitizer(apply_conversion(m,v)) + "➡️", aux, flags=re.IGNORECASE)
            if i > 0:
                matched = True
                break
        if not matched:
            aux = re.sub(r"➡️(.)", r"\\1➡️", aux, flags=re.DOTALL)

    return aux.rstrip('➡️')
    """)

    (content,i) = re.subn(r"defrts?\s.*?\sendrt", lambda fn: convert(fn), content, 0, re.DOTALL)

    if i > 0:
        content = """
def apply_conversion(_m,_v):
    _x = [_m.group(0).lstrip("➡️"), *_m.groups()]
    return eval(_v)

    """ + content
        if not imports_re:
            content = "import re\n\n" + content

    new_filename = '.'.join(filename.split('.')[:-1]) + ".py" if not output_file else output_file
    with open(new_filename, "w", encoding="UTF-8") as f:
        f.write(content)

    return new_filename


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("input_file", help="O ficheiro que contém a(s) função/funções de reescrita textual.", type=str)
    parser.add_argument("-o", "--output", help="O ficheiro convertido.", type=str)

    args = parser.parse_args()
    
    convert_file(args.input_file, args.output)

if __name__ == '__main__':
    main()