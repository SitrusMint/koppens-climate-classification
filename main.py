def devide():
    precipitation = 0
    err_msg = "雨量は0より小さくはならない"

    coldest_temp = float(input("最寒月の平均気温は？(℃)"))

    warmest_temp = float(input("最暖月の平均気温は？(℃)"))
    
    precipitation = float(input("年間降水量は？(mm)"))
    if precipitation < 0:
        return f"Err: {err_msg}"

    min_rainfall = float(input("最小雨月の雨量は？(mm)"))
    
    max_rainfall = float(input("最大雨月の雨量は？(mm)")) 
    
    if not(min_rainfall < 0 or max_rainfall < 0):
        f_or_other = min_rainfall*3 < max_rainfall
    else:
        return f"Err: {err_msg}" 

    if 8.0 < coldest_temp and warmest_temp < 15.0: # H 高山
        return "H"

    if coldest_temp < 3.0: # E 寒帯
        if 0.0 <= warmest_temp < 10.0:
            return "ET"
        else:
            return "EF"

    if coldest_temp < 3.0 and 10.0 < warmest_temp: # D 冷帯
        if f_or_other:
            return "Dw"
        else:
            return "Df"

    if 18.0 <= coldest_temp and 500.0 <= precipitation: # A 熱帯
        if f_or_other:
            return "Af"
        else:
            return "Aw"

    if precipitation < 500.0: # B 乾燥帯
        if 250.0 <= precipitation:
            return "BS"
        else:
            return "BW"

    if -3.0 <= coldest_temp < 18.0 and 500.0 <= precipitation: # C 温帯
        if f_or_other and 22.0 <= warmest_temp:
            return "Cfa"
        elif f_or_other and warmest_temp < 22:
            return "Cfb"
        else:
            def summer_or_winter(answer):
                if answer == "y":
                    return "Cs"
                elif answer == "n":
                    return "Cw"
                else:
                    return "Err"

            month = input("最小雨月の気温は高いですか？[y/n]")
            result = summer_or_winter(month)
            while result != "Err":
                result = summer_or_winter(input("入力を間違えています\n[y/n]？"))
            return result

    return "Err"

def main():
    print("ケッペンの気候区分プログラム")
    result = devide()
    if result == "Err":
        raise Exception
    print(f"気候は{result}です")

if __name__ == '__main__':
    main()