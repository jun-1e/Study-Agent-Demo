import json

class tools:
    def calculator(num1,op,num2):
        result = 0
        match op:
            case "+": result = num1 + num2
            case "-": result = num1 - num2
            case "*": result = num1 * num2
            case "/": 
                try:
                    result = num1 / num2
                except ZeroDivisionError as e:
                    return (str(e) + "happened, calculate failed")
        return str(result)

    def search_courses(kword):
        pass

    def savefile(keyword,message):
        info = {
            "keyword": keyword,
            "message": message
        }

        with open("userFiles.json", "a", encoding="utf-8") as f:
            json.dump(info, f, ensure_ascii=False, indent=2)
        return str(message)+"has been saved."
