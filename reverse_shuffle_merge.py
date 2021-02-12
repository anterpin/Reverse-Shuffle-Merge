# Complete the reverseShuffleMerge function below.
count = {}
actual_count = {}
passed_count = {}

def can_discard(letter,temp_passed_letter):
    global count
    global actual_count
    global passed_count
    total = count[letter]
    used = actual_count.get(letter,0)
    discarded = passed_count.get(letter,0) + temp_passed_letter - 1 - used
    return discarded < int(total/2)

def can_use(letter):
    global count
    global actual_count
    total = count[letter]
    used = actual_count.get(letter,0)
    return used < int(total/2)

def update_passed(temp_passed):
    global passed_count
    for letter, count in temp_passed.items():
        passed_count[letter] = passed_count.get(letter,0) + count

def get_min_non_discartable_letter(index,actual,s):
    global passed_count
    minimum = '{'
    minimum_index = index
    i = index
    temp_passed = {}
    while i >= 0:
        letter = s[i]
        temp_passed[letter] = temp_passed.get(letter,0) + 1
        if can_use(letter):
            if letter < minimum:
                minimum = letter
                minimum_index = i
                update_passed(temp_passed)
                temp_passed = {}
        if not can_discard(letter,temp_passed.get(letter,0)):
            break
        i += -1
    return (minimum,minimum_index)

def reverseShuffleMerge(s):
    global count
    global actual_count
    global passed_count
    count = {x:s.count(x) for x in set(s)}
    passed_count = {}
    actual_count = {}
    index = len(s)-1
    actual = ''
    i = 0
    while i < int(len(s)/2):
        (letter,letter_index) = get_min_non_discartable_letter(index,actual,s)
        actual += letter
        actual_count[letter] = actual_count.get(letter,0) + 1
        index = letter_index - 1
        i += 1
    return actual

if __name__ == '__main__':
    s = reverseShuffleMerge('bdabaceadaedaaaeaecdeadababdbeaeeacacaba')
    print(s)
    print('aaaaaabaaceededecbdb')
    s = reverseShuffleMerge('djjcddjggbiigjhfghehhbgdigjicafgjcehhfgifadihiajgciagicdahcbajjbhifjiaajigdgdfhdiijjgaiejgegbbiigida')
    print(s)
    print('aaaaabccigicgjihidfiejfijgidgbhhehgfhjgiibggjddjjd')
    s = reverseShuffleMerge('fwfcrwgpfflojzfiljoqluudqxrymtegsydlyvvgmfgpwkqxixelvpnlvlrxlzxyyuwmvlmnnnfvvzloypchaaqxinfvraefxrwdtlaydcljlfxkmaznojjtjaesunggyjrkkfruyjlnqjksttnegzaenrhbefrybuzobtpglngfkrckbxognhzzqwaimpqoepkcjralekbrtgdziltaznrazwoljjgrjtfrmpwutzltlfyxcmrsvjkddhnkytdvbhydfxnsoyrnrmtahvhkdfogdeghjbtlgmckossrgsaoxijvpjickcunwjgkldcnprtkrfvytlyibsngvlbtkheeokwbalqmjksmjscqkhplkghgehgbjzzynmrppfonuvlpjlzeeqjztcexvcbecdstrggoemgpmsmmlroyglzdmunrfjtmqbkrrfqewpafhfmqhzhokzyjigiwkgkrkrhtqqvpgetwtzflcmxnsljuxcvivjsmjzyjptrofjfxocidxzefznuxnhzvjcgxpnymvkicnqqfchotgavqvwmivulgniatmeoqzymvsfjcqhcondbxqsukpulvuisjvzozedtepydvkoumpyvylzkqjvozhzrhkjfgkggwxjzesxtectvfvpkmfxddhjstomgfjqdyooxezsinfxwrknvtczgwwukwagjvdwiuwmbjigxnbrdyzepgeqfaezzekqvqdkkyiwpdfrjvxzxbltjrmulfceffmuzpzftodalvjejycdyzvgtggbaeedfvsstqomwmmdfsbxocfgqhkxjkqmradotmneufmbhgaklsrxkdkjlysgivqegsqtrrzpwrptelykgeatacslhqotootuhxloutefrksqwuiyvclfcmjkocjxgtqjshiyryccgesfgpjtxjohevathpvdmtppcbsnmsfezkbulprtphgcmqywrlefmbrebemjzfzhiqcolvhdduukstgrlo')
    assert s == 'aaaaaaaaaccddeikusbccfseagluimqvagocfqqcikvcjvhnuezxdcoxffortjyzjmsjvivcxujlsnxcfztwtegpvqqtgkwgijyzkohzhqmfhapweqbqmtfnumdzgolmmsmpgmeoggrtsdcebcvxectzjqeezjplvunofppmnyzzbgheghgklphkqcsjmsjmqabwkoeehktblvgnsbiltyvfrktrpcdkgjwnuckcijpvixosgrssokcmgltbhedgodkhvhtmrnryosnxfdyhbvdtykhddkjvsrmxyfltlztuwpmrftjrgjjlowzrnztizdgtrbkelrjkpeoqpmiwqzzhgoxbkrkfggptbozuyrfehrezenttskjqjyurfkkrjyggnusejtjjonzmkxfjldyltdwrxfervfixqhpyolzvvfnnnmlvmwuyyxzlxrlvlnpvlexixqkwpfmgvvyldysetmyrxqduulqojlfzjolffpgwrfwf'


