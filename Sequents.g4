grammar Sequents;

// we skip whitespaces
WS: [ \t\n]+ -> skip ;
ATOM: [a-z] [a-zA-Z0-9_]* ;
VARIABLE: [A-Z] [a-zA-Z0-9_]* ;

sequent: seq=decorated_sequent EOF # DecoratedSequent
       | seq=simple_sequent EOF # SimpleSequent
       ;

// sequents without lambda terms

simple_sequent: hyps=hypotheses '|-' cons=consequence ;

hypotheses: (first=formula)? (',' rest+=formula)* ;

consequence: form=formula ;

formula: '<' monadtype=ATOM? '>' body=formula    # MonadFormula
       | left=formula '*' right=formula          # TensorFormula
       | left=formula '-o' right=formula         # ImplicationFormula
       | body=ATOM ('.' c_type=ATOM)?            # AtomFormula
       | body=VARIABLE ('.' v_type=ATOM)?        # VariableFormula
       | '(' body=formula ')'                    # ParensFormula
       ;




// sequents with lambda terms

decorated_sequent: hyps=decorated_hypotheses '|-' cons=consequence ;

decorated_hypotheses: (first=decorated_formula)? (',' rest+=decorated_formula)* ;

decorated_formula: term=ATOM ':' form=formula ;




