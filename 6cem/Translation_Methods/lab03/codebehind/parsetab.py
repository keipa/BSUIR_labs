
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'IDENTIFIER NON_STRICT_COMPARISON NON_EQUALITY COMPARISON ASSIGNMENT SEMICOLON EQUALITY COLON COMMA OPEN_BRACKET CLOSE_BRACKET NUMBER FLOAT_NUMBER PLUS MINUS DIV MUL STRING POINT TYPE_REAL DO BEGIN CONST TYPE_STRING FOR TO READLN AND WRITELN DOWNTO WHILE THEN TYPE_INTEGER VAR END INC OR IF\n        program : var begin\n    \n        var : VAR declare\n    \n        begin : BEGIN body END POINT\n    \n        declare : declaration declare\n                 | empty\n    \n        block : BEGIN body END SEMICOLON\n    \n        body : expression\n    \n    expression : assignment body\n                | if body\n                | function body\n                | empty\n                | while body\n    \n        declaration : IDENTIFIER COLON type SEMICOLON\n    \n        type : TYPE_STRING\n             | TYPE_INTEGER\n             | TYPE_REAL\n    \n        empty :\n    \n        assignment : IDENTIFIER ASSIGNMENT arithmetic_expression\n                    | IDENTIFIER ASSIGNMENT arithmetic_expression SEMICOLON\n    \n    arithmetic_expression : IDENTIFIER PLUS arithmetic_expression\n                     | IDENTIFIER MINUS arithmetic_expression\n                     | IDENTIFIER MUL arithmetic_expression\n                     | IDENTIFIER DIV arithmetic_expression\n\n                     | NUMBER PLUS arithmetic_expression\n                     | NUMBER MINUS arithmetic_expression\n                     | NUMBER MUL arithmetic_expression\n                     | NUMBER DIV arithmetic_expression\n                     | FLOAT_NUMBER\n                     | NUMBER\n                     | IDENTIFIER\n                     | STRING\n    \n        function : WRITELN OPEN_BRACKET arithmetic_expression CLOSE_BRACKET SEMICOLON\n                    | READLN OPEN_BRACKET IDENTIFIER CLOSE_BRACKET SEMICOLON\n                    | INC OPEN_BRACKET IDENTIFIER CLOSE_BRACKET SEMICOLON\n    \n     predicate :    IDENTIFIER EQUALITY arithmetic_expression\n                  | NUMBER  EQUALITY arithmetic_expression\n                  | IDENTIFIER  NON_EQUALITY arithmetic_expression\n                  | NUMBER  NON_STRICT_COMPARISON arithmetic_expression\n                  | IDENTIFIER  NON_STRICT_COMPARISON arithmetic_expression\n                  | NUMBER  NON_EQUALITY arithmetic_expression\n                  | NUMBER COMPARISON arithmetic_expression\n                  | NUMBER\n                  | IDENTIFIER\n    \n        while : WHILE predicate DO block\n    \n        if : IF predicate THEN block\n            | IF predicate THEN expression\n    '
    
_lr_action_items = {'CLOSE_BRACKET':([51,52,53,54,56,58,59,85,86,87,88,89,90,91,92,],[-31,-29,-28,-30,79,82,83,-24,-26,-27,-25,-20,-22,-23,-21,]),'DO':([26,27,28,51,52,53,54,63,64,65,66,67,68,69,85,86,87,88,89,90,91,92,],[42,-42,-43,-31,-29,-28,-30,-41,-38,-36,-40,-37,-35,-39,-24,-26,-27,-25,-20,-22,-23,-21,]),'TYPE_STRING':([24,],[38,]),'NON_STRICT_COMPARISON':([27,28,],[44,49,]),'THEN':([27,28,34,51,52,53,54,63,64,65,66,67,68,69,85,86,87,88,89,90,91,92,],[-42,-43,57,-31,-29,-28,-30,-41,-38,-36,-40,-37,-35,-39,-24,-26,-27,-25,-20,-22,-23,-21,]),'ASSIGNMENT':([13,],[30,]),'TYPE_INTEGER':([24,],[40,]),'NUMBER':([11,18,30,33,43,44,45,46,47,48,49,71,72,73,74,75,76,77,78,],[27,27,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'WHILE':([5,10,12,14,16,20,21,25,29,32,36,50,51,52,53,54,57,61,62,70,80,81,85,86,87,88,89,90,91,92,93,94,95,97,],[11,11,11,-11,11,11,-7,-10,-9,-8,-12,-18,-31,-29,-28,-30,11,11,-44,-19,-46,-45,-24,-26,-27,-25,-20,-22,-23,-21,-32,-33,-34,-6,]),'MUL':([52,54,],[72,76,]),'DIV':([52,54,],[73,77,]),'MINUS':([52,54,],[74,78,]),'COMPARISON':([27,],[43,]),'BEGIN':([1,2,6,8,9,23,42,57,60,],[5,-17,-17,-2,-5,-4,61,61,-13,]),'EQUALITY':([27,28,],[45,48,]),'SEMICOLON':([38,39,40,41,50,51,52,53,54,79,82,83,85,86,87,88,89,90,91,92,96,],[-14,-16,-15,60,70,-31,-29,-28,-30,93,94,95,-24,-26,-27,-25,-20,-22,-23,-21,97,]),'POINT':([31,],[55,]),'OPEN_BRACKET':([17,19,22,],[33,35,37,]),'COLON':([7,],[24,]),'PLUS':([52,54,],[71,75,]),'IDENTIFIER':([2,5,6,10,11,12,14,16,18,20,21,25,29,30,32,33,35,36,37,43,44,45,46,47,48,49,50,51,52,53,54,57,60,61,62,70,71,72,73,74,75,76,77,78,80,81,85,86,87,88,89,90,91,92,93,94,95,97,],[7,13,7,13,28,13,-11,13,28,13,-7,-10,-9,54,-8,54,58,-12,59,54,54,54,54,54,54,54,-18,-31,-29,-28,-30,13,-13,13,-44,-19,54,54,54,54,54,54,54,54,-46,-45,-24,-26,-27,-25,-20,-22,-23,-21,-32,-33,-34,-6,]),'$end':([3,4,55,],[0,-1,-3,]),'END':([5,10,12,14,15,16,20,21,25,29,32,36,50,51,52,53,54,57,61,62,70,80,81,84,85,86,87,88,89,90,91,92,93,94,95,97,],[-17,-17,-17,-11,31,-17,-17,-7,-10,-9,-8,-12,-18,-31,-29,-28,-30,-17,-17,-44,-19,-46,-45,96,-24,-26,-27,-25,-20,-22,-23,-21,-32,-33,-34,-6,]),'STRING':([30,33,43,44,45,46,47,48,49,71,72,73,74,75,76,77,78,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'WRITELN':([5,10,12,14,16,20,21,25,29,32,36,50,51,52,53,54,57,61,62,70,80,81,85,86,87,88,89,90,91,92,93,94,95,97,],[17,17,17,-11,17,17,-7,-10,-9,-8,-12,-18,-31,-29,-28,-30,17,17,-44,-19,-46,-45,-24,-26,-27,-25,-20,-22,-23,-21,-32,-33,-34,-6,]),'FLOAT_NUMBER':([30,33,43,44,45,46,47,48,49,71,72,73,74,75,76,77,78,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'VAR':([0,],[2,]),'NON_EQUALITY':([27,28,],[46,47,]),'IF':([5,10,12,14,16,20,21,25,29,32,36,50,51,52,53,54,57,61,62,70,80,81,85,86,87,88,89,90,91,92,93,94,95,97,],[18,18,18,-11,18,18,-7,-10,-9,-8,-12,-18,-31,-29,-28,-30,18,18,-44,-19,-46,-45,-24,-26,-27,-25,-20,-22,-23,-21,-32,-33,-34,-6,]),'TYPE_REAL':([24,],[39,]),'READLN':([5,10,12,14,16,20,21,25,29,32,36,50,51,52,53,54,57,61,62,70,80,81,85,86,87,88,89,90,91,92,93,94,95,97,],[19,19,19,-11,19,19,-7,-10,-9,-8,-12,-18,-31,-29,-28,-30,19,19,-44,-19,-46,-45,-24,-26,-27,-25,-20,-22,-23,-21,-32,-33,-34,-6,]),'INC':([5,10,12,14,16,20,21,25,29,32,36,50,51,52,53,54,57,61,62,70,80,81,85,86,87,88,89,90,91,92,93,94,95,97,],[22,22,22,-11,22,22,-7,-10,-9,-8,-12,-18,-31,-29,-28,-30,22,22,-44,-19,-46,-45,-24,-26,-27,-25,-20,-22,-23,-21,-32,-33,-34,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'body':([5,10,12,16,20,61,],[15,25,29,32,36,84,]),'function':([5,10,12,16,20,57,61,],[10,10,10,10,10,10,10,]),'begin':([1,],[4,]),'type':([24,],[41,]),'assignment':([5,10,12,16,20,57,61,],[16,16,16,16,16,16,16,]),'predicate':([11,18,],[26,34,]),'while':([5,10,12,16,20,57,61,],[20,20,20,20,20,20,20,]),'program':([0,],[3,]),'block':([42,57,],[62,81,]),'declaration':([2,6,],[6,6,]),'var':([0,],[1,]),'arithmetic_expression':([30,33,43,44,45,46,47,48,49,71,72,73,74,75,76,77,78,],[50,56,63,64,65,66,67,68,69,85,86,87,88,89,90,91,92,]),'expression':([5,10,12,16,20,57,61,],[21,21,21,21,21,80,21,]),'declare':([2,6,],[8,23,]),'empty':([2,5,6,10,12,16,20,57,61,],[9,14,9,14,14,14,14,14,14,]),'if':([5,10,12,16,20,57,61,],[12,12,12,12,12,12,12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> var begin','program',2,'p_program','mtran_lab3.py',52),
  ('var -> VAR declare','var',2,'p_var','mtran_lab3.py',59),
  ('begin -> BEGIN body END POINT','begin',4,'p_begin','mtran_lab3.py',66),
  ('declare -> declaration declare','declare',2,'p_declare','mtran_lab3.py',73),
  ('declare -> empty','declare',1,'p_declare','mtran_lab3.py',74),
  ('block -> BEGIN body END SEMICOLON','block',4,'p_block','mtran_lab3.py',84),
  ('body -> expression','body',1,'p_body','mtran_lab3.py',91),
  ('expression -> assignment body','expression',2,'p_expression','mtran_lab3.py',98),
  ('expression -> if body','expression',2,'p_expression','mtran_lab3.py',99),
  ('expression -> function body','expression',2,'p_expression','mtran_lab3.py',100),
  ('expression -> empty','expression',1,'p_expression','mtran_lab3.py',101),
  ('expression -> while body','expression',2,'p_expression','mtran_lab3.py',102),
  ('declaration -> IDENTIFIER COLON type SEMICOLON','declaration',4,'p_declaration','mtran_lab3.py',110),
  ('type -> TYPE_STRING','type',1,'p_type','mtran_lab3.py',118),
  ('type -> TYPE_INTEGER','type',1,'p_type','mtran_lab3.py',119),
  ('type -> TYPE_REAL','type',1,'p_type','mtran_lab3.py',120),
  ('empty -> <empty>','empty',0,'p_empty','mtran_lab3.py',127),
  ('assignment -> IDENTIFIER ASSIGNMENT arithmetic_expression','assignment',3,'p_assignment','mtran_lab3.py',134),
  ('assignment -> IDENTIFIER ASSIGNMENT arithmetic_expression SEMICOLON','assignment',4,'p_assignment','mtran_lab3.py',135),
  ('arithmetic_expression -> IDENTIFIER PLUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','mtran_lab3.py',151),
  ('arithmetic_expression -> IDENTIFIER MINUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','mtran_lab3.py',152),
  ('arithmetic_expression -> IDENTIFIER MUL arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','mtran_lab3.py',153),
  ('arithmetic_expression -> IDENTIFIER DIV arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','mtran_lab3.py',154),
  ('arithmetic_expression -> NUMBER PLUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','mtran_lab3.py',156),
  ('arithmetic_expression -> NUMBER MINUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','mtran_lab3.py',157),
  ('arithmetic_expression -> NUMBER MUL arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','mtran_lab3.py',158),
  ('arithmetic_expression -> NUMBER DIV arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','mtran_lab3.py',159),
  ('arithmetic_expression -> FLOAT_NUMBER','arithmetic_expression',1,'p_arithmetic_expression','mtran_lab3.py',160),
  ('arithmetic_expression -> NUMBER','arithmetic_expression',1,'p_arithmetic_expression','mtran_lab3.py',161),
  ('arithmetic_expression -> IDENTIFIER','arithmetic_expression',1,'p_arithmetic_expression','mtran_lab3.py',162),
  ('arithmetic_expression -> STRING','arithmetic_expression',1,'p_arithmetic_expression','mtran_lab3.py',163),
  ('function -> WRITELN OPEN_BRACKET arithmetic_expression CLOSE_BRACKET SEMICOLON','function',5,'p_function','mtran_lab3.py',187),
  ('function -> READLN OPEN_BRACKET IDENTIFIER CLOSE_BRACKET SEMICOLON','function',5,'p_function','mtran_lab3.py',188),
  ('function -> INC OPEN_BRACKET IDENTIFIER CLOSE_BRACKET SEMICOLON','function',5,'p_function','mtran_lab3.py',189),
  ('predicate -> IDENTIFIER EQUALITY arithmetic_expression','predicate',3,'p_predicate','mtran_lab3.py',210),
  ('predicate -> NUMBER EQUALITY arithmetic_expression','predicate',3,'p_predicate','mtran_lab3.py',211),
  ('predicate -> IDENTIFIER NON_EQUALITY arithmetic_expression','predicate',3,'p_predicate','mtran_lab3.py',212),
  ('predicate -> NUMBER NON_STRICT_COMPARISON arithmetic_expression','predicate',3,'p_predicate','mtran_lab3.py',213),
  ('predicate -> IDENTIFIER NON_STRICT_COMPARISON arithmetic_expression','predicate',3,'p_predicate','mtran_lab3.py',214),
  ('predicate -> NUMBER NON_EQUALITY arithmetic_expression','predicate',3,'p_predicate','mtran_lab3.py',215),
  ('predicate -> NUMBER COMPARISON arithmetic_expression','predicate',3,'p_predicate','mtran_lab3.py',216),
  ('predicate -> NUMBER','predicate',1,'p_predicate','mtran_lab3.py',217),
  ('predicate -> IDENTIFIER','predicate',1,'p_predicate','mtran_lab3.py',218),
  ('while -> WHILE predicate DO block','while',4,'p_while','mtran_lab3.py',251),
  ('if -> IF predicate THEN block','if',4,'p_if','mtran_lab3.py',259),
  ('if -> IF predicate THEN expression','if',4,'p_if','mtran_lab3.py',260),
]
