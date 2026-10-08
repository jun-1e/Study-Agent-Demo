functions = [
    { #计算器
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Return calculate result of two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "num1": {
                        "type": "number",
                        "description": "first number you should count."
                    },
                    "op": {
                        "type": "string",
                        "description": "Arithmetic operator"
                    },
                    "num2": {
                        "type": "number",
                        "description": "second number you should count."
                    }
                },
                "required": [
                    "num1",
                    "op",
                    "num2"
                ]
            }
        }
    },

    { #保存用户信息 （暂时只能保存一条）
        "type": "function",
        "function": {
            "name": "savefile",
            "description": "Save descriptive informations from users to local files whereby assistant can refer to them in replies.",
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "the keyword of saved messages."
                    },
                    "message": {
                        "type": "string",
                        "description": "informations that may be useful in replies later."
                    }
                },                               
                "required": [
                    "keyword",
                    "message"
                ]
            }
        }
    }
]