import random
import socket
from Bot import Bot

class ChatterBot(Bot):
    def __init__(self, filename, server, channel, nick):
        self.grammar = {}
        self.parseGrammar(filename)
        Bot.__init__(self, server, channel, nick)
    
    def parseGrammar(self, filename):
        file = open(filename, 'r')
        line = file.readline()
        while line != "":
            self.addToGrammar(line)
            line = file.readline()
    
    def addToGrammar(self, line):
        line.strip()
        terminals = line.split("::=")
        nonterminal = terminals[0]
        rules = terminals[1].split("|")
        rule_list = []
        for rule in rules:
            tokens = tuple(rule.split())
            rule_list.append(tokens)
        self.grammar[nonterminal] = rule_list

    def generate(self, nonterminal):
        rules = self.grammar.get(nonterminal)
        if rules is None:
            nonterminal += " "
            return nonterminal

        rule = self.pickRule(rules)
        generated = ""
        for terminal in rule:
            generated += self.generate(terminal)
        return generated

    def pickRule(self, rules):
        index = random.randint(0, len(rules) - 1)
        return rules[index]
