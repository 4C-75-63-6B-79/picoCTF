message = input('Enter the message numbers seprated by space: ').strip();

message_list = message.split(" ");

character_set = 'abcdefghijklmnopqrstuvwxyz0123456789_'.upper();

decryptedMessage = "";

for message_piece in message_list:
    decryptedMessage += character_set[int(message_piece) % 37];

print("flag: picoCTF{" + str(decryptedMessage) + "}");