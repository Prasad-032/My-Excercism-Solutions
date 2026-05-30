def translate(w):
    ws = w.split()
    trns_ws = []
    for wr in ws:
        if wr[0] in "aeiou" or wr.startswith("xr") or wr.startswith("yt"):
            pass  # no change needed
        elif wr[0] == "y":
            wr =  wr[1:] + wr[0] # move y to end
        else:
            if wr[:3] == "squ":
                wr = wr[3:] + wr[:3]
            elif wr[:2] == "qu":
                wr = wr[2:] + wr[:2]
            else:
                count = 0
                while wr[0] not in "aeiou" and not (wr[0] == "y" and count > 0):
                    wr = wr[1:] + wr[0]
                    count += 1
                    if count == len(wr):  # fix typo here too
                        break
        wr = wr + "ay"
        trns_ws.append(wr)
    return " ".join(trns_ws)