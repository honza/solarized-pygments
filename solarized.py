from pygments.style import Style
from pygments.token import *


base03  =  '#002b36'
base02  =  '#073642'
base01  =  '#586e75'
base00  =  '#657b83'
base0   =  '#839496'
base1   =  '#93a1a1'
base2   =  '#eee8d5'
base3   =  '#fdf6e3'
yellow  =  '#b58900'
orange  =  '#cb4b16'
red     =  '#dc322f'
magenta =  '#d33682'
violet  =  '#6c71c4'
blue    =  '#268bd2'
cyan    =  '#2aa198'
green   =  '#859900'


def make(fg, bg=base03):
    return 'bg:%s %s' % (bg, fg)


class SolarizedStyle(Style):
    default_style = ""
    styles = {
        Token:                         make(base1),

        # Text:                          '',
        # Whitespace:                    'w',
        # Error:                         'err',
        # Other:                         'x',

        Keyword:                       make(green),
        Keyword.Constant:              make(cyan), # false, null, undefined
        Keyword.Declaration:           make(blue), # var, function
        Keyword.Namespace:             make(orange),
        # Keyword.Pseudo:                make(violet),
        # Keyword.Reserved:              make(violet),
        # Keyword.Type:                  make(violet),

        # Name:                          make(yellow),
        # Name.Attribute:                make(violet),
        Name.Builtin:                  make(red), # Object, Array
        Name.Builtin.Pseudo:           make(blue),
        Name.Class:                    make(blue),
        # Name.Constant:                 make(blue),
        Name.Decorator:                make(blue),
        Name.Entity:                   make(violet),
        Name.Exception:                make(yellow),
        Name.Function:                 make(blue),
        # Name.Property:                 'py',
        # Name.Label:                    'nl',
        # Name.Namespace:                'nn',
        # Name.Other:                    'nx',
        # Name.Tag:                      'nt',
        # Name.Variable:                 'nv',
        # Name.Variable.Class:           'vc',
        # Name.Variable.Global:          'vg',
        # Name.Variable.Instance:        'vi',

        # Literal:                       'l',
        # Literal.Date:                  'ld',

        String:                        make(cyan),
        # String.Backtick:               'sb',
        # String.Char:                   'sc',
        # String.Doc:                    'sd',
        # String.Double:                 's2',
        # String.Escape:                 'se',
        # String.Heredoc:                'sh',
        # String.Interpol:               'si',
        # String.Other:                  'sx',
        # String.Regex:                  'sr',
        # String.Single:                 's1',
        # String.Symbol:                 'ss',

        Number:                        make(cyan),
        # Number.Float:                  'mf',
        # Number.Hex:                    'mh',
        # Number.Integer:                'mi',
        # Number.Integer.Long:           'il',
        # Number.Oct:                    'mo',

        # Operator:                      'o',
        Operator.Word:                 make(green),

        # Punctuation:                   'p',

        Comment:                       make(base01),

        # Generic:                       'g',
        # Generic.Deleted:               'gd',
        # Generic.Emph:                  'ge',
        # Generic.Error:                 'gr',
        # Generic.Heading:               'gh',
        # Generic.Inserted:              'gi',
        # Generic.Output:                'go',
        # Generic.Prompt:                'gp',
        # Generic.Strong:                'gs',
        # Generic.Subheading:            'gu',
        # Generic.Traceback:             'gt',
    }
