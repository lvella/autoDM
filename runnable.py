# coding=UTF-8

import random
import bisect

def apply_hability_hierarchy(props, hierarchy):
    for h in hierarchy:
        for i in xrange(len(h)):
            if h[i] in props:
                for j in xrange(i+1, len(h)):
                    props.discard(h[j])
    return props

class choice:
    "Relates ranges of probabilities to other runnables."

    def __init__(self, name, data):
        self.keys = []
        self.vals = []
        self.name = name
        data.sort();
        i = 0
        for e in data:
            if i != e[0]:
                i = e[0]
                self.keys.append(i)
                self.vals.append(e[1])

    def run(self):
        r = random.randint(1, self.keys[-1])
        elem = self.vals[bisect.bisect_left(self.keys, r)]

        res = None
        try:
            res = elem.run()
        except AttributeError:
            res = elem
        return (self.name, res)

class value:
    "Defines a random runnable value."

    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

    def run(self):
        def d(num, size):
            return sum([random.randint(1, size) for x in range(num)])

        return (self.name, '%d' % (eval(self.expr)))

class CP(value):
    def __init__(self, expr):
        value.__init__(self, 'Peças de cobre', expr)


class SP(value):
    def __init__(self, expr):
        value.__init__(self, 'Peças de prata', expr)

class GP(value):
    def __init__(self, expr):
        value.__init__(self, 'Peças de ouro', expr)

class PP(value):
    def __init__(self, expr):
        value.__init__(self, 'Peças de platina', expr)

def mrun(runnable):
    "Funtion to be mapped to lists of runnables."

    try:
        return runnable.run()
    except AttributeError:
        return runnable

class array:
    "Allows multiple runnables' results at once."

    def __init__(self, name, array):
        self.name = name
        self.array = array

    def run(self):
        return (self.name, map(mrun, self.array))

class mult:
    "Evaluates one runnable multiple times."

    def __init__(self, name, num, runnable):
        self.name = name
        self.num = num
        self.runnable = runnable

    def run(self):
        res = []
        for i in range(self.num):
            try:
                res.append(self.runnable.run())
            except AttributeError:
                res.append(self.runnable)
        return (self.name, res)

def unify(p):
    "Creates a single list of primitives discarding the names from results."

    ret = []
    if isinstance(p, list):
        for e in p:
            ret.extend(unify(e))
    elif isinstance(p, tuple):
        ret.extend(unify(p[1]))
    else:
        ret.append(p)
    return ret

class property:
    "Defines a random set of properties to a runnable's result."

    def __init__(self, ch, runnable):
        self.choice = ch
        self.runnable = runnable

    def run(self):
        props = ', '.join(set(unify(self.choice.run())))

        try:
            res = self.runnable.run()
            return (res[0], (props, res[1]))
        except AttributeError:
            return (props, self.runnable)

class sized(property):
    "Size property to mundane armors."

    def __init__(self, runnable):
        self.choice = choice('', [(10, 'Pequeno'), (100, 'Médio')])
        self.runnable = runnable

class msized(property):
    "Size property to magic armors."

    def __init__(self, runnable):
        self.choice = choice('', [(30, 'Pequeno'),
                                  (90, 'Médio'),
                                  (100, 'Tamanho a escolha do meste')])
        self.runnable = runnable

class name:
    "Applies a name to a runnable."

    def __init__(self, name, runnable):
        self.name = name
        self.runnable = runnable
    def run(self):
        try:
            run = self.runnable.run()
            return (run[0], (self.name, run[1]))
        except AttributeError:
            return (self.name, self.runnable)

class callable:
    "Runnable that runs a function."

    def __init__(self, name, function):
        self.name = name
        self.function = function

    def run(self):
        return (self.name, self.function())
