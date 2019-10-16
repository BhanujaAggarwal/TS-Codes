def convert2digits(n: int ) -> str:
    upto20=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","eleven ", "twelve ","thirteen ",
    "fourteen ", "fifteen ","sixteen ", "seventeen ", "eighteen ","nineteen "]
    tens=["","ten","twenty ", "thirty ", "forty ","fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
    if n<20:
        return upto20[n]
    return tens[n//10] + upto20[n%10]

def convert3digits(n:int) -> str:
    if n<100:
        return convert2digits(n)
    return upto20[n//100] + "Hundred" + convert2digits(n%100)

def split(n:int,denoms:[int]) -> [(int,int)]:
    if len(denoms) == 1:
        return [(n,denoms[0])]
    return [n//denoms[0],denoms[0]]+split(n%denoms[0],denoms[1: ])

def convert_denoms(pairs:[(int,int)],names:{int:str}) -> [(int,str)]:
    return [(a,names[b]) for a,b in pairs]

def convert_times(pairs:[(int,str)]) -> [(str,str)]:
    return [(convert3digits(a),b) for a,b in pairs if a>0]

def fig2words(n:int) -> str:
    denoms={10000000:"crore",100000:"lakh",1000:"thousand",1:""}
    denom_names=denom.values()
    denom_values=denom.keys()
    num_pairs=split(n,denom_values)
    num_name_pairs=convert_denoms(num_pairs,denoms)
    name_pairs=convert_times(num_name_pairs)
    return name_pairs
