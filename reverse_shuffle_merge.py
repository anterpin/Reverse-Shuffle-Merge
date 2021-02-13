# Complete the reverseShuffleMerge function below.
class Counter:
    def __init__(self,s):
        self.count = {x:s.count(x) for x in set(s)}
        self.actual_count = {}
        self.passed_count = {}
        
    def can_discard(self,letter,temp_passed_letter):
        total = self.count[letter]
        used = self.actual_count.get(letter,0)
        discarded = self.passed_count.get(letter,0) + temp_passed_letter - 1 - used
        return discarded < int(total/2)

    def can_use(self,letter):
        total = self.count[letter]
        used = self.actual_count.get(letter,0)
        return used < int(total/2)

    def update_passed(self,temp_passed):
        for letter, count in temp_passed.items():
            self.passed_count[letter] = self.passed_count.get(letter,0) + count
           
    def increase_actual_count(self,letter):
        self.actual_count[letter] = self.actual_count.get(letter,0) + 1

def get_min_non_discartable_letter(index,counter,s):
    global passed_count
    minimum = '{'
    minimum_index = index
    i = index
    temp_passed = {}
    while i >= 0:
        letter = s[i]
        temp_passed[letter] = temp_passed.get(letter,0) + 1
        if counter.can_use(letter):
            if letter < minimum:
                minimum = letter
                minimum_index = i
                counter.update_passed(temp_passed)
                temp_passed = {}
        if not counter.can_discard(letter,temp_passed.get(letter,0)):
            break
        i += -1
    return (minimum,minimum_index)

def reverseShuffleMerge(s):
    counter = Counter(s)
    index = len(s)-1
    actual = ''
    i = 0
    while i < int(len(s)/2):
        (letter,letter_index) = get_min_non_discartable_letter(index,counter,s)
        actual += letter
        counter.increase_actual_count()
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


