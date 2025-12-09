########################################################
# Task A9_T5
# Developer Karl Erich Remmelgas
# Date 2025-12-09
########################################################

def askIntByte(PPrompt: str) -> int:
    Feed = input(PPrompt)
    try: 
        color = int(Feed)
        if Feed.isnumeric():
            pass
        else:
            raise Exception(f"\"{Feed}\" is non-numeric value.")
        if (0 <= color <=  255):
            return color
        else: 
            raise Exception(f"Value \"{color}\" is out of the range 0-255.")
    except ValueError:
        print(f"\"{Feed}\" is non-numeric value.")
        raise Exception(f"\"{Feed}\" is non-numeric value.")
    except Exception as err:
        print(err)
        raise err

def createHex(PRed: int, PGreen: int, PBlue: int) -> str:
    hex = "#{:02x}{:02x}{:02x}".format(PRed, PGreen, PBlue)
    return  hex

def main():
    print("Program starting.")
    try:
        red = askIntByte("Insert red: ")
        green = askIntByte("Insert green: ")
        blue = askIntByte("Insert blue: ")
        hex = createHex(red, green, blue)
        red_binary = format(red, '08b')
        green_binary = format(green, '08b')
        blue_binary = format(blue, '08b')
        print(f"RGB Details:\n- Red {red}\n- Green {green}\n- Blue {blue}\n- Hex {hex}\n- Red-byte(base-2): {red_binary}\n- G-byte(base-2): {green_binary}\n- B-byte(base-2): {blue_binary}")
    except Exception:
        print("Couldn't perform the designed task due to the invalid input values.")
    print("Program ending.")

if __name__ == "__main__":
    main()
