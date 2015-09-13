Expression Tree Calculator
========
    
The primary logic is simple:

* Take full expression and get the priority scope. (deepest nested "()")
* Take the priority scope and get the priority simple expression. (operation and two operands, per operation precedence)
* Evaluate the simple expression
* Replace the priority expression in the full expression with the answer to the priority expression

### Illustration

Note: Not exactly the same implementation, but the same idea. Start reading from the bottom. (highest priority scope and expression)

![Expression Tree Illustration](http://www.composingprograms.com/img/expression_tree.png)

### Program execution trace examples

Example 1:

    Initial expression:  (2+3)
    ------------------------------------------------

    get_priority_scope('(2+3)',) -> (2+3)

    get_priority_simple_expr('(2+3)',) -> 2+3

    eval_basic_expr('2+3',) -> 5.0

    replace_expr('(2+3)', '2+3', '5.0') -> 5.0

    ------------------------------------------------
    Answer:              5.0

Example 2:

    Initial expression:  (2*(2/3)-4)
    ------------------------------------------------

    get_priority_scope('(2*(2/3)-4)',) -> (2/3)

    get_priority_simple_expr('(2/3)',) -> 2/3

    eval_basic_expr('2/3',) -> 0.6666666666666666

    replace_expr('(2*(2/3)-4)', '2/3', '0.6666666666666666') -> (2*0.6666666666666666-4)

    get_priority_scope('(2*0.6666666666666666-4)',) -> (2*0.6666666666666666-4)

    get_priority_simple_expr('(2*0.6666666666666666-4)',) -> 2*0.6666666666666666

    eval_basic_expr('2*0.6666666666666666',) -> 1.3333333333333333

    replace_expr('(2*0.6666666666666666-4)', '2*0.6666666666666666', '1.3333333333333333') -> (1.3333333333333333-4)

    get_priority_scope('(1.3333333333333333-4)',) -> (1.3333333333333333-4)

    get_priority_simple_expr('(1.3333333333333333-4)',) -> 1.3333333333333333-4

    eval_basic_expr('1.3333333333333333-4',) -> -2.666666666666667

    replace_expr('(1.3333333333333333-4)', '1.3333333333333333-4', '-2.666666666666667') -> -2.666666666666667

    ------------------------------------------------
    Answer:              -2.666666666666667
    
Example 3:
    
    Initial expression:  (2+2-4*(8-7+3+3/4))
    ------------------------------------------------

    get_priority_scope('(2+2-4*(8-7+3+3/4))',) -> (8-7+3+3/4)

    get_priority_simple_expr('(8-7+3+3/4)',) -> 3/4

    eval_basic_expr('3/4',) -> 0.75

    replace_expr('(2+2-4*(8-7+3+3/4))', '3/4', '0.75') -> (2+2-4*(8-7+3+0.75))

    get_priority_scope('(2+2-4*(8-7+3+0.75))',) -> (8-7+3+0.75)

    get_priority_simple_expr('(8-7+3+0.75)',) -> 8-7

    eval_basic_expr('8-7',) -> 1.0

    replace_expr('(2+2-4*(8-7+3+0.75))', '8-7', '1.0') -> (2+2-4*(1.0+3+0.75))

    get_priority_scope('(2+2-4*(1.0+3+0.75))',) -> (1.0+3+0.75)

    get_priority_simple_expr('(1.0+3+0.75)',) -> 1.0+3

    eval_basic_expr('1.0+3',) -> 4.0

    replace_expr('(2+2-4*(1.0+3+0.75))', '1.0+3', '4.0') -> (2+2-4*(4.0+0.75))

    get_priority_scope('(2+2-4*(4.0+0.75))',) -> (4.0+0.75)

    get_priority_simple_expr('(4.0+0.75)',) -> 4.0+0.75

    eval_basic_expr('4.0+0.75',) -> 4.75

    replace_expr('(2+2-4*(4.0+0.75))', '4.0+0.75', '4.75') -> (2+2-4*4.75)

    get_priority_scope('(2+2-4*4.75)',) -> (2+2-4*4.75)

    get_priority_simple_expr('(2+2-4*4.75)',) -> 4*4.75

    eval_basic_expr('4*4.75',) -> 19.0

    replace_expr('(2+2-4*4.75)', '4*4.75', '19.0') -> (2+2-19.0)

    get_priority_scope('(2+2-19.0)',) -> (2+2-19.0)

    get_priority_simple_expr('(2+2-19.0)',) -> 2+2

    eval_basic_expr('2+2',) -> 4.0

    replace_expr('(2+2-19.0)', '2+2', '4.0') -> (4.0-19.0)

    get_priority_scope('(4.0-19.0)',) -> (4.0-19.0)

    get_priority_simple_expr('(4.0-19.0)',) -> 4.0-19.0

    eval_basic_expr('4.0-19.0',) -> -15.0

    replace_expr('(4.0-19.0)', '4.0-19.0', '-15.0') -> -15.0

    ------------------------------------------------
    Answer:              -15.0    
    
### Implementation Notes

* Non formal ad hoc implementation  
* No error handling, expects correct (slightly formatted) expression into calc_eval
* Code is written in functional programming style (thus also non pythonic in parts)
* All main function are pure functions, except calc_eval which has a "of no significant importance" parameter and printing. Thus:
    * Function output depends only on input. All functions also have a return value.
    * Trace of functions gives full high level overview of program execution
    * Easily testable
    * Separation of concerns
    * Fine grained modulation
    * Stateless