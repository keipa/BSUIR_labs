
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'IDENTIFIER NON_STRICT_COMPARISON NON_EQUALITY COMPARISON ASSIGNMENT SEMICOLON EQUALITY COLON OPEN_BRACKET CLOSE_BRACKET OPEN_SQUARE_BRACKET CLOSE_SQUARE_BRACKET NUMBER PLUS MINUS DIV MUL STRING POINT ZAPYATAYA DOWNTO THEN WRITE ELSE TYPE_REAL CONST READ FOR LENGTH WRITELN IN TO OR READLN NOT END TYPE_STRING BEGIN AND BREAK IF DO TYPE_INTEGER VAR INC WHILE\n        consts : CONST IDENTIFIER EQUALITY NUMBER SEMICOLON begin_program\n                | CONST IDENTIFIER EQUALITY STRING SEMICOLON begin_program\n                | CONST IDENTIFIER EQUALITY matrix SEMICOLON begin_program\n                | begin_program\n    \n        matrix : OPEN_SQUARE_BRACKET identifiers CLOSE_SQUARE_BRACKET\n    \n        identifiers : IDENTIFIER ZAPYATAYA identifiers\n                    | NUMBER ZAPYATAYA identifiers\n                    | STRING ZAPYATAYA identifiers\n                    | IDENTIFIER\n                    | NUMBER\n                    | STRING\n    \n        begin_program : VAR declarations BEGIN body END POINT\n    \n        block : BEGIN body END SEMICOLON\n    \n        body : expression\n    \n        identifier : IDENTIFIER\n    \n    expression : assignment expression\n                | if expression\n                | function expression\n                | empty\n                | while expression\n                | for expression\n                | break\n    \n        break : BREAK SEMICOLON\n    \n        declarations : declaration declarations\n                    | empty\n    \n        declaration : IDENTIFIER another_identifiers COLON type SEMICOLON\n    \n        another_identifiers : ZAPYATAYA IDENTIFIER another_identifiers\n                            | empty\n    \n        type : TYPE_STRING\n             | TYPE_INTEGER\n             | TYPE_REAL\n    \n        empty :\n    \n        assignment : identifier ASSIGNMENT arithmetic_expression SEMICOLON\n                   | identifier ASSIGNMENT function SEMICOLON\n                   | identifier ASSIGNMENT function\n                   | identifier ASSIGNMENT arithmetic_expression\n    \n    arithmetic_expression : NUMBER\n                     | identifier\n                     | STRING\n                     | function\n                     | identifier PLUS arithmetic_expression\n                     | identifier MINUS arithmetic_expression\n                     | identifier MUL arithmetic_expression\n                     | identifier DIV arithmetic_expression\n                     | NUMBER PLUS arithmetic_expression\n                     | NUMBER MINUS arithmetic_expression\n                     | NUMBER MUL arithmetic_expression\n                     | NUMBER DIV arithmetic_expression\n                     | function PLUS arithmetic_expression\n                     | function MINUS arithmetic_expression\n                     | function MUL arithmetic_expression\n                     | function DIV arithmetic_expression\n                     | identifier OPEN_SQUARE_BRACKET arithmetic_expression CLOSE_SQUARE_BRACKET\n                     | arithmetic_expression PLUS arithmetic_expression\n                     | arithmetic_expression MINUS arithmetic_expression\n                     | arithmetic_expression MUL arithmetic_expression\n                     | arithmetic_expression DIV arithmetic_expression\n    \n        function : WRITE OPEN_BRACKET arithmetic_expression CLOSE_BRACKET SEMICOLON\n                    | WRITELN OPEN_BRACKET arithmetic_expression CLOSE_BRACKET SEMICOLON\n                    | READ OPEN_BRACKET identifier CLOSE_BRACKET SEMICOLON\n                    | READLN OPEN_BRACKET identifier CLOSE_BRACKET SEMICOLON\n                    | LENGTH OPEN_BRACKET identifier CLOSE_BRACKET\n                    | INC OPEN_BRACKET identifier CLOSE_BRACKET SEMICOLON\n    \n    predicate :    arithmetic_expression COMPARISON arithmetic_expression\n                  | arithmetic_expression EQUALITY arithmetic_expression\n                  | arithmetic_expression NON_EQUALITY arithmetic_expression\n                  | arithmetic_expression NON_STRICT_COMPARISON arithmetic_expression\n                  | arithmetic_expression IN identifier\n                  | arithmetic_expression IN matrix\n    \n        some_predicates : OPEN_BRACKET predicate CLOSE_BRACKET AND some_predicates\n                        | OPEN_BRACKET predicate CLOSE_BRACKET OR some_predicates\n                        | OPEN_BRACKET predicate CLOSE_BRACKET\n                        | OPEN_BRACKET NOT OPEN_BRACKET predicate CLOSE_BRACKET CLOSE_BRACKET AND some_predicates\n                        | OPEN_BRACKET NOT OPEN_BRACKET predicate CLOSE_BRACKET CLOSE_BRACKET OR some_predicates\n                        | OPEN_BRACKET NOT OPEN_BRACKET predicate CLOSE_BRACKET CLOSE_BRACKET\n    \n        while : WHILE OPEN_BRACKET predicate CLOSE_BRACKET DO block\n              | WHILE some_predicates DO block\n    \n        for : FOR assignment TO arithmetic_expression DO block\n              | FOR assignment DOWNTO arithmetic_expression DO block\n    \n        if : IF OPEN_BRACKET predicate CLOSE_BRACKET THEN block\n            | IF OPEN_BRACKET predicate CLOSE_BRACKET THEN block else\n    \n        else : ELSE block\n    '
    
_lr_action_items = {'TYPE_INTEGER':([21,],[52,]),'IDENTIFIER':([1,4,8,11,15,17,26,27,28,31,35,37,42,55,56,57,61,63,65,66,70,71,74,75,77,80,82,83,84,85,86,88,96,97,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,125,126,127,128,129,131,132,133,135,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,178,181,183,185,186,188,189,192,],[5,7,7,20,31,44,31,31,31,-15,31,31,31,31,31,31,31,31,31,31,31,31,44,44,44,-26,-38,-35,-37,-39,-36,-40,31,31,31,31,31,31,31,-34,31,31,31,31,31,31,31,31,-33,31,31,31,31,31,31,31,31,31,-62,-77,31,31,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,-80,31,-76,-79,-78,-81,-13,-82,]),'MINUS':([31,82,83,84,85,86,88,89,99,100,131,137,138,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,162,165,166,172,175,176,177,],[-15,109,114,118,-39,123,114,123,123,123,-62,123,123,-63,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,-61,-60,-59,-58,-53,]),'THEN':([124,],[159,]),'IN':([31,82,84,85,88,89,131,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,],[-15,-38,-37,-39,-40,128,-62,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,]),'BREAK':([15,26,27,28,31,37,42,82,83,84,85,86,88,110,119,131,132,133,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,178,183,185,186,188,189,192,],[30,30,30,30,-15,30,30,-38,-35,-37,-39,-36,-40,-34,-33,-62,-77,30,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,-80,-76,-79,-78,-81,-13,-82,]),'EQUALITY':([5,31,82,84,85,88,89,131,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,],[10,-15,-38,-37,-39,-40,125,-62,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,]),'DOWNTO':([31,67,82,83,84,85,86,88,110,119,131,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,],[-15,96,-38,-35,-37,-39,-36,-40,-34,-33,-62,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,]),'NOT':([65,181,],[94,94,]),'IF':([15,26,27,28,31,37,42,82,83,84,85,86,88,110,119,131,132,133,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,178,183,185,186,188,189,192,],[25,25,25,25,-15,25,25,-38,-35,-37,-39,-36,-40,-34,-33,-62,-77,25,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,-80,-76,-79,-78,-81,-13,-82,]),'TYPE_STRING':([21,],[51,]),'TYPE_REAL':([21,],[53,]),'DIV':([31,82,83,84,85,86,88,89,99,100,131,137,138,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,162,165,166,172,175,176,177,],[-15,106,111,116,-39,120,111,120,120,120,-62,120,120,-63,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,120,-61,-60,-59,-58,-53,]),'WHILE':([15,26,27,28,31,37,42,82,83,84,85,86,88,110,119,131,132,133,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,178,183,185,186,188,189,192,],[33,33,33,33,-15,33,33,-38,-35,-37,-39,-36,-40,-34,-33,-62,-77,33,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,-80,-76,-79,-78,-81,-13,-82,]),'CLOSE_SQUARE_BRACKET':([31,44,45,46,47,82,84,85,88,101,102,103,131,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,],[-15,-9,-11,76,-10,-38,-37,-39,-40,-6,-8,-7,-62,-63,-43,-44,177,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,]),'COMPARISON':([31,82,84,85,88,89,131,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,],[-15,-38,-37,-39,-40,129,-62,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,]),'NON_STRICT_COMPARISON':([31,82,84,85,88,89,131,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,],[-15,-38,-37,-39,-40,126,-62,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,]),'WRITELN':([15,26,27,28,31,37,42,56,57,65,70,71,82,83,84,85,86,88,96,97,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,125,126,127,129,131,132,133,135,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,178,181,183,185,186,188,189,192,],[40,40,40,40,-15,40,40,40,40,40,40,40,-38,-35,-37,-39,-36,-40,40,40,40,40,40,40,40,-34,40,40,40,40,40,40,40,40,-33,40,40,40,40,40,40,40,40,-62,-77,40,40,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,-80,40,-76,-79,-78,-81,-13,-82,]),'ZAPYATAYA':([7,20,44,45,47,],[11,11,74,75,77,]),'FOR':([15,26,27,28,31,37,42,82,83,84,85,86,88,110,119,131,132,133,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,178,183,185,186,188,189,192,],[35,35,35,35,-15,35,35,-38,-35,-37,-39,-36,-40,-34,-33,-62,-77,35,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,-80,-76,-79,-78,-81,-13,-82,]),'$end':([2,3,73,78,79,98,],[-4,0,-1,-3,-2,-12,]),'NON_EQUALITY':([31,82,84,85,88,89,131,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,],[-15,-38,-37,-39,-40,127,-62,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,]),'PLUS':([31,82,83,84,85,86,88,89,99,100,131,137,138,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,162,165,166,172,175,176,177,],[-15,108,113,117,-39,122,113,122,122,122,-62,122,122,-63,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,122,-61,-60,-59,-58,-53,]),'OPEN_BRACKET':([23,25,29,32,33,34,40,41,94,168,169,194,195,],[55,57,61,63,65,66,70,71,135,181,181,181,181,]),'WRITE':([15,26,27,28,31,37,42,56,57,65,70,71,82,83,84,85,86,88,96,97,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,125,126,127,129,131,132,133,135,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,178,181,183,185,186,188,189,192,],[41,41,41,41,-15,41,41,41,41,41,41,41,-38,-35,-37,-39,-36,-40,41,41,41,41,41,41,41,-34,41,41,41,41,41,41,41,41,-33,41,41,41,41,41,41,41,41,-62,-77,41,41,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,-80,41,-76,-79,-78,-81,-13,-82,]),'BEGIN':([4,6,8,9,14,80,92,159,170,173,174,187,],[-32,-25,-32,15,-24,-26,133,133,133,133,133,133,]),'CONST':([0,],[1,]),'CLOSE_BRACKET':([31,76,81,82,84,85,87,88,90,91,93,95,99,100,131,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,162,163,164,165,166,171,172,175,176,177,184,190,],[-15,-5,104,-38,-37,-39,124,-40,130,131,134,136,139,140,-62,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-65,-67,-66,-68,-69,-64,-61,184,-60,-59,-58,-53,191,193,]),'COLON':([7,12,13,20,50,],[-32,-28,21,-32,-27,]),'DO':([31,64,82,84,85,88,131,134,137,138,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,180,182,191,193,196,197,],[-15,92,-38,-37,-39,-40,-62,170,173,174,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,-70,-71,-75,-72,-73,-74,]),'OPEN_SQUARE_BRACKET':([10,31,82,128,],[17,-15,107,17,]),'INC':([15,26,27,28,31,37,42,56,57,65,70,71,82,83,84,85,86,88,96,97,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,125,126,127,129,131,132,133,135,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,178,181,183,185,186,188,189,192,],[23,23,23,23,-15,23,23,23,23,23,23,23,-38,-35,-37,-39,-36,-40,23,23,23,23,23,23,23,-34,23,23,23,23,23,23,23,23,-33,23,23,23,23,23,23,23,23,-62,-77,23,23,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,-80,23,-76,-79,-78,-81,-13,-82,]),'AND':([134,191,193,],[168,194,168,]),'END':([15,22,26,27,28,31,36,37,38,39,42,58,59,60,62,68,72,82,83,84,85,86,88,110,119,131,132,133,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,167,172,175,176,177,178,183,185,186,188,189,192,],[-32,-19,-32,-32,-32,-15,-22,-32,-14,69,-32,-18,-21,-16,-23,-17,-20,-38,-35,-37,-39,-36,-40,-34,-33,-62,-77,-32,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,179,-60,-59,-58,-53,-80,-76,-79,-78,-81,-13,-82,]),'POINT':([69,],[98,]),'VAR':([0,43,48,49,],[4,4,4,4,]),'ASSIGNMENT':([24,31,],[56,-15,]),'OR':([134,191,193,],[169,195,169,]),'NUMBER':([10,17,56,57,65,70,71,74,75,77,96,97,105,106,107,108,109,111,112,113,114,115,116,117,118,120,121,122,123,125,126,127,129,135,181,],[16,47,84,84,84,84,84,47,47,47,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,84,]),'SEMICOLON':([16,18,19,30,31,51,52,53,54,76,82,83,84,85,86,88,104,130,131,136,139,140,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,179,],[43,48,49,62,-15,-29,-30,-31,80,-5,-38,110,-37,-39,119,-40,141,166,-62,172,175,176,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,189,]),'ELSE':([178,189,],[187,-13,]),'STRING':([10,17,56,57,65,70,71,74,75,77,96,97,105,106,107,108,109,111,112,113,114,115,116,117,118,120,121,122,123,125,126,127,129,135,181,],[19,45,85,85,85,85,85,45,45,45,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,]),'LENGTH':([15,26,27,28,31,37,42,56,57,65,70,71,82,83,84,85,86,88,96,97,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,125,126,127,129,131,132,133,135,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,178,181,183,185,186,188,189,192,],[32,32,32,32,-15,32,32,32,32,32,32,32,-38,-35,-37,-39,-36,-40,32,32,32,32,32,32,32,-34,32,32,32,32,32,32,32,32,-33,32,32,32,32,32,32,32,32,-62,-77,32,32,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,-80,32,-76,-79,-78,-81,-13,-82,]),'READLN':([15,26,27,28,31,37,42,56,57,65,70,71,82,83,84,85,86,88,96,97,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,125,126,127,129,131,132,133,135,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,178,181,183,185,186,188,189,192,],[29,29,29,29,-15,29,29,29,29,29,29,29,-38,-35,-37,-39,-36,-40,29,29,29,29,29,29,29,-34,29,29,29,29,29,29,29,29,-33,29,29,29,29,29,29,29,29,-62,-77,29,29,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,-80,29,-76,-79,-78,-81,-13,-82,]),'READ':([15,26,27,28,31,37,42,56,57,65,70,71,82,83,84,85,86,88,96,97,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,125,126,127,129,131,132,133,135,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,178,181,183,185,186,188,189,192,],[34,34,34,34,-15,34,34,34,34,34,34,34,-38,-35,-37,-39,-36,-40,34,34,34,34,34,34,34,-34,34,34,34,34,34,34,34,34,-33,34,34,34,34,34,34,34,34,-62,-77,34,34,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,-80,34,-76,-79,-78,-81,-13,-82,]),'MUL':([31,82,83,84,85,86,88,89,99,100,131,137,138,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,162,165,166,172,175,176,177,],[-15,105,112,115,-39,121,112,121,121,121,-62,121,121,-63,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,121,-61,-60,-59,-58,-53,]),'TO':([31,67,82,83,84,85,86,88,110,119,131,141,142,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,166,172,175,176,177,],[-15,97,-38,-35,-37,-39,-36,-40,-34,-33,-62,-63,-43,-44,-41,-42,-52,-51,-49,-50,-47,-48,-45,-46,-57,-56,-54,-55,-61,-60,-59,-58,-53,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'some_predicates':([33,168,169,194,195,],[64,180,182,196,197,]),'empty':([4,7,8,15,20,26,27,28,37,42,133,],[6,12,6,22,12,22,22,22,22,22,22,]),'begin_program':([0,43,48,49,],[2,73,78,79,]),'else':([178,],[188,]),'identifier':([15,26,27,28,35,37,42,55,56,57,61,63,65,66,70,71,96,97,105,106,107,108,109,111,112,113,114,115,116,117,118,120,121,122,123,125,126,127,128,129,133,135,181,],[24,24,24,24,24,24,24,81,82,82,90,91,82,95,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,163,82,24,82,82,]),'type':([21,],[54,]),'consts':([0,],[3,]),'predicate':([57,65,135,181,],[87,93,171,190,]),'function':([15,26,27,28,37,42,56,57,65,70,71,96,97,105,106,107,108,109,111,112,113,114,115,116,117,118,120,121,122,123,125,126,127,129,133,135,181,],[26,26,26,26,26,26,83,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,26,88,88,]),'for':([15,26,27,28,37,42,133,],[27,27,27,27,27,27,27,]),'another_identifiers':([7,20,],[13,50,]),'block':([92,159,170,173,174,187,],[132,178,183,185,186,192,]),'assignment':([15,26,27,28,35,37,42,133,],[28,28,28,28,67,28,28,28,]),'declarations':([4,8,],[9,14,]),'declaration':([4,8,],[8,8,]),'identifiers':([17,74,75,77,],[46,101,102,103,]),'arithmetic_expression':([56,57,65,70,71,96,97,105,106,107,108,109,111,112,113,114,115,116,117,118,120,121,122,123,125,126,127,129,135,181,],[86,89,89,99,100,137,138,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,161,162,165,89,89,]),'break':([15,26,27,28,37,42,133,],[36,36,36,36,36,36,36,]),'if':([15,26,27,28,37,42,133,],[37,37,37,37,37,37,37,]),'expression':([15,26,27,28,37,42,133,],[38,58,59,60,68,72,38,]),'body':([15,133,],[39,167,]),'matrix':([10,128,],[18,164,]),'while':([15,26,27,28,37,42,133,],[42,42,42,42,42,42,42,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> consts","S'",1,None,None,None),
  ('consts -> CONST IDENTIFIER EQUALITY NUMBER SEMICOLON begin_program','consts',6,'p_consts','main.py',70),
  ('consts -> CONST IDENTIFIER EQUALITY STRING SEMICOLON begin_program','consts',6,'p_consts','main.py',71),
  ('consts -> CONST IDENTIFIER EQUALITY matrix SEMICOLON begin_program','consts',6,'p_consts','main.py',72),
  ('consts -> begin_program','consts',1,'p_consts','main.py',73),
  ('matrix -> OPEN_SQUARE_BRACKET identifiers CLOSE_SQUARE_BRACKET','matrix',3,'p_matrix','main.py',83),
  ('identifiers -> IDENTIFIER ZAPYATAYA identifiers','identifiers',3,'p_identifiers','main.py',90),
  ('identifiers -> NUMBER ZAPYATAYA identifiers','identifiers',3,'p_identifiers','main.py',91),
  ('identifiers -> STRING ZAPYATAYA identifiers','identifiers',3,'p_identifiers','main.py',92),
  ('identifiers -> IDENTIFIER','identifiers',1,'p_identifiers','main.py',93),
  ('identifiers -> NUMBER','identifiers',1,'p_identifiers','main.py',94),
  ('identifiers -> STRING','identifiers',1,'p_identifiers','main.py',95),
  ('begin_program -> VAR declarations BEGIN body END POINT','begin_program',6,'p_begin_program','main.py',105),
  ('block -> BEGIN body END SEMICOLON','block',4,'p_block','main.py',112),
  ('body -> expression','body',1,'p_body','main.py',119),
  ('identifier -> IDENTIFIER','identifier',1,'p_identifier','main.py',126),
  ('expression -> assignment expression','expression',2,'p_expression','main.py',135),
  ('expression -> if expression','expression',2,'p_expression','main.py',136),
  ('expression -> function expression','expression',2,'p_expression','main.py',137),
  ('expression -> empty','expression',1,'p_expression','main.py',138),
  ('expression -> while expression','expression',2,'p_expression','main.py',139),
  ('expression -> for expression','expression',2,'p_expression','main.py',140),
  ('expression -> break','expression',1,'p_expression','main.py',141),
  ('break -> BREAK SEMICOLON','break',2,'p_break','main.py',152),
  ('declarations -> declaration declarations','declarations',2,'p_declarations','main.py',159),
  ('declarations -> empty','declarations',1,'p_declarations','main.py',160),
  ('declaration -> IDENTIFIER another_identifiers COLON type SEMICOLON','declaration',5,'p_declaration','main.py',170),
  ('another_identifiers -> ZAPYATAYA IDENTIFIER another_identifiers','another_identifiers',3,'p_another_identifiers','main.py',182),
  ('another_identifiers -> empty','another_identifiers',1,'p_another_identifiers','main.py',183),
  ('type -> TYPE_STRING','type',1,'p_type','main.py',196),
  ('type -> TYPE_INTEGER','type',1,'p_type','main.py',197),
  ('type -> TYPE_REAL','type',1,'p_type','main.py',198),
  ('empty -> <empty>','empty',0,'p_empty','main.py',205),
  ('assignment -> identifier ASSIGNMENT arithmetic_expression SEMICOLON','assignment',4,'p_assignment','main.py',212),
  ('assignment -> identifier ASSIGNMENT function SEMICOLON','assignment',4,'p_assignment','main.py',213),
  ('assignment -> identifier ASSIGNMENT function','assignment',3,'p_assignment','main.py',214),
  ('assignment -> identifier ASSIGNMENT arithmetic_expression','assignment',3,'p_assignment','main.py',215),
  ('arithmetic_expression -> NUMBER','arithmetic_expression',1,'p_arithmetic_expression','main.py',222),
  ('arithmetic_expression -> identifier','arithmetic_expression',1,'p_arithmetic_expression','main.py',223),
  ('arithmetic_expression -> STRING','arithmetic_expression',1,'p_arithmetic_expression','main.py',224),
  ('arithmetic_expression -> function','arithmetic_expression',1,'p_arithmetic_expression','main.py',225),
  ('arithmetic_expression -> identifier PLUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','main.py',226),
  ('arithmetic_expression -> identifier MINUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','main.py',227),
  ('arithmetic_expression -> identifier MUL arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','main.py',228),
  ('arithmetic_expression -> identifier DIV arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','main.py',229),
  ('arithmetic_expression -> NUMBER PLUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','main.py',230),
  ('arithmetic_expression -> NUMBER MINUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','main.py',231),
  ('arithmetic_expression -> NUMBER MUL arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','main.py',232),
  ('arithmetic_expression -> NUMBER DIV arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','main.py',233),
  ('arithmetic_expression -> function PLUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','main.py',234),
  ('arithmetic_expression -> function MINUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','main.py',235),
  ('arithmetic_expression -> function MUL arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','main.py',236),
  ('arithmetic_expression -> function DIV arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','main.py',237),
  ('arithmetic_expression -> identifier OPEN_SQUARE_BRACKET arithmetic_expression CLOSE_SQUARE_BRACKET','arithmetic_expression',4,'p_arithmetic_expression','main.py',238),
  ('arithmetic_expression -> arithmetic_expression PLUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','main.py',239),
  ('arithmetic_expression -> arithmetic_expression MINUS arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','main.py',240),
  ('arithmetic_expression -> arithmetic_expression MUL arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','main.py',241),
  ('arithmetic_expression -> arithmetic_expression DIV arithmetic_expression','arithmetic_expression',3,'p_arithmetic_expression','main.py',242),
  ('function -> WRITE OPEN_BRACKET arithmetic_expression CLOSE_BRACKET SEMICOLON','function',5,'p_function','main.py',288),
  ('function -> WRITELN OPEN_BRACKET arithmetic_expression CLOSE_BRACKET SEMICOLON','function',5,'p_function','main.py',289),
  ('function -> READ OPEN_BRACKET identifier CLOSE_BRACKET SEMICOLON','function',5,'p_function','main.py',290),
  ('function -> READLN OPEN_BRACKET identifier CLOSE_BRACKET SEMICOLON','function',5,'p_function','main.py',291),
  ('function -> LENGTH OPEN_BRACKET identifier CLOSE_BRACKET','function',4,'p_function','main.py',292),
  ('function -> INC OPEN_BRACKET identifier CLOSE_BRACKET SEMICOLON','function',5,'p_function','main.py',293),
  ('predicate -> arithmetic_expression COMPARISON arithmetic_expression','predicate',3,'p_predicate','main.py',306),
  ('predicate -> arithmetic_expression EQUALITY arithmetic_expression','predicate',3,'p_predicate','main.py',307),
  ('predicate -> arithmetic_expression NON_EQUALITY arithmetic_expression','predicate',3,'p_predicate','main.py',308),
  ('predicate -> arithmetic_expression NON_STRICT_COMPARISON arithmetic_expression','predicate',3,'p_predicate','main.py',309),
  ('predicate -> arithmetic_expression IN identifier','predicate',3,'p_predicate','main.py',310),
  ('predicate -> arithmetic_expression IN matrix','predicate',3,'p_predicate','main.py',311),
  ('some_predicates -> OPEN_BRACKET predicate CLOSE_BRACKET AND some_predicates','some_predicates',5,'p_some_predicates','main.py',366),
  ('some_predicates -> OPEN_BRACKET predicate CLOSE_BRACKET OR some_predicates','some_predicates',5,'p_some_predicates','main.py',367),
  ('some_predicates -> OPEN_BRACKET predicate CLOSE_BRACKET','some_predicates',3,'p_some_predicates','main.py',368),
  ('some_predicates -> OPEN_BRACKET NOT OPEN_BRACKET predicate CLOSE_BRACKET CLOSE_BRACKET AND some_predicates','some_predicates',8,'p_some_predicates','main.py',369),
  ('some_predicates -> OPEN_BRACKET NOT OPEN_BRACKET predicate CLOSE_BRACKET CLOSE_BRACKET OR some_predicates','some_predicates',8,'p_some_predicates','main.py',370),
  ('some_predicates -> OPEN_BRACKET NOT OPEN_BRACKET predicate CLOSE_BRACKET CLOSE_BRACKET','some_predicates',6,'p_some_predicates','main.py',371),
  ('while -> WHILE OPEN_BRACKET predicate CLOSE_BRACKET DO block','while',6,'p_while','main.py',385),
  ('while -> WHILE some_predicates DO block','while',4,'p_while','main.py',386),
  ('for -> FOR assignment TO arithmetic_expression DO block','for',6,'p_for','main.py',396),
  ('for -> FOR assignment DOWNTO arithmetic_expression DO block','for',6,'p_for','main.py',397),
  ('if -> IF OPEN_BRACKET predicate CLOSE_BRACKET THEN block','if',6,'p_if','main.py',404),
  ('if -> IF OPEN_BRACKET predicate CLOSE_BRACKET THEN block else','if',7,'p_if','main.py',405),
  ('else -> ELSE block','else',2,'p_else','main.py',415),
]
