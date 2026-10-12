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
                    "keyword_1": {
                        "type": "string",
                        "description": "the belonger's keyword of saved messages."
                    },
                    "keyword_2":{
                        "type": "string",
                        "description": "the keyword of saved messages."
                    },
                    "message": {
                        "type": "string",
                        "description": "informations that may be useful in replies later."
                    }
                },                               
                "required": [
                    "keyword_1",
                    "keyword_2",
                    "message"
                ]
            }
        }
    },
    { #读取保存的关键信息
        "type": "function",
        "function": {
            "name": "ref_userfile",
            "description": "refer to saved userfile to search for detailed user information",
            "parameters": {
                "type": "object",
                "properties": {
                    "kword_1": {
                        "type": "string",
                        "description": "the belonger of the message you want to search for"
                    },
                    "kword_2": {
                        "type": "string",
                        "description": "the keyword of the message you want to search for"
                    }
                },
                "required": [
                    "kword_1",
                    "kword_2"
                ]
            }
        }
    }
]