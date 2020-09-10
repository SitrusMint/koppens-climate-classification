def devide():
    precipitation = 0
    err_msg = "雨量は0より小さくはならない"

    coldest_temp = float(input("最寒月の平均気温は？(℃)"))

    precipitation = float(input("年間降水量は？(mm)"))
    if precipitation < 0:
        return f"Err: {err_msg}"

    warmest_temp = float(input("最暖月の平均気温は？(℃)"))

    min_rainfall = float(input("最小雨月の雨量は？(mm)"))
    if min_rainfall < 0:
        return f"Err: {err_msg}"

    max_rainfall = float(input("最大雨月の雨量は？(mm)")) 
    if max_rainfall < 0:
        return f"Err: {err_msg}"

    if 18.0 <= coldest_temp and 500.0 <= precipitation: # A 熱帯
        if min_rainfall*3 < max_rainfall:
            return "Af"
        else:
            return "Aw"

    if precipitation < 500.0: # B 乾燥帯
        if 250.0 <= precipitation:
            return "BS"
        else:
            return "BW"

    if -3.0 <= coldest_temp < 18.0 and 500.0 <= precipitation: # C 温帯
        if min_rainfall*3.0 < max_rainfall and 22.0 < warmest_temp:
            return "Cfa"
        else:
            return "Cfb"

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

    if coldest_temp < 3.0 and 10.0 < warmest_temp: # D 冷帯
        if min_rainfall*3.0 < max_rainfall:
            return "Dw"
        else:
            return "Df"

    if coldest_temp < 3.0: # E 寒帯
        if 0.0 <= warmest_temp < 10.0:
            return "ET"
        else:
            return "EF"

    if 8.0 < coldest_temp and warmest_temp < 15.0:
        return "H"

    return "Err"

def main():
    print("ケッペンの気候区分プログラム")
    result = devide()
    if result == "Err":
        raise Exception
    print(f"気候は{result}です")

if __name__ == '__main__':
    main()