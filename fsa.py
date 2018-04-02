import sys

lines = [l.strip() for l in sys.stdin]
states=[s for s in lines[0].split()]
transitions=dict([((a.split()[0], a.split()[1]), a.split()[2]) for a in lines[1:-1]])
input_string=lines[-1]
state=states[0]

if len(input_string)==0:
    print state

for letter in input_string:
    print state, letter, 
    try:
        state=transitions[(state, letter)]
    except:
        print "\nREJECT"
        sys.exit(0)
    print '->',state

accept=True if state[0].upper()==state[0] else False

if accept:
    print 'ACCEPT'
else:
    print 'REJECT'