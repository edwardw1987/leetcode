class Solution(object):

    def handle_loop(self, arr, s):
        mc = arr.pop()
        while arr:
            for i in range(len(arr) - 1, -1, -1):
                arr_i = arr[i]
                if arr_i:
                    if mc:
                        s += mc.pop()
                    s += arr_i.pop()
                    if not arr_i:
                        arr.pop(i)

        while mc:
            s += mc.pop()
            if len(s) >= 2:
                if s[-1] == s[-2]:
                    return ""
        return s

    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """ 
        counter = {}
        for i in S:
            counter.setdefault(i, []).append(i)
        arr = sorted(counter.values(), key=lambda x: len(x))
        s = ''
        if len(arr[-1]) <= len(arr) or len(arr[-1]) >= sum(len(a) for a in arr[:-1]):
            return self.handle_loop(arr, s)
        while arr:
            for i in range(len(arr) - 1, 0, -2):
                a = arr[i]
                b = arr[i - 1]
                # print s, len(s), a,b
                while a and b:
                    if a:
                        s += a.pop()
                    if b:
                        s += b.pop()
                if not a:
                    arr.pop(i)
                if not b:
                    arr.pop(i - 1)
            if len(arr) == 1 and len(arr[0]) > 1:
                return ""
            arr = sorted(arr, key=lambda x: len(x))
            if arr and len(arr[-1]) <= len(arr):
                return self.handle_loop(arr, s)
        return s


if __name__ == '__main__':
    s = "tndsewnllhrtwsvxenkscbivijfqnysamckzoyfnapuotmdexzkkrpmppttficzerdndssuveompqkemtbwbodrhwsfpbmkafpwyedpcowruntvymxtyyejqtajkcjakghtdwmuygecjncxzcxezgecrxonnszmqmecgvqqkdagvaaucewelchsmebikscciegzoiamovdojrmmwgbxeygibxxltemfgpogjkhobmhwquizuwvhfaiavsxhiknysdghcawcrphaykyashchyomklvghkyabxatmrkmrfsppfhgrwywtlxebgzmevefcqquvhvgounldxkdzndwybxhtycmlybhaaqvodntsvfhwcuhvuccwcsxelafyzushjhfyklvghpfvknprfouevsxmcuhiiiewcluehpmzrjzffnrptwbuhnyahrbzqvirvmffbxvrmynfcnupnukayjghpusewdwrbkhvjnveuiionefmnfxao"
    s2 = "gpneqthatplqrofqgwwfmhzxjddhyupnluzkkysofgqawjyrwhfgdpkhiqgkpupgdeonipvptkfqluytogoljiaexrnxckeofqojltdjuujcnjdjohqbrzzzznymyrbbcjjmacdqyhpwtcmmlpjbqictcvjgswqyqcjcribfmyajsodsqicwallszoqkxjsoskxxstdeavavnqnrjelsxxlermaxmlgqaaeuvneovumneazaegtlztlxhihpqbajjwjujyorhldxxbdocklrklgvnoubegjrfrscigsemporrjkiyncugkksedfpuiqzbmwdaagqlxivxawccavcrtelscbewrqaxvhknxpyzdzjuhvoizxkcxuxllbkyyygtqdngpffvdvtivnbnlsurzroxyxcevsojbhjhujqxenhlvlgzcsibcxwomfpyevumljanfpjpyhsqxxnaewknpnuhpeffdvtyjqvvyzjeoctivqwann"
    # run()
    for s in [
    "aab",
    "aaab",
    'baaba',
    "vvvlo",
    "bbbbbbb",
    "ogccckcwmbmxtsbmozli",
    "blflxll",
    "bababababababababbab",
    "zqugrfbsznyiwbokwkpvpmeyvaosdkedbgjogzdpwawwl",
    "abbabbaaab",
    "krkrktktkakpkqkwkzk",
    s,
    s2,
    ]:
        print "REAL:$%s" % repr(Solution().reorganizeString(s))
        # print len(s)
                                                         # czcxcwctmsmlmkbibgoo
                                                         # cocgcickmlmsmtbwbxoz