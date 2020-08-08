from base.color import Color
from write_palette import write_palette

bg0 = Color(300, 25, 18)
bg1 = Color(300, 25, 25)
bg2 = Color(300, 25, 35)
bg3 = Color(300, 25, 55)

fg0 = Color(300, 10, 60)
fg1 = Color(300, 10, 70)
fg2 = Color(300, 10, 80)

mid0 = Color(300, 35, 80)
mid1 = Color(320, 55, 90)
mid2 = Color(340, 65, 90)
mid3 = Color(275, 40, 90)

accent_teal = Color(193, 35, 82)
accent_orange = Color(359, 40, 90)
accent_red = Color(359, 70, 90)
accent_red_dim = Color(359, 45, 72)
accent_yellow = Color(40, 25, 100)
accent_green = Color(92, 26, 75)

all_colors = [
  bg0,
  bg1,
  bg2,
  bg3,
  fg0,
  fg1,
  fg2,
  mid0,
  mid1,
  mid2,
  mid3,
  accent_teal,
  accent_orange,
  accent_red,
  accent_red_dim,
  accent_yellow,
  accent_green,
]

terminal_colors = [
  bg0.hex,            # 00 - Black
  accent_red.hex,     # 01 - Red
  accent_green.hex,   # 02 - Green
  accent_yellow.hex,  # 03 - Yellow
  mid0.hex,           # 04 - Blue
  mid1.hex,           # 05 - Purple
  accent_teal.hex,    # 06 - Cyan
  fg2.hex,            # 07 - White
  bg2.hex,            # 08 - Dim Black
  accent_red_dim.hex, # 09 - Dim Red
  accent_green.hex,   # 10 - Dim Green
  accent_yellow.hex,  # 11 - Dim Yellow
  mid3.hex,           # 12 - Dim Blue
  mid2.hex,           # 13 - Dim Purple
  accent_teal.hex,    # 14 - Dim Cyan
  fg0.hex,            # 15 - Dim White
]

write_palette(all_colors)

class Hi:
  def __init__(self, group, fg=None, bg=None):
    self.group = group
    self.fg = fg
    self.bg = bg

  def _get_value(self, value):
    if isinstance(value, Color):
      return value.hex
    else:
      return value

  def write(self, out):
    if self.fg is not None:
      out.write('hi {} guifg={}\n'.format(self.group, self._get_value(self.fg)))
    if self.bg is not None:
      out.write('hi {} guibg={}\n'.format(self.group, self._get_value(self.bg)))

highlights = [
  Hi('Normal', fg=fg2, bg=bg0),
  Hi('fzfBorder', fg=bg2),

  Hi('Search', fg=bg0, bg=accent_green),

  Hi('Comment', fg=bg3),
  Hi('Todo', fg=fg0, bg='NONE'),

  Hi('Cursor', fg=bg0, bg=fg2),
  Hi('CursorLine', bg=bg1),

  Hi('Visual', bg=bg2),

  Hi('LineNr', fg=bg2),
  Hi('CursorLineNr', fg=fg2, bg=bg1),

  Hi('PMenu', fg=fg0, bg=bg1),
  Hi('PMenuSel', fg=fg2, bg=bg3),

  Hi('VertSplit', fg=bg0, bg=bg0),
  Hi('StatusLine', fg=bg0, bg=bg3),
  Hi('StatusLineNC', fg=bg1, bg=bg3),
  Hi('NonText', fg=bg3),

  # stuff like press enter messages, green probs
  Hi('Question', fg=accent_green, bg=bg0), 
  Hi('SpecialKey', fg=fg2, bg=bg0), # misc?

  # Used for some other misc stuff, NOT just directories
  Hi('Directory', fg=fg2, bg=bg0),

  # Language General
  Hi('Statement', fg=mid0),
  Hi('Constant', fg=accent_teal),
  Hi('Identifier', fg=mid1),
  Hi('PreProc', fg=mid0),
  Hi('Type', fg=mid0),
  Hi('Boolean', fg=mid2),
  Hi('MatchParen', fg=mid2, bg='NONE'),
  Hi('Special', fg=mid3),

  # JavaScript Specific
  Hi('jsNull', fg=mid2),
  Hi('jsNumber', fg=mid2),
  Hi('jsGlobalObjects', fg=fg2),
  Hi('jsTemplateBraces', fg=mid2),
  Hi('xmlTag', fg=mid0),
  Hi('xmlEndTag', fg=mid0),
  Hi('xmlTagName', fg=mid1),
  Hi('xmlTagN', fg=mid1),

  # C Specific
  Hi('cFloat', fg=mid2),
  Hi('cNumber', fg=mid2),
  Hi('cppNumber', fg=mid2),
]

theme_name = 'purple_soft'

vim_header = """\
hi clear
syntax reset
set background=dark

let g:colors_name = "{}"

""".format(theme_name)

vim_footer = """\
if has("nvim")
  let g:terminal_color_0  = "{}"
  let g:terminal_color_1  = "{}"
  let g:terminal_color_2  = "{}"
  let g:terminal_color_3  = "{}"
  let g:terminal_color_4  = "{}"
  let g:terminal_color_5  = "{}"
  let g:terminal_color_6  = "{}"
  let g:terminal_color_7  = "{}"
  let g:terminal_color_8  = "{}"
  let g:terminal_color_9  = "{}"
  let g:terminal_color_10 = "{}"
  let g:terminal_color_11 = "{}"
  let g:terminal_color_12 = "{}"
  let g:terminal_color_13 = "{}"
  let g:terminal_color_14 = "{}"
  let g:terminal_color_15 = "{}"
endif
""".format(*terminal_colors)

with open('{}.vim'.format(theme_name), 'w') as out:
  out.write(vim_header)
  for highlight in highlights:
    highlight.write(out)
  out.write(vim_footer)

kitty_terminal_colors = """\
color0  {}
color1  {}
color2  {}
color3  {}
color4  {}
color5  {}
color6  {}
color7  {}
color8  {}
color9  {}
color10 {}
color11 {}
color12 {}
color13 {}
color14 {}
color15 {}
""".format(*terminal_colors)

kitty_app_colors = [
  ['active_tab_foreground', fg2],
  ['active_tab_background', bg0],

  ['inactive_tab_foreground', bg3],
  ['inactive_tab_background', bg0],

  ['foreground', fg2],
  ['background', bg0],

  ['selection_foreground', bg0],
  ['selection_background', fg2],

  ['active_border_color', fg2],
  ['inactive_border_color', bg0],

  ['cursor', mid2],
  ['cursor_text_color', bg0],
]

with open('theme_{}.conf'.format(theme_name), 'w') as out:
  out.write(kitty_terminal_colors)
  for field, color in kitty_app_colors:
    out.write('{} {}\n'.format(field, color.hex))

