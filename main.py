import random

if __name__ == '__main__':
    const = ["Если головка машины указывает на символ ", "При условии что под головкой машины находится символ ",
             "В том случае, когда под головкой символ "]
    final_text = ""
    dict = {}
    s = input().rstrip()
    ok = False
    key, value = "", []
    while '-1' not in s.strip():
        if "#" in s.strip():
            s = s[s.find("#")+1:]
        if 'table:' in s:
            ok = True
            s = input().rstrip()
            continue
        if ok:
            el = s.split(":")[0].rstrip()
            cnt = el.count("  ")
            if cnt == 1:
                dict[key.strip()] = value
                key = el
                value = []
            elif cnt == 2:
                value.append(s.strip())
        else:
            key, value = s.split(": ")
            dict[key] = value
        s = input().rstrip()


    if key.strip() not in dict:
        dict[key.strip()] = value
    ok = False
    end_state = list(dict.keys())[-1]
    temp = []
    for key in dict.keys():
        if key == 'start state':
            ok = True
            continue
        if ok:
            for el in dict[key]:
                ans = [key]
                symbol, do = "", ""
                if len(el.split(": ")) == 2:
                    symbol, do = el.split(": ")
                else:
                    for i in range(len(el)):
                        a = el[i]
                        if el[i] == ":":
                            symbol = el[:i]
                            do = el[i + 1:]
                            break

                t = 1
                ans0 = ans.copy()
                symbol1 = [symbol]
                do0 = do
                if symbol1[0][0] == "[":
                    symbol1 = symbol1[0].replace("[", "").replace("]", "").split(",")
                    t = len(symbol1)
                for _ in range(t):
                    symbol = symbol1[_]
                    do = do0
                    ans = ans0.copy()
                    ans.append(symbol)
                    if len(do.strip()) == 1:
                        ans.append(symbol)
                        ans.append(do.strip())
                        ans.append(key)
                    else:
                        do = do.replace("{", "").replace("}", "").split(",")
                        el = do[0]
                        dir = ""
                        if 'write' in do[0]:
                            ans.append(do[0].split(":")[1].strip())
                            dir = do[1]
                        else:
                            dir = do[0]
                            ans.append(symbol)
                        dir = dir.split(":")
                        if len(dir) == 1:
                            ans.append(dir[0].strip())
                            ans.append(key.strip())
                        else:
                            ans.append(dir[0].strip())
                            ans.append(dir[1].strip())
                    for _ in range(len(ans)):
                        ans[_] = ans[_].strip()
                    print(*ans, sep=", ")
                    form = {}
                    text = ""
                    if not temp:
                        temp.append(ans)
                    elif key.strip() == temp[-1][0]:
                        temp.append(ans)
                    else:
                        start_state = temp[0][0]
                        text += "Машина находится в состоянии " + start_state + ". "
                        for i in range(len(temp)):
                            k = temp[i]
                            cur_symbol = k[1].strip()
                            write_symbol = k[2].strip()
                            direction = k[3].strip()
                            next_state = k[4].strip()
                            it = random.randint(0, 2)
                            rand_state = const[it]
                            text += rand_state + cur_symbol + ", "
                            if cur_symbol == write_symbol:
                                text += "на ленте печатается тот же символ, "
                            else:
                                text += "на ленте печатается символ " + write_symbol + ", "
                            text += "головка машины сдвигается "
                            if direction == "R":
                                text += "вправо"
                            else:
                                text += "влево"
                            if next_state == start_state:
                                text += ". "
                            else:
                                text += ", "
                                if next_state != end_state:
                                    text += "машина переходит в состояние " + next_state + ". "
                                else:
                                    text += "машина переходит в конечное состояние " + next_state + ". "
                        temp = [ans]
                    final_text += text
                    final_text += "\n"
    if "Машина находится в состоянии " + key not in final_text:
        start_state = temp[0][0]
        text += "Машина находится в состоянии " + start_state + ". "
        for i in range(len(temp)):
            k = temp[i]
            cur_symbol = k[1].strip()
            write_symbol = k[2].strip()
            direction = k[3].strip()
            next_state = k[4].strip()
            it = random.randint(0, 2)
            rand_state = const[it]
            text += rand_state + cur_symbol + ", "
            if cur_symbol == write_symbol:
                text += "на ленте печатается тот же символ, "
            else:
                text += "на ленте печатается символ " + write_symbol + ", "
            text += "головка машины сдвигается "
            if direction == "R":
                text += "вправо"
            else:
                text += "влево"
            if next_state == start_state:
                text += ". "
            else:
                text += ", "
                if next_state != end_state:
                    text += "машина переходит в состояние " + next_state + ". "
                else:
                    text += "машина переходит в конечное состояние " + next_state + ". "
        final_text += text
    print(final_text)
