
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = '2B2A110D42CBB532415FA61D324535C7'
    
_lr_action_items = {'RPAREN':([9,11,12,15,],[-9,-8,14,-7,]),'NAME':([0,7,8,13,14,17,],[1,11,11,11,1,1,]),'NUMBER':([7,8,13,],[9,9,9,]),'ELSE':([9,10,11,15,16,],[-9,-4,-8,-7,17,]),'LPAREN':([5,],[8,]),'OPERATOR':([9,10,11,12,15,],[-9,13,-8,13,13,]),'END':([9,10,11,15,16,19,],[-9,-4,-8,-7,18,20,]),'IF':([0,],[5,]),'ASSIGN':([1,],[7,]),'$end':([2,3,4,6,9,10,11,15,18,20,],[-2,0,-1,-3,-9,-4,-8,-7,-5,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'assignment':([0,14,17,],[2,16,19,]),'program':([0,],[3,]),'expression':([7,8,13,],[10,12,15,]),'statement':([0,],[4,]),'if':([0,],[6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement','program',1,'p_program','task5.py',49),
  ('statement -> assignment','statement',1,'p_statement','task5.py',51),
  ('statement -> if','statement',1,'p_statement','task5.py',52),
  ('assignment -> NAME ASSIGN expression','assignment',3,'p_assignment','task5.py',54),
  ('if -> IF LPAREN expression RPAREN assignment END','if',6,'p_if','task5.py',56),
  ('if -> IF LPAREN expression RPAREN assignment ELSE assignment END','if',8,'p_if','task5.py',57),
  ('expression -> expression OPERATOR expression','expression',3,'p_expression','task5.py',60),
  ('expression -> NAME','expression',1,'p_expression_name','task5.py',64),
  ('expression -> NUMBER','expression',1,'p_expression_num','task5.py',67),
]