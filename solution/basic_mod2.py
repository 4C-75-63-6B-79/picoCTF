message = input('Enter the message numbers seprated by space: ').strip();

message_list = message.split(" ");

character_set = 'abcdefghijklmnopqrstuvwxyz0123456789_'.upper();

decryptedMessage = "";

def findModularInverse(a, c):
    for i in range(0, c):
        if( ( a * i ) % c == 1 ):
            return(i-1);

for message_piece in message_list:
    decryptedMessage += character_set[findModularInverse(int(message_piece), 41)];

print("flag: picoCTF{" + str(decryptedMessage) + "}");