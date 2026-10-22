import json
import os
import sys

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

    def savefile(keyword_1,keyword_2, message):
        file_path = "files/userFiles.json"
        info = {
            "keyword_1": keyword_1, 
            "keyword_2": keyword_2,
            "message": message
                }
        try:
            if os.path.exists(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError:
                        data = []
            else:
                data = []
            data.append(info)
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return f"{message} has been saved."
        except Exception as e:
            sys.exit(f"Error: {e}")

    def ref_userfile(kword_1,kword_2):
        with open("fiels/userFiles.json","r",encoding="utf-8") as f:
            files = json.load(f)
            for file in files:
                if (kword_1 == file["keyword_1"] or kword_1 ==file["keyword_2"] 
                or kword_2 == file["keyword_1"] or kword_2 ==file["keyword_2"]):
                    return file["message"]
                else: return "No related file saved."
