from ast import NodeVisitor, Name, parse, unparse
from sys import stdout, argv

if len(argv) < 2:
    stdout.write("Usage: python main.py <python path> [-doc] [-gui] [-asr] [-icon <icon path>] [-nogc] [-o <output name>]\n")
else:
    filename = argv[1]
    gui = False
    doc = False
    asr = False
    nogc = False
    output = "filename.exe"
    output_al = False
    icon = None
    icon_al = False
    for i in argv[2:]:
        match i.lower():
            case "-gui": gui = True
            case "-doc": doc = True
            case "-asr": asr = True
            case "-nogc": nogc = True
            case "-o": output_al = True
            case "-icon": icon_al = True
            case _:
                if icon_al:
                    icon = i
                    icon_al = False
                if output_al:
                    output = i
                    output_al = False


    class A(NodeVisitor):
        __slots__ = ("v", "c", "L")
        def __init__(self, L) -> None:
            self.v = {}
            self.c = {}
            self.L = L

        def _e(self, node) -> object:
            try:
                return eval(unparse(node), self.c)
            except:
                return None

        def _s(self, nom, val, ln):
            self.c[nom] = val
            s = self.L[ln-1] if 0 <= ln-1 < len(self.L) else ""
            t = 0.0
            for ch in s:
                if ch == "\t":
                    t += 1
                elif ch == " ":
                    t += 0.25
                else:
                    break
            self.v[ln] = f"{'\t' * int(t)}{nom} = {val!r}"

        def visit_Assign(self, n):
            for t in n.targets:
                if isinstance(t, Name):
                    self._s(t.id, self._e(n.value), n.lineno)
            self.generic_visit(n)

        def visit_AnnAssign(self, n):
            if n.value and isinstance(n.target, Name):
                self._s(n.target.id, self._e(n.value), n.lineno)
            self.generic_visit(n)

        def visit_With(self, n):
            for it in n.items:
                if it.optional_vars and isinstance(it.optional_vars, Name):
                   self._s(it.optional_vars.id, self._e(it.context_expr), n.lineno)
            self.generic_visit(n)

    out = open(path, encoding="utf-8").read().splitlines
    a = A(out)
    a.visit(parse(code))

    header = [
        "from sys import stdout, dont_write_bytecode",
        "stdout.reconfigure(encoding='utf-8')",
        "dont_write_bytecode = True",
        "del dont_write_bytecode",
        "del stdout"
    ]
    if nogc:
        header.append("from gc import disable")
        header.append("disable()")
        header.append("del disable")

    for ln, rep in a.v.items():
        i = ln + len(header) - 1
        if 0 <= i < len(out):
            out[i] = rep

    text = "\n".join(out)

    # ---------------------------------------------------------
    # 🔥 Compression des sauts de ligne hors string
    # ---------------------------------------------------------
    res = []
    in_str = False
    str_char = ""
    i = 0
    last_nl = False

    while i < len(text):
        ch = text[i]
        # Début string
        if not in_str and ch in ("'", '"'):
            if text[i:i+3] in ("'''", '"""'):
                in_str = True
                str_char = text[i:i+3]
                res.append(str_char)
                i += 3
                continue
            else:
                in_str = True
                str_char = ch
                res.append(ch)
                i += 1
                continue

        # Fin string
        if in_str:
            if str_char in ("'''", '"""') and text[i:i+3] == str_char:
                in_str = False
                res.append(str_char)
                i += 3
                continue
            elif str_char in ("'", '"') and ch == str_char:
                in_str = False
                res.append(ch)
                i += 1
                continue

            res.append(ch)
            i += 1
            continue

        # Hors string → compression des \n
        if ch == "\n":
            if not last_nl:
                res.append("\n")
            last_nl = True
        else:
            last_nl = False
            res.append(ch)

        i += 1

    result = "".join(res)

#supprime les lignes saut de ligne inutiles
#implementer les fonctions a leurs endroit d'appelle au lieu de les appeller simplement
#ajouter les __slots__ pour les classes
#recuperer les sorties consoles
