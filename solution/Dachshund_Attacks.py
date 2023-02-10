import binascii

def findConvergent(continuedFraction):
    convergent = {'q': continuedFraction[-1], 'r': 1}
    for i in range(2,len(continuedFraction)+1):
            r = convergent['q'] * continuedFraction[-i] + convergent['r']
            k = convergent['q']  # swapping the q and r
            convergent['q'] = r
            convergent['r'] = k
    return convergent;

def getContinuedFraction(N, e, continuedFraction):
    continuedFraction.append(N // e)
    if N % e == 0:
        return continuedFraction
    getContinuedFraction(e, N%e, continuedFraction);
    return continuedFraction

def getAllConvergent(continuedFraction):
    convergents = [];
    for i in range(1, len(continuedFraction)+1):
        convergent = findConvergent(continuedFraction[0:i]);
        convergents.append(convergent)
    return convergents

def nth_power(number, root): #optimized
    upper_limit = 1;
    while upper_limit ** root <= number:
        upper_limit *= 2;

    lower_limit = upper_limit // 2;
    mid = 0;
    while(lower_limit < upper_limit):
        mid = ( upper_limit + lower_limit ) // 2;
        mid_nth = mid ** root;

        if(lower_limit < mid and mid_nth < number):
            lower_limit = mid;
        elif(upper_limit > mid and mid_nth > number):
            upper_limit = mid;
        else:
            return mid
    return mid + 1;

e= 19649751034810400943283548429390064217341526009009000122281000612844616743362438196340509523080590930937923662757064230544860981149006228071923628243481699288525054208810014205979819187519706937063534080759281353920860320294997591430867738516427205745638140672054298191479069645267327155626206548692931191789
n= 89356789188620988570596358650100101258016048853085356642697048564457016995054963149409477708013023410771909954592504681780777028223799640066214540691249385207159079903238615244109019808666670336491368305232421829040458810037096815143698297431899397246903111035351422819655115937796515914305750474697075335727
ci= 31495636123284301671864958502326483431236216519186292390522204433377295836516199001038994481364113533494993303448021967446328436613418919873419791570765433430070859544243741420738171131390685622742023908874651151842275040237126477074750224430955088888080447529105923176538999954347242935995356027941420356686

# every thing I did is correct the only problem is that the error i get is that oddlength string
# the error was that the ci was named c and it was getting reassigned when doing the roots thing
continuedFraction = getContinuedFraction(n, e, [])
allConvergents = getAllConvergent(continuedFraction)


for convergent in allConvergents:
    d = convergent['q']
    k = convergent['r']

    if(d % 2 == 0 or (e * d - 1) % k != 0): continue;

    fiN = (e*d - 1) // k;
    a = 1
    b = -1 * ( n - fiN + 1 )
    c = n
    plusx = ( - b + nth_power( (b ** 2 - 4 * a * c), 2) ) // 2
    negx = ( - b - nth_power( (b ** 2 - 4 * a * c), 2) ) // 2
    if(negx > 0 and plusx > 0 and negx * plusx == n):
        dc = pow(ci,d,n);
        st = ("{:x}".format(dc));
        print(binascii.unhexlify(st));
