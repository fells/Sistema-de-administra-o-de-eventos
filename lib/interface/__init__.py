
class Menu:
    def readInt(msg):
        while True:
            try:
                n = int(input(msg))
            except (ValueError, TypeError):
                print("ERRO: por favor, digite uma das opções.")
                continue
            else:
                return n

    def line (lenght = 42):
        return "=" * lenght

    def window (txt):
        print(Menu.line())
        print(txt.center(42))
        print(Menu.line())

    def menu (list):
        Menu.window("MENU PRINCIPAL")
        nums = 1
        for item in list:
            print(f"{nums} - {item}")
            nums += 1
        print(Menu.line())
        option = Menu.readInt('Sua opção: ')
        return option