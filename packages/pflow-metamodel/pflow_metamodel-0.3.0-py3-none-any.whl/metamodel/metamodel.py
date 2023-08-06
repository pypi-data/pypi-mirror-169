from metamodel.error import *


class MetaModel(object):
    """
    MetaModel serves as an internal DSL
    useful for declaring Petri-net models
    """

    def __init__(self):
        self.arcs = []
        self.places = {}
        self.transitions = {}
        self.roles = {}

    def reindex(self):
        """ load model as state machine """

        # initialize empty delta vectors
        for label, t in self.transitions.items():
            t['delta'] = [0] * len(self.places)

        for arc in self.arcs:
            t = None
            p = None
            w = 0

            if arc['source'].place != None:
                p_label = arc['source'].label
                t_label = arc['target'].label
                p = self.places[p_label]
                t = self.transitions[t_label]
                w = 0 - arc['weight']

                if 'inhibit' in arc:
                    delta = [0] * len(self.places)
                    delta[p['offset']] = w
                    t['guards'][p_label] = delta
                    continue

            if arc['source'].transition != None:
                t_label = arc['source'].label
                p_label = arc['target'].label
                t = self.transitions[t_label]
                p = self.places[p_label]
                w = arc['weight']

                if 'inhibit' in arc:
                    raise InvalidInhibitor(
                        "fx - inhibitor arcs must target transition")

            t['delta'][p['offset']] = w

        return self

    def append_arc(self, **arc):
        self._assert_valid_arc(arc['source'], arc['target'])
        self.arcs.append(arc)

    @staticmethod
    def _assert_valid_arc(a, b):
        """ test that arc defined using internal DSL is valid """
        if (a.place is not None and b.place is None) or (a.transition is not None and b.transition is None):
            return
        raise InvalidArc("%s -> %s" % (a.label, b.label))

    def role(self, name):
        """ declare roles to for ACL around transitions """
        if name in self.roles:
            raise DuplicateLabel(name)

        self.roles[name] = name
        return name

    def cell(self, label, **cell):
        """ define a place """
        if "initial" not in cell:
            cell["initial"] = 0
        if "capacity" not in cell:
            cell["capacity"] = 0
        cell["offset"] = len(self.places)
        if label in self.places:
            raise DuplicateLabel(label)
        self.places[label] = cell
        return Node(self, label, place=cell)

    def defun(self, label, **fn):
        """ define a transition function """
        if "delta" not in fn:
            fn["delta"] = [0]
        fn["offset"] = len(self.transitions)

        assert fn["role"] in self.roles

        if "guards" not in fn:
            fn["guards"] = {}

        if label in self.transitions:
            raise DuplicateLabel(label)

        self.transitions[label] = fn
        return Node(self, label, transition=fn)


class Node(object):
    """ provide points on a graph linking state machine elements """

    def __init__(self, mm, label, **place_or_transition):
        self.mm = mm
        self.label = label
        if "place" in place_or_transition:
            self.place = place_or_transition["place"]
            self.transition = None
        elif "transition" in place_or_transition:
            self.place = None
            self.transition = place_or_transition["transition"]
        else:
            raise InvalidInput("Node must be place|transition")

    def tx(self, *tx):
        """ tx 'transmit' - Connect place and transaction elements with an arc """
        self.mm.append_arc(source=self, target=tx[1], weight=tx[0])
        return self

    def guard(self, *tx):
        """ guard clause - if weight condition is satisfied, target transition is fire-able """
        self.mm.append_arc(
            source=self, target=tx[1], weight=tx[0], inhibit=True)
        return self
