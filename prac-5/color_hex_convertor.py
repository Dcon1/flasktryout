COLOR_HEX = {"aliceblue": "#f0f8ff", "blanchedalmond": "#ffebcd", "blue": "#0000ff", "brown": "#a52a2a",
             "coral": "#ff7f50", "cyan": "#00ffff", "darkgreen": "#006400", "darkorange": "#ff8c00",
             "darkviolet": "#9400d3", "gold": "#ffd700", "gray": "#bebebe", "hotpink": "#ff69b4"}

color = str(input("Enter a color"))
while color.lower() != "":
    if color.lower() in COLOR_HEX:
        print("{} is {}".format(color, COLOR_HEX[color.lower()]))
    else:
        print("invalid color try again")
    color = str(input("Enter a color"))