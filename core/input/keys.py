import pygame


def createKeys():
	"""
	Remaps the Pygame key constants to a PyGM dict yo
	"""
	keys = {}
	keys['backspace'] = pygame.K_BACKSPACE
	keys['tab'] = pygame.K_TAB
	keys['clear'] = pygame.K_CLEAR
	keys['return'] = pygame.K_RETURN
	keys['pause'] = pygame.K_PAUSE
	keys['escape'] = pygame.K_ESCAPE
	keys['space'] = pygame.K_SPACE
	keys['exclaim'] = pygame.K_EXCLAIM
	keys['quotedbl'] = pygame.K_QUOTEDBL
	keys['hash'] = pygame.K_HASH
	keys['dollar'] = pygame.K_DOLLAR
	keys['ampersand'] = pygame.K_AMPERSAND
	keys['quote'] = pygame.K_QUOTE
	keys['leftparen'] = pygame.K_LEFTPAREN
	keys['rightparen'] = pygame.K_RIGHTPAREN
	keys['asterisk'] = pygame.K_ASTERISK
	keys['plus'] = pygame.K_PLUS
	keys['comma'] = pygame.K_COMMA
	keys['minus'] = pygame.K_MINUS
	keys['period'] = pygame.K_PERIOD
	keys['slash'] = pygame.K_SLASH
	keys['0'] = pygame.K_0
	keys['1'] = pygame.K_1
	keys['2'] = pygame.K_2
	keys['3'] = pygame.K_3
	keys['4'] = pygame.K_4
	keys['5'] = pygame.K_5
	keys['6'] = pygame.K_6
	keys['7'] = pygame.K_7
	keys['8'] = pygame.K_8
	keys['9'] = pygame.K_9
	keys['colon'] = pygame.K_COLON
	keys['semicolon'] = pygame.K_SEMICOLON
	keys['less'] = pygame.K_LESS
	keys['equals'] = pygame.K_EQUALS
	keys['greater'] = pygame.K_GREATER
	keys['question'] = pygame.K_QUESTION
	keys['at'] = pygame.K_AT
	keys['leftbracket'] = pygame.K_LEFTBRACKET
	keys['backslash'] = pygame.K_BACKSLASH
	keys['rightbracket'] = pygame.K_RIGHTBRACKET
	keys['caret'] = pygame.K_CARET
	keys['underscore'] = pygame.K_UNDERSCORE
	keys['backquote'] = pygame.K_BACKQUOTE
	keys['a'] = pygame.K_a
	keys['b'] = pygame.K_b
	keys['c'] = pygame.K_c
	keys['d'] = pygame.K_d
	keys['e'] = pygame.K_e
	keys['f'] = pygame.K_f
	keys['g'] = pygame.K_g
	keys['h'] = pygame.K_h
	keys['i'] = pygame.K_i
	keys['j'] = pygame.K_j
	keys['k'] = pygame.K_k
	keys['l'] = pygame.K_l
	keys['m'] = pygame.K_m
	keys['n'] = pygame.K_n
	keys['o'] = pygame.K_o
	keys['p'] = pygame.K_p
	keys['q'] = pygame.K_q
	keys['r'] = pygame.K_r
	keys['s'] = pygame.K_s
	keys['t'] = pygame.K_t
	keys['u'] = pygame.K_u
	keys['v'] = pygame.K_v
	keys['w'] = pygame.K_w
	keys['x'] = pygame.K_x
	keys['y'] = pygame.K_y
	keys['z'] = pygame.K_z
	keys['delete'] = pygame.K_DELETE
	keys['kp0'] = pygame.K_KP0
	keys['kp1'] = pygame.K_KP1
	keys['kp2'] = pygame.K_KP2
	keys['kp3'] = pygame.K_KP3
	keys['kp4'] = pygame.K_KP4
	keys['kp5'] = pygame.K_KP5
	keys['kp6'] = pygame.K_KP6
	keys['kp7'] = pygame.K_KP7
	keys['kp8'] = pygame.K_KP8
	keys['kp9'] = pygame.K_KP9
	keys['kp_period'] = pygame.K_KP_PERIOD
	keys['kp_divide'] = pygame.K_KP_DIVIDE
	keys['kp_multiply'] = pygame.K_KP_MULTIPLY
	keys['kp_minus'] = pygame.K_KP_MINUS
	keys['kp_plus'] = pygame.K_KP_PLUS
	keys['kp_enter'] = pygame.K_KP_ENTER
	keys['kp_equals'] = pygame.K_KP_EQUALS
	keys['up'] = pygame.K_UP
	keys['down'] = pygame.K_DOWN
	keys['right'] = pygame.K_RIGHT
	keys['left'] = pygame.K_LEFT
	keys['insert'] = pygame.K_INSERT
	keys['home'] = pygame.K_HOME
	keys['end'] = pygame.K_END
	keys['pageup'] = pygame.K_PAGEUP
	keys['pagedown'] = pygame.K_PAGEDOWN
	keys['f1'] = pygame.K_F1
	keys['f2'] = pygame.K_F2
	keys['f3'] = pygame.K_F3
	keys['f4'] = pygame.K_F4
	keys['f5'] = pygame.K_F5
	keys['f6'] = pygame.K_F6
	keys['f7'] = pygame.K_F7
	keys['f8'] = pygame.K_F8
	keys['f9'] = pygame.K_F9
	keys['f10'] = pygame.K_F10
	keys['f11'] = pygame.K_F11
	keys['f12'] = pygame.K_F12
	keys['f13'] = pygame.K_F13
	keys['f14'] = pygame.K_F14
	keys['f15'] = pygame.K_F15
	keys['numlock'] = pygame.K_NUMLOCK
	keys['capslock'] = pygame.K_CAPSLOCK
	keys['scrollock'] = pygame.K_SCROLLOCK
	keys['rshift'] = pygame.K_RSHIFT
	keys['lshift'] = pygame.K_LSHIFT
	keys['rctrl'] = pygame.K_RCTRL
	keys['lctrl'] = pygame.K_LCTRL
	keys['ralt'] = pygame.K_RALT
	keys['lalt'] = pygame.K_LALT
	keys['rmeta'] = pygame.K_RMETA
	keys['lmeta'] = pygame.K_LMETA
	keys['lsuper'] = pygame.K_LSUPER
	keys['rsuper'] = pygame.K_RSUPER
	keys['mode'] = pygame.K_MODE
	keys['help'] = pygame.K_HELP
	keys['print'] = pygame.K_PRINT
	keys['sysreq'] = pygame.K_SYSREQ
	keys['break'] = pygame.K_BREAK
	keys['menu'] = pygame.K_MENU
	keys['power'] = pygame.K_POWER
	keys['euro'] = pygame.K_EURO

	return keys


def createMB():
	"""
	Returns a dict of the mouse buttons
	"""

	buttons = {}

	buttons['left'] = 0
	buttons['right'] = 1
	buttons['middle'] = 2

	return buttons
