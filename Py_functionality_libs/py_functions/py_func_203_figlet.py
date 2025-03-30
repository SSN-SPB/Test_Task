from pyfiglet import Figlet, FigletFont


def print_figlet():
    # list of fonts: terminal pyfiglet -l
    # figfont = Figlet(font="slant")
    # for x in pyfiglet.FigletFont.getFonts():
    selected_font = Figlet(font="5x7")
    print(selected_font.renderText("List of fonts"))
    for x in FigletFont.getFonts():
        print(x)


def main():
    print_figlet()


if __name__ == "__main__":
    main()
