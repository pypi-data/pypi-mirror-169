from sly import Parser
from .lexer import telgineLexer
from .nodes import Tag, If, For, Else, Text
from dataclasses import dataclass
from .nodes import Expr

# --- Navigation Map ---
# Use search in your IDE by following labels:
# - TAG
# - ASSIGN VALUES
# - DIRECTIVES
# - ATTRIBUTES


@dataclass
class Directives:
    if_: any
    else_: any
    for_: any


@dataclass
class TagMeta:
    args: dict
    directives: Directives


class telgineParser(Parser):
    tokens = telgineLexer.tokens
    start = 'tag'

    @_('LT ID v_if attribute GT tags CLOSE ID GT')
    def v_if_branch(self, p):
        v_if: If = p[2]
        v_if.body = [Tag(p[1], p[5], p[3])]
        return v_if

    @_('LT ID v_else attribute GT tags CLOSE ID GT')
    def v_else_branch(self, p):
        return Tag(p[1], p[4], p[2])

    @_('v_if_branch v_else_branch')
    def tag(self, p):
        v_if: If = p[0]
        v_if.orelse = [p[1]]
        return v_if

    @_('v_if_branch')
    def tag(self, p):
        return p[0]

    @_('LT ID attribute GT tags CLOSE ID GT')
    def tag(self, p):
        return Tag(p[1], p[4], p[2])

    @_('TEXT')
    def tag(self, p):
        return Text(p[0])

    @_('tag')
    def tags(self, p):
        return [p.tag]

    @_('tags tags')
    def tags(self, p):
        return p[0] + p[1]

    @_('')
    def tags(self, p):
        return []

    @_('IF ASSIGN STRING')
    def v_if(self, p):
        return If(test=p.STRING)

    @_('ELSE ASSIGN STRING')
    def v_else(self, p):
        if len(p.STRING) > 0:
            raise SyntaxError('v-else statement must be have empty!')
        return Else()

    @_('ID ASSIGN STRING')
    def attribute(self, p):
        return {p.ID: p.STRING}

    @_('COLON ID ASSIGN STRING')
    def attribute(self, p):
        return {p.ID: Expr(p.STRING)}

    @_('attributes attributes')
    def attribute(self, p):
        return p[0] | p[1]

    @_('')
    def attributes(self, p):
        return {}








def parse(iterator):
    return telgineParser().parse(iterator)[0]

# [token for token in tokens_gen]
