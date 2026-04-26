import emoji

alias = input("input: ")
emoji = emoji.emojize(alias, language="alias")
print(f"output: {emoji}")