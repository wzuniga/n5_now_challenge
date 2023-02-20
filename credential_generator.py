import base64

client_id = input("Enter Your client_id!\n")
print()
client_secret = input("Enter Your client_secret!\n")
print()
credential = "{0}:{1}".format(client_id, client_secret)
print("Base64 token:")
print(base64.b64encode(credential.encode("utf-8")))
